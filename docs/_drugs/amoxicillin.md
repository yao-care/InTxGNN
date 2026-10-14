---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 57
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic, originally used to treat bacterial infections such as urinary tract infection, otitis media, pharyngitis and bacterial pneumonia.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. The high score appears to be a computational artifact rather than a real therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia, pharyngitis, etc.) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, amoxicillin is a beta-lactam antibacterial that inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections is well established.

Polyclonal hyperviscosity syndrome is driven by excess immunoglobulins and has no antibacterial target. No plausible mechanistic link to amoxicillin was identified. The high TxGNN score appears to be a graph-based artifact, with no supporting clinical or literature evidence. The prediction is therefore **not considered reasonable** on current evidence.

### Other Predictions Reviewed

The same review covered other top-ranked predictions. None has meaningful support, except one worth noting:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Hyperamylasemia | 99.63% | L5 | A laboratory finding, not a bacterial process; no trials or publications |
| 3 | Congenital analbuminemia | 99.59% | L5 | Genetic albumin synthesis disorder; no known amoxicillin effect |
| 4 | Blood group incompatibility | 99.40% | L4 | Only a case report of infection during transplant care; not therapeutic evidence |
| 5 | Premalignant hematological system disease | 99.29% | L5 | Non-bacterial; no supporting evidence |
| 6 | Monoclonal gammopathy | 99.22% | L4 | Evidence concerns infection supportive care only |
| 7 | Hematological disease with acquired peripheral neuropathy | 99.14% | L5 | No mechanistic link or evidence |
| 8 | Septicemic plague | 99.13% | L4 | Biologically plausible at class level; flagged as a research question |

Septicemic plague is the only candidate with a plausible rationale: *Yersinia pestis* is a Gram-negative bacterium and beta-lactams target cell wall synthesis. However, standard plague therapy relies on aminoglycosides, fluoroquinolones and tetracyclines, and beta-lactams are generally considered less reliable, especially against intracellular bacteria.

## Clinical Trial Evidence

For the top-ranked prediction (polyclonal hyperviscosity syndrome), currently no related clinical trials are registered.

For reference, one trial was found for a lower-ranked prediction (monoclonal gammopathy), but it does not support repurposing:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | Not applicable | Terminated | 351 | Oral moxifloxacin vs ciprofloxacin plus amoxicillin/clavulanic acid for fever in low-risk neutropenic cancer patients; infection supportive care, not treatment of monoclonal gammopathy |

## Literature Evidence

For the top-ranked prediction, currently no related literature is available.

For the plague prediction (rank 8), the most relevant publications are preclinical or indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Amoxicillin was active in vitro against *Y. pestis*, and several antibiotics were compared in a mouse systemic infection model |
| [21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/) | 2011 | In vitro | Antimicrob Agents Chemother | Efficacy of antibiotics commonly used for plague against intracellular *Y. pestis* |
| [30563467](https://pubmed.ncbi.nlm.nih.gov/30563467/) | 2018 | In vitro | BMC Microbiol | Rapid susceptibility testing and beta-lactam-induced morphology changes in Gram-negative threat pathogens |
| [3957763](https://pubmed.ncbi.nlm.nih.gov/3957763/) | 1986 | Case report | J Am Vet Med Assoc | A cat with bubonic plague treated successfully with amoxicillin and streptomycin |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 83683 | EEshmox DX 250mg/250mg Capsule | Strip of 10 capsules | Not specified |
| 1386 | Almox DT 125 Tablet | Strip of 10 dispersible tablets | Not specified |
| 139442 | Monoclav 500 mg/125 mg Tablet | Strip of 10 tablets | Not specified |
| 131138 | Lenoxy 1000mg/200mg Injection | Vial of 20 ml injection | Not specified |
| 148810 | Moxydak-CV Oral Suspension | Bottle of 30 ml oral suspension | Not specified |

In total, 20 valid registrations exist, covering oral capsules, tablets, dispersible tablets, suspension, dry syrup and an injection.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: long QT syndrome, torsades de pointes, ventricular tachycardia, liver failure, liver disease, cholestasis, porphyria, kidney disease, gallbladder disease, osteoporosis, bone fracture, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, myasthenia gravis, and infectious mononucleosis. These should be verified against the official package insert.
- **Drug Interactions**: 271 interactions were identified. Notable ones:
  - **Major**: methotrexate; live cholera vaccine (*Vibrio cholerae* CVD 103-HgR)
  - **Moderate**: doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, anisindione, dicoumarol, mycophenolate mofetil, entecavir, balsalazide, and some probiotics (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*)
  - **Minor**: allopurinol, amiloride, azithromycin, clarithromycin, erythromycin

Package insert warnings and contraindications were not available; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome rests on a model score alone (L5), with no clinical trials or literature and no plausible mechanistic link to an antibacterial. The other top-ranked predictions are likewise unsupported. Only septicemic plague has a plausible class-level rationale, and it is better treated as a research question since standard therapy uses other antibiotic classes.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products, needed for safety screening
- Mechanism of action data (for example from DrugBank)
- For septicemic plague, comparative in vivo or clinical data showing amoxicillin is adequate against intracellular *Y. pestis*
- Any clinical or mechanistic evidence linking amoxicillin to hyperviscosity or immunoglobulin-related disease; otherwise the prediction should be deprioritised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

