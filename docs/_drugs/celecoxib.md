---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Arthritis Management to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib (Celebrex) is a selective COX-2 inhibitor used globally for osteoarthritis, rheumatoid arthritis, and related inflammatory conditions, though it currently has no registered products in India.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (including ankylosing spondylitis and axial spondyloarthritis),
with **19 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India regulatory data; globally indicated for OA, RA, ankylosing spondylitis, JIA, acute pain |
| Predicted New Indication | Inflammatory Spondylopathy |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, Celecoxib is a selective cyclooxygenase-2 (COX-2) inhibitor — the first of the "coxib" class to enter clinical practice. By selectively inhibiting COX-2 without meaningful COX-1 inhibition, it suppresses prostaglandin E2 (PGE2) production at sites of inflammation while sparing gastric prostaglandin synthesis, delivering anti-inflammatory efficacy with a significantly improved gastrointestinal safety profile compared to non-selective NSAIDs.

Inflammatory spondylopathy — encompassing ankylosing spondylitis (AS), axial spondyloarthritis (axSpA), and psoriatic arthritis with spinal involvement — shares a core inflammatory cascade driven by IL-17 and TNF-mediated enthesitis and pathological new bone formation. PGE2 plays a central role in this process: it amplifies IL-17 and TNF signalling at entheseal sites and drives osteoblast differentiation through Wnt pathway modulation. By suppressing PGE2, Celecoxib directly targets these mechanisms, placing it squarely within the disease's pathophysiology.

