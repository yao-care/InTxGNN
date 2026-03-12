"""Tests for data loading module"""

import pytest
import pandas as pd
from pathlib import Path


class TestDataLoader:
    """Tests for data loader functions"""

    def test_load_fda_drugs(self):
        """Test loading FDA drugs data"""
        from intxgnn.data import load_fda_drugs

        df = load_fda_drugs()

        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert "name" in df.columns
        assert "short_composition1" in df.columns

    def test_filter_active_drugs(self):
        """Test filtering active drugs"""
        from intxgnn.data import load_fda_drugs, filter_active_drugs

        df = load_fda_drugs()
        active = filter_active_drugs(df)

        assert isinstance(active, pd.DataFrame)
        assert len(active) <= len(df)
        # All rows should have non-discontinued status
        if "Is_discontinued" in active.columns:
            assert not active["Is_discontinued"].any()

    def test_get_drug_summary(self):
        """Test drug summary statistics"""
        from intxgnn.data import load_fda_drugs, get_drug_summary

        df = load_fda_drugs()
        summary = get_drug_summary(df)

        assert isinstance(summary, dict)
        assert "total_count" in summary
        assert summary["total_count"] == len(df)


class TestFieldConfig:
    """Tests for field configuration"""

    def test_fields_yaml_exists(self):
        """Test that fields.yaml exists and is valid"""
        import yaml

        config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
        assert config_path.exists()

        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        assert "country_code" in config
        assert config["country_code"] == "IN"
        assert "field_mapping" in config
        assert "ingredients" in config["field_mapping"]
