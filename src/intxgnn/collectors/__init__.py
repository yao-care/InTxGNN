"""Data collectors for evidence gathering."""

from .base import BaseCollector, CollectorResult
from .clinicaltrials import ClinicalTrialsCollector
from .drugbank import DrugBankCollector
from .ictrp import ICTRPCollector
from .pubmed import PubMedCollector
from .cdsco import CDSCOCollector

__all__ = [
    "BaseCollector",
    "CollectorResult",
    "ClinicalTrialsCollector",
    "DrugBankCollector",
    "ICTRPCollector",
    "PubMedCollector",
    "CDSCOCollector",
]
