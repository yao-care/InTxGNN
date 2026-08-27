---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: From Sedation/Anesthesia to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine originally used for procedural sedation, anesthesia induction, and anxiolysis across clinical settings.
The TxGNN model predicts it may be effective for **Insomnia**, with **2 directly relevant clinical trials** and **4 RCT-level publications** currently supporting this direction.
While the pharmacological rationale is mechanistically strong (TxGNN score: 99.74%), its very short half-life and dependence risk raise significant barriers to repositioning for chronic insomnia management.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Sedation, anesthesia induction, and anxiolysis (no regulatory data on file) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Midazolam is a short-acting benzodiazepine that acts as a **positive allosteric modulator of GABA-A receptors**, enhancing inhibitory GABAergic neurotransmission to produce sedation, hypnosis, and anxiolytic effects. This mechanism directly targets the same biological pathway as established hypnotic drug classes—classical benzodiazepines, Z-drugs (zolpidem, zopiclone), and orexin antagonists—making the TxGNN prediction pharmacologically well-grounded. The exceptionally high prediction score of 0.9974 reflects the strong drug–disease association embedded in the knowledge graph.

Insomnia is characterised by cortical and subcortical hyperarousal, with a functional deficit in sleep-promoting GABAergic tone. Early clinical trials from the 1980s–1990s directly demonstrated midazolam's efficacy as an oral hypnotic for both sleep-onset and sleep-duration endpoints in patients with insomnia secondary to various conditions. Perioperative trials also consistently use sleep quality as a secondary endpoint when midazolam is administered, further accumulating indirect evidence.

