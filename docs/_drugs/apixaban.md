---
layout: default
title: Apixaban
parent: Model Prediction Only (L5)
nav_order: 62
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "Apixaban"
predicted_indications: ["migraine disorder"]
description: "Apixaban: predicted new indication Migraine disorder (evidence level L5). In India: at least 20 listed products"
---

# Apixaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Apixaban: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Apixaban is an oral anticoagulant that inhibits factor Xa. The TxGNN model predicts it may be relevant to **migraine disorder**, but the evidence level is **L5**: no study supports apixaban for migraine. The one listed clinical trial addresses stroke recurrence after patent foramen ovale, not migraine, and the case reports describe migraine with aura that worsened or did not resolve on apixaban.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9902 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for apixaban: "Apixaban is a selective inhibitor of FXa. It does not require antithrombin III for antithrombotic activity. Apixaban inhibits free and clot-bound FXa, and prothrombinase activity. Apixaban has no direct effect on platelet aggregation, but indirectly inhibits platelet aggregation induced by thrombin." ([DailyMed: Eliquis (apixaban) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41a133ef-e461-48ad-8221-b735bdd0ec25), label version 2026-09-24; accessed 2026-11-19.) Apixaban is known as a direct factor Xa inhibitor used as an anticoagulant.

The proposed link is thromboembolic. Migraine with aura has been associated with paradoxical embolism through a patent foramen ovale and with antiphospholipid antibodies, so anticoagulation could plausibly affect migraine in selected patients.

However, the available case reports describe migraine with aura worsening after starting apixaban, and no benefit compared with warfarin. This argues against a consistent therapeutic effect. The high model score is not supported by clinical data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulants vs antiplatelet therapy to prevent stroke recurrence. Migraine is not the primary endpoint, the population is cryptogenic stroke patients, and apixaban is not clearly the studied anticoagulant. Only indirectly related. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Retrospective study (75 patients) | Lupus | Response to antithrombotic therapy in refractory migraine with antiphospholipid antibodies. The drugs studied and the design should be verified. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case report and review | The Neurologist | Migraine with aura worsened after starting apixaban. The authors note that literature on direct oral anticoagulants in migraine is scarce and controversial. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case report | Headache | Migraine with aura remained in remission on warfarin for 12 years, returned within 3 weeks of switching to apixaban, and resolved again on resuming warfarin. |

## India Market Information

At least 20 valid single-ingredient licences are recorded, and the list may be partial. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 72922 | Eliquis 2.5mg Tablet (Pfizer Ltd) | Strip of 14 tablets | Not recorded |
| 72362 | Eliquis 5mg Tablet (Pfizer Ltd) | Box of 20 tablets | Not recorded |
| 174055 | Pixaflo 2.5mg Tablet (Lupin Ltd) | Strip of 10 tablets | Not recorded |
| 174532 | Paxiba 5 Tablet (Glenmark Pharmaceuticals Ltd) | Strip of 10 tablets | Not recorded |
| 243850 | Xapilis 5 Tablet (Abbott) | Strip of 14 tablets | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded. Major-level examples include acetylsalicylic acid, cobicistat, deferasirox, ibritumomab tiuxetan and tositumomab. Moderate-level examples include aprepitant, clarithromycin, dexamethasone, miconazole and rolapitant.
- Case reports suggest apixaban may worsen migraine with aura in some patients.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. No study supports apixaban for migraine, and the available case reports point to worsening or no benefit. The high model score is not backed by clinical data.

**To proceed, the following is needed:**
- Controlled studies that directly assess apixaban in migraine, ideally in subgroups with PFO or antiphospholipid antibodies
- Detailed mechanism of action data
- Package insert warnings and contraindications
- Review of the reported worsening of migraine with aura on apixaban

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Eliquis (apixaban) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41a133ef-e461-48ad-8221-b735bdd0ec25) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

