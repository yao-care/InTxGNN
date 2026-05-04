---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (Tecentriq) is a humanized anti-PD-L1 monoclonal antibody immunotherapy, globally approved for multiple advanced cancers including urothelial carcinoma, non-small cell lung cancer, and hepatocellular carcinoma, though not currently registered in India.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma** — a clinically significant subtype of non-muscle invasive bladder cancer (NMIBC) — with **2 clinical trials** currently supporting this direction.
This prediction is biologically well-grounded: high PD-L1 expression is a hallmark of urothelial malignancies, and one of the supporting trials (NCT02844816, Phase 2, Completed) was specifically designed to enroll BCG-unresponsive NMIBC patients, including those with prostatic urethral involvement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma, NSCLC, hepatocellular carcinoma (global approvals; not registered in India) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on publicly known information, Atezolizumab is a humanized IgG1 monoclonal antibody that targets **PD-L1 (Programmed Death-Ligand 1)**. By blocking PD-L1 from binding to its receptors PD-1 and B7.1, it prevents tumor cells from suppressing cytotoxic T-cell activity — effectively "releasing the brakes" on the immune system to attack cancer cells. This mechanism has been validated across numerous solid tumors and is the basis for its global approvals.

Prostatic urethra urothelial carcinoma arises at the segment of urethra traversing the prostate and is classified as a high-risk subtype within NMIBC staging (T1/Tis with prostatic urethral involvement). Urothelial carcinomas throughout the urinary tract share a common molecular landscape, including **high PD-L1 expression rates (approximately 25–50%)** and elevated tumor mutational burden (TMB) — both well-established biomarkers of anti-PD-L1 responsiveness. This biological homology makes anti-PD-L1 therapy mechanistically applicable to this anatomical subtype without requiring a fundamentally different rationale.

Critically, NCT02844816 — a **Phase 2 completed trial** with 172 enrolled patients — was specifically designed for BCG-unresponsive NMIBC and explicitly included patients with prostatic urethral involvement (T1/Tis staging criteria). This is the strongest form of direct clinical evidence available for this predicted indication and directly supports the L2 evidence level assigned.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive NMIBC; enrolled patients with prostatic urethral involvement (T1/Tis); primary objective was to assess whether anti-PD-L1 immunotherapy can enable the immune system to attack BCG-refractory urothelial tumors and inhibit their growth and spread |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, Not Recruiting | 914 | Large-scale basket study of Cabozantinib + Atezolizumab across multiple solid tumors, with a dedicated advanced urothelial carcinoma cohort (bladder, renal pelvis, ureter, urethra); provides safety, tolerability, PK, and preliminary combination efficacy data relevant to the broader urothelial carcinoma class |

---

## Literature Evidence

Currently no related literature specifically for prostatic urethra urothelial carcinoma is available.

---

## India Market Information

Atezolizumab is **not currently registered or marketed in India**. No local authorization records exist in this dataset. Note that atezolizumab (Tecentriq®) holds global regulatory approvals from the US FDA and EMA across multiple indications; any clinical use in India would require a separate regulatory pathway.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-PD-L1 monoclonal antibody (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low (primary toxicity profile consists of immune-related adverse events [irAEs], not myelosuppression; CBC monitoring still recommended at baseline) |
| Emetogenicity Classification | Minimal (monoclonal antibody; not associated with chemotherapy-induced nausea/vomiting) |
| Monitoring Items | Liver function (AST, ALT, bilirubin), thyroid function (TSH, free T4), adrenal axis, blood glucose, serum creatinine, CBC — all required to detect irAEs early; ECG and pulmonary function if clinically indicated |
| Handling Protection | Standard biologic/monoclonal antibody handling procedures apply; **not** classified as a conventional cytotoxic agent — dedicated cytotoxic handling facilities are not required, but standard PPE (gloves, eye protection) should be used per institutional SOPs |

---

## Safety Considerations

**Drug Interactions (75 total interactions identified; key interactions listed below):**

**Major interactions — require proactive management:**

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Adalimumab | Major | TNF-α inhibitor combined with PD-L1 blockade risks additive immunosuppression and opportunistic infections |
| Baricitinib | Major | JAK1/2 inhibitor combination significantly increases immunosuppression risk |
| BCG vaccine (Bacillus Calmette-Guérin, Tice strain) | Major | Live attenuated vaccine is contraindicated during immunotherapy; notably, BCG is the standard prior treatment for NMIBC — treatment sequencing must be carefully managed |

**Moderate interactions — monitor and adjust as needed:**

| Drug Class | Representative Agents | Concern |
|-----------|----------------------|---------|
| Systemic corticosteroids | Dexamethasone, Prednisolone, Prednisone, Methylprednisolone, Hydrocortisone, Budesonide, Betamethasone, Triamcinolone, Deflazacort | May attenuate checkpoint inhibitor anti-tumor efficacy if used prophylactically; however, short courses are routinely used to treat irAEs — timing and dose are critical |
| Other immunosuppressants | Azathioprine, Alemtuzumab, Anakinra, Alefacept | Concurrent use may reduce anti-tumor immune response |
| PDE4 inhibitor | Roflumilast | Immunomodulatory interaction; monitor carefully |
| Live vaccines | Anthrax vaccine, tetanus toxoid (inactivated), adenovirus antigen | Immune response may be altered during anti-PD-L1 therapy |

> **Important:** Full prescribing information including formal warnings and contraindications was not available in this Evidence Pack. Please refer to the official FDA prescribing information or EMA SmPC for Atezolizumab (Tecentriq®) before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
NCT02844816 is a completed Phase 2 trial (n=172) specifically designed for BCG-unresponsive NMIBC with prostatic urethral involvement (T1/Tis) as an eligible criterion — this constitutes direct, indication-specific L2 evidence. Combined with the well-established biological rationale of high PD-L1 expression in urothelial carcinoma and atezolizumab's proven anti-PD-L1 mechanism, the scientific foundation for this predicted indication is substantive. The primary limiting factors are the lack of subgroup-specific outcome data for prostatic urethral involvement and the absence of an India market authorization.

**To proceed, the following is needed:**

- **Subgroup data extraction:** Request or identify published subgroup analyses from NCT02844816 specifically reporting outcomes for patients with prostatic urethral involvement (T1/Tis staging) — this is the critical data gap for upgrading from L2 toward L1
- **MOA documentation:** Retrieve full mechanism of action from DrugBank (DB11595) to complete the mechanistic analysis
- **Full safety profile:** Download and parse the official prescribing information (FDA label / EMA SmPC) to capture formal warnings, contraindications, and special population guidance
- **India regulatory strategy:** Atezolizumab is not currently marketed in India; a regulatory pathway assessment is required (new drug application, import license, or parallel import framework)
- **Biomarker testing plan:** Define PD-L1 and TMB testing requirements for patient selection in this specific NMIBC subtype
- **irAE management protocol:** Develop an institutional immune-related adverse event monitoring and management plan, with attention to the major DDI risk with BCG (the standard prior-line treatment in this exact patient population)
- **Sequencing strategy:** Given that BCG failure defines this patient population, clearly define the washout period and transition protocol from BCG to atezolizumab
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

