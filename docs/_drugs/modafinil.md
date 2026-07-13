---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 1
---

# Modafinil
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

# Modafinil: From Excessive Sleepiness (Narcolepsy/Sleep Disorders) to Insomnia

## One-Sentence Summary

Modafinil is a wake-promoting agent approved in multiple markets (US FDA, EU) for narcolepsy, obstructive sleep apnea, and shift work sleep disorder. The TxGNN model predicts it may be effective for **Insomnia**, with **29 clinical trials** and **19 publications** identified — however, the mechanistic rationale contains a fundamental paradox that warrants careful interpretation. Evidence level is currently **L3**, and most clinical data involves the related compound armodafinil or secondary endpoints rather than primary insomnia treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Narcolepsy, obstructive sleep apnea, shift work sleep disorder (globally approved; no India registration found) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Modafinil promotes wakefulness primarily by inhibiting the dopamine transporter (DAT) and enhancing histaminergic and orexin (hypocretin) neurotransmission, while also exerting indirect effects on the norepinephrine system. These mechanisms suppress non-REM sleep and sustain alertness — which is why it is effective for conditions of pathological daytime sleepiness.

Here lies the central paradox: administering a potent wake-promoting agent to patients with difficulty falling or staying asleep is mechanistically counterintuitive. In principle, reinforcing wakefulness signals in an already-hyperaroused insomnia patient would be expected to worsen sleep onset, not improve it. The TxGNN model's high prediction score likely reflects the proximity of insomnia and sleep-wake dysregulation in the knowledge graph — they are closely connected disease nodes — rather than a direct therapeutic alignment.

