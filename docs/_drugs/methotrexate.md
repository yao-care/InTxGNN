---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Hematologic Malignancies to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate is a well-established antifolate antimetabolite with decades of clinical use across hematologic malignancies (including leukemia, lymphoma, and osteosarcoma) and autoimmune diseases (including rheumatoid arthritis and psoriasis).
The TxGNN model predicts it may be effective for **Pulmonary Blastoma**,
with **no clinical trials** and **no publications** currently supporting this specific direction — evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hematologic malignancies and autoimmune diseases (no India regulatory data on file) |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Methotrexate is a folate antagonist belonging to the antifolate antimetabolite class of cytotoxic agents. Its efficacy across hematologic malignancies — particularly acute lymphoblastic leukemia, non-Hodgkin's lymphoma, and primary CNS lymphoma — has been firmly established over decades of clinical use. The drug functions by inhibiting dihydrofolate reductase (DHFR), thereby blocking the synthesis of thymidylate and purines that are essential for DNA replication in rapidly dividing cells. Evidence collected from related predictions in this report (primary pulmonary lymphoma, small cell lung carcinoma, Hodgkin's lymphoma, rhabdomyosarcoma) consistently identifies the DHFR-inhibition pathway as the mechanistic anchor for MTX's antitumor activity.

Pulmonary blastoma is a rare, aggressive embryonal tumor of the lung with a biphasic architecture combining primitive epithelial and mesenchymal components. The TxGNN model predicts that its rapidly proliferating embryonal cells may be sensitive to DHFR inhibition — the same logic that underlies MTX's activity in other high-proliferation embryonal tumors such as rhabdomyosarcoma and Wilms' tumor. The high proliferative index characteristic of embryonal-type malignancies is precisely the cellular state most vulnerable to antifolate-mediated thymidylate depletion.

However, this mechanistic bridge remains entirely theoretical for pulmonary blastoma specifically. There are no clinical trials, no published case reports, and no preclinical studies examining MTX activity in this rare tumor type. The TxGNN prediction score of 99.45% reflects graph neural network pattern recognition based on biological network proximity within the knowledge graph — not direct experimental evidence. Until preclinical data are generated, this remains a hypothesis-only candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Methotrexate has no registered products in India according to this regulatory dataset (0 approved licenses, market status: Not Marketed). International approvals should be referenced for formulation and approved indication details.

---

## Cytotoxicity

Methotrexate is a conventional cytotoxic antimetabolite used across multiple oncology indications. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Antifolate / Antimetabolite class) |
| Myelosuppression Risk | High — bone marrow suppression is a well-recognized dose-limiting toxicity; neutropenia, thrombocytopenia, and anemia are common, particularly with high-dose regimens |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential count, ALT/AST/bilirubin (hepatotoxicity risk), serum creatinine and creatinine clearance (nephrotoxicity risk), serum MTX concentration (mandatory for high-dose protocols), folate/leucovorin rescue status |
| Handling Protection | Must follow cytotoxic drug handling regulations; specialized preparation, administration, and disposal procedures required |

---

## Safety Considerations

**Drug Interactions**: A total of 784 drug-drug interactions have been identified for Methotrexate. Clinically significant interactions include:

**Major interactions (require avoidance or close monitoring):**
- **Rabeprazole** — Proton pump inhibitors impair renal MTX clearance via OAT3 transporter inhibition, substantially raising MTX plasma exposure and toxicity risk
- **Amoxicillin** — Beta-lactam antibiotics compete with MTX for renal tubular secretion, increasing MTX levels and risk of myelosuppression/mucositis
- **Acetylsalicylic acid (Aspirin)** — NSAIDs and salicylates reduce MTX renal clearance and displace it from plasma protein binding, compounding toxicity; concurrent use should be avoided especially at higher MTX doses

**Selected moderate interactions:**
- **Amphotericin B / Amphotericin B (lipid complex)** — Additive nephrotoxicity risk that can reduce MTX renal clearance
- **Mesalazine / Balsalazide** — Aminosalicylates may inhibit hepatic MTX metabolism, increasing systemic exposure
- **Doxycycline / Tetracycline** — Antibiotic interference with MTX absorption and enterohepatic recycling
- **Hydrocortisone / Dexamethasone / Betamethasone / Budesonide / Triamcinolone** — Combined immunosuppression; corticosteroids may modulate MTX anti-inflammatory efficacy
- **Clarithromycin** — Transporter-mediated pharmacokinetic interaction
- **Bupropion** — Moderate interaction; CNS toxicity risk may be additive

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.45%) for Methotrexate in pulmonary blastoma based on graph-level biological network proximity, there is a complete absence of any supporting clinical, observational, or preclinical evidence for this specific indication. Pulmonary blastoma is an extremely rare malignancy with no established chemotherapy standard, and no data exist to confirm DHFR pathway dependency in this tumor subtype.

**To proceed, the following is needed:**
- **Preclinical studies**: In vitro cytotoxicity assays and in vivo xenograft experiments in pulmonary blastoma models to establish MTX antitumor activity
- **Pathway validation**: Confirm DHFR expression levels and folate pathway dependency in pulmonary blastoma tumor tissue or cell lines
- **Retrospective case mining**: Systematic search for any historical case reports describing MTX use in pulmonary blastoma management
- **Safety data gap resolution**: Obtain the official MTX package insert (IND/NDA-approved label) to document full warnings, contraindications, and special population guidance
- **MOA documentation**: Retrieve complete DrugBank mechanism of action data to formally characterize the folate antagonism rationale for this indication
- **Rare disease expert input**: Consultation with thoracic oncologists and pediatric oncologists specializing in rare lung malignancies before any clinical hypothesis is advanced

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

