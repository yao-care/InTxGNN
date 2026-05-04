---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorphine: From Opioid Use Disorder / Pain Management to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial μ-opioid receptor agonist with established use in opioid use disorder (OUD) treatment and moderate-to-severe pain management.
The TxGNN model predicts it may be applicable to **Acute Intermittent Porphyria (AIP)**,
with **0 clinical trials** and **1 publication** currently available to support this direction — evidence remains extremely limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid use disorder; moderate-to-severe pain management |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Buprenorphine is a partial agonist at the μ-opioid receptor and an antagonist at the κ-opioid receptor, giving it a distinctive profile among opioid analgesics — high-ceiling analgesia with a lower respiratory depression risk compared to full agonists.

Acute Intermittent Porphyria (AIP) is a rare metabolic disorder caused by a deficiency in the heme biosynthesis enzyme hydroxymethylbilane synthase (HMBS). During acute attacks, patients experience debilitating neuropathic abdominal pain along with autonomic instability and, in severe cases, neuropsychiatric symptoms. The critical clinical challenge is that many common analgesics and sedatives are porphyrinogenic (i.e., they can trigger or worsen attacks by inducing ALA synthase), making pain management particularly difficult.

The predicted link here is not disease-modifying but rather **symptom-supportive**: buprenorphine, as a non-porphyrinogenic opioid, is considered relatively safe for AIP pain management. The 1993 Japanese case report in the evidence pack describes anesthetic management in a patient with suspected AIP undergoing major surgery, which tangentially supports the notion that opioids (including agents in this class) can be used with caution in this population. However, this is a symptomatic analgesic application, not a targeted therapy addressing the underlying heme enzyme deficiency. The TxGNN model's high prediction score likely reflects the graph-level mechanistic compatibility rather than a novel disease-modifying role.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui (Japanese Journal of Anesthesiology) | Anesthetic management of a 40-year-old female with suspected AIP undergoing radical hysterectomy; describes the challenges of selecting porphyria-safe agents perioperatively. Buprenorphine is not directly evaluated but the case highlights the importance of opioid selection in AIP patients. |

---

## India Market Information

Buprenorphine currently has **no registered products** in the Indian market. No authorization records are available.

---

## Safety Considerations

**Drug Interactions:** A total of **264 drug-drug interactions** have been identified in the DDI database. Key interactions include:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Alvimopan | **Major** | Opioid antagonist; concurrent use may precipitate withdrawal or loss of analgesic effect |
| Morphine | **Major** | Combined opioid use increases risk of CNS/respiratory depression |
| Bupropion | **Major** | May lower seizure threshold and alter opioid metabolism via CYP2D6 inhibition |
| Cisapride | **Major** | Risk of QT prolongation and potentially fatal arrhythmias |
| Dolasetron | **Major** | Additive QT prolongation risk |
| Famotidine | Moderate | May affect buprenorphine absorption/metabolism |
| Clarithromycin | Moderate | CYP3A4 inhibition may increase buprenorphine plasma levels |
| Dexamethasone | Moderate | CYP3A4 induction may reduce buprenorphine efficacy |
| Hyoscyamine / Atropine / Dicyclomine | Moderate | Additive anticholinergic effects |
| Loperamide | Moderate | Combined opioid effects on GI motility |

Please refer to the package insert for full warnings and contraindications, as these data were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for buprenorphine in acute intermittent porphyria is limited to a single indirect case report from 1993, with zero registered clinical trials. The proposed mechanism is symptomatic (analgesic support) rather than disease-modifying, and the drug is not currently approved or marketed in India, creating additional regulatory barriers.

**To proceed, the following is needed:**

- Obtain the India/CDSCO package insert to assess key warnings, contraindications, and approved label language before any safety evaluation can proceed
- Retrieve complete MOA data from DrugBank API (DB00921) to enable rigorous mechanistic analysis
- Conduct a targeted literature review specifically examining buprenorphine (not opioids generally) as a safe analgesic in AIP, distinguishing it from porphyrinogenic agents
- Explore whether any AIP pain management guidelines (e.g., European Porphyria Network / EPNET) list or exclude buprenorphine by name
- If the intended application is purely symptomatic analgesia in AIP attacks, consider whether a full repurposing program is warranted versus a prescribing guidance / formulary inclusion initiative
- Clarify the regulatory pathway for introducing buprenorphine to the Indian market, including controlled substance scheduling requirements

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

