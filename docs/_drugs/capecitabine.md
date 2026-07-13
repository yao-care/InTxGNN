---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal and Breast Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug approved globally for colorectal cancer, breast cancer, and gastric cancer, but currently not authorized in India.
The TxGNN model predicts it may be effective for **Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS)** — an ultra-rare hereditary syndrome caused by APC gene promoter 1B mutations affecting fewer than 200 patients worldwide.
There are currently **no clinical trials** and **no published literature** specifically documenting capecitabine use in GAPPS, placing this prediction at evidence level **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer, breast cancer, gastric cancer (global approvals; no India authorization on record) |
| Predicted New Indication | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Capecitabine is a fluoropyrimidine prodrug that undergoes sequential enzymatic conversion to 5-fluorouracil (5-FU) in the body. The final and rate-limiting conversion step is catalyzed by thymidine phosphorylase (TP), an enzyme that is substantially overexpressed in tumor tissue relative to surrounding normal tissue. This tumor-selective activation allows 5-FU to accumulate preferentially at the cancer site, where it inhibits thymidylate synthase (TS) — a key enzyme in DNA synthesis — ultimately blocking tumor cell proliferation. *Note: DrugBank MOA data was not retrieved in this evidence pack (flagged as a data gap); the mechanism above reflects established pharmacological knowledge from the published literature.*

GAPPS is caused by heterozygous point mutations in the promoter 1B region of the APC gene, leading to carpet-like fundic gland polyposis across the gastric fundus and body, with a lifetime risk of adenocarcinoma transformation estimated at 25–30%. With fewer than 200 cases documented globally, it is among the rarest hereditary gastric cancer syndromes. The TxGNN model's prediction derives from the broad molecular similarity between GAPPS-associated adenocarcinoma and conventional gastric adenocarcinoma — the condition for which capecitabine has established efficacy. Gastric adenocarcinoma cells generally show high TP expression, which is the mechanistic basis for capecitabine sensitivity.

However, GAPPS-associated carcinomas arise from a distinct genetic background (germline APC mutation), predominantly in the fundal region, and may differ in their TP expression profile and 5-FU sensitivity from sporadic gastric adenocarcinoma. No systematic study of TP expression in GAPPS tumor tissue has been conducted. The prediction is therefore a biologically plausible extrapolation rather than one supported by direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug of 5-FU) |
| Myelosuppression Risk | Low to moderate (myelosuppression less frequent than intravenous 5-FU; neutropenia and thrombocytopenia reported in combination regimens) |
| Emetogenicity Classification | Low (oral fluoropyrimidines carry low emetogenic potential per ASCO/NCCN guidelines) |
| Monitoring Items | CBC with differential (baseline and each cycle), liver function tests, serum creatinine/CrCl (dose reduction required for CrCl 30–50 mL/min; contraindicated if CrCl < 30 mL/min), hand-foot syndrome (palmar-plantar erythrodysesthesia) grading at each visit |
| Handling Protection | Must follow cytotoxic drug handling regulations for oral chemotherapy agents — closed-system preparation, avoid crushing tablets, appropriate PPE for caregivers |

---

## Safety Considerations

**Drug Interactions (335 total interactions identified in this evidence pack):**

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Metronidazole | Moderate | Potential enhancement of anticoagulant/toxicity effects; monitor closely |
| Tinidazole | Moderate | Similar concern as metronidazole; clinical vigilance warranted |
| Levofloxacin | Minor | Monitor for additive effects |
| Aluminum hydroxide | Minor | May affect absorption; separate administration timing |
| Magnesium hydroxide | Minor | Same precaution as aluminum hydroxide |
| Magnesium carbonate | Minor | Same precaution as aluminum hydroxide |
| Magnesium oxide | Minor | Same precaution as aluminum hydroxide |
| Magaldrate | Minor | Same precaution as aluminum hydroxide |

Additional interactions of unknown clinical significance were identified with: Pantoprazole, Omeprazole, Lansoprazole, Metformin, Glimepiride, Simvastatin, Prednisone, Hydrocortisone, Morphine, Doxycycline, Atropine, Dolasetron.

Please refer to the package insert for complete warnings and contraindications. CDSCO package insert data was not retrieved in this evidence pack (flagged as a blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
GAPPS affects fewer than 200 patients globally, and there is no clinical trial, case report, or preclinical data supporting capecitabine use in this condition. The TxGNN prediction score reflects broad mechanistic analogy to gastric adenocarcinoma rather than any evidence specific to GAPPS, and the unique genetic context (germline APC 1B mutation) means efficacy cannot be assumed from conventional gastric cancer data.

**To proceed, the following is needed:**
- Characterization of TP/TS expression in GAPPS-associated adenocarcinoma tissue (biomarker rationale)
- International registry collaboration or rare disease consortium approach — single-center trials are not feasible given the extreme rarity
- Case report documentation of any fluoropyrimidine use in GAPPS patients who develop adenocarcinoma
- Retrieval of CDSCO/package insert data to complete the safety assessment (currently a blocking data gap per DG001)
- DrugBank MOA data retrieval to complete mechanistic analysis (DG002)
- Consider redirecting attention to higher-evidence gastric cancer subtypes in this evidence pack (e.g., **gastric tubular adenocarcinoma** at rank 2, evidence level L1, with 20 publications and multiple Phase 3 RCTs including the CLASSIC trial directly validating CAPOX)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

