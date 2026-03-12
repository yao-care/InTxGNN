"""Tests for prediction module"""

import pytest
import pandas as pd


class TestRepurposing:
    """Tests for drug repurposing functions"""

    def test_load_drug_disease_relations(self):
        """Test loading drug-disease relations"""
        from intxgnn.predict import load_drug_disease_relations

        df = load_drug_disease_relations()

        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert "relation" in df.columns
        assert "x_name" in df.columns
        assert "y_name" in df.columns

    def test_find_repurposing_candidates(self):
        """Test finding repurposing candidates"""
        from intxgnn.predict import find_repurposing_candidates

        # Create mock drug mapping
        drug_mapping = pd.DataFrame({
            "license_id": ["001", "002"],
            "brand_name": ["Drug A", "Drug B"],
            "normalized_ingredient": ["METFORMIN", "ASPIRIN"],
            "drugbank_id": ["DB00331", "DB00945"]
        })

        # Create empty indication mapping (simulating no indication data)
        indication_mapping = pd.DataFrame(columns=["license_id", "disease_name"])

        candidates = find_repurposing_candidates(drug_mapping, indication_mapping)

        assert isinstance(candidates, pd.DataFrame)
        # Should find candidates from TxGNN KG
        if len(candidates) > 0:
            assert "license_id" in candidates.columns
            assert "potential_indication" in candidates.columns

    def test_generate_repurposing_report(self):
        """Test generating repurposing report"""
        from intxgnn.predict import generate_repurposing_report

        # Test with empty DataFrame
        empty_df = pd.DataFrame()
        report = generate_repurposing_report(empty_df)

        assert isinstance(report, dict)
        assert report["total_candidates"] == 0

        # Test with sample data
        sample_df = pd.DataFrame({
            "license_id": ["001", "002", "003"],
            "drug_ingredient": ["METFORMIN", "METFORMIN", "ASPIRIN"],
            "potential_indication": ["cancer", "heart disease", "pain"]
        })
        report = generate_repurposing_report(sample_df)

        assert report["total_candidates"] == 3
        assert report["unique_drugs"] == 2


class TestTxGNNNodes:
    """Tests for TxGNN node functions"""

    def test_load_txgnn_nodes(self):
        """Test loading TxGNN nodes"""
        from intxgnn.predict import load_txgnn_nodes

        nodes_df = load_txgnn_nodes()

        assert isinstance(nodes_df, pd.DataFrame)
        assert len(nodes_df) > 0
        # Check for expected columns
        assert "node_id" in nodes_df.columns or "node_index" in nodes_df.columns


class TestCollectors:
    """Tests for evidence collectors"""

    def test_pubmed_collector_import(self):
        """Test PubMed collector can be imported"""
        from intxgnn.collectors import PubMedCollector

        collector = PubMedCollector()
        assert collector.source_name == "pubmed"

    def test_clinicaltrials_collector_import(self):
        """Test ClinicalTrials collector can be imported"""
        from intxgnn.collectors import ClinicalTrialsCollector

        collector = ClinicalTrialsCollector()
        assert collector.source_name == "clinicaltrials"

    def test_cdsco_collector_import(self):
        """Test CDSCO collector can be imported"""
        from intxgnn.collectors import CDSCOCollector

        collector = CDSCOCollector()
        assert collector.source_name == "cdsco"
