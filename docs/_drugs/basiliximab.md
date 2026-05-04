---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Basiliximab
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

# Basiliximab: From Organ Transplant Rejection to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab (Simulect) is a chimeric monoclonal antibody originally approved to prevent acute rejection in kidney transplantation by blocking the IL-2 receptor (CD25) on activated T cells.
The TxGNN model predicts it may be relevant for **Plasma Cell Myeloma**, with **3 clinical trials** currently supporting this direction — though all trials evaluate Basiliximab as a GVHD prophylaxis agent within the hematopoietic stem cell transplantation (HSCT) framework, rather than as a direct antimyeloma therapy.
There is currently no published literature specifically linking Basiliximab to plasma cell myeloma treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of acute organ rejection in kidney transplantation |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Basiliximab is a chimeric (human/murine) IgG1κ monoclonal antibody that specifically binds to the alpha subunit (CD25) of the high-affinity IL-2 receptor on activated T lymphocytes. By competitively blocking IL-2 binding, it prevents clonal T-cell expansion and suppresses the alloimmune response — the mechanism underpinning its efficacy in solid organ transplant rejection.

The connection to plasma cell myeloma is indirect and operates through the HSCT framework. For relapsed or refractory multiple myeloma, allogeneic HSCT remains a potential treatment option, with the graft-versus-myeloma (GVM) effect being central to long-term disease control. However, acute graft-versus-host disease (aGVHD) is the principal life-threatening obstacle. Basiliximab, by selectively blocking IL-2/CD25 signaling on activated donor T cells, may suppress GVHD while theoretically preserving sufficient GVM activity — thereby improving HSCT outcomes in myeloma patients. Additionally, CD25 is highly expressed on regulatory T cells (Tregs), which suppress anti-tumor immunity; partial Treg depletion via CD25 blockade could theoretically reduce immune escape in the myeloma microenvironment.

An essential conceptual distinction must be made: the available evidence frames Basiliximab strictly as a **supportive immunomodulatory agent within the HSCT setting** (GVHD prophylaxis), not as a **direct antimyeloma drug**. No clinical study has evaluated Basiliximab's direct cytotoxic or tumor-suppressive efficacy against myeloma cells, and this mechanistic leap remains unvalidated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Regulatory T-cell depletion to improve autologous SCT outcomes in multiple myeloma — assesses safety and feasibility of immune modulation; indirect evidence supporting immune axis manipulation in the myeloma-HSCT context |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab combined with cyclosporine for in vivo activated T-cell depletion to prevent GVHD after non-myeloablative allogeneic transplantation for hematologic cancers — patient cohort may include myeloma; primary endpoint is GVHD control, not myeloma response |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | N/A | Terminated | 10 | Basiliximab + cyclosporine vs. cyclosporine alone for GVHD prevention — terminated early due to inadequate enrollment; insufficient data for meaningful conclusions |

---

## Safety Considerations

**Drug Interactions (69 total interactions identified):**

Major interactions requiring avoidance or close monitoring:

- **Adalimumab** (Major): Dual biologic immunosuppression substantially increases the risk of serious and opportunistic infections
- **Baricitinib** (Major): Additive immunosuppressive effects with a JAK inhibitor; combined use heightens infection risk
- **BCG Vaccine — Tice strain (live)** (Major): Live vaccines are contraindicated during immunosuppression; risk of disseminated BCG infection
- **Certolizumab pegol** (Major): TNF inhibitor combined with IL-2R blockade creates profound immunosuppression

Moderate interactions include concurrent use of: Azathioprine, Alemtuzumab, Anakinra, Canakinumab, Alefacept, Roflumilast, Bifidobacterium longum infantis, and multiple attenuated or killed vaccines (Anthrax, Cholera CVD 103-HgR, Adenovirus serotype 4, Tetanus toxoid).

> Please refer to the product package insert for complete information on warnings and contraindications, as this data was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every piece of clinical evidence in this pack positions Basiliximab as an adjunctive GVHD prophylaxis tool within the allogeneic HSCT setting — not as a direct plasma cell myeloma treatment. There is no Phase 2 or higher trial, nor any published literature, specifically designed to evaluate Basiliximab's direct anti-myeloma activity. The mechanistic leap from IL-2R blockade to myeloma cell kill is theoretically plausible but entirely unvalidated.

**To proceed, the following is needed:**

- **Clarify the research question**: "Basiliximab for GVHD prevention in myeloma patients undergoing allo-HSCT" is a scientifically tractable question supported by existing L3 evidence; "Basiliximab as direct myeloma treatment" is not supported by current data and requires a full de novo mechanistic rationale
- **Dedicated Phase 2 trial design** if pursuing the HSCT-supportive angle: myeloma-specific endpoints such as GVM effect preservation, GVHD-free / relapse-free survival (GRFS), and post-HSCT progression-free survival
- **DrugBank MOA data**: Formal pharmacological profiling to characterize Basiliximab's effects on the myeloma immune microenvironment, including Treg dynamics and CD25 expression on myeloma cells
- **Regulatory safety data**: Obtain CDSCO/TFDA package insert to complete the safety profile, particularly regarding warnings in hematologic malignancy populations
- **Note — higher-priority indication identified**: The strongest evidence in this Evidence Pack is for **hemoglobinopathy** (Rank 4: L2 evidence, Phase 4 completed RCT with n=205 directly evaluating Basiliximab for GVHD prevention in thalassemia major HSCT; recommendation: "Proceed with Guardrails"). A separate dedicated evaluation report for that indication is recommended as a higher-priority next step.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

