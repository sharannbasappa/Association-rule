# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#################################QUESTION-1######################################
                             ################# 
import pandas as pd
conda install mlxtend 
from mlxtend.frequent_patterns import apriori, association_rules 

df = pd.read_csv("C:\\Users\\shilpa\\Desktop\\Datasets_Association Rules\\book.csv")

df.columns
df.count
df.info
df.describe

frequenct_items = apriori(df, min_support  = 0.0085, max_len=5, use_colnames = True)   ## use max length(items in a combination) of 5 and use given minimum support 

###most frequent items set based on support
frequenct_items.sort_values("support", ascending = False, inplace = True )##provide support in assending order perminentaly 

###barplot for top 10
import matplotlib.pyplot as plt

plt.bar(x = list(range(0,10)), height = frequenct_items.support[0:10], color = 'rgmyk')
plt.xticks(list(range(0, 10)), frequenct_items.itemsets[0:10], rotation = 10)
plt.xlabel("items")
plt.ylabel("support")
plt.show()

rules = association_rules(frequenct_items, metric = "lift",  min_threshold=1) ##using association rule sort lift ratio wise with grater then 1 lift ratio
rules.head(10)

rules.sort_values("lift", ascending = False).head(10) ##sort wrt lift ratio and provide top 10
rules.head()

#consider only required column and removing profusion

def to_list(i):
    return (sorted(list(i)))

ma_x = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list) ##considering antecedents and consequence columns and convering in to list
ma_x = ma_x.apply(sorted)  ##sorting in sequence

rules_sets = list(ma_x)  ## convering from string to list
unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)] ##using set to remove duplicates


index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
    ##getting rules without any redandancy
    rules_no_redudancy = rules.iloc[index_rules, :]
    
## sorting them with respect to list and getting top 10
    hight_lift_ratio = rules_no_redudancy.sort_values("lift", ascending = False).head(10)
hight_lift_ratio.head()


##################################QUESTION-2########################################
                         #############################
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

groceries = []
with open("C:\\Users\\shilpa\\Desktop\\Datasets_Association Rules\\groceries.csv") as f :  ###reading file, without pandas
    groceries = f.read()
type(groceries)
# splitting the data into separate transactions using separator as "\n"
groceries = groceries.split("\n") ##split into number of rows,(file.split(,)) split by n rows

groceries_list = []
for i in groceries:
    groceries_list.append(i.split(","))  ## split growseries data by , and put into empty list(list within a list)

all_groceries_list = [i for item in groceries_list for i in item] ##iteriate every item in the list

from collections import Counter # ,OrderedDict

item_frequencies = Counter(all_groceries_list)  ##count each item and convert n the form of dictinary 

# after sorting
item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

# barplot of top 10 
import matplotlib.pyplot as plt


# Creating Data Frame for the transactions data
groceries_series = pd.DataFrame(pd.Series(groceries_list))
groceries_series = groceries_series.iloc[:9835, :] # removing the last empty transaction

groceries_series.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name

X = groceries_series['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')

frequent_itemsets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)


def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

##############################question-3#########################################
                      #######################

import pandas as pd
conda install mlxtend 
from mlxtend.frequent_patterns import apriori, association_rules 

df_1= pd.read_csv("C:\\Users\\shilpa\\Desktop\\Datasets_Association Rules\\my_movies.csv")
df = df_1.drop(["V1", "V2", "V3", "V4", "V5"], axis = 1)
df.columns
df.count
df.info
df.describe

frequenct_items = apriori(df, min_support  = 0.0085, max_len=5, use_colnames = True)   ## use max length(items in a combination) of 5 and use given minimum support 

###most frequent items set based on support
frequenct_items.sort_values("support", ascending = False, inplace = True )##provide support in assending order perminentaly 

###barplot for top 10
import matplotlib.pyplot as plt

