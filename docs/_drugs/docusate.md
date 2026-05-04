---
layout: default
title: Docusate
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 2
---

# Docusate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Docusate: From Stool Softener to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is an anionic surfactant stool softener, primarily used to relieve constipation by reducing stool surface tension to facilitate intestinal water absorption.
The TxGNN model predicts it may be effective for **Plummer-Vinson Syndrome**,
however there are currently **0 clinical trials** and **0 publications** supporting this direction, and this prediction likely stems from a knowledge graph proximity artifact rather than true mechanistic relevance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration data (drug not marketed in India) |
| Predicted New Indication | Plummer-Vinson Syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Docusate is an anionic surfactant stool softener that reduces intestinal surface tension to soften stool, and may additionally inhibit P-glycoprotein and enhance drug membrane permeability. Its efficacy in constipation treatment has been established, but mechanistically this appears difficult to apply to Plummer-Vinson Syndrome.

Plummer-Vinson Syndrome (also known as Patterson-Kelly Syndrome) presents a triad of iron-deficiency anemia, esophageal web, and dysphagia, with core pathology involving iron metabolism disorders and mucosal atrophy. The known mechanisms of Docusate — reducing intestinal surface tension, P-glycoprotein inhibition, and enhancing drug membrane permeability — have no direct biological plausibility link to iron-deficiency pathology or esophageal web formation.

The TxGNN high prediction score (0.9918) is likely derived from a **graph proximity artifact** in the knowledge graph through "gastrointestinal tract / mucosa-related node" graph distance effects, rather than a true mechanistic association. This prediction requires particularly cautious interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Docusate is currently not marketed in India and has no approved drug registrations.

---

## Safety Considerations

**Drug Interactions:** The following clinically relevant drug interactions have been identified:

| Interacting Drug | Interaction Level | Notes |
|-----------------|------------------|-------|
| Lactulose | Moderate | Combined use with other laxatives may increase risk of electrolyte disturbance |
| Mineral oil | Moderate | Docusate may promote mineral oil absorption, increasing systemic exposure risk |
| Phenolphthalein | Moderate | Combined use may enhance laxative effect and associated adverse reactions |
| Linaclotide | Minor | Combined laxative effects; clinical significance limited |

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently zero supporting evidence (no clinical trials, no relevant literature) for Docusate in Plummer-Vinson Syndrome, and mechanistic analysis indicates this TxGNN prediction most likely represents a knowledge graph graph proximity artifact rather than a genuine drug repurposing opportunity. Additionally, the drug is not marketed in India and lacks regulatory approval data.

**To proceed, the following is needed:**

- Obtain official Docusate package insert (MOA, warnings, contraindications) — currently a blocking data gap
- Confirm Docusate's mechanism of action via DrugBank API query to reassess biological plausibility
- Conduct basic scientific literature review to determine whether any preclinical evidence supports Docusate's role in iron-deficiency anemia or esophageal mucosa repair
- If mechanistic plausibility cannot be established, recommend removing this candidate from the repurposing pipeline and prioritizing other drug candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

