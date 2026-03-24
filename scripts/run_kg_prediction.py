#!/usr/bin/env python3
"""Knowledge Graph Method - Drug Repurposing Prediction

Use TxGNN knowledge graph for drug-disease relationship prediction.
This method is fast and doesn't require deep learning environment.

Usage:
    uv run python scripts/run_kg_prediction.py

Prerequisites:
    1. Run process_fda_data.py
    2. Run prepare_external_data.py
"""

import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

import pandas as pd

from intxgnn.data import load_fda_drugs, filter_active_drugs
from intxgnn.mapping import (
    map_fda_drugs_to_drugbank,
    map_fda_indications_to_diseases,
    get_mapping_stats,
    get_indication_mapping_stats,
)
from intxgnn.predict import find_repurposing_candidates, generate_repurposing_report


def main():
    print("=" * 60)
    print("Knowledge Graph Method - India Drug Repurposing Prediction")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    processed_dir = base_dir / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    # 1. Load drug data
    print("Step 1/5: Loading India drug data...")
    df = load_fda_drugs()
    print(f"  Total drugs: {len(df)}")

    # 2. Filter active drugs
    print("Step 2/5: Filtering active drugs...")
    active = filter_active_drugs(df)
    print(f"  Active drugs: {len(active)}")

    # 3. Drug ingredient mapping
    print("Step 3/5: Mapping drug ingredients to DrugBank...")
    drug_mapping = map_fda_drugs_to_drugbank(active)
    drug_mapping.to_csv(processed_dir / "drug_mapping.csv", index=False)
    stats = get_mapping_stats(drug_mapping)
    print(f"  Ingredient mapping rate: {stats['mapping_rate']:.2%}")
    print(f"  Mapped to DrugBank drugs: {stats['unique_drugbank_ids']}")

    # 4. Indication mapping
    # Note: Indian Medicine Dataset does not have indication field
    # We create an empty DataFrame with expected columns for compatibility
    print("Step 4/5: Checking indication data...")
    indication_mapping = map_fda_indications_to_diseases(active)

    # Handle empty indication mapping (no indication field in Indian data)
    if len(indication_mapping) == 0 or "disease_id" not in indication_mapping.columns:
        print("  Note: No indication field in source data")
        print("  Using TxGNN knowledge graph for all predictions")
        # Create empty DataFrame with expected columns
        indication_mapping = pd.DataFrame(columns=[
            "license_id", "brand_name", "original_indication",
            "extracted_indication", "disease_id", "disease_name", "confidence"
        ])
    else:
        ind_stats = get_indication_mapping_stats(indication_mapping)
        print(f"  Indication mapping rate: {ind_stats['mapping_rate']:.2%}")
        print(f"  Mapped to diseases: {ind_stats['unique_diseases']}")

    indication_mapping.to_csv(processed_dir / "indication_mapping.csv", index=False)

    # 5. Drug repurposing prediction
    print("Step 5/5: Running drug repurposing prediction...")
    candidates = find_repurposing_candidates(drug_mapping, indication_mapping)
    output_path = processed_dir / "repurposing_candidates.csv.gz"
    candidates.to_csv(output_path, index=False)

    # Generate report
    report = generate_repurposing_report(candidates)

    print()
    print("=" * 60)
    print("Prediction Complete!")
    print("=" * 60)
    print()
    print(f"Results file: {output_path}")
    print()
    print("Summary Statistics:")
    print(f"  Drug repurposing candidates: {report['total_candidates']}")
    print(f"  Unique drugs involved: {report['unique_drugs']}")
    print(f"  Potential new indications: {report['unique_diseases']}")


if __name__ == "__main__":
    main()
