"""DrugBank Mapping Module"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
import yaml

from .normalizer import extract_ingredients, get_all_synonyms


def load_field_config() -> dict:
    """Load field mapping configuration"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_drugbank_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 DrugBank 詞彙表

    Args:
        filepath: CSV 檔案路徑，預設為 data/external/drugbank_vocab.csv

    Returns:
        DrugBank 詞彙表 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drugbank_vocab.csv"

    return pd.read_csv(filepath)


def build_name_index(drugbank_df: pd.DataFrame) -> Dict[str, str]:
    """建立名稱索引（名稱 -> DrugBank ID）

    Args:
        drugbank_df: DrugBank 詞彙表

    Returns:
        名稱到 ID 的對照字典
    """
    index = {}

    for _, row in drugbank_df.iterrows():
        name_upper = row["drug_name_upper"]
        drugbank_id = row["drugbank_id"]

        # 完整名稱
        index[name_upper] = drugbank_id

        # 移除常見鹽類後綴，建立別名
        # 例如 "METFORMIN HCL" -> "METFORMIN"
        salt_suffixes = [
            " HCL", " HYDROCHLORIDE", " SODIUM", " POTASSIUM",
            " SULFATE", " SULPHATE", " MALEATE", " ACETATE",
            " CITRATE", " PHOSPHATE", " BROMIDE", " CHLORIDE",
            " TARTRATE", " FUMARATE", " SUCCINATE", " MESYLATE",
            " BESYLATE", " CALCIUM", " MAGNESIUM", " NITRATE",
            " LACTATE", " GLUCONATE", " DISODIUM", " MONOHYDRATE",
            " DIHYDRATE", " TRIHYDRATE", " ANHYDROUS",
            " DIPROPIONATE", " PROPIONATE", " ACETONIDE",
            " VALERATE", " BUTYRATE", " HEXAHYDRATE",
        ]

        for suffix in salt_suffixes:
            if name_upper.endswith(suffix):
                base_name = name_upper[:-len(suffix)].strip()
                if base_name and base_name not in index:
                    index[base_name] = drugbank_id

    # 添加常見同義詞對照
    # 格式：{FDA 成分名稱: DrugBank 名稱}
    synonym_map = {
        # ===== 維生素（通用名 -> DrugBank 化學名）=====
        "NIACINAMIDE": "NICOTINAMIDE",
        "NICOTINIC ACID": "NIACIN",
        "VITAMIN B1": "THIAMINE",
        "THIAMINE HCL": "THIAMINE",
        "THIAMINE MONONITRATE": "THIAMINE",
        "VITAMIN B2": "RIBOFLAVIN",
        "VITAMIN B6": "PYRIDOXINE",
        "PYRIDOXINE HCL": "PYRIDOXINE",
        "VITAMIN B12": "CYANOCOBALAMIN",
        "VITAMIN C": "ASCORBIC ACID",
        "VITAMIN E": "TOCOPHEROL",
        "TOCOPHEROL ACETATE": "ALPHA-TOCOPHEROL ACETATE",
        "ALPHA-TOCOPHEROL": "TOCOPHEROL",
        "VITAMIN A": "RETINOL",
        "RETINOL PALMITATE": "RETINOL",
        "VITAMIN D3": "CHOLECALCIFEROL",
        "VITAMIN D2": "ERGOCALCIFEROL",
        "VITAMIN K1": "PHYTONADIONE",
        "PANTOTHENATE CALCIUM": "PANTOTHENIC ACID",
        "CALCIUM PANTOTHENATE": "PANTOTHENIC ACID",
        "PANTHENOL": "DEXPANTHENOL",
        "D-PANTHENOL": "DEXPANTHENOL",
        # ===== 常見藥物別名 =====
        "ASPIRIN": "ACETYLSALICYLIC ACID",
        "PARACETAMOL": "ACETAMINOPHEN",
        "ADRENALINE": "EPINEPHRINE",
        "L-ADRENALINE": "EPINEPHRINE",
        "NORADRENALINE": "NOREPINEPHRINE",
        "LIGNOCAINE": "LIDOCAINE",
        "FRUSEMIDE": "FUROSEMIDE",
        "SALBUTAMOL": "ALBUTEROL",
        "SIMETHICONE": "DIMETHICONE",
        "ALUMINUM HYDROXIDE DRIED GEL": "ALUMINUM HYDROXIDE",
        "ALUMINIUM HYDROXIDE": "ALUMINUM HYDROXIDE",
        # ===== 葡萄糖/右旋糖 =====
        "DEXTROSE": "D-GLUCOSE",
        "DEXTROSE MONOHYDRATE": "D-GLUCOSE",
        "GLUCOSE": "D-GLUCOSE",
        "GLUCOSE MONOHYDRATE": "D-GLUCOSE",
        # ===== L-/D-/DL- 前綴處理 =====
        "L-MENTHOL": "LEVOMENTHOL",
        "MENTHOL": "LEVOMENTHOL",
        "DL-MENTHOL": "RACEMENTHOL",
        "DL-METHIONINE": "METHIONINE",
        "L-METHIONINE": "METHIONINE",
        "L-LYSINE HCL": "LYSINE",
        "L-LYSINE": "LYSINE",
        # ===== 水合物/無水形式 =====
        "CAFFEINE ANHYDROUS": "CAFFEINE",
        "ATORVASTATIN CALCIUM TRIHYDRATE": "ATORVASTATIN",
        "LIDOCAINE HCL MONOHYDRATE": "LIDOCAINE",
        # ===== 抗生素 =====
        "AMOXYCILLIN": "AMOXICILLIN",
        "CEPHRADINE": "CEFRADINE",
        "RIFAMPIN": "RIFAMPICIN",
        "GENTAMYCIN": "GENTAMICIN",
        # ===== 心血管藥物 =====
        "AMLODIPINE BESILATE": "AMLODIPINE",
        # ===== 免疫抑制劑 =====
        "CYCLOSPORIN": "CYCLOSPORINE",
        "CICLOSPORIN": "CYCLOSPORINE",
        # ===== 通用映射 =====
        "ALCOHOL": "ETHANOL",
        "L-CARNITINE": "LEVOCARNITINE",
        "L-CYSTEINE": "CYSTEINE",
        "PHYTOMENADIONE": "PHYLLOQUINONE",
        "HYOSCINE": "SCOPOLAMINE",
        "ISOPROTERENOL": "ISOPRENALINE",
        "TORSEMIDE": "TORASEMIDE",
        "URSODIOL": "URSODEOXYCHOLIC ACID",
        "VALACYCLOVIR": "VALACICLOVIR",
        # ===== 常見化合物 =====
        "CALCIUM": "CALCIUM",
        "MAGNESIUM": "MAGNESIUM",
        "ZINC": "ZINC",
        "BIOTIN": "BIOTIN",
        "FOLIC ACID": "FOLIC ACID",
        "CHARCOAL": "ACTIVATED CHARCOAL",
        "CAMPHOR": "CAMPHOR",
        "WARFARIN": "WARFARIN",
        "IBUPROFEN": "IBUPROFEN",
        "METFORMIN": "METFORMIN",
        "ATROPINE": "ATROPINE",
        "EPINEPHRINE": "EPINEPHRINE",
        "THEOPHYLLINE": "THEOPHYLLINE",
        "CAFFEINE": "CAFFEINE",
    }

    for alias, canonical in synonym_map.items():
        if canonical in index and alias not in index:
            index[alias] = index[canonical]

    return index


