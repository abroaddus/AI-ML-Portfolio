# -*- coding: utf-8 -*-
"""20 Capstone EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PJ1TQLfabzuxylkjZSIXlyoQl5yr48aB

#**Capstone Project: London Transport Policy Analysis**
##**Exploratory Data Analysis**
###Andrea Broaddus

##**1. Data Cleaning**

First we load the data and look at the feature types and sample data.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/drive/MyDrive/MLAI_Haas/data/London_CC_LSOA.csv')

data.info()

data.sample(5)

"""##2.1 Check for duplicates and outliers


"""

#Check for duplicates
data.duplicated().sum()

pd.set_option('display.float_format', lambda x: '%.2f' % x)
data.describe()

#Drop non numeric features and features that will not be used as predictors
X=data.drop(columns=['lsoa01', 'lsoa01_name', 'lsoa_area', 'car_time_2001'])
X.shape

#Method of identifying outliers from https://www.kaggle.com/code/marcinrutecki/best-techniques-and-metrics-for-imbalanced-dataset
from collections import Counter

def IQR_method (data,n,features):
    """
    Takes a dataframe and returns an index list corresponding to the observations
    containing more than n outliers according to the Tukey IQR method.
    """
    outlier_list = []

    for column in features:
        # 1st quartile (25%)
        Q1 = np.percentile(data[column], 25)
        # 3rd quartile (75%)
        Q3 = np.percentile(data[column],75)
        # Interquartile range (IQR)
        IQR = Q3 - Q1
        # outlier step
        outlier_step = 1.5 * IQR
        # Determining a list of indices of outliers
        outlier_list_column = data[(data[column] < Q1 - outlier_step) | (data[column] > Q3 + outlier_step )].index
        # appending the list of outliers
        outlier_list.extend(outlier_list_column)

    # selecting observations containing more than x outliers
    outlier_list = Counter(outlier_list)
    multiple_outliers = list( k for k, v in outlier_list.items() if v > n )

    # Calculate the number of records below and above lower and above bound value respectively
    out1 = data[data[column] < Q1 - outlier_step]
    out2 = data[data[column] > Q3 + outlier_step]

    print('Total number of records below lower bound value: ', out1.shape[0])
    print('Total number of records above upper bound value: ', out2.shape[0])

    #Save the cleaned dataset
    out1.to_csv('/content/drive/MyDrive/MLAI_Haas/Capstone/outliers_below.csv', index=False)
    out2.to_csv('/content/drive/MyDrive/MLAI_Haas/Capstone/outliers_above.csv', index=False)

    # Create a new column 'outlier' in data, initialized to 0
    data['out_below'] = 0
    data['out_above'] = 0
    # Set 'outlier' to 1 for rows identified as outliers
    data.loc[out1.index, 'out_below'] = 1
    data.loc[out2.index, 'out_above'] = 1

    print('Total number of detected outliers is:', out1.shape[0]+out2.shape[0])
    print('Percentage of dataset that is outliers is:', (out1.shape[0]+out2.shape[0])/len(X))

    return multiple_outliers

# detecting outliers
numeric_columns=X.columns
Outliers_IQR = IQR_method(data,1,numeric_columns)

cross_tab = pd.crosstab(data['out_below'], data['cc'])
print(cross_tab)

cross_tab = pd.crosstab(data['out_above'], data['cc'])
print(cross_tab)

"""##2.2 Summary of Data Cleaning

*   All the features are numerical  
*   No duplicates were found
*   Many features have highly skewed distributions, therefore all data was normalized to be on the same scale
*   328 cases (6.8%) were found to have outliers in multiple features, 44 of which were in the congestion charge zone, but since they were accurate data they were left in the dataset
*   Many features have a significant percentage of null values, such as counts of large firms with over 500 employees which are only present in a few LSOAs. Since the null values represented counts of zero in other areas, nulls were replaced with zeroes in the dataset.

##**3. Data Exploration and Feature Engineering**

##3.1 Feature Distributions

Now we will use the cleaned and prepared dataset to look at the descriptive statistics, with visualizations, and make some observations.

