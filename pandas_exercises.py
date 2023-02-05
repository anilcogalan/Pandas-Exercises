

##################################################
# Pandas Exercises
##################################################

import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Task 1: Identify the Titanic dataset from the Seaborn library.
#########################################

df = sns.load_dataset('titanic')

df.head()

#########################################
# Task 2: Find the number of male and female passengers in the Titanic dataset described above.
#########################################

df['sex'].value_counts()


#########################################
# Task 3: Find the number of unique values for each column.
#########################################

df.nunique()

#########################################
# Task 4: Find the unique values of the variable pclass.
#########################################

df['pclass'].unique()


#########################################
# Task 5: Find the number of unique values of pclass and parch variables.
#########################################

pclass_and_parch = df[['pclass', 'parch']]

pclass_and_parch.nunique()

#########################################
# Task 6: Check the type of the embarked variable. Change its type to category. Check the repetition type.
#########################################

data = df.copy()

df['embarked'].dtype

data['embarked'] = data['embarked'].astype('category')

data['embarked'].dtype





#########################################
# Task 7: Show all the sages of those with embarked value C.
#########################################

df[df['embarked']== 'C']


#########################################
# Task 8: Show all the sages of those whose embarked value is not S.
#########################################

df[df['embarked'] != 'S']

#########################################
# Task 9: Show all information for female passengers younger than 30 years old.

df[(df['age'] < 30) & (df['sex'] == 'female')]


#########################################
# Task 10: Show the information of passengers whose Fare is over 500 or 70 years old.
#########################################

df[(df['fare'] > 500) | (df['age'] > 70)]


#########################################
# Task 11: Find the sum of the null values in each variable.
#########################################

df.isnull().sum()


#########################################
# Task 12: Drop the who variable from the dataframe.
#########################################

who = data.pop('who')

data.head()

df.head()

#########################################
# Task 13: Fill the empty values in the deck variable with the most repeated value (mode) of the deck variable.
#########################################

df['deck'].mode()

data['deck'].fillna(data['deck'].mode()[0], inplace=True)

data.head()


#########################################
# Task 14: Fill the empty values in the age variable with the median of the age variable.
#########################################

data['age'].fillna(data['age'].median(), inplace=True)

data.age.isnull().any() #output:False

#########################################
# Task 15: Find the sum, count, mean values of the survived variable in the breakdown of the Pclass and Gender variables.
#########################################

df.groupby(['pclass','sex']).agg({'survived': ['sum', 'count', 'mean']})



#########################################
# Task 16: Write a function that returns 1 for those under 30 and 0 for those above or equal to 30.
# Using the function you wrote, create a variable named age_flag in the titanic data set. (use apply and lambda constructs)
#########################################

data['age_flag']= data['age'].apply(lambda x: "1" if x < 30  else "0" ,axis = 1)

data.head()

#########################################
# Task 17: Define the Tips dataset from the Seaborn library.
#########################################

df_tips = sns.load_dataset("tips")

df_tips.head()



#########################################
# Task 18: Find the sum, min, max and average of the total_bill values according to the categories (Dinner, Lunch) of the Time variable.
#########################################

df_tips.groupby('time').agg({'total_bill': ['sum', 'min', 'max', 'mean']})


#########################################
# Task 19: Find the sum, min, max and average of total_bill values by days and time.
#########################################

df_tips.groupby(['day','time']).agg({'total_bill': ['sum', 'min', 'max', 'mean']})

#########################################
# Task 20: Find the sum, min, max and average of the total_bill and type values of the female customers, according to the day, for the lunch time.
#########################################
df_tips.head(20)

df_tips.loc[(df_tips['time'] == 'Lunch') &
            (df_tips['sex'] == 'Female')].\
            groupby('day').agg({'tip': ['sum', 'min', 'max', 'mean'],
                                'total_bill': ['sum', 'min', 'max', 'mean']}).T


#########################################
# Task 21: What is the average of orders with size less than 3 and total_bill greater than 10?
#########################################

df_tips.loc[(df_tips['size'] < 3) &
            (df_tips['total_bill'] > 10)]\
            .mean(numeric_only=True)


#########################################
# Task 22: Create a new variable called total_bill_tip_sum. Let him give the sum of the total bill and tip paid by each customer.
#########################################

total_bill_tip_sum = df_tips['total_bill'] + df_tips['tip']
df_tips.info() # check

#########################################
# Task 23: Sort according to the total_bill_tip_sum variable from largest to smallest and assign the first 30 people to a new dataframe.
#########################################


df_tips['total_bill_tip_sum'] = total_bill_tip_sum
df_first_thirty = df_tips.sort_values(ascending=False, by= "total_bill_tip_sum").loc[:30]
df_first_thirty