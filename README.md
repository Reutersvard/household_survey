# Survey Project
An analysis project utilising data from the Scottish Household Survey. The aim of this project is to provide an answer to the following questions:

1. Are there certain groups of people that have good local access to green space in Scotland?

2. Are there groups that are lacking access?

3. Are there any differences in access between rural and urban areas?

4. How do people in neighbourhoods with good access to green space differ from those who have no good
access? Are there differences in how they rate their neighbourhoods and communities?

5. Are there any characteristics that would allow us to predict the neighbourhood and community ratings in the future?

## Context

The Scottish Household Survey (SHS) is a continuous survey based on a random sample of the general population in private residences in Scotland. Questions are asked by an interviewer in homes all over Scotland. Its large sample size allows analysis of all Scotland's 32 local authorities. It is important in helping make representative estimates both at Scotland, as well as at local-authority level.

The survey provides robust evidence on the composition, characteristics, attitudes and behaviour of private households and individuals, as well as evidence on the physical condition of Scotland’s homes. The large scale of the SHS enables everyone using the survey findings to obtain an understanding of many issues by being able to analyse across key demographic household characteristics such as deprivation, age, income, gender, rurality, ethnicity, and others. This is crucial to informing the Fairer Scotland agenda, National Performance Framework and feeds in to the Scottish Surveys Core Questions (SSCQ) sample.  

#### Business intelligence and data-driven decision making

With the aid of the present analysis, the policy makers at Scottish Government could gain an understanding of the relationship between many demographic variables and access to green and blue spaces in the country. A Green and Blue Space is described in the Scottish Household Survey as comprising ‘public green or open spaces in your local area, for example a park, countryside, wood, play area, canal path, riverside or beach' ([source](https://nationalperformance.gov.scot/access-green-and-blue-space)). These insights can help diagnose and improve access to green spaces, and to help develop the SHS itself so it can better serve its purpose to inform governmental decision-making.

In addition, the second part of this project is dedicated to building predictive models that may help make sense of what constitutes good communities and neighbourhoods by targeting and attempting to predict these in the form of self-reported ratings. Again, this predictive analysis has the second purpose of reporting about the structure of the data itself and how to improve its quality for future uses.

#### Scottish Household Survey and the business context

The Scottish Household Survey (SHS) is an annual survey of over 10,000 households. As already mentioned, it covers a range of different topics including household, neighbourhood and views on local public services.

The Scottish Government, local councils and various charities use the results to improve the lives of people regionally and across Scotland. The survey has been running since 1999 and is independent of all political parties.

The survey interview is in two parts. The first part asks the owner or main tenant (or partner) about their home and their household. The second part asks a random adult about a range of topics including their neighbourhood, use of transport and local services. Afterwards, some people who take part in the survey will be asked if they would be willing for a surveyor to conduct a non-intrusive survey of their home to assess its energy efficiency and condition, at a day and time that suits them.