Comparison of feature changes inside and outside zone
"""

#Check the percentage of target features, it is highly imbalanced
in_cc=data['cc']==1
print("Number of LSOAs inside the Congestion Zone:", in_cc.value_counts())
print("Percentage of LSOAs inside the Congestion Zone:", in_cc.value_counts(1),"%)")

# Replace zeros with NaN for all columns except 'cc'
for column in data.columns:
    if column != 'cc':
        data[column] = data[column].replace(0, np.nan)

#Distribution of population
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="pop_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Residents per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="pop_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
axs[1].legend(labels=['In CC zone', 'Not'])
axs[1].set_title('Residents per LSOA 2011')
axs[1].set_ylabel('Count of LSOAs')

#Distribution of employment
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="jobs_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Jobs per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="jobs_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
axs[1].legend(labels=['In CC zone', 'Not'])
axs[1].set_title('Jobs per LSOA 2011')
axs[1].set_ylabel('Count of LSOAs')

#Distribution of car travel times
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="car_time_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Car travel time per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="car_time_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Car travel time per LSOA 2011')

#Distribution of public transit travel times
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="pt_time_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Public transit travel time per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="pt_time_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Public transit travel time per LSOA 2011')

#Distribution of office rent values
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="rent_off_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Average office rent per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="rent_off_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Average office rent LSOA 2011')

#Distribution of retail rent values
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="rent_ret_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Average retail rent per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="rent_ret_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Average retail rent LSOA 2011')

#Distribution of office rent values
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="rent_whs_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Average warehouse rent per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="rent_whs_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Average warehouse rent LSOA 2011')

#Distribution of large firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="large_firms_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Large firms per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="large_firms_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Large firms per LSOA 2011')

data['lrg_firms_2001_log'] = np.log1p(data['large_firms_2001'])
data['lrg_firms_2011_log'] = np.log1p(data['large_firms_2011'])

#Distribution log of large firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="lrg_firms_2001_log", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Large firms per LSOA 2001 Log')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="lrg_firms_2011_log", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Large firms per LSOA 2011 Log')

#Distribution of medium firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="med_firms_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Medium firms per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="med_firms_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Medium firms per LSOA 2011')

data['med_firms_2001_log'] = np.log1p(data['med_firms_2001'])
data['med_firms_2011_log'] = np.log1p(data['med_firms_2011'])

#Distribution log of medium firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="med_firms_2001_log", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Medium firms per LSOA 2001 Log')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="med_firms_2011_log", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Medium firms per LSOA 2011 Log')

#Distribution of small firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="small_firms_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Small firms per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="small_firms_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Small firms per LSOA 2011')

data['sm_firms_2001_log'] = np.log1p(data['small_firms_2001'])
data['sm_firms_2011_log'] = np.log1p(data['small_firms_2011'])

#Distribution log of small firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="sm_firms_2001_log", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Small firms per LSOA 2001 Log')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="sm_firms_2011_log", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Small firms per LSOA 2011 Log')

#Distribution of micro firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="micro_firms_2001", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Micro firms per LSOA 2001')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="micro_firms_2011", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Micro firms per LSOA 2011')

data['micro_firms_2001_log'] = np.log1p(data['micro_firms_2001'])
data['micro_firms_2011_log'] = np.log1p(data['micro_firms_2011'])

#Distribution log of micro firms
fig, axs = plt.subplots(1, 2, figsize=(10,5))
sns.histplot(data=data, x="micro_firms_2001_log", hue='cc', multiple="dodge", legend=False, ax=axs[0])
axs[0].legend(labels=['In CC zone', 'Not'])
axs[0].set_title('Micro firms per LSOA 2001 Log')
axs[0].set_ylabel('Count of LSOAs')
sns.histplot(data=data, x="micro_firms_2011_log", hue='cc', multiple="dodge", legend=False, ax=axs[1])
plt.legend(labels=['In CC zone', 'Not'])
plt.title('Micro firms per LSOA 2011 Log')

#Boxplots to check skewness, using code from https://www.kaggle.com/code/marcinrutecki/voting-classifier-for-better-results
def boxplots_custom(dataset, columns_list, rows, cols, suptitle):
    fig, axs = plt.subplots(rows, cols, sharey=True, figsize=(25,25))
    fig.suptitle(suptitle,y=1, size=25)
    axs = axs.flatten()
    for i, data in enumerate(columns_list):
        sns.boxplot(data=dataset[data], orient='h', ax=axs[i])
        axs[i].set_title(data + ', skewness is: '+str(round(dataset[data].skew(axis = 0, skipna = True),2)))

boxplots_custom(dataset=data, columns_list=X01, rows=9, cols=3, suptitle='Boxplots for each variable')
plt.tight_layout()



#Save the cleaned dataset
data.to_csv('/content/drive/MyDrive/MLAI_Haas/data/London_CC_LSOA_cleaned.csv')

"""## Summary of Observations


