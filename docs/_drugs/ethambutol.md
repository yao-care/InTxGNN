---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 5
---

# Ethambutol
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is a first-line antimycobacterial agent used as part of RHZE combination therapy for tuberculosis (TB). This multi-indication TxGNN analysis predicts 5 new potential applications, with **Epiglottitis** ranked highest (99.90% score); however, mechanistic evaluation reveals this as likely a knowledge-graph artifact, while **Tuberculous Peritonitis** (Rank 4) represents the most evidence-supported prediction with **L3 evidence** backed by a Cochrane review and 20 publications. **No clinical trials** were identified for any of the 5 predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (first-line RHZE combination therapy) |
| Predicted New Indication (Top Rank) | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data was not available from queried data sources. Based on established pharmacological knowledge, Ethambutol acts by specifically inhibiting arabinosyl transferase enzymes (EmbA, EmbB, EmbC) that are essential for synthesizing arabinogalactan in the mycobacterial cell wall. This target exists exclusively in mycobacteria — primarily *Mycobacterium tuberculosis* and certain non-tuberculous mycobacteria (NTM) — and is absent in all other bacterial species.

The principal pathogens responsible for conventional epiglottitis — *Haemophilus influenzae* type b (Hib), Group A *Streptococcus*, and *Staphylococcus aureus* — do not carry EmbA/B/C targets. Ethambutol therefore has no antibacterial activity against these organisms. Tuberculous epiglottitis is an extremely rare extrapulmonary TB manifestation; when it does occur, using Ethambutol as part of standard RHZE therapy represents treatment of an established TB indication rather than a genuine repurposing opportunity.

The TxGNN model's high prediction score (99.90%) is most likely attributable to over-generalization through TB-associated laryngeal nodes in the knowledge graph, creating an apparent — but mechanistically empty — link to conventional epiglottitis. This pattern of high-score false positives for spectrum-limited antimicrobials is a recognized limitation of KG-based prediction models.

---

## Multi-Indication Prediction Overview

This report covers a 5-indication multi-prediction analysis. All predictions are summarized below for comparative evaluation:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Assessment |
|------|---------|-------------|----------------|----------------|------------|
| 1 | Epiglottitis | 99.90% | L5 | Hold | KG over-generalization; no mechanistic basis against common bacterial pathogens |
| 2 | Laryngitis | 99.71% | L4 | Research Question | TB laryngitis mechanistically valid; 20 case-level publications and case series |
| 3 | Meningococcal Infection | 99.63% | L5 | Hold | KG false positive; *Neisseria meningitidis* lacks EmbA/B/C targets |
| 4 | **Peritonitis** | **99.20%** | **L3** | **Proceed with Guardrails** | Tuberculous peritonitis: Cochrane review + systematic review provide direct support |
| 5 | Infectious Otitis Media | 99.06% | L5 | Hold | No mechanistic basis; 0 publications identified |

**Priority indication for further action:** **Tuberculous Peritonitis** (Rank 4) is the mechanistically sound and best-evidenced application in this analysis.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the 5 predicted indications.

---

## Literature Evidence

