---
layout: default
title: Diazoxide
parent: Model Prediction Only (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Diazoxide: predicted new indication Alopecia (evidence level L5). Approved use: Hyperinsulinemic hypoglycemia (including insulinoma…"
monitor_inn: "Diazoxide"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Diazoxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Diazoxide: From Hyperinsulinemic Hypoglycemia to Alopecia

## One-Sentence Summary

Diazoxide is a KATP channel opener, originally used to treat hyperinsulinemic hypoglycemia, including insulinoma and congenital hyperinsulinism.
The TxGNN model's top-ranked predictions are hair-related conditions. The most clinically meaningful of these is **Alopecia** (score 99.91%), supported by **0 clinical trials** and **6 publications**. These are mostly indirect: reviews, case reports and one animal study.
This report evaluates alopecia (rank 4) as the lead candidate. The three higher-scoring predictions have no trials or literature at all, so they are covered only in the notes below the Quick Overview table.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperinsulinemic hypoglycemia (including insulinoma, congenital hyperinsulinism, islet cell adenomatosis). The approved indication text on the India licenses is blank |
| Predicted New Indication | Alopecia (the top-ranked prediction, hypotrichosis simplex of the scalp, has no supporting evidence) |
| TxGNN Prediction Score | 99.91% (alopecia); 99.96% for the top-ranked hypotrichosis simplex of the scalp |
| Evidence Level | L4 (preclinical and indirect evidence only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

**Notes on the other top predictions:**
- Hypotrichosis simplex of the scalp, congenital hypotrichosis milia and diffuse alopecia areata (ranks 1–3) have no trials or literature (L5).
- Hypertrichosis (rank 7) is an adverse effect of diazoxide, so the prediction is not a treatment opportunity.
- Autosomal dominant hyperinsulinism due to Kir6.2 deficiency (rank 10) falls within the original indication class. However, KATP channel variants often impair diazoxide response, and no specific evidence was retrieved.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Diazoxide is known to open KATP channels (SUR/Kir6.x). In the pancreas this suppresses insulin release, which explains its use in hyperinsulinemic hypoglycemia.

The link to hair disorders comes from a well-documented side effect: hypertrichosis. It has been reported in neonates and children on systemic diazoxide. In a Japanese post-marketing survey of 384 patients, it was the most common adverse reaction (8.6%). Diazoxide shares this property with minoxidil, whose sulfate metabolite is also a KATP opener. Minoxidil is a recognised hair-growth agent.

Supporting this, topical diazoxide induced hair regrowth in the bald scalps of macaques (PMID 2085505, PMID 8326148). The original and new indications are not pharmacologically related. The prediction rests on a shared channel-opening mechanism and a side-effect phenotype, not on any disease-pathway similarity. The high TxGNN score likely reflects hair-phenotype network proximity.

For alopecia areata (rank 3), the immune-mediated follicular attack is not addressed by KATP opening.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Alopecia-specific retrieved literature (no human efficacy study among them):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Animal study | J Dermatol Sci | Topical diazoxide acted on hair follicular growth in the bald scalp of stumptailed macaques, with systemic side effects monitored |
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Review | J Invest Dermatol | Topical minoxidil and diazoxide, both with hypertrichotic side effects, induced significant hair regrowth in bald macaque scalps |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Review | Drug Safety | Drug-induced hair loss and hair growth: incidence, management and avoidance |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Case report | Pediatr Dermatol | Generalised hypertrichosis from secondary minoxidil exposure; diazoxide listed among causative drugs (indirect) |
| [4340017](https://pubmed.ncbi.nlm.nih.gov/4340017/) | 1972 | Case series | Arch Dis Child | Fetal exposure to diazoxide in four infants born to treated mothers (indirect) |
| [20682429](https://pubmed.ncbi.nlm.nih.gov/20682429/) | 2010 | Review | Vet Clin North Am Exot Anim Pract | Medical management of insulinoma in ferrets, including diazoxide (indirect) |

Related safety and original-indication literature (from the hypertrichosis search):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30083030](https://pubmed.ncbi.nlm.nih.gov/30083030/) | 2018 | Post-marketing survey | Clin Pediatr Endocrinol | 384 children with hyperinsulinemic hypoglycemia: 30.5% had an adverse reaction; hypertrichosis 8.6%, water retention 8.3%, cardiac failure 3.4% |
| [40917359](https://pubmed.ncbi.nlm.nih.gov/40917359/) | 2025 | Real-world observational | Front Endocrinol | Diazoxide is first-line in congenital hyperinsulinism, but many patients still have hypoglycemia and side effects |
| [33483452](https://pubmed.ncbi.nlm.nih.gov/33483452/) | 2021 | Cohort | Pediatrics | Necrotizing enterocolitis in neonates with hyperinsulinemic hypoglycemia treated with diazoxide |
| [36726424](https://pubmed.ncbi.nlm.nih.gov/36726424/) | 2023 | Case report | Clin Med Insights Case Rep | Diazoxide-induced hypertrichosis in a neonate with transient hyperinsulinism |
| [37919617](https://pubmed.ncbi.nlm.nih.gov/37919617/) | 2024 | Long-term open-label study | Obesity | 1-year diazoxide choline extended-release in Prader-Willi syndrome |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 26462 | Balila 25mg Capsule (Jolly Healthcare) | Strip of 10 capsules | Not stated |
| 26294 | Balila Capsule (Jolly Healthcare) | Strip of 15 capsules | Not stated |

Both licences are valid single-ingredient oral products. The marketed forms are oral capsules. No topical formulation is registered, and the only animal evidence for hair regrowth used topical application.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these are model-derived associations, not package insert text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, kidney disease, kidney failure, uremia, pyoureter, liver disease, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, congestive heart failure, potassium deficiency, gout, hyperuricemia, cerebrovascular disorder and coronary artery disease.

**Drug interactions:** 209 interactions were identified. The 20 listed all carry a Moderate severity level. Main ones:
- Antidiabetic agents, whose glucose-lowering effect is opposed by diazoxide: acarbose, metformin, pioglitazone, chlorpropamide, acetohexamide, alogliptin, albiglutide, dulaglutide, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin.
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone.
- Others: bupropion, morphine, dronabinol.

**Reported adverse effects in the literature:** hypertrichosis, fluid retention, cardiac failure, necrotizing enterocolitis in neonates, petechial rash and acute renal failure.

Package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions are driven by the hypertrichosis side effect, and the evidence is limited to a macaque study, reviews and case reports. No human trial exists for any hair-loss indication. Systemic diazoxide also carries a substantial safety burden: fluid retention, cardiac failure and glucose interactions. The registered oral capsules are therefore poorly suited to a cosmetic or dermatological use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which currently block safety screening
- Mechanism of action data (MOA)
- Human data for a topical diazoxide formulation in androgenetic alopecia, with a registered topical product or a development plan
- Comparison against minoxidil, the existing KATP-opener standard, to show added value
- Systemic exposure and safety data for topical use
- For the Kir6.2 hyperinsulinism prediction (rank 10), a separate review of variant-specific diazoxide responsiveness in the congenital hyperinsulinism literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

