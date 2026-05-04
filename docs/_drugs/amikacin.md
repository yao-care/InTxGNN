---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Amikacin
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

# Amikacin: From Serious Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is a broad-spectrum aminoglycoside antibiotic originally used to treat serious Gram-negative bacterial infections, particularly in multidrug-resistant (MDR) settings.
The TxGNN model predicts it may be effective for **Paratyphoid Fever**, supported by its established in vitro activity against *Salmonella paratyphi*.
Currently **no registered clinical trials** and **12 publications** (predominantly case reports and epidemiological studies) support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious Gram-negative bacterial infections (aminoglycoside antibiotic; not currently registered in India) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Amikacin is a semi-synthetic aminoglycoside antibiotic that exerts its bactericidal effect by irreversibly binding to the 30S ribosomal subunit of susceptible bacteria, thereby disrupting mRNA translation and causing misreading of the genetic code. This mechanism confers broad activity against aerobic Gram-negative bacilli, including members of the *Enterobacteriaceae* family. Detailed MOA data from the regulatory package insert is currently unavailable for this market; the mechanism described here is based on established pharmacological knowledge of the aminoglycoside class.

*Salmonella paratyphi* — the causative agent of paratyphoid fever — is a Gram-negative facultative intracellular rod that falls squarely within Amikacin's spectrum of activity. In vitro susceptibility studies and antibiogram surveys consistently demonstrate sensitivity of *S. paratyphi* strains to Amikacin, particularly in contexts where first-line agents (fluoroquinolones, third-generation cephalosporins, or chloramphenicol) have failed due to resistance. Multiple clinical case reports document Amikacin being deployed as a rescue or combination antibiotic in MDR enteric fever scenarios originating from the Indian subcontinent and surrounding regions.

The key biological limitation to this prediction is the intracellular niche of *Salmonella* during systemic infection: aminoglycosides penetrate poorly into eukaryotic cells, reducing efficacy against the intracellular reservoir of the pathogen. Consequently, Amikacin is not a first-line treatment for paratyphoid fever, but represents a clinically reasonable option in MDR or fluoroquinolone-resistant settings. The TxGNN knowledge-graph model's prediction is therefore mechanistically grounded — the link is real, but the clinical utility is niche and context-dependent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective Cohort | Journal of the Indian Medical Association | Prospective study of 145 blood culture-positive enteric fever cases in children; documents antibiotic sensitivity patterns for *S. typhi* and *S. paratyphi*, including aminoglycoside susceptibility. |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Clinical Treatment Study | Mikrobiyoloji Bulteni | Treatment outcomes in 48 children with *Salmonella paratyphi B* infection resistant to classical antibiotics; aminoglycoside regimens evaluated as alternatives. |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case Report | Pediatric Hematology and Oncology | Acalculous cholecystitis caused by *S. paratyphi B* in a child with leukemia; successful treatment with cefepime plus Amikacin and granulocyte colony-stimulating factor. |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case Report | The Journal of Infection | Newborn meningitis due to quinolone-resistant *S. paratyphi B*; illustrates the need for alternative agents including aminoglycosides when fluoroquinolones fail. |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Case Series | Indian Journal of Pediatrics | Paratyphoid sepsis in a neonate; blood culture grew multidrug-susceptible *S. paratyphi A*; documents clinical profile and antibiotic management. |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Epidemiological/Microbiological | Pakistan Journal of Biological Sciences | Isolation and identification of *Salmonella paratyphi* in Quetta City; reports increasing incidence and antimicrobial susceptibility patterns including aminoglycosides. |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Retrospective Antibiogram | JNMA – Journal of the Nepal Medical Association | Blood culture isolate antibiogram from a teaching hospital; Amikacin susceptibility data included for Salmonella spp. |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Antibiogram Study | Medical Journal, Armed Forces India | In vitro susceptibility of *S. typhi* and *S. paratyphi A* from northern India; all strains sensitive to aminoglycosides. |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiological Survey | The New Microbiologica | Occurrence of *S. typhi* and *S. paratyphi* in Jordan 1988–2000; background epidemiological context for treatment relevance. |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case Series | Journal of Pediatric Surgery | Splenic abscess in pediatric patients treated with needle aspiration and antibiotics; context includes enteric fever complications managed with combination regimens. |

