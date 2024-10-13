## Capstone Project: London Transport Policy Analysis

**Andrea Broaddus, PhD**

#### Executive summary
This project investigates whether certain transportation policies can have a discernible impact on land use values and firm locations over time in a city. This was the topic of my doctoral dissertation at UC Berkeley in 2015. Using average travel time by car and public transit as transportation accessibility indicators and urban economic data such as residential and firm populations and rents, binary classification models are estimated to understand the features most associated with areas located inside the congestion charge zone, compared with areas outside, and the most significant drivers of change over time.

#### Rationale
There is a great deal of political resistance to the idea of reducing vehicle traffic in cities via congestion charging policies. If the policy is merely a tax on drivers which lacks benefits to the urban economy, this is correct. However if there are are demonstrable economic benefits in terms of employment growth and transit quality improvements, this would be an important finding in the field of urban planning.

#### Research Objectives
This project seeks evidence of changes in the urban economy of downtown London during a ten-year period after public transport improvements were introduced along with a congestion charging zone. If no evidence is found, the null hypothesis that these transport policies have no discernible impacts on land use will be supported.

#### Hypothesis
Public transit improvements paired with congestion charging produced accessibility benefits within the congestion charging zone which were capitalized into higher residential and commercial land rents. There were two primary drivers of change, lower travel times by public transit and increasing commercial rents. Improved accessibility by public transit made the zone more attractive to employers, meaning the population of firms grew and jobs became more concentrated there. Certain industries that were growing during the timeframe of the study became more concentrated in the zone, particularly creative and professional industries whose productivity relies upon employee interactions and knowledge spillovers, and business services industries whose customers are other firms. Other industries that were shrinking or did not receive productivity benefits were less able to keep up with rising commercial rents and became less concentrated in the zone, such as wholesalers and manufacturers. Higher commercial rents made the zone less attractive to others, in particular employers with vehicle fleets, small employers, and shrinking industries became less concentrated. Meanwhile higher residential rents kept the residential population stable or shrinking.

#### Research Questions
In the congestion charge zone, compared to other areas of London:
-	Has the population of people grown or shrunk at a faster or slower rate? 
-	Has employment in the congestion charge area grown or shrunk at a faster or slower rate? 
-	Have average access times by car and public transit become faster or slower? 
-	Have office, retail, and warehouse rents increased or decreased? 
-	Have the number of large, medium, small and micro firms increased or decreased? 
-	Which industries became more concentrated inside the zone, and which less concentrated?

#### Background
Congestion charging defines a zone or set of road corridors where drivers are charged usage fees during peak congestion hours. A congestion charging zone was implemented in London in 2003. It is a ring around the historic downtown area where the bulk of firms, governmental agencies, and cultural amenities are located. Vehicles that drive across the perimeter were initially charged a fee of £5 to enter the downtown zone. The congestion charge fee was increased to £8 in 2008 and £10 in 2011. It congestion charge was considered an instant success when implemented: 20% fewer cars drove into central London, meaning reduced traffic congestion and faster travel times by bus. 

The congestion charge was paired with extensive improvements to the public transport system. For example, many new buses were added to the fleet, and service frequencies were increased for both bus and rail services. Many studies have established the impact of public transport accessibility on land values, over time. For example, rents typically increase rapidly within a half-mile area around new commuter rail stations after they are built. In the lingo of urban economics, the accessibility benefits of public transport are capitalized into higher land values. A secondary impact of higher rents resulting from accessibility benefits is firm relocation. Only the firms that highly value accessibility are willing to pay higher rents for it. For example, large firms with many employees, or firms whose customers are other firms that value locating in urban agglomerations. Since congestion charging is an accessibility benefit similar to public transport improvements, should it have a similar observable effect? The research goal is to understand whether the congestion charging zone has discernible differences in urban economic data, after nearly a decade in operation.

#### Constraints
Since the congestion charge zone was paired with extensive improvements to the public transit system, it is difficult to disengle the effects of each measure. Since we do not have a counterfactual, or London without a congestion charge, it is impossible to isolate its impacts.

#### Data Description
Since this project seeks evidence of change over time, it uses a panel dataset with features representing the cases (LSOAs) at two points in time, and change over time:
-	Before the congestion charge was implemented, in 2001
-	After the congestion charge was implemented, in 2011
-	Percent change over this period
The target variable “cc” is a binary class representing whether the geographic unit (LSOA) is located inside the congestion charge zone or not. 

The unit of analysis is the LSOA, or lower super output area, a statistical geography used by the city of London. The dataset contains 4765 of these, along with about 25 features for each. Each LSOA is created to contain 400-1200 households or 1000-3000 people. Thus they vary in geographical size but are normalized for population. For this reason, this project does not normalize the data for spatial area, that is, it uses population counts per LSOA rather than population density. More details about LSOAs can be found on the UK Office for National Statistics website, https://www.ons.gov.uk/methodology/geography/ukgeographies/statisticalgeographies  

