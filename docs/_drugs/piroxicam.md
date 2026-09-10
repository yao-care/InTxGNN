---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 673
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From NSAID Therapy for Rheumatic Disease to Juvenile Idiopathic Arthritis

> **Note on indication selection:** TxGNN returned 10 candidate indications for Piroxicam. Ranks 1–8 (ultra-rare congenital/genetic syndromes such as colobomatous microphthalmia-rhizomelic dysplasia, brachydactyly-syndactyly syndrome, WHIM syndrome, etc.) carry the highest raw TxGNN scores, but the model's own mechanistic rationale for each explicitly states there is **no plausible pharmacological link** and **zero supporting evidence** — these likely reflect disease-node similarity artifacts in the knowledge graph rather than real repurposing signals. This report therefore focuses on **rank 10: Juvenile Idiopathic Arthritis (JIA)**, the only candidate backed by substantive literature and a coherent mechanism.

## One-Sentence Summary

Piroxicam is a classic non-selective COX-1/COX-2 inhibitor (NSAID) historically used for rheumatic and musculoskeletal inflammatory pain. The TxGNN model predicts it may be effective for **Juvenile Idiopathic Arthritis**, a prediction supported by **13 publications**, including two piroxicam-specific pediatric RCTs from the 1980s, though **no clinical trials are currently registered** for this specific drug-disease pair.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as a registered India label (drug not marketed); literature context describes Piroxicam as an NSAID for rheumatoid arthritis, osteoarthritis, and ankylosing spondylitis |
| Predicted New Indication | Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on known information, Piroxicam is a traditional non-selective COX-1/COX-2 inhibitor that reduces prostaglandin synthesis, producing anti-inflammatory and analgesic effects — this classification is consistent throughout the literature evidence collected (e.g., PMID 3539573 lists piroxicam alongside aspirin, ibuprofen, and naproxen as therapy for "rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, musculoskeletal disorders").

Juvenile Idiopathic Arthritis is characterized by chronic synovial inflammation, mechanistically identical to the adult rheumatic conditions Piroxicam is already known to treat. The prostaglandin-inhibition pathway targeted by Piroxicam directly addresses the joint inflammation and pain driving JIA symptoms, making this one of the more mechanistically coherent NSAID repurposing candidates rather than a novel biological hypothesis.

This is corroborated by direct historical evidence: Piroxicam was already studied head-to-head against naproxen in pediatric JCA/JRA populations in the 1980s (PMID 2957205, PMID 3510686), both showing comparable efficacy to an established NSAID comparator. More recent systematic reviews and network meta-analyses (2021, 2024) continue to evaluate NSAIDs, including piroxicam, as a treatment class for JIA.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | RCT | European Journal of Rheumatology and Inflammation | 26 children (age 3–25) with juvenile rheumatoid arthritis randomized to piroxicam or naproxen; painful/swollen joint counts decreased significantly with piroxicam |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT | British Journal of Rheumatology | Multicentre 8-week double-blind cross-over study, piroxicam vs. naproxen in 47 children with seronegative JCA (age 5–16); no significant difference between treatments |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Review (Network Meta-analysis) | World Journal of Clinical Cases | Systematic review/network meta-analysis of various NSAIDs (including piroxicam) for JIA; optimal regimen still undetermined |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Review (Meta-analysis) | Indian Pediatrics | Systematic review/network meta-analysis comparing efficacy and safety of nine NSAIDs in JIA patients |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic Study | European Journal of Clinical Pharmacology | Steady-state PK of piroxicam (0.4 mg/kg once daily) in 10 children with rheumatic disease; Cmax 3.6–9.8 mg/L, half-life ~32.6h |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Review (Safety) | Clinical Rheumatology | Long-term toxicity study of antirheumatic/anti-inflammatory drugs (155 NSAID exposures) in a pediatric rheumatology cohort |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderärztliche Praxis | Discusses pharmacologic therapy of juvenile chronic arthritis, highlighting piroxicam and sulfasalazine as treatment options |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohort | International Ophthalmology | Chronic iridocyclitis frequency (56%) in ANA-positive pauciarticular JCA; no ocular complications during follow-up |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review | Critical Reviews in Therapeutic Drug Carrier Systems | Reviews microencapsulation drug-delivery systems for NSAIDs across arthritis types, including JIA |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Review | Drugs | Nabumetone therapeutic/safety review in OA and RA, contextualizing NSAID class comparisons |

## India Market Information

Piroxicam is not currently marketed in India (0 registered licenses); no product registration data is available.

## Safety Considerations

- **Drug Interactions**: 216 documented interactions on record (sample of 20 provided). Notable **Moderate**-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetics (metformin, glimepiride, chlorpropamide), acetylsalicylic acid, and aminosalicylates (mesalazine, balsalazide) — combinations that may increase GI bleeding risk or affect glycemic control. **Minor**-level interactions include H2-receptor antagonists (famotidine, ranitidine, cimetidine) and linaclotide.

Key warnings and contraindication data are not currently available (Blocking-severity data gap — TFDA/India label text not yet obtained); please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two piroxicam-specific pediatric RCTs plus recent systematic reviews/meta-analyses of NSAIDs in JIA provide L1-level evidence with a mechanistically direct rationale (COX inhibition → reduced synovial inflammation). However, the drug has no current India market presence and lacks formal label/safety documentation, so guardrails are required before advancing.

**To proceed, the following is needed:**
- TFDA/India package insert warnings and contraindications (currently a Blocking data gap)
- Formal mechanism-of-action documentation from DrugBank (currently a High-severity data gap)
- Confirmation of whether any modern, registered clinical trials evaluate piroxicam specifically in JIA (existing RCTs are from the 1980s)
- A pediatric-specific safety monitoring plan given the long-term GI/renal risk profile of NSAID use in children
- Re-review of ranks 1–8 candidates is not recommended given the absence of any mechanistic or evidentiary support noted by the model itself
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

