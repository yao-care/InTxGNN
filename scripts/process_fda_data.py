#!/usr/bin/env python3
"""Process India CDSCO Drug Data

Convert downloaded CDSCO drug data files to standard JSON format.

Usage:
    uv run python scripts/process_fda_data.py

Prerequisites:
    Download CDSCO drug data from:
    https://cdsco.gov.in/opencms/opencms/en/Approved-New-Drugs/

Output:
    data/raw/in_fda_drugs.json
"""

import json
import zipfile
from pathlib import Path

import pandas as pd


def find_data_file(raw_dir: Path) -> Path:
    """Find data file in raw directory

    Supports ZIP, JSON, CSV, and Excel formats.

    Args:
        raw_dir: data/raw/ directory path

    Returns:
        Found data file path

    Raises:
        FileNotFoundError: When no data file found
    """
    # Search for common file formats
    for pattern in ["*.zip", "*.json", "*.csv", "*.xlsx", "*.xls"]:
        data_files = list(raw_dir.glob(pattern))
        if data_files:
            return data_files[0]

    raise FileNotFoundError(
        f"No data file found in {raw_dir}\n"
        f"Please download CDSCO drug data and place it in data/raw/ directory.\n"
        f"Supported formats: ZIP, JSON, CSV, Excel\n"
        f"Download from: https://cdsco.gov.in/opencms/opencms/en/Approved-New-Drugs/"
    )


def process_data_file(input_path: Path, output_path: Path) -> Path:
    """Process data file and convert to JSON

    Args:
        input_path: Input file path
        output_path: Output JSON file path

    Returns:
        Output file path
    """
    print(f"Reading data file: {input_path}")
    print(f"File size: {input_path.stat().st_size / 1024 / 1024:.1f} MB")

    suffix = input_path.suffix.lower()

    # Process based on file type
    if suffix == ".zip":
        print("Extracting ZIP file...")
        with zipfile.ZipFile(input_path, 'r') as zf:
            # Look for JSON, CSV, or Excel inside ZIP
            for ext in ['.json', '.csv', '.xlsx', '.xls']:
                matching_files = [f for f in zf.namelist() if f.lower().endswith(ext)]
                if matching_files:
                    inner_file = matching_files[0]
                    print(f"Found data file: {inner_file}")

                    with zf.open(inner_file) as f:
                        if ext == '.json':
                            data = json.loads(f.read().decode('utf-8'))
                        elif ext == '.csv':
                            df = pd.read_csv(f)
                            data = df.to_dict(orient="records")
                        else:  # Excel
                            df = pd.read_excel(f)
                            data = df.to_dict(orient="records")
                    break
            else:
                raise ValueError("No supported data file found in ZIP")

    elif suffix == ".json":
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    elif suffix == ".csv":
        df = pd.read_csv(input_path)
        data = df.to_dict(orient="records")

    elif suffix in [".xlsx", ".xls"]:
        df = pd.read_excel(input_path)
        data = df.to_dict(orient="records")

    else:
        raise ValueError(f"Unsupported file format: {suffix}")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save JSON
    print(f"Saving to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Done! Total {len(data)} drug records")
    return output_path


def main():
    print("=" * 60)
    print("Process India CDSCO Drug Data")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "in_fda_drugs.json"

    # Ensure raw directory exists
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Find and process data file
    input_path = find_data_file(raw_dir)
    process_data_file(input_path, output_path)

    print()
    print("Next step: Prepare vocabulary data")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
