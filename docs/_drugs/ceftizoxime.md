---
layout: default
title: Ceftizoxime
parent: Moderate Evidence (L3-L4)
nav_order: 160
evidence_level: L3
indication_count: 6
last_modified_at: 2026-10-14
description: "Ceftizoxime: predicted new indication Gonococcal urethritis (evidence level L3). Approved use: Urinary tract infection, streptococcal and staphylococcal infections…"
monitor_inn: "Ceftizoxime"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "xanthogranulomatous pyelonephritis", "uterine inflammatory disease", "epiglottitis", "urogenital tuberculosis"]
---

# Ceftizoxime
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **6** 
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

# Ceftizoxime: From Urinary Tract and Gonococcal Infections to Gonococcal Urethritis

## One-Sentence Summary

Ceftizoxime is a third-generation cephalosporin antibiotic, originally used for bacterial infections such as urinary tract infection, pneumonia, staphylococcal and streptococcal infections, and gonorrhea.
The TxGNN model predicts it may be effective for **gonococcal urethritis**, supported by **0 registered clinical trials** and **6 publications** (3 single-arm or comparative clinical studies from the 1980s and 1990s, plus in vitro and resistance reports).
Because gonorrhea is already a listed indication, this is largely an extension within the same pathogen rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, streptococcal and staphylococcal infections, pneumonia, gonorrhea (original indications from the knowledge graph; the Indian license records list no approved indication text) |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 18 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ceftizoxime is a third-generation cephalosporin, a class that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against *Neisseria gonorrhoeae*, including penicillinase-producing strains.

Its efficacy in gonorrhea, acute gonococcal cervicitis and endometritis is already recognised. Gonococcal urethritis is the male urethral presentation of the same infection, so the prediction is mechanistically straightforward. Published studies from the 1980s and 1990s report high cure rates after single-dose treatment, and one comparative study evaluated it against ceftriaxone.

An important caveat is resistance. A 2001 report described cephem- and aztreonam-high-resistant *N. gonorrhoeae* that did not produce beta-lactamase, which limits how relevant these older efficacy data are to current practice.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2264006](https://pubmed.ncbi.nlm.nih.gov/2264006/) | 1990 | Clinical study | Sexually Transmitted Diseases | Single-dose ceftizoxime in 175 men with confirmed uncomplicated gonococcal urethritis |
| [1948517](https://pubmed.ncbi.nlm.nih.gov/1948517/) | 1991 | Comparative clinical study | Sexually Transmitted Diseases | Single-dose ceftizoxime compared with ceftriaxone in uncomplicated urethral gonorrhea |
| [6324399](https://pubmed.ncbi.nlm.nih.gov/6324399/) | 1984 | Clinical study | Sexually Transmitted Diseases | 1 g intramuscular ceftizoxime cured all 55 men, including 26 with penicillinase-producing strains; well tolerated |
| [6325750](https://pubmed.ncbi.nlm.nih.gov/6325750/) | 1983 | Clinical study | The Japanese Journal of Antibiotics | 41 men treated with ceftizoxime plus probenecid; bacteriological and clinical evaluation of 80 isolates |
| [6092006](https://pubmed.ncbi.nlm.nih.gov/6092006/) | 1984 | In vitro / in vivo study | Chemotherapy | Most penicillin-resistant strains were highly susceptible to ceftizoxime (MIC90 0.004 µg/mL) |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistance surveillance | Journal of Infection and Chemotherapy | Emergence of cephem- and aztreonam-high-resistant *N. gonorrhoeae* without beta-lactamase production |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 230404 | Unizox 1gm Injection | Vial of 20 ml injection | Not stated in the license records |
| 41380 | Cefizox 500mg Injection (Glaxo SmithKline) | Vial of 1 injection | Not stated in the license records |
| 83173 | Eldcef 250mg Injection | Vial of 5 ml injection | Not stated in the license records |
| 78749 | Epocelin 1gm Injection | Vial of 1 injection | Not stated in the license records |
| 224494 | Trizox 1mg Injection | Vial of 1 powder for injection | Not stated in the license records |

All 18 registrations are valid single-ingredient injectable products; the table shows five of them.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions**: 12 moderate-level interactions were identified, including:
  - Aminoglycosides (kanamycin, neomycin, streptomycin, amikacin, amikacin liposome, gentamicin)
  - Warfarin
  - Chloramphenicol
  - Ethinylestradiol
  - Mycophenolic acid
  - Pemetrexed
  - Picosulfuric acid

Please refer to the package insert for warnings and formal contraindications; these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several clinical studies report high cure rates for gonococcal urethritis, and gonorrhea is already a recognised indication, so the biological plausibility is strong. However, the evidence is old, no registered trials exist, and cephalosporin-resistant gonococci have been reported, so use should be conditional on current susceptibility data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator's records (currently missing and blocking for safety screening)
- Mechanism of action data from DrugBank
- Current local *N. gonorrhoeae* susceptibility data for ceftizoxime, and a comparison with presently recommended first-line agents
- Review of renal function, bleeding risk and *C. difficile* risk, and a plan for the aminoglycoside and warfarin interactions

**Other predicted indications (for reference):**
- **Uterine inflammatory disease** (L4, Hold): plausible for pelvic inflammatory disease pathogens, but only indirect microbiology data support it.
- **Xanthogranulomatous pyelonephritis** (L5, Hold): inferred only from the urinary infection indication; definitive management is usually surgical.
- **Epiglottitis** (L4, Hold): organisms are within the spectrum, but no evidence is available and ceftriaxone is preferred in practice.
- **Ureaplasma urethritis** (L5, Hold): Ureaplasma lacks a cell wall, so beta-lactams are not expected to work; likely a graph artifact.
- **Urogenital tuberculosis** (L5, Hold): *M. tuberculosis* is intrinsically resistant to most beta-lactams; not supported by mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

