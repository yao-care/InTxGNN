---
layout: default
title: Armodafinil
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 1
---

# Armodafinil
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

# Armodafinil: From Excessive Sleepiness to Insomnia

## One-Sentence Summary

Armodafinil (Nuvigil) is the R-enantiomer of modafinil, a wakefulness-promoting agent approved in the US for excessive sleepiness associated with narcolepsy, obstructive sleep apnea, and shift work sleep disorder.
The TxGNN model predicts it may be effective for **Insomnia**, with **12 clinical trials** and **19 publications** currently supporting this direction.
While seemingly counterintuitive, emerging evidence suggests armodafinil may benefit insomnia in specific populations — particularly cancer survivors and patients with comorbid sleep-disordered breathing — by normalizing the disrupted sleep-wake cycle.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Excessive sleepiness (narcolepsy, obstructive sleep apnea, shift work sleep disorder) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known published information, Armodafinil is the longer-lasting R-enantiomer of modafinil — a wakefulness-promoting agent believed to act primarily through inhibition of the dopamine transporter (DAT), with secondary activity on norepinephrine, serotonin, and orexin/hypocretin systems. This makes it pharmacologically distinct from classic amphetamine-type stimulants. Its three FDA-approved indications all involve a core deficit of excessive daytime sleepiness, and its use for insomnia in this context may appear paradoxical at first glance.

However, insomnia and excessive sleepiness frequently co-exist in the same patient — especially in oncology populations after chemotherapy, where disrupted circadian rhythms cause simultaneous daytime fatigue and nighttime wakefulness. By consolidating wakefulness during the day, armodafinil may restore sleep pressure and improve nighttime sleep architecture, producing a beneficial secondary effect on insomnia. This "bi-directional" sleep-wake normalization hypothesis is directly tested in at least three Phase 2 randomised trials involving breast cancer survivors.

