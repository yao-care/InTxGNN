---
layout: default
title: Midazolam
parent: Moderate Evidence (L3-L4)
nav_order: 550
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-28
description: "Midazolam: predicted new indication Insomnia (evidence level L3). Approved use: Anxiety"
monitor_inn: "Midazolam"
predicted_indications: ["insomnia (disease)"]
---

# Midazolam
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **1** 
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

## Midazolam: From Anxiety to Insomnia
{: .text-alpha }

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine, originally used for anxiety and sedation.
The TxGNN model predicts it may be effective for **insomnia**,
with **2 clinical trials** (both only indirectly relevant) and **10 publications** (several directly studying oral midazolam as a hypnotic) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L3 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on the known pharmacology of the class, midazolam is a short-acting benzodiazepine that enhances GABA-A receptor-mediated inhibitory neurotransmission, producing sedative-hypnotic effects.

This mechanism is shared with approved benzodiazepine hypnotics such as flurazepam and triazolam. Anxiety and insomnia often occur together and both respond to enhanced inhibitory signalling, so the biological link is plausible.

Oral midazolam has also been studied, and in some countries used, as a hypnotic. The prediction is therefore closer to the rediscovery of an existing use than a novel repurposing. The very high TxGNN score is a computational prediction and does not replace clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Dexmedetomidine vs midazolam sedation with spinal anaesthesia: postoperative sleep quality after transurethral prostatic resection. Midazolam was the comparator, in a perioperative setting rather than chronic insomnia |
| [NCT00886314](https://clinicaltrials.gov/study/NCT00886314) | Not applicable | Unknown | 80 | Clown doctors vs sedative premedication for preoperative anxiety in children. Not related to insomnia |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | Randomized, double-blind, multicenter trial | J Clin Psychopharmacol | Flurazepam vs midazolam over 14 days in chronic insomniacs, assessing sleep, performance and mood |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | Multicenter clinical trial | J Clin Psychopharmacol | Executive summary of the 14-day flurazepam vs midazolam study in chronic insomniacs (sleep, performance, plasma levels) |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | Double-blind trial | Br J Clin Pharmacol | Midazolam 15 mg vs Vesparax in 30 patients with insomnia secondary to neuromuscular disease. Both were effective hypnotics, and midazolam was better tolerated without hangover effects |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Dose-finding study | Arzneimittel-Forschung | Oral midazolam 10-30 mg in 75 hospitalized patients with mild to moderate secondary insomnia, establishing the optimal dose range |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | Clinical use of hypnotics and the need for a variety of agents with differing pharmacokinetic profiles |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orv Hetil | Insomnia and cerebral hypoperfusion. General background, not midazolam-specific |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Pilot clinical study | J Clin Med | Lemborexant for insomnia and delirium prevention after endoscopic procedures. Midazolam is not the focus |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 135368 | Mezolam 5mg Injection | Vial of 5 ml injection | Not specified |
| 136398 | Medistat 0.5mg Tablet | Strip of 1 tablet | Not specified |
| 134770 | Midazom 0.5 Nasal Spray | Bottle of 5 ml nasal spray | Not specified |
| 140031 | Megarest 5mg Injection | Vial of 5 ml injection | Not specified |
| 133584 | Midacip Nasal Spray | Packet of 5 ml nasal spray | Not specified |

Twenty valid single-ingredient registrations are listed in total, covering injection, tablet and nasal spray forms.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease associations, not label text): chronic obstructive pulmonary disease (including severe early-onset), cirrhosis of liver, angle-closure glaucoma, and chronic kidney disease (including chronic renal failure and end-stage renal failure).
- **Drug Interactions**: 177 interactions were identified in total. Moderate-level examples include morphine, clarithromycin, cimetidine, ranitidine, omeprazole, bupropion, aprepitant, metoclopramide, miconazole, clotrimazole, dronabinol and nabilone. Minor-level examples include dexamethasone, betamethasone, magnesium oxide, aluminum hydroxide and calcium carbonate. Concomitant opioids and other central nervous system depressants warrant particular caution because of additive sedation and respiratory depression.

Package insert warnings were not available, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The supporting studies are mainly older (1981-1990) small trials of oral midazolam in secondary or chronic insomnia, and the two registered trials are only indirectly relevant. There is no recent Phase 3 evidence. The Indian registrations are mostly injectable and nasal forms, with no clear oral hypnotic presentation (a single tablet is listed, with no stated indication). The package insert safety review is still outstanding.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory source, as the safety screen cannot be completed without them
- Mechanism of action data confirmed from DrugBank
- Confirmation of which registered products and routes (especially oral) are suitable for a hypnotic use
- Review of the full text of the older insomnia trials, and a comparison with currently approved hypnotics
- A safety plan for patients with respiratory, hepatic or renal impairment, and for those on opioids or other central nervous system depressants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

