---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Protozoal/Anaerobic Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a nitroimidazole antibiotic with established efficacy against anaerobic bacteria and protozoa (including amebiasis, trichomoniasis, and bacterial vaginosis).
The TxGNN model predicts it may be effective for **Pneumocystosis** (*Pneumocystis jirovecii* pneumonia),
with **0 relevant clinical trials** and **10 literature references** (predominantly reviews and case reports in the HIV/AIDS co-infection context) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Protozoal and anaerobic bacterial infections (amebiasis, trichomoniasis, bacterial vaginosis, Clostridial infections) |
| Predicted New Indication | Pneumocystosis (*Pneumocystis jirovecii* pneumonia) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided dataset. Based on known pharmacological information, Metronidazole is a nitroimidazole-class antibiotic and antiprotozoal agent. Its mechanism involves intracellular reduction of the nitro group by anaerobic electron transport carriers, generating short-lived cytotoxic radical intermediates that cause DNA strand breakage and cell death in susceptible organisms. This mechanism is well-established against strict anaerobes (e.g., *Bacteroides*, *Clostridium*) and protozoa (e.g., *Entamoeba histolytica*, *Trichomonas vaginalis*, *Giardia lamblia*).

The high TxGNN prediction score for pneumocystosis almost certainly reflects a historical artefact in the knowledge graph: *Pneumocystis jirovecii* was originally classified as a protozoan, placing it in the same ontological neighbourhood as organisms genuinely sensitive to metronidazole. However, *P. jirovecii* has since been definitively reclassified as an Ascomycete fungus. Fungi lack the anaerobic electron transport proteins that activate metronidazole's cytotoxic radicals, rendering *P. jirovecii* inherently insensitive to this drug. The current standard of care for pneumocystosis is Trimethoprim-Sulfamethoxazole (TMP-SMX) as first-line therapy, or Pentamidine as an alternative.

The literature associations found in this Evidence Pack arise exclusively from the HIV/AIDS co-infection context — patients who received metronidazole concurrently for amebiasis or anaerobic infections, and who subsequently developed pneumocystosis as an opportunistic infection, not as a condition treated by metronidazole. There is no biological rationale supporting direct activity against *P. jirovecii*.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

> **Note:** Although 23 clinical trials were retrieved in the search query, all were rated as irrelevant (Grade C) — covering topics such as head and neck cancer survivorship, opioid management, diabetes care, and primary care system design. None involved Metronidazole or pneumocystosis in any meaningful connection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | HIV-related opportunistic infections overview; pneumocystosis remains a leading cause of death despite ART; standard treatment is TMP-SMX, not metronidazole |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Infectious complications of AIDS reviewed; PCP identified as most common life-threatening infection; metronidazole referenced for concurrent anaerobic co-infections only |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | Am Rev Respiratory Disease | PCP and CMV pneumonia in a previously healthy adult male; patient had received metronidazole for a prior diarrheal illness — not as treatment for PCP |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Series | J Japanese Assoc Infectious Diseases | Two AIDS patients in Japan; Case 1 received metronidazole for amebic dysentery/liver abscess, then separately developed PCP — metronidazole played no role in PCP management |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Narrative Review | Mayo Clinic Proceedings | Antiparasitic agents overview; TMP-SMX cited as drug of choice for pneumocystosis; metronidazole listed for separate protozoal indications |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Narrative Review | American Family Physician | Drugs of choice for protozoal infections; TMP-SMX recommended for PCP; metronidazole assigned to amebiasis and trichomoniasis — separate categories |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | Pharmacokinetic justification for antiprotozoal therapy; discusses differentiation between organisms sensitive and resistant to metronidazole |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | J Formosan Medical Association | HIV patient with cecum perforation due to amebic colitis and CMV co-infection; received metronidazole for amebic colitis, not for pneumocystosis |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Reviews of Infectious Diseases | Critique of antimicrobial prophylaxis trials; does not support metronidazole for pneumocystosis prevention or treatment |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | Overview of antiprotozoal drug use; no direct evidence for metronidazole activity against *P. jirovecii* |

---

## India Market Information

Metronidazole is currently not registered in India based on the regulatory data provided, with 0 active licenses on record.

> **Important caveat:** Metronidazole is a long-established, widely available generic medicine included on the WHO Essential Medicines List. The "0 registrations" figure likely reflects a data gap in the current dataset rather than true market absence. A direct query to the CDSCO (Central Drugs Standard Control Organisation) database is recommended to verify actual market status before drawing regulatory conclusions.

---

## Safety Considerations

Detailed package insert warnings and contraindications are not available in the current dataset. Please refer to the official CDSCO-approved package insert for complete safety information.

**Key Drug Interactions** (620 total interactions on record; notable interactions listed below):

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|--------------|
| Ethanol | **Major** | Disulfiram-like reaction: flushing, nausea, vomiting, tachycardia. Alcohol must be strictly avoided during treatment and for 48 hours after the last dose |
| Paclitaxel | Moderate | Potential pharmacokinetic interaction; monitor for enhanced toxicity |
| Adalimumab | Moderate | Potential immunomodulatory interaction; monitor clinically |
| Trastuzumab emtansine | Moderate | Potential pharmacokinetic interaction |
| Ethinylestradiol | Moderate | May reduce oral contraceptive efficacy; advise additional contraception |
| Amiodarone | Moderate | Both agents have potential QT effects; cardiac monitoring recommended |
| Celecoxib | Moderate | Monitor for increased adverse effects |
| Estradiol | Moderate | Potential reduction in estrogen efficacy |
| Butalbital | Moderate | Enhanced CNS depression possible |
| Loperamide | Moderate | Monitor for CNS-related side effects |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.99% TxGNN prediction score for pneumocystosis is a false positive driven by the historical misclassification of *P. jirovecii* as a protozoan in older biomedical knowledge graphs. Since *P. jirovecii* is now established as a fungus inherently insensitive to metronidazole's mechanism, there is no pharmacological basis for this repurposing direction. All 23 retrieved clinical trials were irrelevant, and the 10 literature references document only coincidental co-administration in HIV/AIDS patients — not therapeutic activity against pneumocystosis.

**To proceed, the following is needed:**

- **Resolve data gaps first:** Download and parse CDSCO-approved package insert to obtain complete warnings, contraindications, and MOA data (currently blocking entry into safety evaluation Stage S1)
- **Verify India market status:** Direct query to CDSCO database to confirm actual registration status, as the current "0 registrations" is likely a data gap for this well-known generic
- **Prioritise higher-evidence candidates from this same Evidence Pack:**
  - **Cap polyposis (Rank 9, L3, "Proceed with Guardrails")** — 6 literature references directly support metronidazole use; PMID 12141801 specifically investigates whether the anti-inflammatory mechanism (not the antibiotic mechanism) drives remission — this is the most actionable candidate
  - **Myiasis (Rank 8, L4, "Research Question")** — biologically plausible rationale (anaerobic secondary infection coverage); case report evidence supports adjunct use
  - **Ulcerative proctosigmoiditis (Rank 3, L5)** — no current evidence but mechanistically plausible given metronidazole's established role in Crohn's disease; worth a targeted literature review
- **Do not pursue pneumocystosis** as a repurposing candidate without first demonstrating *in vitro* activity against *P. jirovecii* under current fungal classification — this would require new preclinical work with very low prior probability of success
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