Furthermore, shift work sleep disorder — one of armodafinil's approved indications — inherently encompasses an insomnia component (inability to sleep at non-traditional hours). The TxGNN model's high-confidence prediction is therefore mechanistically plausible within the broader sleep medicine framework, and the clinical evidence base, while targeted at specific populations, provides meaningful support for exploratory investigation into general insomnia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completed | 39 | Direct insomnia study: Armodafinil vs CBT-I vs combination for insomnia comorbid with obstructive sleep apnea; assessed sleep continuity and CPAP adherence |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Phase 2 | Completed | 226 | Randomised Phase 2: CBT-I ± armodafinil for insomnia and fatigue in breast cancer survivors post-chemotherapy |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Completed | 138 | Four-arm RCT of CBT-I and armodafinil in breast cancer patients with post-chemotherapy sleep disturbances |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Phase 2 | Completed | 70 | Pilot study of BBT-I ± armodafinil 150 mg/day for insomnia in breast cancer patients during active cancer treatment |
| [NCT01080807](https://clinicaltrials.gov/study/NCT01080807) | Phase 4 | Completed | 385 | Armodafinil 150 mg for shift work disorder: improved clinical condition late in shift including the commute home; functional and patient-reported outcomes |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | Completed | 399 | Armodafinil 150 mg/day adjunctive to mood stabilisers for major depression in Bipolar I Disorder |
| [NCT01072929](https://clinicaltrials.gov/study/NCT01072929) | Phase 3 | Completed | 433 | Armodafinil 150/200 mg/day adjunctive therapy for major depression associated with Bipolar I Disorder |
| [NCT01072630](https://clinicaltrials.gov/study/NCT01072630) | Phase 3 | Completed | 492 | Armodafinil 150/200 mg/day vs placebo for Bipolar I major depression; additional data on sleep-related outcomes |
| [NCT00678691](https://clinicaltrials.gov/study/NCT00678691) | Phase 4 | Completed | 55 | Armodafinil augmentation for fibromyalgia-related fatigue; builds on off-label evidence for fatigue/sleep disruption management |
| [NCT00481195](https://clinicaltrials.gov/study/NCT00481195) | Phase 2 | Completed | 257 | Armodafinil 150 mg/day adjunctive therapy for inadequately responsive Bipolar I major depression |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | Expert Opinion on Pharmacotherapy | Comprehensive review of pharmacological and non-pharmacological management of sleep disturbances; discusses wakefulness-promoting agents including armodafinil class |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Meta-analysis | PLoS ONE | Systematic review and meta-analysis confirming modafinil (parent compound) efficacy for fatigue and excessive daytime sleepiness in neurological disorders |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | Parkinsonism & Related Disorders | Systematic review of pharmacological interventions for daytime sleepiness and sleep disorders; highlights evidence gaps for insomnia treatment |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Review | Drugs | Evidence-based review of approved and investigational uses of modafinil covering narcolepsy, shift work disorder, fatigue, and off-label applications |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Review | Neurotherapeutics | Review of treatment options for sleep disorders in comorbid populations; CBT and pharmacotherapy for insomnia discussed alongside wakefulness-promoting agents |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Systematic Review | Movement Disorders | MDS Evidence-Based Medicine review covering non-motor symptoms treatment; evaluates evidence for sleep dysfunction including insomnia and hypersomnia |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | Shift work sleep disorder: burden of illness and management including modafinil-class agents for both the sleepiness and insomnia components |
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Review | Postgraduate Medicine | Emerging therapies for shift work disorder, specifically noting armodafinil for the dual presentation of excessive sleepiness and insomnia |
| [24138359](https://pubmed.ncbi.nlm.nih.gov/24138359/) | 2013 | Review | Medical Journal of Australia | Sleep loss and circadian disruption in shift work; highlights insomnia as a core co-morbidity alongside SWD and discusses management principles |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Review | Expert Opinion on Emerging Drugs | Emerging treatments for narcolepsy and related disorders; describes pharmacological profile of modafinil/armodafinil relevant to sleep-wake regulation |

---

## India Market Information

Armodafinil is currently **not marketed in India**. No product registrations were identified in the CDSCO database (total licences: 0). Any clinical development or use pathway would require a new regulatory submission to CDSCO for import or manufacture approval.

---

## Safety Considerations

**Drug Interactions**: Armodafinil has **170 known drug interactions** on record. The most clinically significant are summarised below:

| Severity | Interacting Drugs |
|----------|------------------|
| **Moderate** | Rabeprazole, Esomeprazole, Dexamethasone, Cisapride, Eliglustat, Linagliptin |
| **Minor** | Hydrocortisone, Pioglitazone, Aprepitant, Triamcinolone, Betamethasone, Cimetidine, Clarithromycin, Clotrimazole, Dronabinol, Miconazole, Naldemedine, Naloxegol, Nitisinone, Granisetron |

Key interaction mechanisms to note:
- **CYP2C19 inhibition**: Armodafinil inhibits CYP2C19, increasing plasma levels of proton pump inhibitors (Rabeprazole, Esomeprazole) — relevant in oncology populations often on GI prophylaxis
- **CYP3A4 induction**: Armodafinil induces CYP3A4, potentially reducing efficacy of co-administered drugs metabolised by this pathway (Cisapride, Eliglustat)
- **Corticosteroid interactions**: Multiple corticosteroids show Minor interactions; monitoring is advised in cancer patients on steroid regimens

Please refer to the full package insert for complete warnings and contraindications, as this data was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.89% is strongly supportive, and the evidence base includes multiple completed Phase 2 RCTs directly targeting insomnia (particularly in cancer populations), as well as one dedicated study for insomnia comorbid with sleep-disordered breathing. Armodafinil's established safety and tolerability profile from approved sleep disorder indications provides a meaningful foundation. However, armodafinil is not currently marketed in India, detailed MOA data is absent, and Phase 3 evidence specific to insomnia (as opposed to bipolar depression or SWD) has not yet been generated.

**To proceed, the following is needed:**
- Retrieve complete MOA data from DrugBank to formally substantiate the biological link between wakefulness promotion and insomnia improvement
- Obtain and review the full package insert for key warnings and contraindications (blocking data gap)
- Define the target insomnia subpopulation: cancer survivors, shift workers, or sleep-disordered breathing patients have the strongest existing evidence; broad general insomnia requires a dedicated trial
- Design a Phase 3 RCT in the identified population to elevate evidence from L2 to L1
- Assess CDSCO regulatory pathway for new drug registration or import licence in India
- Conduct comprehensive DDI screening for the 170 known interactions in the context of typical insomnia polypharmacy (e.g., co-prescribing with hypnotics, antidepressants, or melatonin agonists)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