def map_ingredient_to_drugbank(
    ingredient: str,
    name_index: Dict[str, str],
) -> Optional[str]:
    """將單一成分映射到 DrugBank ID

    映射策略（優先順序）：
    1. 完全匹配
    2. 移除鹽類後綴後匹配
    3. 使用基本名稱匹配

    Args:
        ingredient: 標準化後的成分名稱
        name_index: 名稱索引

    Returns:
        DrugBank ID，若無法映射則回傳 None
    """
    if not ingredient:
        return None

    ingredient = ingredient.upper().strip()

    # 1. 完全匹配
    if ingredient in name_index:
        return name_index[ingredient]

    # 2. 移除台灣 FDA 常見的鹽類後綴
    salt_patterns = [
        r"\s+HCL$", r"\s+HYDROCHLORIDE$", r"\s+SODIUM$",
        r"\s+POTASSIUM$", r"\s+SULFATE$", r"\s+MALEATE$",
        r"\s+ACETATE$", r"\s+CITRATE$", r"\s+PHOSPHATE$",
        r"\s+BROMIDE$", r"\s+CHLORIDE$", r"\s+TARTRATE$",
        r"\s+HBR$", r"\s+HYDROBROMIDE$", r"\s+FUMARATE$",
        r"\s+SUCCINATE$", r"\s+MESYLATE$", r"\s+BESYLATE$",
        r"\s+CALCIUM$", r"\s+MAGNESIUM$", r"\s+NITRATE$",
        r"\s+LACTATE$", r"\s+GLUCONATE$", r"\s+DISODIUM$",
        r"\s+ANHYDROUS$", r"\s+MONOHYDRATE$", r"\s+DIHYDRATE$",
        r"\s+TRIHYDRATE$", r"\s+HEXAHYDRATE$",
        r"\s+DIPROPIONATE$", r"\s+PROPIONATE$", r"\s+ACETONIDE$",
        r"\s+VALERATE$", r"\s+BUTYRATE$", r"\s+MONONITRATE$",
    ]

    base_ingredient = ingredient
    for pattern in salt_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 2b. 移除 L-/D-/DL- 前綴
    prefix_patterns = [r"^L-", r"^D-", r"^DL-"]
    base_ingredient = ingredient
    for pattern in prefix_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 3. 嘗試移除括號內容
    base_ingredient = re.sub(r"\s*\([^)]*\)", "", ingredient).strip()
    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    return None


