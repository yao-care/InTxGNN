"""Tests for mapping module"""

import pytest
import pandas as pd


class TestNormalizer:
    """Tests for drug name normalizer"""

    def test_normalize_ingredient(self):
        """Test basic ingredient normalization"""
        from intxgnn.mapping import normalize_ingredient

        # Test basic normalization (returns uppercase)
        result = normalize_ingredient("metformin")
        assert result == "METFORMIN"

        # Test with suffix removal
        result = normalize_ingredient("metformin hydrochloride")
        assert "METFORMIN" in result

    def test_extract_ingredients(self):
        """Test ingredient extraction from composition"""
        from intxgnn.mapping import extract_ingredients

        # Test single ingredient
        result = extract_ingredients("Paracetamol(500mg)")
        assert len(result) >= 1

        # Test multiple ingredients
        result = extract_ingredients("Paracetamol(500mg) + Caffeine(65mg)")
        assert len(result) >= 1


class TestDrugBankMapper:
    """Tests for DrugBank mapping"""

    def test_load_drugbank_vocab(self):
        """Test loading DrugBank vocabulary"""
        from intxgnn.mapping import load_drugbank_vocab

        df = load_drugbank_vocab()

        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert "drugbank_id" in df.columns
        assert "drug_name" in df.columns

    def test_map_ingredient_to_drugbank(self):
        """Test mapping single ingredient to DrugBank"""
        from intxgnn.mapping import load_drugbank_vocab, build_name_index, map_ingredient_to_drugbank

        drugbank_df = load_drugbank_vocab()
        name_index = build_name_index(drugbank_df)

        # Test common drug
        result = map_ingredient_to_drugbank("metformin", name_index)
        assert result is not None
        assert result.startswith("DB")

        # Test unknown drug
        result = map_ingredient_to_drugbank("nonexistent_drug_xyz", name_index)
        assert result is None


class TestDiseaseMapper:
    """Tests for disease mapping"""

    def test_disease_dict_exists(self):
        """Test that DISEASE_DICT is populated"""
        from intxgnn.mapping import DISEASE_DICT

        assert isinstance(DISEASE_DICT, dict)
        assert len(DISEASE_DICT) > 100  # Should have 150+ entries

    def test_load_disease_vocab(self):
        """Test loading disease vocabulary"""
        from intxgnn.mapping import load_disease_vocab

        df = load_disease_vocab()

        assert isinstance(df, pd.DataFrame)
        assert len(df) > 0
        assert "disease_id" in df.columns
        assert "disease_name" in df.columns

    def test_translate_indication(self):
        """Test indication translation"""
        from intxgnn.mapping import translate_indication

        # Test English term (should return as-is or normalized)
        result = translate_indication("diabetes")
        assert result is not None

        # Test Hindi term (if in dictionary)
        result = translate_indication("madhumeh")
        # Should translate to diabetes or similar
        assert result is not None