What makes this prediction particularly compelling is Celecoxib's structural advantage over other NSAIDs. A 2025 systematic review and meta-analysis (PMID 39757202) demonstrated that Celecoxib is the **only NSAID capable of inhibiting radiographic spinal progression** (bone bridge formation) in spondyloarthritis — a property not replicated by diclofenac or other COX inhibitors. This likely occurs through Celecoxib's unique suppression of PGE2-dependent Wnt signalling in bone-forming cells, elevating its therapeutic rationale from symptomatic control to potential disease modification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week RCT comparing celecoxib 200mg QD, 200mg BID, and diclofenac in AS; confirmatory efficacy and safety trial across dose levels |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Double-blind RCT of celecoxib 200mg QD vs diclofenac 75mg SR in Chinese AS patients with 6-week extension; pivotal evidence for Asian population |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: celecoxib added to golimumab vs golimumab alone in radiographic axSpA — evaluates impact on structural spinal damage progression over 2 years |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Multi-center open-label RCT of etanercept alone, celecoxib alone, or combination in active AS over 54 weeks; includes MRI SPARCC scoring of sacroiliac joints |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | 12-week RCT of celecoxib 200mg QD vs 400mg QD vs diclofenac TID in AS; confirms findings of earlier 6-week Phase 3 study |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | Completed Phase 4 trial evaluating NSAID effects on MRI-detected inflammatory lesions in axial spondyloarthritis |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | Multi-center RCT comparing Naxozol (naproxen + esomeprazole) vs celecoxib for GI protection and pain relief in OA/RA/AS; celecoxib used as active comparator |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Large trial optimizing TNF inhibitor dose reduction in stable AS; celecoxib included as background therapy, providing real-world combination data |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | Innovative N-of-1 trial comparing selective COX-2 vs non-selective COX inhibitors for individualized treatment in axSpA; terminated early, limiting conclusions |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Pilot RCT comparing 4 NSAIDs in axial spondyloarthritis over 6 weeks; terminated early due to recruitment challenges — no valid conclusions extractable |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Systematic Review / Meta-analysis | BMB Reports | Celecoxib is the only NSAID shown to inhibit radiographic bone progression (ankylosis) in SpA, potentially via PGE2-dependent Wnt pathway suppression — unique mechanistic differentiation |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | RCT / Mechanistic Study | Clinical Rheumatology | Imrecoxib vs celecoxib in axSpA: both COX-2 inhibitors reduce sacroiliac joint inflammation by regulating bone metabolism markers and angiogenesis |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Medical Science Monitor | Imrecoxib vs celecoxib in axSpA (n=51): both show significant clinical response; DKK-1 serum levels correlate with imaging score changes |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT | Annals of the Rheumatic Diseases | CONSUL trial results: celecoxib + golimumab vs golimumab alone — structural damage and radiographic progression data in r-axSpA over 2 years |
| [38832489](https://pubmed.ncbi.nlm.nih.gov/38832489/) | 2024 | RCT | Scandinavian Journal of Rheumatology | Iguratimod + celecoxib vs celecoxib alone in active axSpA: randomized, double-blind, placebo-controlled; celecoxib as backbone therapy |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Cohort / Real-World Evidence | Scandinavian Journal of Rheumatology | Nationwide cohort study: CVD and GI bleeding risk is comparable between celecoxib and nsNSAIDs in AS patients — reassuring long-term safety profile |
| [27603385](https://pubmed.ncbi.nlm.nih.gov/27603385/) | 2016 | Population-Based Case-Control | Medicine | Taiwan NHI database (n=4,829 AS patients): celecoxib use associated with reduced risk of coronary artery disease in AS — potential cardioprotective signal |
| [25623277](https://pubmed.ncbi.nlm.nih.gov/25623277/) | 2015 | Cohort | Arthritis Care & Research | Swedish national cohort: comparative safety of etoricoxib, celecoxib, and nsNSAIDs in AS/SpA — GI, renal, and cardiovascular event rate comparison |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Systematic Review | Drugs | Comprehensive review of celecoxib clinical evidence in OA, RA, and AS; confirms superior GI tolerability and established efficacy across inflammatory arthritis |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | RCT | Journal of Rheumatology | Early pivotal RCT demonstrating celecoxib efficacy and tolerability in AS patients; foundational evidence supporting the AS indication |

---

## India Market Information

Celecoxib currently has **no registered products in India**. There are 0 licenses on record.

> Celecoxib is commercially available internationally under the brand name **Celebrex®** (Pfizer) and has regulatory approval in the United States, European Union, Japan, China, and other markets for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, juvenile idiopathic arthritis (≥2 years), acute pain, and primary dysmenorrhea. A formal CDSCO registration application would be required before any India deployment.

---

## Safety Considerations

**Drug Interactions**: Celecoxib has **646 documented drug interactions** on record. Clinically significant interactions include:

| Severity | Interacting Drug(s) | Clinical Implication |
|----------|---------------------|----------------------|
| **Major** | Eliglustat | Avoid combination; celecoxib may significantly increase eliglustat exposure via CYP2C8 inhibition, risking cardiac arrhythmia |
| Moderate | Hydrocortisone | Combined use increases GI adverse effect risk; monitor for gastric symptoms |
| Moderate | Glimepiride, Glipizide, Glyburide, Nateglinide, Acetohexamide | NSAIDs may potentiate hypoglycaemic effects of sulfonylureas and secretagogues; monitor blood glucose |
| Moderate | Metformin, Exenatide | Monitor glycaemic control; pharmacodynamic interaction in diabetic patients |
| Moderate | Metronidazole | Monitor for adverse effects; potential pharmacokinetic interaction |
| Moderate | Levofloxacin, Kanamycin | Monitor closely; increased risk of CNS or renal adverse effects |
| Moderate | Mesalazine, Balsalazide, Olsalazine | Concurrent use with aminosalicylates may increase renal toxicity risk; monitor renal function |
| Moderate | Cimetidine | Cimetidine inhibits CYP2C9/2D6, potentially increasing celecoxib plasma levels |
| Moderate | Naltrexone | Monitor for altered pain response or reduced analgesic efficacy |

**Monitoring Requirements for Long-Term Use in Inflammatory Spondylopathy:**
- **Cardiovascular**: APTC event risk (MI, stroke, arterial thrombosis) is elevated with chronic NSAID use; baseline and periodic cardiovascular risk assessment required
- **Renal**: Serum creatinine and eGFR — a 2024 cohort study (PMID 39315555) confirms long-term NSAID use in AS patients affects liver and kidney function
- **Hepatic**: AST and ALT monitoring with prolonged therapy

> Formal package insert warnings and contraindications (CDSCO/TFDA label data) were not available in this evidence pack. Please refer to the current Celebrex® prescribing information for complete contraindication and precaution details before clinical deployment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs directly evaluating celecoxib in ankylosing spondylitis (including NCT00648141, n=458 and NCT00762463, n=240), combined with a 2025 meta-analysis uniquely identifying celecoxib as the only NSAID capable of inhibiting radiographic spinal progression, provide robust L1 evidence supporting the inflammatory spondylopathy indication. However, celecoxib is entirely unregistered in India, carries 646 drug interactions, and requires cardiovascular and renal risk management for the long-term AS patient population.

**To proceed, the following is needed:**
- **India registration**: File a CDSCO New Drug Application (NDA) — the drug is currently unregistered in India (0 licenses); international approval data (US FDA, EMA) can support a bridging strategy
- **Package insert review**: Obtain complete CDSCO-compliant labelling with India-specific warnings, contraindications, and dosing guidance
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank API (flagged as data gap DG002) to strengthen dossier
- **Cardiovascular risk management plan**: Establish baseline CV risk stratification protocol and monitoring schedule for the target AS/axSpA population, given the known APTC event signal with chronic NSAIDs
- **DDI risk framework**: Develop prescriber guidance for the 646 documented interactions, with priority focus on the Major interaction with Eliglustat and Moderate interactions in diabetic patients on sulfonylureas or insulin secretagogues
- **Renal and hepatic monitoring protocol**: Define minimum monitoring intervals for long-term use (at least 6-monthly creatinine and liver enzymes), consistent with rheumatology society guidelines for chronic NSAID therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