---

## India Market Information

Amikacin (DB00479) is **not currently registered or marketed in India** according to the regulatory data in this Evidence Pack. No license records, dosage form approvals, or approved indication texts are available.

> Note: Amikacin is widely available in other markets (e.g., intravenous injection formulations are approved in the US, EU, and numerous Asian countries) for serious Gram-negative bacterial infections. The absence from this dataset may reflect a data gap rather than true unavailability in the Indian market. Independent verification via CDSCO databases is recommended.

---

## Safety Considerations

**Drug Interactions (212 interactions identified; key interactions listed below):**

| Severity | Interacting Drug | Clinical Significance |
|----------|-----------------|----------------------|
| **Major** | Magnesium sulfate | Risk of enhanced neuromuscular blockade and respiratory depression; avoid concurrent use or monitor closely |
| **Major** | Mannitol | Combined nephrotoxicity risk; concurrent use may increase renal impairment |
| Moderate | Amphotericin B (all formulations) | Additive nephrotoxicity; monitor renal function closely if co-administration is unavoidable |
| Moderate | Kanamycin / Neomycin | Additive ototoxicity and nephrotoxicity (aminoglycoside-on-aminoglycoside); avoid combination |
| Moderate | Acetylsalicylic acid | May mask aminoglycoside-induced ototoxicity; monitor hearing |
| Moderate | PPIs (Omeprazole, Esomeprazole, Pantoprazole, Lansoprazole, Dexlansoprazole, Rabeprazole) | Pharmacokinetic interaction; clinical significance varies, monitor response |
| Moderate | 5-ASA agents (Mesalazine, Olsalazine, Balsalazide) | Potential additive nephrotoxicity in patients with inflammatory bowel disease |
| Moderate | Exenatide | Altered drug absorption/transit; monitor glycaemic control and antibiotic efficacy |

> **Key clinical note:** Amikacin belongs to the aminoglycoside class, which carries well-established risks of **nephrotoxicity** and **ototoxicity** (both auditory and vestibular). These require therapeutic drug monitoring (TDM), renal function tracking, and audiometric surveillance, particularly with prolonged use or in renally impaired patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Amikacin and *Salmonella paratyphi* is biologically valid — aminoglycosides bind the 30S ribosomal subunit and *S. paratyphi* consistently shows in vitro susceptibility — making this a plausible rescue therapy for fluoroquinolone- or multi-drug-resistant paratyphoid fever. However, the evidence base consists entirely of case reports, antibiogram surveys, and epidemiological studies (L4), with no registered clinical trials, and the drug is not currently approved in India, which limits immediate clinical translation.

**To proceed, the following is needed:**

- **Formal MOA documentation:** Retrieve the package insert or DrugBank full record to confirm mechanism of action and class-specific warnings
- **Regulatory gap assessment:** Verify actual CDSCO registration status through the official database, as the current dataset shows zero records which may be incomplete
- **Resistance landscape review:** Commission a contemporary antibiogram survey of *S. paratyphi* strains in the target geography to confirm that clinically relevant Amikacin susceptibility persists
- **PK/PD analysis for intracellular pathogens:** Evaluate whether liposomal Amikacin formulations or alternative dosing strategies (e.g., once-daily high-dose) could overcome the intracellular penetration limitation
- **Prospective pilot study design:** Given L4 evidence, a small prospective cohort or comparative case series study in MDR-paratyphoid patients (where standard therapy has failed) would be the appropriate next step before any clinical adoption
- **Safety monitoring plan:** Define nephrotoxicity and ototoxicity monitoring protocols (serum creatinine, BUN, trough/peak levels, audiometry) appropriate for the target patient population

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content is subject to the YMYL standard: predicted indications must undergo formal clinical evaluation before therapeutic use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