*   Some features had highly skewed distributions, we we engineered new log features, for example firm population features
*   The car_time feature for 2001 did not have a distribution at all; all values were 5 minutes access time. This means there was no differentiation between areas of London, in terms of car accessibility. This feature will be dropped, as it cannot provide any predictive power.
*   This also means that the 2011 car_time feature is actually the difference from this uniform baseline in 2001, that is, it represents whether car access time increased or decreased over time.

##3.3 Correlations with congestion charge feature

*   We expect to see the congestion charge zone indicator have a stronger correlation with features that are more prevalent inside the zone, for example, higher office rents, and weaker correlation with features that are less prevalent, like warehouse counts
*   We also expect to see correlation between features that may overlap or be co-located in the same LSOAs, for example, higher office and retail rents, or higher counts of management consulting and business support firms
*   We expect to see strong correlation between the same features in different years, for example, job counts for 2001 and 2011, versus percent change
*   Some features are similar and have potential to be strongly correlated, so the aim is to select those with the most normal distribution and lowest amount of missing data. For example, the counts of firms by size (small, medium, large) versus aggregated together (nonmicro)
"""

#New dataframes containing only LSOAs inside or outside the Congestion Charge zone
data_cc = data[data["cc"] == 1]
data_notcc = data[data["cc"] == 0]
data_cc.shape

#Descriptive statistics for LSOAs in the congestion zone
data_cc[['pop_2001', 'jobs_2001', 'pt_time_2001', 'car_time_2001', 'large_firms_2001', 'micro_firms_2001' ]].describe()

#Descriptive statistics for LSOAs not in the congestion zone
data_notcc[['pop_2001', 'jobs_2001', 'pt_time_2001', 'car_time_2001', 'large_firms_2001', 'micro_firms_2001' ]].describe()

corr_2001 = data[['cc', 'afm_firms_2001', 'bizsup_firms_2001', 'comtelrd_firms_2001', 'creative_firms_2001', 'cult_firms_2001', 'devel_firms_2001', 'eduhsw_firms_2001', 'mgmt_firms_2001', 'pubutil_firms_2001', 'retail_firms_2001', 'tsp_firms_2001', 'ws_firms_2001']].corr(numeric_only = True)
sns.heatmap(corr_2001, annot=True, cmap="coolwarm")
plt.title("Firm Population by Industry Category 2001")

corr_2011 = data[['cc', 'afm_firms_2011', 'bizsup_firms_2011', 'comtelrd_firms_2011', 'creative_firms_2011', 'cult_firms_2011', 'devel_firms_2011', 'eduhsw_firms_2011', 'mgmt_firms_2011', 'pubutil_firms_2011', 'retail_firms_2011', 'tsp_firms_2011', 'ws_firms_2011']].corr(numeric_only = True)
sns.heatmap(corr_2011, annot=True, cmap="coolwarm")
plt.title("Firm Population by Industry Category 2011")

corr_pc = data[['cc', 'afm_pct_chg', 'bizsup_pct_chg', 'comtelrd_pct_chg', 'creative_pct_chg', 'cult_pct_chg', 'devel_pct_chg', 'eduhsw_pct_chg', 'mgmt_pct_chg', 'pubutil_pct_chg', 'retail_pct_chg', 'tsp_pct_chg', 'ws_pct_chg']].corr(numeric_only = True)
sns.heatmap(corr_pc, annot=True, cmap="coolwarm")
plt.title("Firm Population Change by Industry Category")

corr_2001 = data[['cc', 'jobs_2001', 'large_firms_2001', 'med_firms_2001', 'small_firms_2001', 'micro_firms_2001']].corr(numeric_only = True)
sns.heatmap(corr_2001, annot=True, cmap="coolwarm")
plt.title("Firm Population 2001")

corr_2011 = data[['cc', 'jobs_2011', 'large_firms_2011', 'med_firms_2011', 'small_firms_2011', 'micro_firms_2011']].corr(numeric_only = True)
sns.heatmap(corr_2011, annot=True, cmap="coolwarm")
plt.title("Firm Population 2011")

corr = data[['cc', 'jobs_pct_chg', 'large_pct_chg', 'med_pct_chg', 'small_pct_chg', 'micro_pct_chg']].corr(numeric_only = True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Firm Population Change")

corr_2001 = data[['cc', 'pop_2001', 'jobs_2001', 'pt_time_2001', 'rent_off_2001', 'rent_ret_2001', 'rent_whs_2001']].corr(numeric_only = True)
sns.heatmap(corr_2001, annot=True, cmap="coolwarm")
plt.title("Jobs, Access and Rent Levels 2001")

corr_2011 = data[['cc', 'pop_2011', 'jobs_2011', 'car_time_2011', 'pt_time_2011', 'rent_off_2011', 'rent_ret_2011', 'rent_whs_2011']].corr(numeric_only = True)
sns.heatmap(corr_2011, annot=True, cmap="coolwarm")
plt.title("Jobs, Access and Rent Levels 2011")

corr = data[['cc', 'pop_pct_chg', 'jobs_pct_chg', 'car_time_pct_chg', 'pt_time_pct_chg', 'rent_off_pct_chg', 'rent_ret_pct_chg', 'rent_whs_pct_chg']].corr(numeric_only = True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Jobs, Access and Rent Change")

"""##**4. Feature Engineering**

