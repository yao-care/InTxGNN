---
layout: default
title: Dapsone
parent: High Evidence (L1-L2)
nav_order: 232
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
description: "Dapsone: predicted new indication Pneumocystosis (evidence level L1). Approved use: Dermatitis herpetiformis, acne, leprosy"
monitor_inn: "Dapsone"
predicted_indications: ["pneumocystosis"]
---

# Dapsone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Dapsone: From Dermatitis Herpetiformis to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Dapsone is an anti-infective and anti-inflammatory drug originally used for dermatitis herpetiformis, acne and leprosy.
The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis pneumonia, PCP)**,
with **10 clinical trials** (4 rated as directly relevant Phase 3 studies) and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis herpetiformis, acne, leprosy (the approved indication text in the India registrations is empty) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, dapsone inhibits dihydropteroate synthase (DHPS) in the folate synthesis pathway, the same target as sulfonamides such as sulfamethoxazole.

*Pneumocystis jirovecii* depends on de novo folate synthesis and has a DHPS enzyme, so inhibiting it impairs growth of the organism. This gives a plausible mechanism for both prevention and treatment of PCP. Dapsone's proven antimicrobial use in leprosy rests on the same folate-pathway inhibition, so the new indication is a natural extension of its original anti-infective role.

The clinical picture is also consistent. A review of dapsone notes its use for PCP prophylaxis in HIV disease, and trials have tested it against trimethoprim-sulfamethoxazole, atovaquone and pentamidine, mainly in patients who cannot tolerate trimethoprim-sulfamethoxazole. The very high TxGNN score fits this picture.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Daily dapsone vs daily atovaquone for PCP prophylaxis in HIV patients intolerant of trimethoprim/sulfonamides |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Monthly aerosolized pentamidine vs thrice-weekly dapsone for PCP prophylaxis in HIV patients intolerant of trimethoprim/sulfonamides |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Three anti-Pneumocystis regimens (dapsone among them) plus zidovudine for primary prevention in advanced HIV |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim and clindamycin/primaquine vs trimethoprim-sulfamethoxazole for mild-to-moderate PCP |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly oral dapsone for PCP prophylaxis in HIV-infected children; toxicity and pharmacokinetics |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate with leucovorin plus dapsone vs trimethoprim-sulfamethoxazole for moderately severe PCP; dapsone's own contribution is hard to isolate |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | Not specified | Completed | Not reported | Dapsone 100 mg vs 50 mg for primary PCP prophylaxis |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | Not specified | Completed | Not reported | Dapsone plus trimethoprim vs trimethoprim-sulfamethoxazole for first-episode PCP in AIDS patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic review / network meta-analysis | Clin Microbiol Infect | Compares PCP prophylaxis regimens in people with HIV, including trimethoprim-sulfamethoxazole, dapsone-based regimens, aerosolized pentamidine and atovaquone |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic review / network meta-analysis | Clin Microbiol Infect | Compares PCP treatment regimens in people with HIV; trimethoprim-sulfamethoxazole remains the primary treatment |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guideline | J Antimicrob Chemother | ECIL-5 guidelines for PCP prophylaxis in haematological malignancy and stem cell transplant; trimethoprim-sulfamethoxazole is the drug of choice |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | Expert Opin Pharmacother | Review of *Pneumocystis jirovecii* with a focus on prevention and treatment |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Review | Dermatol Clin | Dapsone is useful for PCP prophylaxis in HIV disease and is the treatment of choice for dermatitis herpetiformis |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | J Formos Med Assoc | Overview of Pneumocystis pneumonia, which remains the leading opportunistic infection in AIDS patients |
| [21246536](https://pubmed.ncbi.nlm.nih.gov/21246536/) | 2011 | Clinical study | Cancer | Dose-related risk factors for dapsone-associated methemoglobinemia in paediatric oncology patients on PCP prophylaxis |
| [8757424](https://pubmed.ncbi.nlm.nih.gov/8757424/) | 1996 | Case series | J Acquir Immune Defic Syndr Hum Retrovirol | Five cases of methemoglobinemia from dapsone and/or primaquine in HIV-infected patients |
| [31631707](https://pubmed.ncbi.nlm.nih.gov/31631707/) | 2021 | Review | Drug Chem Toxicol | Dapsone-induced hepatic complications beyond methemoglobinemia |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case report | Ann Pharmacother | Dapsone-induced methemoglobinemia during PCP prophylaxis |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 58400 | Dapsone Tablet (Glaxo SmithKline Pharmaceuticals Ltd) | Tablet, bottle of 1000 | Not stated in registration data |
| 176343 | Pustulex Gel (Amwill Healthcare) | Gel, 20 g tube | Not stated in registration data |
| 792 | Acnedap Plus Gel (Cipla Ltd) | Gel, 15 g tube | Not stated in registration data |
| 64701 | Dapsib Gel (Indiabulls Pharmaceutical Ltd) | Gel, 15 g tube | Not stated in registration data |
| 1408 | Acnewar Plus Gel (Akumentis Healthcare Ltd) | Gel, 15 g tube | Not stated in registration data |

Only one of the 7 valid registrations is an oral product (the tablet). The other six are topical gels, which are not suitable for treating or preventing PCP.

## Safety Considerations

- **Contraindications and risk conditions (from knowledge-graph associations, not label text)**: G6PD deficiency, methemoglobinemia due to methemoglobin reductase deficiency, anemia (including macrocytic anemia), liver disease, gallbladder disease, glycogen storage disease, cystinuria, galactosemia, and pyruvate dehydrogenase E3 deficiency.
- **Key adverse effects seen in the literature**: Methemoglobinemia is the most frequently reported, including cases in HIV patients, children, oncology patients and transplant recipients. Hepatic complications, acute pancreatitis and dapsone hypersensitivity syndrome are also reported. A large Phase 4 study (NCT02550080) examined HLA-B*13:01 screening for hypersensitivity risk.
- **Drug interactions**: 350 interactions were identified. Moderate-level ones include aprepitant, metronidazole, picosulfuric acid, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, activated charcoal and troglitazone. Other listed interactions, of unknown severity, include calcitriol, pantoprazole, glimepiride, morphine, metformin, omeprazole, sucralfate, rosiglitazone, lansoprazole and vancomycin.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 trials (400 to 700 participants) and recent network meta-analyses support dapsone for PCP prophylaxis, and the folate-pathway mechanism is plausible. However, guidelines still favour trimethoprim-sulfamethoxazole as first-line, so dapsone is best positioned as an alternative for patients who cannot tolerate it. Its methemoglobinemia and hemolysis risks also require guardrails.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the oral tablet (currently missing, and a blocking gap for safety screening)
- Approved indication text for the Indian registrations, to confirm whether PCP is covered
- Confirmation of the mechanism of action in DrugBank
- G6PD screening and methemoglobin monitoring plan before and during use
- Review of the 10 moderate-level interactions, especially with other agents that can cause methemoglobinemia or hemolysis
- Confirmation that only the oral formulation is used for this indication, since the other six registrations are topical gels
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

