# Scottish Household Survey Project

An analysis project utilising data from the Scottish Household Survey. The aim of this project is to provide an answer to the following questions:

1. Are there certain groups of people that have good local access to green spaces in Scotland?

2. Are there groups that are lacking such access?

3. Are there any differences in access between rural and urban areas?

4. How do people in neighbourhoods with good access to green spaces differ from those who have no good
access? Are there differences in how they rate their neighbourhoods and communities?

5. Are there any characteristics that would allow us to predict neighbourhood and community ratings in the future?

<br>
<br>

## Context

The Scottish Household Survey (SHS) is a continuous survey based on a random sample of the general population in private residences. Questions are asked by an interviewer in homes all over Scotland. Its large sample size allows for analysis of all of Scotland's 32 local authorities. It is important in helping to make representative estimates both Scotland-wide and at local-authority level.

The survey provides robust evidence on the composition, characteristics, attitudes and behaviour of private households and individuals, as well as evidence on the physical condition of Scotland’s homes. The large scale of the SHS enables everyone using the survey findings to obtain an understanding of many issues by being able to analyse across key demographic household characteristics such as deprivation, age, income, gender, rurality, ethnicity, and others. This is crucial to informing the Fairer Scotland agenda and National Performance Framework. It also feeds into the Scottish Surveys Core Questions (SSCQ) sample.  

<br>

### **Business intelligence and data-driven decision making**

With the aid of the present analysis, the policy makers at the Scottish Government may gain an understanding of the relationship between many demographic variables and access to green and blue spaces in the country. A Green or Blue Space is described in the Scottish Household Survey as comprising ‘public green or open spaces in your local area, for example a park, countryside, wood, play area, canal path, riverside or beach' ([source](https://nationalperformance.gov.scot/access-green-and-blue-space)). These insights can help to diagnose and improve access to green spaces, and to help develop the SHS itself so it can better serve its purpose to inform governmental decision-making.

In addition, the second part of this project is dedicated to building predictive models that may help make sense of what constitutes good communities and neighbourhoods, by targeting and attempting to predict these in the form of self-reported ratings. This predictive analysis has the second purpose of reporting about the structure of the data itself and how to improve its quality for future uses.

<br>

### **Scottish Household Survey and the business context**

The Scottish Household Survey (SHS) is an annual survey of over 10,000 households. As already mentioned, it covers a range of different topics including household, neighbourhood and views on local public services.

The Scottish Government, local councils and various charities use the results to improve the lives of people regionally and across Scotland. The survey has been running since 1999 and is independent of all political parties.

The survey interview has two parts. The first part asks the owner or main tenant (or partner) about their home and their household. The second part asks a random adult about a range of topics including their neighbourhood, use of transport and local services. Afterwards, some participants are asked if they would be willing for a surveyor to conduct a non-intrusive survey of their home to assess its energy efficiency and condition, at a day and time that suits them.

