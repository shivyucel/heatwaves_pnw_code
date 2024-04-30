# Pacific Northwest heatwave activity change code

This GitHub repository contains code for (in-text citation), using a simultaneous modelling approach to examine activity changes during heatwaves.

# Overview 
The steps presented in the repository are as follows:

|File                 |Description|
|---------------------|-----------|
|0.1_identify_heatwaves.ipynb         |Identify heatwaves from ERA5 temperature data|
|0.2_identify_control_days.ipynb               |Implement control day algorithm|
|0.3_merge_mobility_data.ipynb          |Merge Google mobility data and heatwave data across Pacific Northwest|
|0.4_feature_eng_1.ipynb   |Construct initial response variables and basic co-variates|
|0.5_merge_census.ipynb            |Merge socio-economic variables for each county|
|0.6_feature_eng_2.ipynb|Finalize covariates and produce modelling-ready data set|
|0.7_multivariate.nb.html|Use R2MlwiN to produce unconditional means and full model|

Notes:
* Additional files include detect_heatwave.py, which modifies code from Hobday et. al (2016).

* Multivariate multi-level model is run using R2MLwiNs

> Hobday, A.J. et al. (2016), A hierarchical approach to defining marine heatwaves, Progress in Oceanography, 141, pp. 227-238. https://doi.org/10.1016/j.pocean.2015.12.014 

> Zhang, Z., Parker, R. M. A., Charlton, C. M. J., Leckie, G., & Browne, W. J. (2016). R2MLwiN: A Package to Run MLwiN from within R. Journal of Statistical Software, 72(10). https://doi.org/10.18637/jss.v072.i10