Now we split up the dataset into target and predictive features, and separated for analysis by year: 2001, 2011 and percent change. First we replace all null values with zeroes, to avoid issues with modeling.



"""

#Check for missing values
data.isnull().sum()

#Replace all null values with zeroes
data.replace(np.nan, 0, inplace=True)
data.isna().sum()

#Create the target dataset
#Save the y dataset
y = data['cc']
y.to_csv('/content/drive/MyDrive/MLAI_Haas/Capstone/y.csv', index=False)
y.info()

#Drop non numeric features and features that will not be used as predictors
X=data.drop(columns=['lsoa01', 'lsoa01_name', 'lsoa_area', 'car_time_2001'])
X.shape

"""## 4.1 Normalize all the features"""

#Scale the predictors using StandardScalar
from sklearn.preprocessing import StandardScaler

# create a StandardScaler object
scaler = StandardScaler()

# fit and transform the data
scaled_data = StandardScaler().fit_transform(X)

# create a new DataFrame with the scaled data
X = pd.DataFrame(scaled_data, columns=X.columns)

#Save scaled dataset
X.to_csv('/content/drive/MyDrive/MLAI_Haas/Capstone/X.csv')
X.head()

"""## 4.2 Split into target and predictor datasets"""

#Split scaled X features into sets representing 2001, 2011, and percent change predictors
X01 = X.filter(regex='_2001')
X11 = X.filter(regex='_2011')
Xpc = X.filter(regex='_pct_chg')
X01.info()
#Save the 2001 Dataset
X01.to_csv('/content/drive/MyDrive/MLAI_Haas/Capstone/X01.csv', index=False)
#Save the 2011 Dataset
X11.to_csv('/content/drive/MyDrive/MLAI_Haas/Capstone/X11.csv', index=False)
#Save the Pct Chg Dataset
Xpc.to_csv('/content/drive/MyDrive/MLAI_Haas/Capstone/Xpc.csv', index=False)



"""##**5. Summary of Observations**

The final cleaned dataset has 149,861 vehicle listings. Now we will look at the descriptive statistics, with visualizations, and make some observations.

##Summary of Observations
All or nearly all listings included these attributes: Price, Year, Manufacturer, Model, Fuel, Odometer, Transmission.

"""