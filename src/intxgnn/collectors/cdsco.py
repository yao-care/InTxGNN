"""CDSCO collector - fetches India CDSCO drug data."""

import json
from pathlib import Path
from typing import Any

import yaml

from .base import BaseCollector, CollectorResult


def load_field_config() -> dict:
    """Load field mapping configuration"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class CDSCOCollector(BaseCollector):
    """Collector for India CDSCO (Central Drugs Standard Control Organisation) drug data.

    Reads from local in_fda_drugs.json file that was processed
    from the CDSCO data.
    """

    source_name = "cdsco"

    def __init__(self, data_path: str | Path | None = None):
        """Initialize the collector.

        Args:
            data_path: Path to in_fda_drugs.json file.
                      Defaults to data/raw/in_fda_drugs.json
        """
        if data_path is None:
            self.data_path = (
                Path(__file__).parent.parent.parent.parent
                / "data"
                / "raw"
                / "in_fda_drugs.json"
            )
        else:
            self.data_path = Path(data_path)

        self._data: list[dict] | None = None
        self._config: dict | None = None

    def _get_config(self) -> dict:
        """Get field configuration."""
        if self._config is None:
            self._config = load_field_config()
        return self._config

    def _load_data(self) -> list[dict]:
        """Load CDSCO data from JSON file."""
        if self._data is not None:
            return self._data

        if not self.data_path.exists():
            self._data = []
            return self._data

        with open(self.data_path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

        return self._data

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for CDSCO records matching a drug name.

        Args:
            drug: Drug name (INN or brand name)
            disease: Disease/indication name (used for filtering if provided)

        Returns:
            CollectorResult with CDSCO data
        """
        query = {"drug": drug, "disease": disease}

        try:
            data = self._load_data()

            # Search for matching records
            matches = self._find_matches(drug, data)

            # If disease is provided, further filter by indication
            if disease and matches:
                matches = self._filter_by_indication(matches, disease)

            # Format the result
            result = self._format_result(matches)

            return self._make_result(
                query=query,
                data=result,
                success=True,
            )

        except Exception as e:
            return self._make_result(
                query=query,
                data={"found": False, "records": []},
                success=False,
                error_message=str(e),
            )

    def _find_matches(self, drug: str, data: list[dict]) -> list[dict]:
        """Find records matching the drug name.

        Args:
            drug: Drug name to search for
            data: List of CDSCO records

        Returns:
            List of matching records
        """
        config = self._get_config()
        field_mapping = config.get("field_mapping", {})

        drug_lower = drug.lower()
        matches = []

        # Fields to search in
        search_fields = [
            field_mapping.get("brand_name_local", "brand_name"),
            field_mapping.get("brand_name_en", "brand_name"),
            field_mapping.get("ingredients", "active_ingredients"),
            field_mapping.get("indication", "therapeutic_use"),
        ]

        for record in data:
            for field_name in search_fields:
                field_value = record.get(field_name, "")
                if field_value and drug_lower in str(field_value).lower():
                    matches.append(record)
                    break

        return matches

    def _filter_by_indication(
        self, records: list[dict], disease: str
    ) -> list[dict]:
        """Filter records by indication/disease.

        Args:
            records: List of CDSCO records
            disease: Disease/indication to filter by

        Returns:
            Filtered list of records
        """
        config = self._get_config()
        field_mapping = config.get("field_mapping", {})
        indication_field = field_mapping.get("indication", "therapeutic_use")

        disease_lower = disease.lower()
        filtered = []

        for record in records:
            indication = str(record.get(indication_field, "")).lower()
            if disease_lower in indication:
                filtered.append(record)

        # If no matches with indication filter, return original
        return filtered if filtered else records

    def _format_result(self, records: list[dict]) -> dict:
        """Format the result for the bundle.

        Args:
            records: List of matching CDSCO records

        Returns:
            Formatted result dictionary
        """
        if not records:
            return {"found": False, "records": []}

        config = self._get_config()
        field_mapping = config.get("field_mapping", {})

        formatted_records = []
        for record in records[:20]:  # Limit to 20 records
            formatted = {
                "license_id": record.get(field_mapping.get("license_id", "approval_number"), ""),
                "brand_name": record.get(field_mapping.get("brand_name_local", "brand_name"), ""),
                "ingredients": record.get(field_mapping.get("ingredients", "active_ingredients"), ""),
                "indication": record.get(field_mapping.get("indication", "therapeutic_use"), ""),
                "dosage_form": record.get(field_mapping.get("dosage_form", "dosage_form"), ""),
                "manufacturer": record.get(field_mapping.get("manufacturer", "manufacturer"), ""),
                "approval_date": record.get(field_mapping.get("approval_date", "approval_date"), ""),
                "status": record.get(field_mapping.get("status", "status"), ""),
            }
            formatted_records.append(formatted)

        return {
            "found": True,
            "records": formatted_records,
            "total_matches": len(records),
        }

    def get_by_approval_number(self, approval_number: str) -> dict | None:
        """Get a specific record by approval number.

        Args:
            approval_number: CDSCO approval number

        Returns:
            Record dictionary or None if not found
        """
        config = self._get_config()
        field_mapping = config.get("field_mapping", {})
        license_field = field_mapping.get("license_id", "approval_number")

        data = self._load_data()

        for record in data:
            if record.get(license_field) == approval_number:
                return record

        return None