The survey is run by Ipsos MORI on behalf of the Scottish Government. They are a data supplier that with the stated mission to produce accurate and relevant information and turn it into actionable truth.
'Our passionately curious experts not only provide the most precise measurement, but shape it to provide True Understanding of Society, Markets and People.' ([source](https://www.ipsos.com/en-uk/about-us)).

The present project fits into the wider goals of the survey by providing additional understanding and actionable insights on the data, given the great scope of the SHS. Its results are open data for everyone to examine and analyse.

<br>
<br>

## Data

### **Data sources**

All data necessary for this project is classed as open data and was sourced from the official Scottish Government's site for data and statistics [here](https://statistics.gov.scot/resource?uri=http%3A%2F%2Fstatistics.gov.scot%2Fdef%2Fconcept%2Ffolders%2Fthemes%2Fcommunity-wellbeing-and-social-environment).

In particular, three datasets were sourced for the project:

- Distance to Green or Blue Space - Scottish Household Survey

- Neighbourhood rating - Scottish Household Survey

- Community Belonging - Scottish Household Survey

<br>

### **Types of data and variables**

Data comes in the form of a relational data cube. 'Slices' of the cube can be extracted by querying the data set for two variables. Every variable is categorical and it includes the type `All`, which signifies being held constant. Then, the numerical variable `value` is the percentage of adults that meet the values for the given variable pair, the rest of the variables being constant. In particular, the following variables are considered in this project. Note that unless specified, the variables are present in all three datasets:

- `featurecode`: Categorical with no order. A code for one of the 32 Scottish regions, or for Scotland as a whole. Values: 'S12000026', 'S12000045', 'S12000033', 'S12000041', 'S12000047', 'S12000028', 'S12000034', 'S12000029', 'S12000008', 'S12000019', 'S12000040', 'S12000023', 'S12000039', 'S12000010', 'S12000049', 'S12000050', 'S12000048', 'S12000030', 'S12000038', 'S12000014', 'S12000042', 'S12000036', 'S12000035', 'S12000017', 'S12000006', 'S92000003', 'S12000021', 'S12000011', 'S12000027', 'S12000020', 'S12000005', 'S12000018', 'S12000013'.

- `datecode`: Categorical with levels, or date format. It is the year that the survey was taken. Values: 2013, 2014, 2015, 2016, 2017, 2018, 2019.

- `measurement`: Categorical with levels. The three types of measurement, whether the central measure, or the upper or lower bound of the 95% confidence interval. Values: '95% Lower Confidence Limit, Percent', 'Percent', '95% Upper Confidence Limit, Percent'.

- `units`: Constant. The units in which the column `value` is measured. Value: 'Percent Of Adults'.

- `value`: Numerical. The percentage of adults that meets the two given variable's specific value. Range: 0-100.

- `distance_to_nearest_green_or_blue_space`: Categorical with levels. From the `Distance to Green or Blue Space` dataset, and binned differently to the similar variable in the other two datasets. Values: 'A 5 minute walk or less', "Don't Know", 'Within a 6-10 minute walk', 'An 11 minute walk or more'.

- `walking_distance_to_nearest_greenspace`: Categorical with levels. The analogous variable to the one above in the `Neighbourhood rating` and `Community belonging` datasets. Values: 'More than 10 minutes', 'Less than 10 minutes', "Don't Know", 'All'.

- `age`: Categorical with levels. Different age groups for the survey respondents. Only present in `Distance to Green or Blue Space`. Values: 'All', '16-34 years', '65 years and over', '35-64 years'.

- `gender`: Categorical, binary, no order. The respondent's gender. Values: 'All', 'Female', 'Male'.

- `urban_rural_classification`: Categorical, binary, no order. Whether the household is rural or urban. In the Scottish Household Survey the definition used is as follows: Urban - areas of settlement with 10,000 people or more. Rural - areas of settlement with less than 10,000 people. Values: 'All', 'Urban', 'Rural'.

- `simd_quintiles`: Categorical, binary, with levels. Whether the household falls in the lowest quintile in the SIMD, or the other four. The [Scottish Index of Multiple Deprivation](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/?utm_source=redirect&utm_medium=shorturl&utm_campaign=SIMD) is a relative measure of deprivation that can relate to people having a low income but can also mean e.g. fewer resources or opportunities. Values: 'All', '20% most deprived', '80% least deprived'.

- `type_of_tenure`: Categorical with no order. Property ownership or tenancy. Values: 'All', 'Owned Outright', 'Social Rented', 'Private Rented', 'Other', 'Owned Mortgage/Loan'.

- `household_type`: Categorical, no order. Whether the house has elderly people or children. The 'Adults' value is just whoever does not fit in the other two categories. Values: 'All', 'Pensioners', 'Adults', 'With Children'.

- `ethnicity`: Categorical, binary, no order. Of white ethnicity, or non-white. Values: 'All', 'White', 'Other'.

- `neighbourhood_rating`: Categorical with levels. How the respondent rates their neighbourhood. Values: 'All', 'Very poor', 'Fairly poor', 'No opinion', 'Fairly good', 'Very good'.

- `community belonging`: Categorical with levels. How the respondent rates their sentiment of community belonging. Values: 'All', 'Not at all strongly', 'Not very strongly', "Don't know", 'Fairly strongly', 'Very strongly'.

<br>

### **Data formats**

The three datasets that are the basis of the project were downloaded in .CSV format from the Scottish Government's website in February 2022.

<br>

### **Data quality and bias**

The Scottish Household Survey is an annual, cross-sectional survey, where questions are asked by an interviewer in homes all over Scotland. More recently, the survey has been carried out via phone due to the COVID-19 pandemic.

Self-reported information of this kind may be at risk of being biased. For instance, after examining the distribution of neighbourhood and community ratings, one finds that they are not normally distributed, but rather skewed towards the good ratings (very/fairly good neighbourhood rating and very/fairly strongly community belonging). This may be an indication that respondents are reluctant to give bad ratings to their neighbourhoods and communities when they are being interviewed at home.

In the Scottish Household [website](https://www.gov.scot/publications/scottish-household-survey-2019-methodology-fieldwork-outcomes/pages/10/) the following are listed as a summary about data quality and bias: the quality of survey administration procedures; whether potential respondents can be found at home at times when interviewers call; whether they are able to participate i.e. not restricted by ill health, disability or communication barriers; and the willingness of members of the public to participate in the survey.

Another reason to suggest that the data may be biased is the seemingly limited choice in key demographic categories such as gender and ethnicity. Having only two choices (Male and Female and White and Other, respectively) does not capture how people may feel about their identities, and the information may be biased towards those who feel that fit the provided categories as a result.

One last source of potential bias includes the exclusion list. For example: hospitals, prisons, and military bases are excluded from participating in the survey. A a full explanation for the households excluded from the samples can be found [here](https://www.gov.scot/publications/scottish-household-survey-2019-methodology-fieldwork-outcomes/pages/3/) (For 2019, the last year considered in this project).

Of interest to the organisation may be to include proxies for the ratings questions (e.g. 'how strongly do you feel about moving somewhere else if you were given the choice?' 'Do you know your neighbour's name? Would you ask them for help?') and provide more options for the gender and ethnicity questions.

<br>
<br>

## Ethics

### **Ethical issues in data sourcing and extraction**

Other than the already mentioned concerns for the potential biases in the data, there could be further ethical considerations regarding sourcing and extraction. When interviewers visit people's homes, a non-intrusive inspection of the place may occur should respondents consent to it. The purpose of it is to broadly assess the housing conditions across Scotland, including insulation and state of repair. In all the considered years, surveyors were required to be professionally qualified and were recruited from a variety of different dwelling-related professions such as chartered surveyors, architects, civil engineers, environmental health officers and building control officers. Newly recruited surveyors were required to attend a five-day residential training course, which incorporated fieldwork practise, so that all were fully proficient with the methodology used. The training was led by representatives by Ipsos MORI with the Scottish Government providing support and input.The full methodology followed by the interviewers and surveyors during the fieldwork process can be found [here](https://www.gov.scot/publications/scottish-household-survey-2019-methodology-fieldwork-outcomes/pages/5/).

<br>

### **Ethical implications of business requirements**

Particular to the business questions there are three key variables: walking distance to the nearest green or blue space, neighbourhood rating and community belonging. Of special note is the question of distance to the nearest green space, in so far as this distance is measured in duration (the minutes it takes to walk) and not length (miles or metres). Duration alone probably makes for a better target compared to length alone, given than it has a greater impact on quality of life. For instance, if it were found that people of reduced mobility lacked access to green spaces, then measures to improve walkways, paths, road crossings and stairways should be prescribed. On the other hand, if fully mobile adults were found to lack access, then an increase in the number of green spaces should be prescribed. Unfortunately, the data does not include enough categories to complement this duration variable, such as whether people have reduced mobility. This information would be valuable in prescriptive analysis and as such its absence may carry ethical implications. The other business questions possess no ethical implications further than the ones already mentioned about bias. 

<br>
<br>

## Analysis

### **Stages in the data analysis process**

The full exploratory analysis can be found in `exploratory_analysis.html`. The main stages of this analysis were the following:

- Framing the business requirements according to a brief and sourcing the datasets necessary for analysis.

- Reading in the datasets and cleaning variable names.

- Joining the three datasets via a custom merge function

- Filtering data for Scottish averages, re-binning variables to use the same binning across all data, impute missing values.

- Initial EDA using `Pandas Profiling`.

- Are there certain groups that have local access to green space? Data exploration and visualisations via use of custom functions.

- Are there groups that are lacking access to green spaces? Data exploration and visualisations via use of custom functions.

- How do people in neighbourhoods with good access to green space differ from those who have no good access? Statistical analysis and visualisations via use of custom functions.


The full predictive modelling can be found in `predictive_modelling.html`. The main stages of model building were the following:

- Data preparation: Reading in the two datasets and cleaning variable names.

- Filtering out aggregated values.

- Feature engineering: encoding variables into binary values.

- Train and test set splitting: separating data from years 2013-2018 to use as train set and 2019 as test set. Separated the two response variables (neighbourhood rating and community belonging) from both train and test sets, since the two were at risk of being highly correlated and therefore increase the chance of over-fitting the models.

- Model training: two models were trained, a Logistic Regression model using the engineered features dataset and a Random Forest model using the minimally prepared dataset.

- Model evaluation: scored the two Logistic Regression models in terms of their mean absolute error, cross-validation accuracy and Area Under the ROC Curve metric. Scored the two Random Forest Models in terms of cross-validation accuracy.

<br>

### **Tools for data analysis**

Analysis was carried out in Python language. Tools include git and GitHub, Jupyter Notebooks, Jupyter Lab and VS Code. A full list of Python packages can be found in `requirements.txt`.

<br>

### **Summary conclusions of the analysis**

**Descriptive Analytics**

Conclusions of the exploratory analysis are the following:

- In terms of the very general characteristics of the people who report to live close to green spaces (defined as being within a 5 minute walk), it is concluded that rural households, followed by households with a mortgage or loan, and lastly households with children, score the highest percentages of adults. That is to say most of the people with good access to green spaces in Scotland meet one or more of these characteristics.
- In terms of the characteristics of people who live far from green spaces (more than a 10 min walk): non-ethnic-white households, pensioner/aged 65+ households, and households in the lowest SIMD quitile generally score the highest percentages. That is to say most people who lack access to green spaces in Scotland meet one or more of these.
- Community belonging and neighbourhood rating show no relationship with green space access, as people seem to consistently report feeling fairly/very positive regardless of their access. 

**Diagnostic Analytics**

In terms of the demographics of groups with good access to green spaces and those without good access, Variation across the years is generally minor, suggesting that access is not increasing during the years studied in this report 2013-2019. In an attempt to better understand, explain and predict neighbourhood ratings and community belongings, several predictive models were built.

**Predictive Analytics**

Out of the four predictive models built, only the Logistic Regression model that predicts neighbourhood ratings was accurate enough. In order to build this model, data features were heavily engineered, practically changing the entire dataset. Given that the original survey metrics were abstracted away, the model lacks explanatory power and can be utilised merely as a predicting tool.

**Prescriptive Analytics** the prescriptive aspects of this analysis are towards the data structure only. As it stands, the data can only be used to describe the characteristics of households with and without good access to green spaces. However, the data does not seem to reflect any changes in access over the period of study, nor be easily interpreted to understand or predict the relationship between green space access and neighbourhood/community ratings.


