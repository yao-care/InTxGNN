---
layout: default
title: Piperaquine
parent: Moderate Evidence (L3-L4)
nav_order: 669
evidence_level: L4
indication_count: 10
---

# Piperaquine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Piperaquine: From Malaria to Cystic Echinococcosis

## One-Sentence Summary

Piperaquine is a bisquinoline antimalarial, most commonly used as a component of the fixed-dose combination dihydroartemisinin-piperaquine (DHA-PPQ) for treating malaria. The TxGNN model's top-ranked prediction suggests possible activity against **Cystic Echinococcosis**, but this is currently supported by only **1 review-level publication** and **no clinical trials**, making it a purely exploratory signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malaria (antimalarial quinoline; used as part of the dihydroartemisinin-piperaquine combination; not separately marketed) |
| Predicted New Indication | Cystic Echinococcosis |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for piperaquine in this evidence pack. Based on known pharmacology, piperaquine is a bisquinoline antimalarial that acts primarily by inhibiting heme detoxification in the parasite's digestive vacuole, a mechanism shared with other quinoline-class antiparasitics. Its clinical value has been proven most extensively as the partner drug in dihydroartemisinin-piperaquine (DHA-PPQ), a WHO-recommended first-line treatment for both *Plasmodium falciparum* and *Plasmodium vivax* malaria — a use case backed by extensive trial data (see Note below).

The link to cystic echinococcosis is far weaker and indirect. Both malaria (a protozoal infection) and cystic echinococcosis (a cestode/tapeworm infection caused by *Echinococcus granulosus*) fall under the broad umbrella of parasitic and neglected tropical diseases (NTDs), which is likely why TxGNN's knowledge graph places them close together. However, protozoa and cestodes have fundamentally different biology, and no in vitro, in vivo, or clinical efficacy data currently link piperaquine to anti-echinococcal activity. The single supporting reference is a broad pipeline review of anti-infective drug candidates for NTDs, which mentions piperaquine only as a theoretical candidate for cross-activity — not as a drug with demonstrated efficacy against *Echinococcus*.

**Note on the TxGNN second-ranked prediction:** Interestingly, TxGNN's next-highest-scoring prediction, *Plasmodium vivax* malaria (score 99.52%, rank 8192), is backed by 31 clinical trials (including multiple completed Phase 3 RCTs) and 20 publications, reaching evidence level L1. This reflects piperaquine's already-established antimalarial use rather than a genuinely new indication, but it may represent a more actionable near-term opportunity — e.g., supporting a market-entry or registration case for DHA-PPQ in India — compared to the highly speculative echinococcosis signal that is the primary subject of this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Review | Parasites & Vectors | Pipeline review of oral anti-infective drugs for neglected tropical diseases; piperaquine mentioned only as a theoretical off-label candidate within the broader NTD drug-development landscape, without direct efficacy data against echinococcosis |

---

## India Market Information

Piperaquine currently has no registered products in India (0 registrations, market status: Not Marketed). No dosage form or approved-indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The cystic echinococcosis prediction rests on a high TxGNN score but almost no independent evidence — a single review paper with no direct efficacy data and zero clinical trials (evidence level L4). This does not meet the bar for further investment at this time.

**To proceed, the following is needed:**
- In vitro/in vivo efficacy data of piperaquine against *Echinococcus granulosus*
- Mechanism of action (MOA) data confirming or refuting cross-activity against cestodes
- TFDA/CDSCO-equivalent safety labeling (warnings, contraindications, DDI) — currently a blocking data gap
- Separately, consider evaluating the well-supported *Plasmodium vivax* malaria indication (L1 evidence, "Proceed with Guardrails") as a distinct, more mature opportunity for India market entry via the DHA-piperaquine combination
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

