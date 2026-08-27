---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Antiplatelet/Cardiac Stress Testing to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is a well-established antiplatelet and vasodilatory agent, widely used as a pharmacological stress testing adjunct and thromboembolism prophylaxis. The TxGNN model predicts it may be effective for **Prinzmetal Angina** (vasospastic angina), with **0 registered clinical trials** and **15 older publications** currently retrieved — the majority of which describe dipyridamole's role as a diagnostic provocation agent rather than a therapeutic intervention. This mechanistic nuance warrants careful review before any further development steps.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from India regulatory data (drug not marketed in India); known globally for antiplatelet use and cardiac stress testing |
| Predicted New Indication | Prinzmetal Angina (vasospastic angina) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Dipyridamole acts by inhibiting phosphodiesterase (PDE) and blocking cellular reuptake of adenosine, leading to elevated plasma adenosine levels and subsequent vasodilation of coronary arteries. It also inhibits platelet aggregation by increasing intracellular cyclic AMP. These vasodilatory and antiplatelet properties form the mechanistic basis for why the TxGNN model may associate it with Prinzmetal angina, a condition driven by episodic coronary arterial vasospasm.

Prinzmetal angina (variant angina) is characterised by transient ST-segment elevation due to focal coronary spasm, not fixed atherosclerotic obstruction. In theory, a vasodilatory agent could relieve or prevent such spasm. The connection between dipyridamole and Prinzmetal angina is not new — dipyridamole has long been used as a provocative stress agent to unmask ischaemia, and its effects on coronary vascular tone have been studied in this patient population since the late 1970s.

However, the clinical picture is more complex and potentially contradictory. Several of the retrieved publications describe dipyridamole as a **trigger** for coronary vasospasm in patients with variant angina, particularly when vasodilation is abruptly reversed by aminophylline. This means the drug may provoke the very condition it is predicted to treat. Until detailed MOA data and prospective therapeutic (not diagnostic) trials are available, this prediction should be treated with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Clinical study | Japanese Circulation Journal | Examined effects of dipyridamole 50 mg (and other drugs) on angina attacks at rest in 26 patients including Prinzmetal's variant; propranolol tended to aggravate attacks |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Clinical study | American Journal of Cardiology | Dipyridamole stress testing can trigger coronary vasospasm via rebound mechanism when aminophylline reversal is rapid; evaluated in 36 hospitalised patients |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Clinical study | British Heart Journal | Assessed short-term reproducibility of exercise testing in 25 patients with ST elevation and different dipyridamole echocardiography responses; correlated with coronary arteriography |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Clinical study | Zhonghua Xin Xue Guan Bing Za Zhi | Compared clinical features of typical vs atypical coronary artery spasm; dipyridamole used as provocation context |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Clinical study | Japanese Circulation Journal | Dipyridamole-loading myocardial imaging in 38 CAD patients achieved 66% diagnostic accuracy; useful for patients unable to exercise |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Clinical study | Journal of the American College of Cardiology | Investigated myocardial texture changes during ischaemic episodes induced by various mechanisms including dipyridamole |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Observational | Portuguese Journal of Cardiology | 3-year prognosis of patients with suspected CAD and normal dipyridamole-thallium scintigraphy; generally favourable outcomes |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Pathophysiological basis for noninvasive coronary stenosis evaluation using dipyridamole among other stimuli; discusses diagnostic limitations |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Case report | Clinical Nuclear Medicine | Patient with variant angina, migraine, and asthma; scintigraphic ischaemia documented; discusses shared vasoreactive mechanisms |
| [2221701](https://pubmed.ncbi.nlm.nih.gov/2221701/) | 1990 | Review | Annals of the New York Academy of Sciences | ECG diagnosis of transient myocardial ischaemia; sensitivity and specificity discussion in context of various provocation methods |

---

## India Market Information

Dipyridamole is currently **not marketed in India**. No registered licenses, approved products, or dosage form records are available in the regulatory database.

---

## Safety Considerations

**Drug Interactions:** A total of 321 drug interactions are on record for dipyridamole (DDInter database).

- **Moderate interactions:** Dexfenfluramine, Sibutramine, Fenfluramine — potential additive cardiovascular effects warranting monitoring
- **Unknown-level interactions (selected):** Acetylsalicylic acid (aspirin — commonly co-administered), Calcitriol, Cimetidine, Amphotericin B, Omeprazole, Pantoprazole, Lansoprazole, Glimepiride, Metformin, Rosiglitazone, Morphine, Simvastatin, Prednisone, Vancomycin, Sucralfate, Lactulose, Nystatin

The aspirin interaction is clinically important: dipyridamole is often co-administered with aspirin (e.g., Aggrenox formulation), and the interaction classification of "Unknown" should be clarified before any new indication assessment.

For complete warnings and contraindications, please refer to the originator package insert (detailed TFDA/CDSCO label data not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-perfect prediction score (99.99%), but the available literature does not support dipyridamole as a *therapeutic* agent for Prinzmetal angina — rather, it has been historically studied as a *provocation agent* that can induce coronary vasospasm in susceptible patients (see PMID 3421166). This pharmacodynamic concern directly conflicts with the predicted therapeutic use and represents a potential safety risk. With zero clinical trials, no India market presence, and a key MOA data gap, advancement is premature.

**To proceed, the following is needed:**

- **MOA clarification:** Obtain full DrugBank mechanistic profile — particularly whether dipyridamole's adenosine-mediated vasodilation is net vasospasm-relieving or vasospasm-triggering in the context of Prinzmetal angina
- **Literature reclassification:** Commission expert review of the 15 retrieved papers to determine whether any describe therapeutic (not diagnostic) use in vasospastic angina
- **Dedicated clinical trial search:** Broaden search strategy to include terms such as "vasospastic angina", "variant angina", "coronary spasm" alongside dipyridamole — the current search used only "Prinzmetal angina" which may have missed relevant evidence
- **Safety label retrieval:** Download and parse the originator package insert (FDA/EMA) to extract contraindications and warnings — specifically whether vasospastic angina is listed as a contraindication to dipyridamole stress testing
- **India regulatory pathway:** Confirm whether dipyridamole has ever been evaluated for marketing approval in India and under what conditions it might qualify
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

