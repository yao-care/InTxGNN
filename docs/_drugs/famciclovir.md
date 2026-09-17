---
layout: default
title: Famciclovir
parent: Moderate Evidence (L3-L4)
nav_order: 334
evidence_level: L4
indication_count: 10
---

# Famciclovir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Famciclovir: From [Original Indication Unavailable] to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir's original approved indication is not documented in this evidence pack (mechanism-of-action and indication data are both flagged as data gaps), though cross-referenced trial evidence elsewhere in this pack confirms it is an established antiviral for herpes zoster (shingles). The TxGNN model predicts a possible link to **Post-Infectious Neuralgia**, but the two associated clinical trials do not actually test famciclovir itself, and **no supporting literature** is currently available for this specific pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Post-Infectious Neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

*(Original Indication row omitted — no approved-indication text is present in this evidence pack's regulatory license data.)*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for famciclovir in this evidence pack. Based on information cross-referenced elsewhere within this same pack (see NCT01327144 under the "chickenpox" candidate: a completed Phase 3 trial comparing Famciclovir 500 mg vs. Aciclovir 400 mg in herpes zoster patients), famciclovir is known to be an established oral antiviral used to treat herpes zoster (shingles), caused by reactivation of varicella-zoster virus (VZV).

Post-infectious neuralgia — most commonly manifesting as postherpetic neuralgia (PHN) — is a well-recognized complication of herpes zoster, arising from VZV-induced sensory nerve damage. Biologically, prompt and adequate antiviral treatment of the acute herpes zoster episode is plausible as a way to reduce the incidence or severity of subsequent neuralgia, which gives the TxGNN association some mechanistic face validity.

However, the two clinical trials retrieved for this specific candidate (below) do not test famciclovir at all — one evaluates nerve-block anesthetics and the other evaluates oxycodone, both in the context of acute herpes zoster pain management. Neither trial provides direct evidence that famciclovir itself is effective for post-infectious neuralgia; the link here is disease-context proximity, not a tested intervention.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | N/A | Not Yet Recruiting | 120 | Evaluates liposomal bupivacaine and ropivacaine nerve blocks for acute herpes zoster pain; does not study famciclovir. |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | N/A | Unknown | 140 | Evaluates early oxycodone use during acute herpes zoster to prevent postherpetic neuralgia; does not study famciclovir. |

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

No India market registrations are recorded in this evidence pack — famciclovir's India market status is listed as "Not Marketed" with 0 total licenses.

---

## Safety Considerations

- **Drug Interactions**: A DDInter database query identified 84 potential interacting drugs; severity levels are not classified ("Unknown") in this dataset. A representative sample includes Calcitriol, Doxycycline, Clotrimazole, Pantoprazole, Glimepiride, Morphine, Metformin, Omeprazole, Palonosetron, and Rosiglitazone.

Detailed warnings and contraindications are not available in this dataset — please refer to the package insert for this information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not currently backed by direct clinical or literature evidence — the two retrieved trials study other interventions (nerve blocks, oxycodone) rather than famciclovir, and no publications address famciclovir specifically for post-infectious neuralgia. Combined with missing mechanism-of-action data and a blocking gap in package-insert safety data, the evidence base is too thin to advance.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, blocking)
- Famciclovir mechanism of action data via DrugBank (DG002, high priority)
- A direct search for trials or literature testing famciclovir (not just disease-context studies) for postherpetic/post-infectious neuralgia
- Confirmation of India market/registration status, since none is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