#### Data Sources
The sources for the features described in the data dictionary below are as follows:
•	Population data, UK Census
•	Employment data and travel times, UK Department for Transport Accessibility Statistics
•	Firms data, UK Office for National Statistics, Business Structure Database (microdata)
•	Rents data, UK Valuation Office Agency, Commercial Floorspace Rateable Value Statistics
It is important to note that the data used to represent commercial rent levels is not sourced from actual commercial rents, but from tax ratings data. This proxy was used because it is  publicly available and consistently calculated land valuation data.

I created this dataset from public data sources in London, England during doctoral fieldwork in 2013 and 2014. Economic data was collected for 4765 small geographic areas in London called LSOAs, which are a similar size to electoral wards. Similar data for each LSOA was collected for two years, 2001 and 2011, including counts of people and firms, average travel times by car and public transport, and average rent levels for office and retail space. The methodology is fully described in the UC Berkeley dissertation, https://escholarship.org/uc/item/0px3f6gk 

#### Data Dictionary

| Feature name	| Units	| Definition |
|---------------|-------|------------|
| lsoa01 |  |LSOA is a UK geographical unit “lower super output area” representing 400-1200 households or 1,000 to 3,000 people, defined in 2001
|lsoa01_name |  |LSOA name
| lsoa_area | Hectares | LSOA area 
| cc |		| Indicator is 1 if LSOA is located inside the London Congestion Charge zone and 0 if not
| pop_2001 | People	| Population count 
| pop_2011 | People	| Population count 
| pop_pct_chg |Percent | Percent change in population counts from 2001 to 2011
| Note – each feature below has 2001, 2011, and percent change values, named in the same convention as the population feature above
jobs	|Jobs	| Employment count
| car_time	| Minutes	| Average minimum travel time by car to this LSOA
| pt_time |	Minutes |	Average minimum travel time by transit to this LSOA
| rent_off |	Value per sq meter	| Office space rent proxy, the tax rateable value in 2001
| rent_ret	| Value per sq meter	| Retail space rent proxy, the tax rateable value in 2001
| rent_whs	| Value per sq meter	| Warehouse space rent proxy, the tax rateable value in 2001
| large_firms	| Firms	| Count of firms with 501 to 1000 employees
| med_firms	| Firms	| Count of firms with 101 to 500 employees
| small_firms	| Firms	| Count of firms with 11 to 100 employees
| micro_firms	| Firms	| Count of firms with 1 to 10 employees
| afm	| Firms	| Agriculture, fishing, mining, other natural resources
| bizsup	| Firms	| Business support services, legal, accounting, 
| comtelrd	| Firms	| Computer hardware & software, telecom, research & development
| creative	| Firms	| Publishing, advertising, media, architecture
| cult	| Firms	| Culture, libraries, museums, sports, hotels, restaurants, theatre
| devel	| Firms	| Real estate & construction, hardware, building supply
| eduhsw	| Firms	| Education, health and social work
| mgmt |	Firms	| Management consulting
| pubutil	| Firms	| Public utilities and administration
| retail	| Firms	| Retail trade
| tsp	| Firms	| Transportation
| ws	| Firms	 |Wholesale trade

#### Methodology
This project applied classification and supervised learning methods to address the research questions. Models were estimated for three datasets representing 2001, 2011 and percent change between those years. Results were compared between datasets. An improvement in classifier predictive power over time, as evidenced by higher metrics, was interpreted as evidence that the congestion charge zone has become more differentiated from other LSOAs over time.  

Exploratory Analysis:
-	Data Cleaning and Normalization
-	Feature distributions and correlations
-	Correlations with target feature, congestion charge zone
-	Cluster analysis
-	Principal component analysis

Modeling:
-	Logistic regression model identifying the most important features associated with LSOAs inside and outside the congestion charging zone in 2001, in 2011, and with percent change over time
-	Random Forest binary classification model capable of sorting LSOAs into two classes, inside and outside the congestion zone, which has stronger predictive power in 2011 than 2001
-	Neural Network binary classification model capable of sorting LSOAs into two classes, inside and outside the congestion zone, which has stronger predictive power in 2011 than 2001

#### Constraints
The two transport policies, public transit improvement and congestion charging,  were paired together, making it difficult to disentangle the effects of each measure. Since we do not have a counterfactual case, or London without a congestion charge zone, it is impossible to isolate the impacts of these transport policies from other drivers of change and attribute the findings exclusively to them.

#### Results
Evidence in support of the hypothesis was found. 
Full results are discussed in the Final Report.

#### Next steps
Further investigation of the misclassified cases could be performed, to more fully understand where they are located and why the model is not able to distinguish them. The neural network method could be further improved.

#### Outline of project

- [Exploratory Data Analysis]()
- [Models for 2001 Dataset]()
- [Models for 2001 Dataset]()
- [Models for Percent Change Dataset]()
- [Final Report]()


#### Contact and Further Information
Andrea Broaddus, PdD