There is, however, one indirect mechanistic pathway worth noting. In specific patient subgroups (oncology patients, those with neurodegenerative disease), excessive daytime fatigue disrupts circadian rhythm, which then destabilises nocturnal sleep architecture. In these settings, improving daytime wakefulness with modafinil may indirectly normalise the circadian pattern and reduce secondary insomnia — a hypothesis referred to as "circadian rhythm normalisation." This indirect route has biological plausibility but requires dedicated clinical validation. Critically, it does not translate directly to primary insomnia without comorbidity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | **Most directly relevant.** Examines modafinil (alone or combined with CBT-I) in patients with **primary insomnia** — assessing both daytime functioning and sleep severity. Small sample limits conclusions. |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Armodafinil 150 mg/day combined with CBT-I in breast cancer patients with insomnia. Direct insomnia endpoint, but limited to cancer-related insomnia subgroup. |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I ± armodafinil for insomnia and fatigue in breast cancer survivors post-chemotherapy. Armodafinil, not modafinil; specific oncology population. |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | Armodafinil ± CBT-I for insomnia and fatigue in cancer survivors after chemotherapy. Larger sample; same caveats as above. |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Armodafinil and/or CBT-I for insomnia comorbid with sleep-disordered breathing (OSA). Insomnia directly targeted, but in a comorbid OSA population. |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Phase 2 | Completed | 830 | RECOVER-SLEEP platform trial for sleep disturbances in Long COVID (PASC). Multiple interventions; modafinil may be one arm. Signals emerging from a real-world affected population. |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | Completed | 18 | Modafinil for circadian and cognitive dysfunction in stable bipolar disorder. Sleep quality is a secondary outcome; very small sample. |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | Modafinil for sleep/wake disturbances in older adults. Terminated early due to poor recruitment (n=2); no usable data. |
| [NCT07295834](https://clinicaltrials.gov/study/NCT07295834) | Phase 2 | Not Yet Recruiting | 70 | Modafinil vs. placebo for severe fatigue in inflammatory bowel disease (IBD). Future trial; no data available yet, but confirms ongoing research interest. |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | Completed | 399 | Armodafinil 150 mg/day as adjunct therapy in bipolar I major depression. Large, well-powered trial; sleep not the primary endpoint, and armodafinil differs from modafinil. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Evidence-Based Review | *Drugs* | Comprehensive review of modafinil's approved and investigational uses; covers RCTs across sleepiness, fatigue, and cognitive domains. Anchor reference for modafinil's evidence base. |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic Review & Meta-analysis | *PLOS ONE* | Meta-analysis of modafinil for fatigue and excessive daytime sleepiness in neurological disorders (MS, PD, TBI). Inconsistent results across conditions; supports efficacy for EDS, not primary insomnia. |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | *Parkinsonism & Related Disorders* | Systematic review of pharmacological interventions for daytime sleepiness and sleep disorders in PD. Contextualises modafinil's role within the sleep-wake spectrum. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | EBM Review (MDS) | *Movement Disorders* | Movement Disorder Society EBM review of non-motor PD treatments, including sleep. High-authority reference for understanding modafinil's role in sleep-adjacent conditions. |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | *Expert Opinion on Pharmacotherapy* | Current management of sleep disturbances in PD, covering both pharmacological and non-pharmacological options. Most recent entry; highlights ongoing gaps in evidence. |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | RCT | *Journal of Head Trauma Rehabilitation* | Randomised trial of modafinil for fatigue and excessive daytime sleepiness in chronic traumatic brain injury. Supports modafinil's role in secondary sleep disruption due to neurological injury. |
| [20082966](https://pubmed.ncbi.nlm.nih.gov/20082966/) | 2009 | Review | *Parkinsonism & Related Disorders* | Review of excessive daytime sleepiness in PD; discusses modafinil alongside narcolepsy-like REM intrusion patterns. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Drug Profile Review | *Drug Design, Development and Therapy* | Profile of pitolisant for narcolepsy; places modafinil in the competitive landscape of wake-promoting agents. Useful for positioning. |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | *Revue Neurologique* | Review of narcolepsy with cataplexy; modafinil cited as first-line treatment for EDS. Clarifies where modafinil is established versus speculative. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case Series | *American Journal of Hospice & Palliative Care* | Modafinil reduces fatigue in Charcot-Marie-Tooth disease type 1A. Illustrates modafinil's off-label use for secondary fatigue/sleepiness; low evidence tier but mechanistically informative. |

---

## India Market Information

Modafinil currently has **no registered products** in India. No license data is available for tabulation. The drug is approved in other major markets (US FDA, EU EMA) for narcolepsy, obstructive sleep apnea, and shift work sleep disorder, but has not obtained India marketing authorisation as of the data cutoff (2026-04-04).

---

## Safety Considerations

**Drug Interactions (249 total interactions identified):**

Key interactions to monitor if modafinil use is considered:

| Interacting Drug | Interaction Level | Clinical Relevance |
|----------------|-------------------|-------------------|
| Dexamethasone | Moderate | CYP3A4 induction may reduce dexamethasone efficacy |
| Esomeprazole | Moderate | Potential altered PPI metabolism via CYP2C19 |
| Omeprazole | Moderate | Same CYP2C19 pathway concern as esomeprazole |
| Rabeprazole | Moderate | Similar proton pump inhibitor interaction |
| Eliglustat | Moderate | Narrow therapeutic index drug; CYP interaction risk |
| Linagliptin | Moderate | Possible reduced DPP-4 inhibitor exposure |
| Cisapride | Moderate | QT prolongation risk when combined |
| Clarithromycin | Minor | CYP3A4 inhibitor may increase modafinil exposure |
| Hydrocortisone | Minor | Mild CYP induction effect |
| Pioglitazone | Minor | Modafinil may reduce thiazolidinedione levels |

The total interaction count of 249 indicates a wide drug interaction profile, primarily driven by modafinil's CYP3A4/2C19 induction effects. Formal warnings and contraindications from the package insert are not available in the current dataset — refer to the originator label (Provigil/Nuvigil) for comprehensive safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-perfect score to modafinil for insomnia, but this reflects topological proximity in the knowledge graph rather than a mechanistically coherent treatment hypothesis. Modafinil's core pharmacology — promoting wakefulness via DAT inhibition and orexin enhancement — is directly opposed to the goal of treating insomnia. The only Phase 4 trial in primary insomnia patients (NCT00124384, n=40) is too small to be conclusive, and the remaining clinical evidence predominantly involves armodafinil (a related but distinct compound) in comorbid or secondary insomnia contexts. The drug is also not registered in India, adding a regulatory hurdle.

**To proceed to the next decision stage, the following is needed:**

- **MOA documentation:** Retrieve complete DrugBank mechanistic data to formally characterise the wake-promoting pathway and assess whether any aspect plausibly targets hyperarousal insomnia
- **Full review of NCT00124384:** Obtain the complete results of the primary insomnia Phase 4 trial — specifically whether modafinil worsened, improved, or had no effect on sleep onset/maintenance measures
- **Subgroup clarification:** Define the target patient population — if the indication is "secondary insomnia in cancer or neurodegenerative disease patients with daytime fatigue," the evidence base and mechanistic rationale are substantially stronger than for primary insomnia
- **DDI safety screening:** With 249 interactions documented, a structured safety screen against the intended co-medication profile is required before any clinical advance
- **India regulatory pathway assessment:** Clarify whether a new drug application or import license would be required given current non-marketed status
- **Direct RCT evidence:** Commission or identify a prospective trial specifically in the target insomnia subpopulation before any Phase 2/3 investment is justified

> ⚠️ **Research Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

