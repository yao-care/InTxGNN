---
layout: default
title: Methylene Blue
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 3
---

# Methylene Blue
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Methylene Blue: From Methemoglobinemia to Bronchitis

## One-Sentence Summary

Methylene blue (MB) is a phenothiazine compound with established clinical uses, most notably as first-line treatment for acquired methemoglobinemia and as an endoscopic diagnostic stain.
The TxGNN model predicts it may be effective for **Bronchitis**, with **0 clinical trials** and **10 publications** currently supporting this direction — however, the literature connection is indirect and the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acquired methemoglobinemia (recognized clinical use) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on known information, methylene blue is a phenothiazine dye with multiple pharmacological properties: it acts as a NADPH-dependent methemoglobin reductase cofactor to convert ferric (Fe³⁺) haemoglobin back to functional ferrous (Fe²⁺) form, and it also exhibits antimicrobial, antioxidant, and nitric oxide pathway-modulating activity.

The link between methylene blue and bronchitis in the TxGNN prediction appears to arise from **indirect knowledge graph associations** rather than direct therapeutic evidence. Methylene blue's documented use in fibreoptic bronchoscopy — as a mucosal stain that selectively marks malignant bronchial tissue — creates graph edges connecting MB to the bronchial system. However, this is a **diagnostic application**, not a therapeutic one for bronchitis inflammation or infection.

No preclinical, animal model, or clinical data currently supports methylene blue as a treatment for acute or chronic bronchitis. The repurposing rationale for this indication is assessed as a **likely false positive** arising from indirect node connections in the knowledge graph. The high TxGNN score (0.9997) should be interpreted with caution given the complete absence of mechanistic and experimental support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic Study | Chinese Journal of Surgery | MB staining in fibreoptic bronchoscopy: 97.14% of malignant bronchial tumours stained positively vs. 8.33% of bronchitis cases — confirms diagnostic, not therapeutic, use |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic Study | Terapevticheskii Arkhiv | Chromoendofibroscopy with MB for differential diagnosis of benign vs. malignant bronchial neoplasms — diagnostic technique study |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodological Study | Am Rev Respiratory Dis | MB evaluated as a tracer marker in bronchoalveolar lavage (BAL) quantitation alongside ⁹⁹ᵐTc-DTPA and other markers — technical/methodological application only |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Animal Study | J Ethnopharmacology | Lippia alnifolia essential oil induces tracheal relaxation via multiple pathways; bronchitis and asthma mentioned as traditional indication context — MB not involved |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Animal Study | J Ethnopharmacology | Aloysia gratissima antidepressant effects via L-arginine/NO/cGMP pathway; bronchitis mentioned only as a traditional use — MB not involved |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical Chemistry | Analytica Chimica Acta | Electrochemical aptasensor for theophylline detection; bronchitis cited as disease context for theophylline use — MB not involved |
| [2749902](https://pubmed.ncbi.nlm.nih.gov/2749902/) | 1989 | Basic Research | Tsitologiia | MB (as "chromosmon") studied for methemoglobin reduction in erythrocytes — pharmacological mechanism study, no bronchitis relevance |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Pharmacology Study | Int J Clin Pharmacol Ther Toxicol | MB used as an indicator-dilution marker to measure circulation time in cardiovascular studies — no bronchitis relevance |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case Report | Mikrobiyoloji Bulteni | Case of Moraxella catarrhalis endocarditis; bronchitis mentioned as one of M. catarrhalis' common manifestations — MB not involved |
| [17120034](https://pubmed.ncbi.nlm.nih.gov/17120034/) | 2007 | Case Report | Eur J Pediatrics | Isolated tracheoesophageal fistula diagnosed in a child; MB used in diagnostic contrast studies — bronchitis was a differential diagnosis |

---

## Safety Considerations

**Drug Interactions**: A total of 186 drug interactions have been identified. Representative interactions by severity:

| Severity | Interacting Drugs |
|----------|------------------|
| **Major** | Ondansetron, Granisetron, Dolasetron, Palonosetron (5-HT₃ antagonists); Lorcaserin, Fenfluramine, Dexfenfluramine (serotonergic agents); Morphine, Opium (opioids); Ephedrine, Phentermine, Mazindol, Diethylpropion, Isometheptene (sympathomimetics); Bupropion (noradrenaline–dopamine reuptake inhibitor) |
| **Moderate** | Epinephrine, Epinephrine (ophthalmic), Epinephrine (topical), Ephedrine (nasal) |

**Pattern note**: The clustering of Major interactions with serotonergic drugs (5-HT₃ antagonists, serotonin-releasing agents) is consistent with methylene blue's known MAO-inhibitory activity, which can precipitate **serotonin syndrome** — a potentially life-threatening interaction. Co-administration with serotonergic medications should be avoided or managed with extreme caution.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction carries an L5 evidence level with zero registered clinical trials and no literature directly supporting methylene blue as a bronchitis therapy. The retrieved publications relate exclusively to MB's diagnostic use in bronchoscopy or mention bronchitis only as background context in unrelated studies. The repurposing rationale identifies this prediction as a knowledge graph false positive.

**To proceed, the following is needed:**
- Preclinical in vitro or in vivo data demonstrating a direct therapeutic effect of MB on bronchial inflammation or infection
- A plausible mechanistic hypothesis linking MB's antimicrobial or nitric oxide-modulating properties to bronchitis pathophysiology
- Mechanism of action (MOA) data from DrugBank (currently unavailable — Data Gap DG002) to enable proper mechanistic analysis
- TFDA package insert safety data (currently unavailable — Data Gap DG001) before any clinical feasibility assessment

> **Note on other TxGNN predictions**: Two additional indications were evaluated in this Evidence Pack. Methemoglobinemia due to methemoglobin reductase deficiency (rank 3) is rated **L3 / Proceed with Guardrails**, with a sound mechanistic basis — MB bypasses the deficient NADH pathway via an independent NADPH-dependent route, supported by human and veterinary case reports. This indication may be a more actionable repurposing candidate and merits a dedicated evaluation report.

---
*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

