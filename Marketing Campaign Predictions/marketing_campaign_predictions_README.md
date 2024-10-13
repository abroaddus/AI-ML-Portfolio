### Using Classifiers to Identify Factors Contributing to Marketing Campaign Success

**Andrea Broaddus**

#### Executive summary
The business objective of this project is to identify the factors that most influenced the results of marketing campaigns conducted by a Portuguese bank. The performance of four classifiers (k-nearest neighbors, logistic regression, decision trees, and support vector machines) was compared to a base model for predicting customers subscribing a term deposit. Factors contributing to customers saying ‘yes’ to marketing campaigns were identified, including customer characteristics, campaign timing, and frequency of contact. Successful campaigns targeted highly educated customers who had said yes in a previous campaign and spent the longest time with agents on the phone. They were contacted mid-week in the spring or fall at times when the Euribor rate and Consumer Price Index were both high.  

#### Rationale
Identifying the factors most related to success will allow better targeting of prospective clients and management of firm resources in marketing efforts, increasing efficiency and saving costs.

#### Research Question
The research and data mining goals are to identify the most important predictors of success and to compare the performance of the classifiers (k-nearest neighbors, logistic regression, decision trees, and support vector machines) in predicting customers subscribing a term deposit.

#### Data Sources
The dataset results from 17 marketing campaigns that occurred between 2008 and 2010. It comes from the UCI Machine Learning repository link. 

#### Methodology
This analysis was conducted in python using pandas and sklearn tools on a Jupyter notebook, link. If follows the CRISP-DM project format.

#### Results
The efforts to improve the models did not yield much predictive benefit, in terms of improving accurate prediction of success. However there are a number of interesting findings about which customers are most likely to say ‘yes’ and which are most likely to say ‘no’, allowing for better targeting of resources, as shown in the summary table below. We can also observe the most effective campaign characteristics and timing.

Customers most likely to say ‘yes’ had the highest level of education, a University degree, were students working towards one, and may have already retired. They had said yes in a previous campaign and spent the longest time with agents on the phone. They were contacted mid-week in the spring or fall at times when the Euribor rate and Consumer Price Index were both high.

Customers most likely to say ‘no’ had the lowest level of education, basic 4-year, and worked in blue collar or service jobs. They may have said no in a previous campaign or have not been contacted before. They were contacted in spring or fall by telephone during times when the Employee Variation Rate was high.

No other factors significantly impacted the likelihood of success, including other levels of education or types of jobs, age, marital status, or whether the customer held a housing or personal loan. The number of contacts by any campaign did not make a difference, nor did a high level of the Consumer Confidence Index.

####  Recommendations
Based on these findings, we recommend the following:

• Since previous campaigns were one of the most important predictors of success or failure, subsequent campaigns should a)Cultivate deeper loyalty relationships with customers who say ‘yes’ and b) remove customers who said ‘no’ from further contact

• Since the number of contacts during each campaign did not significantly increase likelihood of success, and each contact has a cost, the number of contacts should be reduced, and reduce contacts by telephone.

• Strategies targeting University students and retirees will be more successful.

• Campaigns should be launched when the Euribor rate and Consumer Price Index are both high, and not launched when the Employees Variation Rate is high.

• The best months to conduct the campaign are March, August and October, and the best day to call a customer is Wednesday.

#### Next steps
We recommend further data collection and modeling to improve predictions, due to the limited results of this effort. In particular, we need better data about the customer contact itself and specific messaging, since it appears that the agent had a significant influence on the outcome of a call.

#### Outline of project

- [Link to Jupyter Notebook](https://github.com/abroaddus/AI-ML-Professional-Portfolio/blob/main/17%20Marketing%20Campaign%20Predictions/Marketing_Campaign_Predictions.ipynb)

- [Link to Final Report](https://github.com/abroaddus/AI-ML-Professional-Portfolio/blob/main/17%20Marketing%20Campaign%20Predictions/Marketing_Campaign_Predictions_Summary_Findings.pdf)


##### Contact and Further Information
andrea.broaddus@gmail.com