The survey is run by Ipsos MORI on behalf of the Scottish Government. They are a data supplier that also aim to produce accurate and relevant information and turn it into actionable truth.
'Our passionately curious experts not only provide the most precise measurement, but shape it to provide True Understanding of Society, Markets and People.' ([source](https://www.ipsos.com/en-uk/about-us)).

The present project fits into the wider goals of the survey by providing additional understanding and actionable insights on the data. Given the great scope of the SHS, its results are open data for everyone to examine and analyse.

## Data

#### Data sources

All data necessary for this project is classed as open data and was sourced from the official Scottish Government's site for data and statistics [here](https://statistics.gov.scot/resource?uri=http%3A%2F%2Fstatistics.gov.scot%2Fdef%2Fconcept%2Ffolders%2Fthemes%2Fcommunity-wellbeing-and-social-environment).

Three datasets were sourced for the project:

- Distance to Green or Blue Space - Scottish Household Survey

- Neighbourhood rating - Scottish Household Survey

- Community Belonging - Scottish Household Survey

#### Types of data and variables

Data comes in the form of a relational data cube. 'Slices' of the cube can be extracted by querying the data set for two variables. Every variable is categorical and it includes the type `All`, which signifies being constant. Then, the numerical variable `value` is the percentage of adults that meet the values for the given variable pair, taking the rest of the variables as constant. Specifically, the following variables are considered. Note that unless specified, the variables are present in all three datasets:

- `featurecode`: Categorical. A code for one of the 32 Scottish regions, or for Scotland as a whole. Values: 'S12000026', 'S12000045', 'S12000033', 'S12000041', 'S12000047', 'S12000028', 'S12000034', 'S12000029', 'S12000008', 'S12000019', 'S12000040', 'S12000023', 'S12000039', 'S12000010', 'S12000049', 'S12000050', 'S12000048', 'S12000030', 'S12000038', 'S12000014', 'S12000042', 'S12000036', 'S12000035', 'S12000017', 'S12000006', 'S92000003', 'S12000021', 'S12000011', 'S12000027', 'S12000020', 'S12000005', 'S12000018', 'S12000013'.

- `datecode`: Categorical. Year the data was taken. Values: 2013, 2014, 2015, 2016, 2017, 2018, 2019.

- `measurement`: Categorical. The three types of measurement, whether the central measure, or the upper or lower bound of the 95% confidence interval. Values: '95% Lower Confidence Limit, Percent', 'Percent', '95% Upper Confidence Limit, Percent'.

- `units`: Constant. The units in which the column `value` is measured. Value: 'Percent Of Adults'.

- `value`: Numerical. The percentage of adults that meets the two given variable's specific value. Range: 0-100.

- `distance_to_nearest_green_or_blue_space`: Categorical. From the `Distance to Green or Blue Space` dataset, and binned differently to the similar variable in the other two datasets. Values: 'A 5 minute walk or less', "Don't Know", 'Within a 6-10 minute walk', 'An 11 minute walk or more'.

- `walking_distance_to_nearest_greenspace`: Categorical. The analogous variable to the one above in the `Neighbourhood rating` and `Community belonging` datasets. Values: 'More than 10 minutes', 'Less than 10 minutes', "Don't Know", 'All'.

- `age`: Categorical. Different age groups for the survey respondents. Only present in `Distance to Green or Blue Space`. Values: 'All', '16-34 years', '65 years and over', '35-64 years'.

- `gender`: Categorical, binary. The respondent's gender. Values: 'All', 'Female', 'Male'.

- `urban_rural_classification`: Categorical, binary. Whether the household is rural or urban. In the Scottish Household Survey the definition used is as follows: Urban - areas of settlement with 10,000 people or more. Rural - areas of settlement with less than 10,000 people. Values: 'All', 'Urban', 'Rural'.

- `simd_quintiles`: Categorical, binary. Whether the household falls in the lowest quintile in the SIMD, or the other four. The [Scottish Index of Multiple Deprivation](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/?utm_source=redirect&utm_medium=shorturl&utm_campaign=SIMD) is a relative measure of deprivation that can relate to people having a low income but can also mean e.g. fewer resources or opportunities. Values: 'All', '20% most deprived', '80% least deprived'.

- `type_of_tenure`: Categorical. 

- `household_type`

- `ethnicity`

- `neighbourhood_rating`

- `community belonging`

#### Data formats

What format did your data come in? E.g. all downloaded flat files (CSV) or any data from APIs, scraping etc.

#### Data quality and bias

Briefly describe the quality of the data and whether you have any reasons to suggest the data is biased e.g. only data from a specific demographic even though a broader demographic would be of interest to the organisation.

## Ethics

#### Ethical issues in data sourcing and extraction

Do you have any ethical concerns regarding the sourcing and extraction of your data? 

#### Ethical implications of business requirements

Are there any ethical implications of the business requirements?

## Analysis

#### Stages in the data analysis process

What were the main stages in your data analysis process?

#### Tools for data analysis

What were the main tools you used for your analysis?

#### Descriptive, diagnostic, predictive and prescriptive analysis

Please report under which of the below categories your analysis falls **and why** (can be more than one) 


**Descriptive Analytics** tells you what happened in the past.

**Diagnostic Analytics** helps you understand why something happened in the past.

**Predictive Analytics** predicts what is most likely to happen in the future.

**Prescriptive Analytics** recommends actions you can take to affect those outcomes.


