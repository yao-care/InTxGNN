---
layout: default
title: Piroxicam
parent: Model Prediction Only (L5)
nav_order: 680
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Piroxicam: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis"
monitor_inn: "Piroxicam"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
---

# Piroxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Piroxicam: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Piroxicam is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis and osteoarthritis.
The TxGNN model's top-ranked prediction is **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental syndrome, but **no clinical trials and no publications** support it, and no plausible mechanistic link has been identified. The best-supported alternative among the model's predictions is **juvenile idiopathic arthritis (JIA)**, which has 10 publications but no registered clinical trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis (the data compiled for this report contain no approved-indication text from the India licences) |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome (top-ranked prediction) |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Piroxicam is generally known as a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin-mediated inflammation and pain. This is consistent with its use in rheumatoid arthritis and osteoarthritis.

For the top-ranked prediction, **no mechanistic link is identified**. Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare developmental skeletal and ocular syndrome, and COX inhibition has no known role in its underlying biology. The very high score is most likely a knowledge-graph artifact, probably driven by graph proximity to skeletal or arthropathy terms. The other top-ranked predictions (brachydactyly-syndactyly syndrome, Hunter-Thompson acromesomelic dysplasia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, WHIM syndrome) show the same pattern: very high scores, no trials, no literature, and no plausible mechanism.

Two lower-ranked predictions are somewhat more plausible:
- **Juvenile idiopathic arthritis (score 99.93%)**: NSAID symptom control is mechanistically consistent with piroxicam's known action. Its long half-life allows once-daily dosing, and paediatric pharmacokinetic data exist. However, the evidence is largely historical (1980s–1990s) and symptomatic rather than disease-modifying, and JIA management has since shifted to DMARDs and biologics.
- **Rheumatoid nodulosis and pseudoachondroplasia**: these are only indirectly plausible (related to rheumatoid arthritis, or general analgesic use for joint pain), with no specific supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the ten predicted indications evaluated.

## Literature Evidence

No literature is available for the top-ranked prediction. The most relevant literature, for the best-supported alternative (juvenile idiopathic arthritis), is shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | RCT | British Journal of Rheumatology | 8-week double-blind crossover study of piroxicam vs naproxen in 47 children with seronegative juvenile chronic arthritis; no significant difference between treatments |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Clinical study | European Journal of Rheumatology and Inflammation | 26 patients with juvenile rheumatoid arthritis randomised to piroxicam or naproxen; painful and swollen joint counts decreased significantly |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic review / network meta-analysis | World Journal of Clinical Cases | Compares different NSAIDs for JIA (the available abstract does not state the conclusions) |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic review / network meta-analysis | Indian Pediatrics | Compares the efficacy and safety of nine NSAIDs in JIA |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic study | European Journal of Clinical Pharmacology | Ten children aged 7–16 on once-daily piroxicam; mean half-life about 32.6 hours |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Review | Kinderarztliche Praxis | Overview of drug therapy for juvenile chronic arthritis, including piroxicam |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Long-term follow-up | Clinical Rheumatology | Long-term toxicity of antirheumatic and anti-inflammatory drugs in 117 children from a paediatric rheumatology clinic |

## India Market Information

Piroxicam has 20 valid single-ingredient registrations in India and none cancelled. The data compiled for this report contain no approved-indication text for any of them. Five representative authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 29607 | Brexic 20mg Tablet DT | Strip of 10 dispersible tablets | Not available |
| 112407 | Inflavan 20mg Tablet | Strip of 10 tablets | Not available |
| 187487 | Roxicam 20mg Injection | Vial of 2 ml injection | Not available |
| 125369 | Lonex 8mg Tablet DT | Strip of 10 dispersible tablets | Not available |
| 61054 | Dupox 40mg Injection | Vial of 2 ml injection | Not available |

Available forms include oral dispersible tablets, standard tablets, and orally disintegrating (MD) tablets, as well as injectables (vials and ampoules).

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: hypertension, kidney disease, liver disease (including acute liver failure, hepatitis and drug-induced liver injury), gallbladder disease, congestive heart failure, myocardial infarction and other cardiovascular or heart disease, stroke and cerebrovascular disorders, thrombotic disease, blood coagulation disease, active peptic ulcer disease, anaemia and haemoglobinopathy, substance abuse/dependence, and vision disorders.
- **Drug Interactions**: 216 interactions were recorded. Examples at Moderate level include acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, sulfonylureas (chlorpropamide, glimepiride), mesalazine, balsalazide, aprepitant, and potassium salts. Minor-level examples include famotidine, ranitidine, cimetidine, and linaclotide.

Package insert warnings and contraindications were not available; please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a very high model score but no clinical trials, no literature, and no plausible mechanism, so it is most likely a knowledge-graph artifact. The best-supported alternative, juvenile idiopathic arthritis, has some historical evidence (L3) but is not a new, disease-modifying use, since NSAID symptom control is already established and care has moved to DMARDs and biologics.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licences (currently blocking safety screening)
- Detailed mechanism of action data from DrugBank
- For JIA: a focused review of current NSAID positioning against DMARDs and biologics, and the conclusions of the 2021 and 2024 network meta-analyses
- Approved-indication text for the India registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