However, midazolam's very short elimination half-life (1.5–2.5 hours; active metabolite α-hydroxymidazolam ~1 hour) limits its practical utility for **sleep maintenance insomnia**—the most prevalent complaint—and clinical guidelines have largely displaced short-acting benzodiazepines in favour of non-benzodiazepine hypnotics or orexin antagonists for chronic insomnia due to concerns about tolerance, physical dependence, rebound insomnia, and next-day cognitive impairment. These pharmacokinetic and safety limitations are the primary reason the recommendation is **Hold** despite strong mechanistic plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Head-to-head RCT directly comparing IV midazolam vs dexmedetomidine on **postoperative sleep quality** in TURP patients; provides the most direct modern RCT evidence for midazolam's effect on sleep outcomes |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Recruiting | 280 | Prospective double-blind RCT of **preoperative oral midazolam** specifically enrolling patients with pre-existing **sleep disturbance or anxiety** undergoing colorectal cancer surgery; primary endpoint is postoperative pain, but safety and hypnotic effect data in sleep-disordered patients will be generated |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | Polysomnographic comparison of dexmedetomidine vs **midazolam** for sleep quality and delirium incidence in mechanically ventilated ICU patients; terminated early due to recruitment difficulties — limited inferential value |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Compared sleep-stage architecture (N2, N3, total sleep time) between α2 agonists and **GABA agonists (including midazolam)** via polysomnography; terminated after enrolment of 6 subjects — mechanistic signal only |
| [NCT03624595](https://clinicaltrials.gov/study/NCT03624595) | N/A | Active, Not Recruiting | 502 | Multicentre RCT of low-dose dexmedetomidine for post-cardiac-surgery delirium with sleep disturbance as a key contributing factor; midazolam serves as contextual comparator for GABAergic sedation risk — indirect relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Phase 1/2 Dose-Finding | *Arzneimittel-Forschung* | Oral midazolam 10–30 mg evaluated in 75 hospitalised patients with mild-to-moderate insomnia secondary to musculoskeletal and neurological disorders; established optimal dose range and confirmed hypnotic efficacy |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | *Br J Clin Pharmacol* | Double-blind parallel RCT of midazolam 15 mg vs Vesparax in 30 female patients with insomnia secondary to neuromuscular disease; midazolam demonstrated equivalent hypnotic efficacy with better tolerability and absence of hangover effect |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | *J Clin Psychopharmacol* | Introduction to multicentre RCT examining sleep, performance, and plasma levels in chronic insomniacs during 14-day use of flurazepam vs midazolam; explored the relationship between half-life, efficacy, and rebound effects in a heterogeneous benzodiazepine-experienced population |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | Multicenter RCT | *J Clin Psychopharmacol* | Executive summary of the 14-day flurazepam vs midazolam multicentre trial; quantified sleep and daytime performance outcomes, confirming midazolam's hypnotic efficacy with shorter residual impairment compared to long-acting flurazepam |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Clinical Review | *Acta Psychiatr Scand Suppl* | Reviewed benzodiazepines as hypnotics with differing pharmacokinetic profiles; explicitly discusses midazolam's clinical role and the importance of matching half-life to insomnia subtype (sleep-onset vs sleep-maintenance) |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Case Series | *J Clin Med* | Pilot study evaluating lemborexant as an alternative to benzodiazepines (including midazolam) for insomnia in high-risk pancreato-biliary endoscopy patients; highlights the delirium-exacerbating risk of benzodiazepines in this population — relevant safety signal |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | *Orvosi Hetilap* | Reviewed primary and secondary insomnia pathogenesis with focus on hyperarousal mechanisms; provides disease-level context supporting the rationale for GABAergic pharmacotherapy |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Animal / Mechanistic | *Pain* | Sciatic nerve ligation mouse model demonstrated that sleep disturbance in neuropathic pain correlates with altered GABAergic transmission in the cingulate cortex; provides mechanistic support for GABA-A modulation as a therapeutic target in insomnia |

---

## India Market Information

Midazolam currently has **no registered products** in the India market (0 approved licenses on record). This absence means there is no existing local regulatory dossier, approved indication text, or post-marketing safety data available for cross-reference.

---

## Safety Considerations

**Drug Interactions (177 known interactions identified; key interactions below):**

| Interacting Drug | Severity | Clinical Significance |
|-----------------|----------|----------------------|
| Clarithromycin | Moderate | CYP3A4 inhibition may substantially elevate midazolam plasma levels, increasing sedation and respiratory depression risk |
| Miconazole / Clotrimazole | Moderate | Azole antifungals inhibit CYP3A4, potentially prolonging and intensifying midazolam effect |
| Morphine | Moderate | Additive CNS and respiratory depression; combination requires careful dose titration and monitoring |
| Metoclopramide | Moderate | May accelerate midazolam absorption, intensifying onset of sedation |
| Omeprazole / Cimetidine / Ranitidine | Moderate | CYP2C19/CYP3A4 inhibition or altered gastric pH may increase midazolam bioavailability |
| Bupropion | Moderate | CNS-lowering threshold interaction; combination may increase seizure risk |
| Aprepitant | Moderate | CYP3A4 inhibitor; co-administration may significantly increase midazolam exposure |
| Dronabinol / Nabilone | Moderate | Additive CNS depression; enhanced sedation and psychomotor impairment |
| Dexamethasone / Betamethasone | Minor | CYP3A4 induction may modestly reduce midazolam exposure; likely clinically minor in single-dose insomnia use |

> Formal package-insert warnings and contraindications (e.g., respiratory insufficiency, sleep apnoea, acute alcohol intoxication, myasthenia gravis) are not available in this data package and must be reviewed from the prescribing information prior to any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Midazolam has a pharmacologically valid and historically documented mechanism for insomnia (GABA-A positive allosteric modulation), and early RCT evidence from the 1980s–1990s confirms its hypnotic efficacy. However, its very short half-life restricts utility to sleep-onset insomnia only, modern clinical guidelines have superseded benzodiazepines with safer alternatives for chronic insomnia (Z-drugs, orexin antagonists, CBT-I), the drug is not currently marketed in India, and critical safety data (package-insert warnings, contraindications) are missing from the current evidence package — all of which prevent progression to a formal S1 evaluation at this stage.

**To proceed, the following is needed:**

- **Regulatory safety data**: Retrieve and review the full prescribing information (warnings, contraindications, special populations) from a jurisdiction where midazolam is approved (e.g., FDA, EMA, or CDSCO equivalent) to complete the S1 safety screen
- **Mechanism of action data**: Confirm and document the official DrugBank/pharmacopoeial MOA for the evidence package
- **Insomnia subtype specification**: Clarify whether the repositioning target is sleep-onset insomnia (where midazolam's pharmacokinetics are most appropriate) or sleep-maintenance insomnia (where the short half-life is a structural barrier)
- **Comparative landscape analysis**: Benchmark midazolam against currently approved hypnotics (zolpidem, eszopiclone, lemborexant, suvorexant) on efficacy, safety, and regulatory risk — particularly regarding dependence scheduling and addiction liability
- **India market entry pathway**: Assess CDSCO requirements for a new indication filing given zero existing registrations; determine whether an import licence or full NDA pathway is required
- **Updated clinical trial search**: The most relevant perioperative trials (NCT02142595, NCT06407518) involve surgical contexts rather than chronic primary insomnia — a targeted search for contemporary outpatient insomnia trials using midazolam is recommended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