def map_fda_drugs_to_drugbank(
    fda_df: pd.DataFrame,
    drugbank_df: Optional[pd.DataFrame] = None,
    ingredient_field: Optional[str] = None,
    license_field: Optional[str] = None,
    brand_field: Optional[str] = None,
) -> pd.DataFrame:
    """Map FDA drugs to DrugBank

    Args:
        fda_df: FDA drugs DataFrame
        drugbank_df: DrugBank vocabulary (optional)
        ingredient_field: Field name for ingredients (from fields.yaml if not specified)
        license_field: Field name for license ID (from fields.yaml if not specified)
        brand_field: Field name for brand name (from fields.yaml if not specified)

    Returns:
        DataFrame with mapping results
    """
    if drugbank_df is None:
        drugbank_df = load_drugbank_vocab()

    # Load field configuration
    config = load_field_config()
    field_mapping = config.get("field_mapping", {})

    # Use provided fields or fall back to config
    if ingredient_field is None:
        ingredient_field = field_mapping.get("ingredients", "active_ingredients")
    if license_field is None:
        license_field = field_mapping.get("license_id", "approval_number")
    if brand_field is None:
        brand_field = field_mapping.get("brand_name_local", "brand_name")

    # Build index
    name_index = build_name_index(drugbank_df)

    results = []

    for _, row in fda_df.iterrows():
        ingredient_str = row.get(ingredient_field, "")
        if not ingredient_str or pd.isna(ingredient_str):
            continue

        # Extract all ingredients and synonyms
        synonyms_data = get_all_synonyms(str(ingredient_str))

        for main_name, synonyms in synonyms_data:
            drugbank_id = None
            mapping_source = "failed"

            # Try main name first
            drugbank_id = map_ingredient_to_drugbank(main_name, name_index)
            if drugbank_id:
                mapping_source = "drugbank"

            # If failed, try synonyms
            if drugbank_id is None:
                for syn in synonyms:
                    drugbank_id = map_ingredient_to_drugbank(syn, name_index)
                    if drugbank_id:
                        mapping_source = "drugbank_synonym"
                        break

            results.append({
                "license_id": row.get(license_field, ""),
                "brand_name": row.get(brand_field, ""),
                "original_ingredient": str(ingredient_str),
                "normalized_ingredient": main_name,
                "synonyms": "; ".join(synonyms) if synonyms else "",
                "drugbank_id": drugbank_id,
                "mapping_success": drugbank_id is not None,
                "mapping_source": mapping_source,
            })

    return pd.DataFrame(results)


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """Calculate mapping statistics

    Args:
        mapping_df: Mapping result DataFrame

    Returns:
        Statistics dictionary
    """
    total = len(mapping_df)
    success = mapping_df["mapping_success"].sum()
    unique_ingredients = mapping_df["normalized_ingredient"].nunique()
    unique_drugbank = mapping_df[mapping_df["mapping_success"]]["drugbank_id"].nunique()

    return {
        "total_ingredients": total,
        "mapped_ingredients": int(success),
        "mapping_rate": success / total if total > 0 else 0,
        "unique_ingredients": unique_ingredients,
        "unique_drugbank_ids": unique_drugbank,
    }
