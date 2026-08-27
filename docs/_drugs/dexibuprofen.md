---
layout: default
title: Dexibuprofen
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Dexibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dexibuprofen: From Pain & Inflammation to Ankylosing Spondylitis

## One-Sentence Summary

Dexibuprofen is the pharmacologically active S(+)-enantiomer of ibuprofen, a non-steroidal anti-inflammatory drug (NSAID) widely used for pain relief, fever reduction, and inflammatory conditions.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**—a chronic inflammatory arthritis of the spine—with **0 clinical trials** but **3 published studies** (including a systematic review of randomised controlled trials) currently supporting this direction.
Among the 10 TxGNN-predicted indications, ankylosing spondylitis stands out as the only candidate with meaningful biological plausibility and real-world literature support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, fever, and inflammatory conditions (general NSAID use) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L2 (Systematic Review of RCTs available) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Dexibuprofen is the S(+)-enantiomer of ibuprofen—the biologically active form that carries the full COX-inhibitory activity of the racemate. By selectively inhibiting cyclooxygenase enzymes (COX-1 and COX-2), it reduces prostaglandin E₂ (PGE₂) synthesis, thereby suppressing inflammation, pain, and fever. Because the inactive R(-)-enantiomer is eliminated, the same therapeutic effect is achievable at roughly half the total drug load compared to racemic ibuprofen.

Ankylosing spondylitis (AS) is a chronic HLA-B27–associated spondyloarthropathy characterised by axial inflammation, progressive spinal ankylosis, and elevated prostaglandin activity. The PGE₂/COX pathway is directly implicated in three key AS disease processes: (1) PGE₂ promotes IL-17 production and Th17 cell differentiation, amplifying the inflammatory cascade; (2) PGE₂ stimulates osteoclast activation and suppresses osteoprotegerin (OPG), driving the paradoxical bone loss and pathological new-bone formation that define AS; and (3) PGE₂ mediates the spinal pain and morning stiffness that are the hallmark symptoms of active disease.

NSAIDs are already the first-line pharmacological treatment for AS per the 2022 ASAS/EULAR guidelines. Dexibuprofen offers a theoretically cleaner pharmacokinetic profile—equivalent COX inhibition at a lower total dose, with improved gastrointestinal tolerability compared to racemic ibuprofen. Clinical data from the 1990s (Seractil® programme) included double-blind RCTs in patients with ankylosing spondylitis specifically, making this prediction biologically and clinically plausible rather than a computational artefact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dexibuprofen in ankylosing spondylitis.

> **Note:** NSAIDs as a drug class have extensive trial data in AS (diclofenac, naproxen, celecoxib). However, Dexibuprofen-specific AS trials have not been registered in ClinicalTrials.gov or ICTRP. Existing evidence derives from older European RCT programmes conducted before mandatory trial registration.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9013382](https://pubmed.ncbi.nlm.nih.gov/9013382/) | 1996 | Systematic Review of RCTs | Journal of Clinical Pharmacology | Re-evaluation of multiple double-blind RCTs of Dexibuprofen (Seractil®) across inflammatory and degenerative diseases including ankylosing spondylitis, rheumatoid arthritis, gonarthrosis, and lumbar syndrome; used Mann-Whitney statistics with confidence intervals for standardised cross-disease efficacy comparison |
| [11771569](https://pubmed.ncbi.nlm.nih.gov/11771569/) | 2001 | Narrative Clinical Review | Clinical Rheumatology | Overview of Dexibuprofen clinical programme: 8 GCP-compliant trials (1,463 patients), 6 double-blind studies vs. placebo, racemic ibuprofen, and diclofenac; meta-analysis of 5 trials; data on dose-finding, pharmacokinetics, tolerability, and special indications including rheumatological conditions |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Technology/Formulation Review | Critical Reviews in Therapeutic Drug Carrier Systems | Reviews microencapsulation strategies for NSAIDs including Dexibuprofen in arthritis management (osteoarthritis, rheumatoid arthritis, septic arthritis, juvenile idiopathic arthritis, and ankylosing spondylitis), addressing challenges of joint-targeted drug delivery and tissue degeneration retardation |

---

## India Market Information

Dexibuprofen (DB09213) currently has **no registered authorisations** in India. No product licences, dosage form approvals, or market authorisations are on record.

> This is a significant regulatory gap. To advance any repurposing programme, an entirely new regulatory submission (IND or NDA equivalent) would be required.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice:** TFDA/CDSCO package insert warnings and contraindications were not retrieved in this Evidence Pack (Data Gap DG001 — Severity: Blocking). Drug-drug interaction data also returned no results from the DDI database query. Before any clinical or regulatory action, a full safety dossier must be assembled from the approved SmPC (Seractil® is approved in several European markets) and DrugBank records.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ankylosing spondylitis is the only TxGNN-predicted indication for Dexibuprofen with credible biological grounding and published clinical data; NSAIDs are already the guideline-recommended first-line treatment for AS, and Dexibuprofen's COX-inhibitory mechanism is directly relevant to the prostaglandin-driven inflammatory pathways that drive AS symptoms and progression. The 1996 systematic review of RCTs (PMID 9013382) specifically included AS patients, providing L2-level evidence. However, Dexibuprofen is not registered in India and lacks a formal safety package in this submission, creating blocking gaps before any development pathway can be opened.

**To proceed, the following is needed:**

- **Regulatory safety package (Blocking — DG001):** Retrieve the approved European SmPC (Seractil®, Austria/Germany) and parse all warnings, contraindications, and special-population restrictions. This is required before Safety Stage 1 can be completed.
- **Mechanism of action documentation (High — DG002):** Query DrugBank API for full MOA, pharmacokinetics, and target data for Dexibuprofen to support mechanistic rationale in any regulatory submission.
- **Dexibuprofen-specific RCT data extraction:** The 1990s Seractil® clinical programme included AS-specific double-blind data; full trial reports should be obtained from the Mundipharma/STADA regulatory dossier or literature archives to determine effect size and safety profile vs. comparator NSAIDs.
- **India regulatory pathway assessment:** Since the drug is not marketed in India, determine whether a new drug application, bridging study strategy, or partnership with an existing NSAID manufacturer (racemic ibuprofen holders) would be the most efficient path to market.
- **Comparative effectiveness positioning:** Define the clinical value proposition vs. widely available NSAIDs (diclofenac, naproxen, celecoxib) in the Indian AS patient population — particularly the GI tolerability advantage at the lower enantiomeric dose.
- **Dismiss Ranks 1–7 and 10 as artefacts:** Brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia, acromesomelic dysplasia (Hunter-Thompson), brachyolmia-amelogenesis imperfecta, myosclerosis, brachyolmia, pseudoachondroplasia, and WHIM syndrome all represent topology proximity artefacts in the TxGNN knowledge graph (musculoskeletal/rare disease node clustering) with zero biological plausibility for COX inhibition and no supporting data; these should be formally closed as non-viable candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

