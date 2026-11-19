---
layout: default
title: Data Sources
nav_order: 93
permalink: /sources/
description: "Data sources behind InTxGNN: the public Indian Medicine Dataset (GitHub), TxGNN, ClinicalTrials.gov, PubMed and DrugBank."
---

# Data Sources

<div class="key-takeaway">
Every conclusion traces back to a public data source — nothing is a black box.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## India: what the local data cover

Local data: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset). The local data are product entries in the Indian Medicine Dataset, a public GitHub dataset. It is not a CDSCO licence register, and CDSCO licence status is not included in this data.

| Item | Value |
|---|---|
| Medicines found in the local data | {{ site.data.local_facts.licence.drugs_with_data }} |
| …with at least one listed entry | {{ site.data.local_facts.licence.drugs_with_current }} |
| …with entries but none listed | {{ site.data.local_facts.licence.drugs_none_current }} |
| Medicines not in the local data | {{ site.data.local_facts.licence.drugs_without_data }} |
| Local entries (products in the Indian Medicine Dataset) | {{ site.data.local_facts.licence.items_total }} |
| …of which listed | {{ site.data.local_facts.licence.items_current }} |

{% if site.data.local_facts.no_current.size > 0 %}Medicines with products in the Indian Medicine Dataset in this data but none listed: {% for r in site.data.local_facts.no_current %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% if site.data.local_facts.no_current_more > 0 %}, and {{ site.data.local_facts.no_current_more }} more{% endif %}{% endif %}

{% if site.data.local_facts.recent_licence_reviews.size > 0 %}Latest corrections of local registration facts: {% for r in site.data.local_facts.recent_licence_reviews %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## Source overview

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Source</th><th>Used for</th></tr>
</thead>
<tbody>
<tr><td>Drug list</td><td><a href="https://raw.githubusercontent.com/junioralive/Indian-Medicine-Dataset/main/DATA/indian_medicine_data.csv">Indian Medicine Dataset</a> (public GitHub dataset, junioralive/Indian-Medicine-Dataset)</td><td>Medicines sold in India with composition, manufacturer, price and a discontinued flag</td></tr>
<tr><td>Prediction model</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Drug&ndash;disease association prediction</td></tr>
<tr><td>Clinical trials</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidence grading (NCT)</td></tr>
<tr><td>Literature</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidence grading (PMID)</td></tr>
<tr><td>Drug information</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Ingredient mapping and target data</td></tr>
<tr><td>Interactions</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Drug&ndash;drug interaction data</td></tr>
</tbody>
</table>

India has no national product-licence database that this site can download, so the drug list comes from the
compiled price dataset above. CDSCO approval status is not included in it.

---

## Licensing

Each source has its own licence — please check before citing:

- **TxGNN**: academic use; cite Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: US NIH public data
- **DrugBank**: non-commercial use subject to its licence terms
- **Indian Medicine Dataset**: public dataset on GitHub; follow the licence stated in its repository

---

## Update frequency

| Data | Frequency |
|------|-----------|
| Discontinued status | Refreshed automatically every week (Mondays) from the dataset's CSV |
| Trial / literature evidence | Re-collected periodically |
| Interaction data | Reviewed quarterly |

---

## Academic citation

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See
<a href="{{ '/about/' | relative_url }}">About</a> for company details, the TxGNN model
background, and the full list of sites in this product line.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