### Peritonitis — Highest Evidence Indication (L3)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16197489](https://pubmed.ncbi.nlm.nih.gov/16197489/) | 2005 | Systematic Review | Alimentary Pharmacology & Therapeutics | Comprehensive review of tuberculous peritonitis covering presentation, diagnostic strategies, and treatment; supports standard antituberculous regimens including Ethambutol |
| [27801499](https://pubmed.ncbi.nlm.nih.gov/27801499/) | 2016 | Cochrane Review | Cochrane Database of Systematic Reviews | Six-month anti-TB regimen (including Ethambutol) shown effective for abdominal tuberculosis; addresses concerns about treatment duration and relapse risk |
| [11396540](https://pubmed.ncbi.nlm.nih.gov/11396540/) | 2001 | Retrospective Study | European Journal of Gastroenterology & Hepatology | 26 cases of tuberculous peritonitis; triple antituberculous therapy efficacy evaluated over 6 months |
| [8384230](https://pubmed.ncbi.nlm.nih.gov/8384230/) | 1993 | Retrospective Study | The Journal of Infection | Ethambutol + rifabutin + amikacin triple therapy in 31 HIV patients with symptomatic MAC infection including peritonitis; clinical response assessed |
| [34666716](https://pubmed.ncbi.nlm.nih.gov/34666716/) | 2021 | Case Report | BMC Nephrology | *Mycobacterium avium*-related peritonitis in a peritoneal dialysis patient; reviews NTM peritonitis management with Ethambutol-containing regimens |
| [16206710](https://pubmed.ncbi.nlm.nih.gov/16206710/) | 2005 | Case Series | Srpski arhiv za celokupno lekarstvo | Tuberculous and fungal peritonitis in peritoneal dialysis patients; antituberculous therapy outcomes and complications |
| [10913399](https://pubmed.ncbi.nlm.nih.gov/10913399/) | 2000 | Case Report + Review | Clinical Infectious Diseases | Tuberculous peritonitis in continuous ambulatory peritoneal dialysis (CAPD) patient; standard RHZE therapy successful |
| [1439720](https://pubmed.ncbi.nlm.nih.gov/1439720/) | 1992 | Case Report | South Dakota Journal of Medicine | TB peritonitis in alcoholic cirrhosis patient; successfully treated with isoniazid + Ethambutol for 24 months |
| [29776936](https://pubmed.ncbi.nlm.nih.gov/29776936/) | 2018 | Case Report | BMJ Case Reports | Severe Ethambutol + isoniazid neurotoxicity (progressive paralysis, vision loss) in a peritoneal dialysis patient; critical safety signal for dose adjustment in renal failure |
| [33690080](https://pubmed.ncbi.nlm.nih.gov/33690080/) | 2021 | Basic Science | Tuberculosis (Edinburgh) | PknL kinase deletion in *M. tuberculosis* reduces Ethambutol and isoniazid efficacy in peritoneal macrophages; mechanistic insight into Ethambutol's action at the infection site |

### Laryngitis — Secondary Indication of Interest (L4)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Retrospective Case Series | European Respiratory Journal | 41 cases of laryngeal TB (1975–1985); treated with isoniazid, rifampicin, and Ethambutol; true vocal cords most commonly affected, epiglottis second |
| [4644838](https://pubmed.ncbi.nlm.nih.gov/4644838/) | 1972 | Case Series | Ftiziologia | Ethambutol delivered via aerosol or endobronchial instillation in laryngeal and bronchopulmonary TB; novel local delivery approach |
| [25397382](https://pubmed.ncbi.nlm.nih.gov/25397382/) | 2014 | Case Report | Ear, Nose & Throat Journal | Primary laryngeal TB: complete resolution with RHZE (including Ethambutol); highlights TB mimicking laryngeal cancer |
| [18702845](https://pubmed.ncbi.nlm.nih.gov/18702845/) | 2009 | Case Report | Journal of Laryngology and Otology | Vocal fold paralysis from *M. kansasii* (NTM) nerve compression; highlights NTM laryngeal disease where Ethambutol may have partial efficacy |
| [33133876](https://pubmed.ncbi.nlm.nih.gov/33133876/) | 2020 | Case Report | Cureus | Coexistent laryngeal + endobronchial + pulmonary TB in an immunocompetent host; treated with standard anti-TB regimen |

### Epiglottitis — Top TxGNN Prediction (L5)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Clinical Review | The Lancet. Infectious Diseases | Laryngeal tuberculosis review; epiglottis identified as one of the anatomical sites involved in laryngeal TB; standard anti-TB treatment discussed |
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Retrospective Case Series | European Respiratory Journal | 41 laryngeal TB cases; epiglottis listed as one of affected sites; treatment regimen included Ethambutol |

---

## Safety Considerations

**Drug Interactions**: Ethambutol has 112 documented interactions in the ddinter database. The following interactions carry at least moderate clinical significance:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Aluminum hydroxide | Moderate | Reduces Ethambutol oral absorption; separate dosing times by at least 2 hours |
| Metronidazole | Moderate | Potential additive peripheral neuropathy risk; monitor neurological status |
| Tinidazole | Moderate | Potential additive neurological effects; monitor during co-administration |
| Simvastatin | Moderate | Potential interaction; monitor for altered statin or Ethambutol levels |
| Rosuvastatin | Moderate | Potential interaction; monitor during co-administration |
| Naltrexone | Moderate | Monitor for altered drug effects during co-administration |
| Picosulfuric acid | Moderate | Monitor during co-administration |

Additional interactions of currently unknown clinical significance include Pantoprazole, Omeprazole, Lansoprazole, Vancomycin, Prednisone, Hydrocortisone, Prednisolone, Sulfasalazine, Ranitidine, Nystatin, and others (112 interactions total).

For complete warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold** *(Epiglottitis — Top TxGNN Prediction)*

**Decision: Proceed with Guardrails** *(Tuberculous Peritonitis — Best-Supported Indication)*

**Rationale:**
The highest-ranked TxGNN prediction (epiglottitis, 99.90%) has no mechanistic plausibility for conventional bacterial etiologies and is supported by only 2 tangential publications; this is a clear knowledge-graph false positive that should not progress further. In contrast, **Tuberculous Peritonitis** is mechanistically sound — Ethambutol's selective antimycobacterial activity directly targets the causative pathogen — and is supported by a Cochrane review and a dedicated systematic review, placing it at L3 evidence with a clear therapeutic rationale.

**To proceed for Tuberculous Peritonitis, the following is needed:**

- Retrieve Ethambutol MOA data from DrugBank (DB00330) to complete the mechanistic section of the dossier
- Obtain the local package insert (TFDA or equivalent authority) to document formal warnings and contraindications — particularly renal impairment dosing, given that PMID 29776936 documents severe neurotoxicity in peritoneal dialysis patients
- Clarify the regulatory pathway for registering Ethambutol in India, as it currently holds zero product licenses
- Establish subpopulation-specific dosing guidelines for peritoneal dialysis and renal impairment populations before any clinical use in peritonitis
- Design a comparative protocol evaluating Ethambutol-containing versus Ethambutol-sparing RHZE regimens specifically for tuberculous peritonitis, given ongoing questions about drug absorption in the abdominal cavity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

