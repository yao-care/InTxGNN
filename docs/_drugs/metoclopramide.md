---
layout: default
title: Metoclopramide
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metoclopramide: From Gastroparesis & Nausea to Gastric Ulcer

## One-Sentence Summary

Metoclopramide is a well-established prokinetic and antiemetic agent, primarily used clinically to treat nausea, vomiting, and delayed gastric emptying (gastroparesis).
The TxGNN model predicts it may be effective for **Gastric Ulcer**,
with **2 clinical trials** and **20 publications** currently available to support this direction — though the majority of evidence is indirect, addressing metoclopramide's prokinetic properties rather than direct ulcer healing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastroparesis, nausea, and vomiting (prokinetic / antiemetic) |
| Predicted New Indication | Gastric Ulcer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally documented in this Evidence Pack. Based on pharmacological evidence embedded in the supporting literature, Metoclopramide is a **dopamine D2 receptor antagonist** and **serotonin 5-HT4 receptor agonist**. Through these dual actions it accelerates gastric emptying, enhances antroduodenal peristaltic coordination, raises lower esophageal sphincter pressure, and reduces bile reflux into the stomach — collectively creating a less hostile mucosal environment.

Gastric ulcer pathophysiology involves an imbalance between aggressive factors (gastric acid, bile reflux, *Helicobacter pylori*) and mucosal defense mechanisms. Metoclopramide's prokinetic effects may reduce the duration of acid–mucosa contact and limit bile-induced injury. Animal studies have demonstrated ulcer-protective effects in aspirin-induced and pylorus-ligated models without altering gastric acid secretion, suggesting the protective mechanism is motility-mediated rather than secretory (PMID: 2730234; PMID: 6436177).

That said, it must be clearly noted that Metoclopramide has no **direct** anti-ulcer mechanism. It neither inhibits acid secretion nor eradicates *H. pylori*, which is responsible for 70–80% of gastric ulcers. The high TxGNN score likely reflects knowledge graph proximity between Metoclopramide and upper GI disease nodes. The most clinically plausible role is **adjunctive therapy** in the subgroup of ulcer patients who also have gastroparesis — not as a standalone ulcer treatment. Clinical translation evidence remains thin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Double-blind RCT evaluating IV metoclopramide as pre-endoscopy premedication in upper GI bleeding (including ulcer bleeds); primary endpoints are the need for repeat endoscopy and quality of gastric wall visualization during the procedure |
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist-led quality improvement programme (P-DQIP) in Scottish primary care; metoclopramide is not the primary intervention and gastric ulcer healing is not an endpoint — low direct relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | RCT | Am J Gastroenterology | Most recent double-blind RCT evaluating IV metoclopramide for gastric visualization in patients with active upper GI bleeding; highest methodological quality in this evidence set |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal Study | Arch Int Pharmacodyn Ther | Metoclopramide (20–50 mg/kg) produced ulcer-protective effects in aspirin-induced and pylorus-ligated rat models; efficacy comparable to ranitidine against aspirin-induced ulcers |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | Animal Study | Indian J Physiol Pharmacol | Metoclopramide protected guinea pigs against all three experimental gastric ulcer models without affecting acid secretion; mechanism attributed to improved gastric drainage and prevention of pyloric reflux |
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT (perioperative) | Yonsei Med J | Prospective double-blind RCT (N=40); IV metoclopramide + ranitidine significantly reduced preoperative gastric volume and acidity versus placebo in laparoscopic gynecologic surgery patients |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | Clinical Study | Curr Med Res Opin | Assessed metoclopramide's effect on bile reflux in gastric ulcer patients alongside smoking and carbenoxolone; bile reflux reduction is a plausible mucosal protective mechanism |
| [28652516](https://pubmed.ncbi.nlm.nih.gov/28652516/) | 2017 | Animal Study | J Smooth Muscle Res | Prokinetic drugs including metoclopramide improved gastric emptying after acetic acid-induced ulcers in rats; drug response varied by ulcer anatomical position |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Narrative Review | Ann Intern Med | Comprehensive pharmacology review; describes metoclopramide's GI smooth muscle stimulatory effects via D2 antagonism and augmented acetylcholine release |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | Clinical Report | ZFA Zeitschrift Allgemeinmed | Early clinical report on metoclopramide in gastric and duodenal ulcer therapy |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Narrative Review | Drugs | Review of pharmacological options for gastric and duodenal ulcer treatment; includes discussion of metoclopramide's adjunctive role |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Clinical Review | Postgrad Med | Strategies for refractory peptic lesions; notes prokinetics as potential adjuncts when standard H2-blocker regimens fail |

---

## India Market Information

Metoclopramide currently has **no registered products** in the CDSCO database. Market status is recorded as **Not Marketed**, with zero authorizations on file. There is no local regulatory reference product or approved labelling available for this jurisdiction.

---

## Safety Considerations

**Drug Interactions**: Metoclopramide has **670 documented drug interactions**. The most clinically significant interactions identified in this Evidence Pack are summarised below:

| Severity | Interacting Drugs |
|----------|------------------|
| **Major** | Tramadol, Amisulpride |
| **Moderate** | Fentanyl, Codeine, Dihydrocodeine, Alfentanil, Alprazolam, Amitriptyline, Amantadine, Ethanol, Cetirizine, Chlorpheniramine, Abiraterone, Amifampridine, Amobarbital, Lidocaine (topical), Phenyltoloxamine, Tetracaine (ophthalmic), Dichloralphenazone |
| **Minor** | Acetaminophen |

Note: Formal key warnings and contraindications data were not available in this Evidence Pack. Please refer to the official prescribing information / package insert for a complete safety profile before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.93%), the clinical evidence base for Metoclopramide specifically targeting gastric ulcer healing is insufficient to justify advancement. Neither registered trial uses ulcer healing as a primary endpoint, and the supporting literature consists primarily of animal studies, older narrative reviews, and perioperative pharmacology data from unrelated surgical settings. More importantly, Metoclopramide lacks the direct anti-ulcer mechanisms — acid suppression or *H. pylori* eradication — that underpin all current guideline-recommended regimens. Its best-case role is narrowly adjunctive in a subgroup of ulcer patients with concurrent gastroparesis, and this hypothesis has not been formally tested.

**To proceed, the following is needed:**
- Obtain the official package insert or CDSCO-equivalent product labelling to document formal warnings and contraindications
- Retrieve complete MOA documentation from DrugBank (DB01233) to fill the current data gap
- Conduct a systematic review targeting Metoclopramide as adjunctive therapy specifically in gastroparesis-complicated gastric ulcer patients
- Design a prospective clinical study with ulcer healing rate and symptom resolution as co-primary endpoints in this defined subgroup
- Assess the regulatory pathway for India market entry, including the feasibility of a bridging submission given the current zero-registration status
- Evaluate whether combination with standard PPI ± *H. pylori* eradication therapy offers measurable benefit over PPI alone in patients with delayed gastric emptying
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

