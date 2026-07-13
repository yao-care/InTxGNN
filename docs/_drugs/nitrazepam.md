---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 3
---

# Nitrazepam
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

# Nitrazepam: From Insomnia/Sedation to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Nitrazepam is a long-acting benzodiazepine with a well-established clinical history as a hypnotic agent, used historically for insomnia and seizure disorders. The TxGNN model predicts it may be effective for **Sleep Disorder, Initiating and Maintaining Sleep**, with **0 registered clinical trials** and **20 publications** currently supporting this direction. While this prediction aligns closely with the drug's known pharmacological profile, no regulatory registration exists in India, warranting a cautious approach before any formal repurposing programme is pursued.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on record (historical clinical use: insomnia, epilepsy/infantile spasms) |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Nitrazepam belongs to the **benzodiazepine class** and acts as a positive allosteric modulator of GABA-A receptors, enhancing inhibitory neurotransmission in the central nervous system. This sedative-hypnotic mechanism is the foundation of its longstanding clinical use for difficulty initiating and maintaining sleep. The brand name Mogadon has been in clinical use since the 1960s, and the drug has been directly compared to newer hypnotics (triazolam, zolpidem, brotizolam, zopiclone) in controlled trials.

The relationship between the drug's historical use and the predicted indication is essentially confirmatory: sleep disorder (initiating and maintaining sleep) is the core indication for which benzodiazepine hypnotics like nitrazepam were developed. The TxGNN model's high confidence score (99.89%) reflects this strong pharmacological alignment. In this context, the "repurposing" framing is more accurately understood as a **reassessment of evidence base** — the question for India is whether sufficient structured evidence exists to support a new market entry application.

The primary concern is not mechanistic plausibility (which is well-established), but rather the drug's safety profile, dependency liability, and whether it offers a favourable risk-benefit ratio relative to newer non-benzodiazepine alternatives (e.g., zolpidem, zopiclone, lemborexant) now available in India.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Clinical Trial | British Medical Journal | Double-blind trial in general medical wards established nitrazepam was as effective as butobarbitone as a hypnotic; 27 overdose patients showed no serious adverse effects beyond drowsiness |
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT | Acta Psychiatrica Scandinavica | Double-blind cross-over study in 26 geriatric inpatients; nitrazepam 5 mg vs. triazolam 0.25 mg showed similar sleep quantity, quality, and psychomotor performance |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | PK Study | Clinical Pharmacokinetics | Comprehensive review of nitrazepam pharmacokinetics including absorption, distribution, metabolism, and elimination relevant to hypnotic dosing |
| [4712500](https://pubmed.ncbi.nlm.nih.gov/4712500/) | 1973 | Clinical Study | British Medical Journal | Early characterisation of nitrazepam's effects on sleep and subconscious processing |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case Report | British Journal of Psychiatry | Documents nitrazepam (Mogadon) dependence, highlighting the risk of long-term use |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | Reviews hypnotic drug effectiveness against the background of REM/NREM sleep physiology; nitrazepam contextualised among benzodiazepine hypnotics |
| [3281819](https://pubmed.ncbi.nlm.nih.gov/3281819/) | 1988 | Review | Drugs | Brotizolam compared to nitrazepam 2.5–5 mg in clinical trials; both showed equivalent improvement in insomnia |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | Review | Drugs | Zolpidem efficacy in insomnia found generally comparable to nitrazepam; supports nitrazepam's benchmark status in hypnotic trials |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | Nitrazepam cited as a long-acting hypnotic with significant residual daytime sedation and accident risk; implications for prescribing in elderly |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | Observational | PLoS ONE | Inappropriate prescribing patterns for benzodiazepines in primary care; dependency, tolerance, and cognitive decline risks highlighted, especially in older adults |

---

## India Market Information

No regulatory authorisations for Nitrazepam have been identified in India. The drug is currently **not marketed**.

---

## Safety Considerations

**Drug Interactions:** A total of **55 drug interactions** have been identified via the DDInter database. All interactions are currently classified as **"Unknown" severity**, meaning the clinical significance has not been formally graded. Representative interacting drugs include:

- CNS/opioid agents: Morphine, Bupropion
- Gastrointestinal agents: Lansoprazole, Pantoprazole, Omeprazole, Famotidine, Nizatidine, Sucralfate, Loperamide, Metoclopramide, Lactulose, Metronidazole
- Corticosteroids: Hydrocortisone, Dexamethasone, Budesonide
- Other: Calcitriol, Metformin, Acetylsalicylic acid, Kanamycin, Vancomycin

Given the drug's class (benzodiazepine), clinically relevant interactions are expected with other CNS depressants, alcohol, CYP3A4 inhibitors/inducers, and opioids. Formal severity grading from a validated interaction database (e.g., Lexicomp, Micromedex) should be obtained before any clinical deployment.

Please refer to the package insert for full safety information once a regulatory dossier or international product monograph is sourced.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is pharmacologically well-grounded — nitrazepam's hypnotic properties are documented in published comparative trials spanning over five decades. However, the drug is not registered in India, CDSCO package insert data is absent, and formal MOA documentation is missing from this pack. Importantly, modern clinical practice has largely shifted toward non-benzodiazepine hypnotics (Z-drugs, orexin antagonists) due to nitrazepam's dependency risk and residual sedation profile; any repurposing or market entry plan must address this competitive and safety context explicitly.

**To proceed, the following is needed:**

- **CDSCO / package insert data**: Obtain official warnings, contraindications, and approved indication text from the Indian regulatory dossier or an international reference label (e.g., UK SPC, TGA PI)
- **Formal MOA documentation**: Retrieve from DrugBank API to complete mechanistic analysis
- **DDI severity grading**: Re-query 55 interactions against a graded database (Lexicomp or Micromedex) to identify any major/contraindicated combinations
- **Comparative safety review**: Structured benefit-risk comparison of nitrazepam vs. current standard-of-care hypnotics in India (e.g., zolpidem, zopiclone) regarding dependency, residual sedation, and fall risk in elderly
- **Regulatory pathway assessment**: Determine whether a New Drug Application (NDA) or abbreviated pathway applies for a drug with established global pharmacology but no current Indian registration
- **Elderly population risk assessment**: Given the evidence on residual effects and fall risk (PMID 15089115) and inappropriate prescribing (PMID 39231170), a targeted risk mitigation strategy for geriatric use is essential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