plt.bar(x = list(range(0,10)), height = frequenct_items.support[0:10], color = 'rgmyk')
plt.xticks(list(range(0, 10)), frequenct_items.itemsets[0:10], rotation = 10)
plt.xlabel("items")
plt.ylabel("support")
plt.show()
frequenct_items.head()
rules = association_rules(frequenct_items, metric = "lift",  min_threshold=1) ##using association rule sort lift ratio wise with grater then 1 lift ratio
rules.head(10)

rules.sort_values("lift", ascending = False).head(10) ##sort wrt lift ratio and provide top 10
rules.head()

#consider only required column and removing profusion

def to_list(i):
    return (sorted(list(i)))

ma_x = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list) ##considering antecedents and consequence columns and convering in to list
ma_x = ma_x.apply(sorted)  ##sorting in sequence
ma_x.head(10)
rules_sets = list(ma_x)  ## convering from string to list
unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)] ##using set to remove duplicates


index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
    ##getting rules without any redandancy
    rules_no_redudancy = rules.iloc[index_rules, :]
    
## sorting them with respect to list and getting top 10
    hight_lift_ratio = rules_no_redudancy.sort_values("lift", ascending = False).head(10)
hight_lift_ratio.head()


###############################QUESTION-4############################################
                        ########################
import pandas as pd
conda install mlxtend 
from mlxtend.frequent_patterns import apriori, association_rules 

df_1= pd.read_csv("C:\\Users\\shilpa\\Desktop\\Datasets_Association Rules\\myphonedata.csv")
df = df_1.drop(["V1", "V2", "V3"], axis = 1)
df.isnull().sum()
df.columns
df.count
df.info
df.describe

frequenct_items = apriori(df, min_support  = 0.0085, max_len=5, use_colnames = True)   ## use max length(items in a combination) of 5 and use given minimum support 
frequenct_items.head()      ##top support items
###most frequent items set based on support
frequenct_items.sort_values("support", ascending = False, inplace = True )##provide support in assending order perminentaly 

###barplot for top 10
import matplotlib.pyplot as plt

plt.bar(x = list(range(0,10)), height = frequenct_items.support[0:10], color = 'rgmyk')
plt.xticks(list(range(0, 10)), frequenct_items.itemsets[0:10], rotation = 10)
plt.xlabel("items")
plt.ylabel("support")
plt.show()

rules = association_rules(frequenct_items, metric = "lift",  min_threshold=1) ##using association rule sort lift ratio wise with grater then 1 lift ratio
rules.head(10)

rules.sort_values("lift", ascending = False).head(10) ##sort wrt lift ratio and provide top 10
rules.head()  ##result of sorted wrt top 10 rules 

#consider only required column and removing profusion

def to_list(i):
    return (sorted(list(i)))

ma_x = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list) ##considering antecedents and consequence columns and convering in to list
ma_x = ma_x.apply(sorted)  ##sorting in sequence

rules_sets = list(ma_x)  ## convering from string to list
unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)] ##using set to remove duplicates


index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
    ##getting rules without any redandancy
    rules_no_redudancy = rules.iloc[index_rules, :]
    
## sorting them with respect to list and getting top 10
    hight_lift_ratio = rules_no_redudancy.sort_values("lift", ascending = False).head(10)
hight_lift_ratio.head()

##################################QUESTION-5##########################################
                        #############################

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

retail = []

with open("C:\\Users\\shilpa\\Desktop\\Datasets_Association Rules\\transactions_retail1.csv") as f :
    retail = f.read()

# splitting the data into separate transactions using separator as "\n"
retail = retail.split("\n")

retail_withoutna = [sub.replace('NA',' ') for sub in retail]


retail_list = []
for i in retail_withoutna:
    retail_list.append(i.split(","))

all_retail_list = [i for item in retail_list for i in item]

from collections import Counter # ,OrderedDict

item_frequencies = Counter(all_retail_list)

# after sorting
item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

# barplot of top 10 
import matplotlib.pyplot as plt

plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), items[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()


# Creating Data Frame for the transactions data
retail_series = pd.DataFrame(pd.Series(retail_list))
retail_series = retail_series.iloc[:557042, :] # removing the last empty transaction

retail_series.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name
X = retail_series['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')

frequent_itemsets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)


def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)
