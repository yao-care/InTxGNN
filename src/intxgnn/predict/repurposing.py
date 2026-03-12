"""Drug Repurposing Prediction - Based on TxGNN Knowledge Graph"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd


def load_drug_disease_relations(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load TxGNN drug-disease relations

    Args:
        filepath: CSV file path

    Returns:
        Drug-disease relations DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drug_disease_relations.csv"

    return pd.read_csv(filepath)


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """Build drug -> indication set mapping

    Args:
        relations_df: Drug-disease relations DataFrame

    Returns:
        {drug_name: {disease1, disease2, ...}}
    """
    # Only keep indication and off-label use
    indications = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"]

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def find_repurposing_candidates(
    drug_mapping_df: pd.DataFrame,
    indication_mapping_df: pd.DataFrame,
    relations_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Find drug repurposing candidates

    Compare existing indications of local drugs with indications in TxGNN knowledge graph,
    to find potential new indications.

    Args:
        drug_mapping_df: Drug DrugBank mapping results
        indication_mapping_df: Indication disease mapping results
        relations_df: TxGNN drug-disease relations

    Returns:
        Drug repurposing candidates DataFrame
    """
    if relations_df is None:
        relations_df = load_drug_disease_relations()

    # Build TxGNN drug indication mapping
    kg_drug_map = build_drug_indication_map(relations_df)

    # Build existing indication set from local drug data
    existing_diseases_df = indication_mapping_df[
        indication_mapping_df["disease_name"].notna()
    ][["license_id", "disease_name"]].copy()
    existing_diseases_df["disease_lower"] = existing_diseases_df["disease_name"].str.lower()
    existing_drug_diseases = existing_diseases_df.groupby("license_id")["disease_lower"].apply(set).to_dict()

    # Build drug info index
    valid_drugs = drug_mapping_df[drug_mapping_df["drugbank_id"].notna()].copy()
    drug_info_map = valid_drugs.groupby(["license_id", "normalized_ingredient"]).first().to_dict("index")

    # Get unique (license_id, ingredient) pairs
    unique_pairs = valid_drugs[["license_id", "normalized_ingredient", "brand_name", "drugbank_id"]].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_id = row["license_id"]
        drug_name = row["normalized_ingredient"]

        # Query TxGNN for all indications of this drug
        kg_diseases = kg_drug_map.get(drug_name, set())
        if not kg_diseases:
            continue

        # Get existing indications
        existing_diseases = existing_drug_diseases.get(license_id, set())

        # Find potential new indications
        for disease in kg_diseases:
            disease_lower = disease.lower()

            # Check if indication is new
            is_new = all(
                existing_d not in disease_lower and disease_lower not in existing_d
                for existing_d in existing_diseases
            )

            if is_new:
                candidates.append({
                    "license_id": license_id,
                    "brand_name": row["brand_name"],
                    "drug_ingredient": drug_name,
                    "drugbank_id": row["drugbank_id"],
                    "potential_indication": disease,
                    "source": "TxGNN Knowledge Graph",
                })

    result_df = pd.DataFrame(candidates)

    # Deduplicate
    if len(result_df) > 0:
        # First: remove exact duplicates per license
        result_df = result_df.drop_duplicates(
            subset=["license_id", "drug_ingredient", "potential_indication"]
        )

        # Second: for DL prediction efficiency, keep only unique (drugbank_id, disease) pairs
        # This prevents redundant DL predictions for the same drug-disease combination
        # We keep the first occurrence (arbitrary license_id as representative)
        result_df = result_df.drop_duplicates(
            subset=["drugbank_id", "potential_indication"],
            keep="first"
        )

    return result_df


def generate_repurposing_report(candidates_df: pd.DataFrame) -> dict:
    """Generate drug repurposing report statistics

    Args:
        candidates_df: Candidate drugs DataFrame

    Returns:
        Statistics report dictionary
    """
    if len(candidates_df) == 0:
        return {
            "total_candidates": 0,
            "unique_drugs": 0,
            "unique_diseases": 0,
            "top_diseases": [],
            "top_drugs": [],
        }

    unique_drugs = candidates_df["drug_ingredient"].nunique()
    unique_diseases = candidates_df["potential_indication"].nunique()

    # Most common potential new indications
    top_diseases = candidates_df["potential_indication"].value_counts().head(10).to_dict()

    # Drugs with most potential new indications
    drug_counts = candidates_df.groupby("drug_ingredient")["potential_indication"].nunique()
    top_drugs = drug_counts.sort_values(ascending=False).head(10).to_dict()

    return {
        "total_candidates": len(candidates_df),
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
        "top_diseases": top_diseases,
        "top_drugs": top_drugs,
    }
