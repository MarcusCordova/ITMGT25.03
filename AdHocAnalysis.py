import pandas as pd
import numpy as np
import json
import matplotlib as plt

with open('C:\\Users\\AMD\Downloads\\transaction-data-adhoc-analysis.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

# read column headers
df.columns

# show first few values
df.head()

df.columns

df.info()

# dfs by month

df[["transaction_date"]]
df["month"] = pd.DatetimeIndex(df["transaction_date"]).month

jan_df = df[(df["month"] == 1)]
feb_df = df[(df["month"] == 2)]
mar_df = df[(df["month"] == 3)]
apr_df = df[(df["month"] == 4)]
may_df = df[(df["month"] == 5)]
june_df = df[(df["month"] == 6)]

# monthly revenues

df["transaction_date"] = pd.to_datetime(df["transaction_date"])
monthly_revenue = df.groupby(df["transaction_date"].dt.strftime("%B"))["transaction_value"].sum()
monthly_revenue.sort_values()

# product list
df.columns

df[["transaction_items"]]

single_transactions = df[(df["transaction_items"].str.contains(";") == False) & 
                         (df["transaction_items"].str.contains("(x1)"))]
single_transactions[["transaction_items", "transaction_value"]]

# product list
prod_list = list(single_transactions["transaction_items"].unique())
prod_list

monthly_transaction = pd.DataFrame()

# item transactions per month
jan_df_split = jan_df["transaction_items"].str.split(pat=",", expand = True)

jan_df_split.rename(columns = {0 : "Brand1", 1 : "Item1", 2 : "Qty/Brand2", 3 : "Item2", 
                               4 : "Qty/Brand3", 5 : "Item3", 6 : "Qty3"}, inplace = True)


jan_df["Item1"] = jan_df_split["Item1"]
jan_df["Qty1"] = jan_df_split["Qty/Brand2"].str[2:3]
jan_df["Item2"] = jan_df_split["Item2"]
jan_df["Qty2"] = jan_df_split["Qty/Brand3"].str[2:3]
jan_df["Item3"] = jan_df_split["Item3"]
jan_df["Qty3"] = jan_df_split["Qty3"].str[2:3]

jan_transaction = jan_df[["Item1", "Qty1", "Item2", "Qty2", "Item3", "Qty3"]]
jan_transaction["Qty2"] = jan_transaction["Qty2"].fillna(0)
jan_transaction["Qty3"] = jan_transaction["Qty3"].fillna(0)

jan_transaction["Qty1"] = jan_transaction["Qty1"].astype(int)
jan_transaction["Qty2"] = jan_transaction["Qty2"].astype(int)
jan_transaction["Qty3"] = jan_transaction["Qty3"].astype(int)

jan_transaction1 = jan_transaction.groupby("Item1")["Qty1"].sum()
jan_transaction2 = jan_transaction.groupby("Item2")["Qty2"].sum()
jan_transaction3 = jan_transaction.groupby("Item3")["Qty3"].sum()
jan_per_item = jan_transaction1 + jan_transaction2 + jan_transaction3

jan_frame = jan_per_item.to_frame()
monthly_transaction["January"] = jan_frame[0]

# item transactions per month
feb_df_split = feb_df["transaction_items"].str.split(pat=",", expand = True)

feb_df_split.rename(columns = {0 : "Brand1", 1 : "Item1", 2 : "Qty/Brand2", 3 : "Item2", 
                               4 : "Qty/Brand3", 5 : "Item3", 6 : "Qty3"}, inplace = True)


feb_df["Item1"] = feb_df_split["Item1"]
feb_df["Qty1"] = feb_df_split["Qty/Brand2"].str[2:3]
feb_df["Item2"] = feb_df_split["Item2"]
feb_df["Qty2"] = feb_df_split["Qty/Brand3"].str[2:3]
feb_df["Item3"] = feb_df_split["Item3"]
feb_df["Qty3"] = feb_df_split["Qty3"].str[2:3]

feb_transaction = feb_df[["Item1", "Qty1", "Item2", "Qty2", "Item3", "Qty3"]]
feb_transaction["Qty2"] = feb_transaction["Qty2"].fillna(0)
feb_transaction["Qty3"] = feb_transaction["Qty3"].fillna(0)

feb_transaction["Qty1"] = feb_transaction["Qty1"].astype(int)
feb_transaction["Qty2"] = feb_transaction["Qty2"].astype(int)
feb_transaction["Qty3"] = feb_transaction["Qty3"].astype(int)

feb_transaction1 = feb_transaction.groupby("Item1")["Qty1"].sum()
feb_transaction2 = feb_transaction.groupby("Item2")["Qty2"].sum()
feb_transaction3 = feb_transaction.groupby("Item3")["Qty3"].sum()
feb_per_item = feb_transaction1 + feb_transaction2 + feb_transaction3

feb_frame = feb_per_item.to_frame()
monthly_transaction["February"] = feb_frame[0]

# item transactions per month
mar_df_split = mar_df["transaction_items"].str.split(pat=",", expand = True)

mar_df_split.rename(columns = {0 : "Brand1", 1 : "Item1", 2 : "Qty/Brand2", 3 : "Item2", 
                               4 : "Qty/Brand3", 5 : "Item3", 6 : "Qty3"}, inplace = True)


mar_df["Item1"] = mar_df_split["Item1"]
mar_df["Qty1"] = mar_df_split["Qty/Brand2"].str[2:3]
mar_df["Item2"] = mar_df_split["Item2"]
mar_df["Qty2"] = mar_df_split["Qty/Brand3"].str[2:3]
mar_df["Item3"] = mar_df_split["Item3"]
mar_df["Qty3"] = mar_df_split["Qty3"].str[2:3]

mar_transaction = mar_df[["Item1", "Qty1", "Item2", "Qty2", "Item3", "Qty3"]]
mar_transaction["Qty2"] = mar_transaction["Qty2"].fillna(0)
mar_transaction["Qty3"] = mar_transaction["Qty3"].fillna(0)

mar_transaction["Qty1"] = mar_transaction["Qty1"].astype(int)
mar_transaction["Qty2"] = mar_transaction["Qty2"].astype(int)
mar_transaction["Qty3"] = mar_transaction["Qty3"].astype(int)

mar_transaction1 = mar_transaction.groupby("Item1")["Qty1"].sum()
mar_transaction2 = mar_transaction.groupby("Item2")["Qty2"].sum()
mar_transaction3 = mar_transaction.groupby("Item3")["Qty3"].sum()
mar_per_item = mar_transaction1 + mar_transaction2 + mar_transaction3

mar_frame = mar_per_item.to_frame()
monthly_transaction["March"] = mar_frame[0]

# item transactions per month
apr_df_split = apr_df["transaction_items"].str.split(pat=",", expand = True)

apr_df_split.rename(columns = {0 : "Brand1", 1 : "Item1", 2 : "Qty/Brand2", 3 : "Item2", 
                               4 : "Qty/Brand3", 5 : "Item3", 6 : "Qty3"}, inplace = True)


apr_df["Item1"] = apr_df_split["Item1"]
apr_df["Qty1"] = apr_df_split["Qty/Brand2"].str[2:3]
apr_df["Item2"] = apr_df_split["Item2"]
apr_df["Qty2"] = apr_df_split["Qty/Brand3"].str[2:3]
apr_df["Item3"] = apr_df_split["Item3"]
apr_df["Qty3"] = apr_df_split["Qty3"].str[2:3]

apr_transaction = apr_df[["Item1", "Qty1", "Item2", "Qty2", "Item3", "Qty3"]]
apr_transaction["Qty2"] = apr_transaction["Qty2"].fillna(0)
apr_transaction["Qty3"] = apr_transaction["Qty3"].fillna(0)

apr_transaction["Qty1"] = apr_transaction["Qty1"].astype(int)
apr_transaction["Qty2"] = apr_transaction["Qty2"].astype(int)
apr_transaction["Qty3"] = apr_transaction["Qty3"].astype(int)

apr_transaction1 = apr_transaction.groupby("Item1")["Qty1"].sum()
apr_transaction2 = apr_transaction.groupby("Item2")["Qty2"].sum()
apr_transaction3 = apr_transaction.groupby("Item3")["Qty3"].sum()
apr_per_item = apr_transaction1 + apr_transaction2 + apr_transaction3

apr_frame = apr_per_item.to_frame()
monthly_transaction["April"] = apr_frame[0]

# item transactions per month
may_df_split = may_df["transaction_items"].str.split(pat=",", expand = True)

may_df_split.rename(columns = {0 : "Brand1", 1 : "Item1", 2 : "Qty/Brand2", 3 : "Item2", 
                               4 : "Qty/Brand3", 5 : "Item3", 6 : "Qty3"}, inplace = True)


may_df["Item1"] = may_df_split["Item1"]
may_df["Qty1"] = may_df_split["Qty/Brand2"].str[2:3]
may_df["Item2"] = may_df_split["Item2"]
may_df["Qty2"] = may_df_split["Qty/Brand3"].str[2:3]
may_df["Item3"] = may_df_split["Item3"]
may_df["Qty3"] = may_df_split["Qty3"].str[2:3]

may_transaction = may_df[["Item1", "Qty1", "Item2", "Qty2", "Item3", "Qty3"]]
may_transaction["Qty2"] = may_transaction["Qty2"].fillna(0)
may_transaction["Qty3"] = may_transaction["Qty3"].fillna(0)

may_transaction["Qty1"] = may_transaction["Qty1"].astype(int)
may_transaction["Qty2"] = may_transaction["Qty2"].astype(int)
may_transaction["Qty3"] = may_transaction["Qty3"].astype(int)

may_transaction1 = may_transaction.groupby("Item1")["Qty1"].sum()
may_transaction2 = may_transaction.groupby("Item2")["Qty2"].sum()
may_transaction3 = may_transaction.groupby("Item3")["Qty3"].sum()
may_per_item = may_transaction1 + may_transaction2 + may_transaction3

may_frame = may_per_item.to_frame()
monthly_transaction["May"] = may_frame[0]

# item transactions per month
june_df_split = june_df["transaction_items"].str.split(pat=",", expand = True)

june_df_split.rename(columns = {0 : "Brand1", 1 : "Item1", 2 : "Qty/Brand2", 3 : "Item2", 
                               4 : "Qty/Brand3", 5 : "Item3", 6 : "Qty3"}, inplace = True)


june_df["Item1"] = june_df_split["Item1"]
june_df["Qty1"] = june_df_split["Qty/Brand2"].str[2:3]
june_df["Item2"] = june_df_split["Item2"]
june_df["Qty2"] = june_df_split["Qty/Brand3"].str[2:3]
june_df["Item3"] = june_df_split["Item3"]
june_df["Qty3"] = june_df_split["Qty3"].str[2:3]

june_transaction = june_df[["Item1", "Qty1", "Item2", "Qty2", "Item3", "Qty3"]]
june_transaction["Qty2"] = june_transaction["Qty2"].fillna(0)
june_transaction["Qty3"] = june_transaction["Qty3"].fillna(0)

june_transaction["Qty1"] = june_transaction["Qty1"].astype(int)
june_transaction["Qty2"] = june_transaction["Qty2"].astype(int)
june_transaction["Qty3"] = june_transaction["Qty3"].astype(int)

june_transaction1 = june_transaction.groupby("Item1")["Qty1"].sum()
june_transaction2 = june_transaction.groupby("Item2")["Qty2"].sum()
june_transaction3 = june_transaction.groupby("Item3")["Qty3"].sum()
june_per_item = june_transaction1 + june_transaction2 + june_transaction3

june_frame = june_per_item.to_frame()
monthly_transaction["June"] = june_frame[0]


monthly_transaction.rename(columns = {"Item1" : "Item"}, inplace = True)
unit_prices = {"Beef Chicharon" : 1299, "Gummy Vitamins" : 1500,  
               "Gummy Worms" : 150, "Kimchi and Seaweed" : 799, 
               "Nutritional Milk" : 1990, "Orange Beans" : 109, "Yummy Vegetables" : 500
              }

monthly_transaction["Unit Price"] = unit_prices.values()
monthly_transaction["jan_total"] = monthly_transaction["January"] * monthly_transaction["Unit Price"]
monthly_transaction

monthly_transaction["Unit Price"] = unit_prices.values()
monthly_transaction["feb_total"] = monthly_transaction["February"] * monthly_transaction["Unit Price"]
monthly_transaction

monthly_transaction["Unit Price"] = unit_prices.values()
monthly_transaction["mar_total"] = monthly_transaction["March"] * monthly_transaction["Unit Price"]
monthly_transaction

monthly_transaction["Unit Price"] = unit_prices.values()
monthly_transaction["apr_total"] = monthly_transaction["April"] * monthly_transaction["Unit Price"]
monthly_transaction

monthly_transaction["Unit Price"] = unit_prices.values()
monthly_transaction["may_total"] = monthly_transaction["May"] * monthly_transaction["Unit Price"]
monthly_transaction

monthly_transaction["Unit Price"] = unit_prices.values()
monthly_transaction["june_total"] = monthly_transaction["June"] * monthly_transaction["Unit Price"]
monthly_transaction

# columns to list
col_list_jan = jan_df.name.values.tolist()
col_list_feb = feb_df.name.values.tolist()
col_list_mar = mar_df.name.values.tolist()
col_list_apr = apr_df.name.values.tolist()
col_list_may = may_df.name.values.tolist()
col_list_june = june_df.name.values.tolist()

# number of engaged customers
def engaged(month):
    list = set(col_list_jan)
    if month == "jan":
        return len(list)
    list = list.intersection(set(col_list_feb))
    if month == "feb":
        return len(list)
    list = list.intersection(set(col_list_mar))
    if month == "mar":
        return len(list)
    list = list.intersection(set(col_list_apr))
    if month == "apr":
        return len(list)
    list = list.intersection(set(col_list_may))
    if month == "may":
        return len(list)
    list = list.intersection(set(col_list_june))
    if month == "jun":
        return len(list)
    
# number of repeaters customers
def repeaters(month):
    list = set(col_list_jan)
    if month == "jan":
        return 0
    if month == "feb":
        list = set(col_list_jan).intersection(set(col_list_feb))
        return len(list)
    if month == "mar":
        list = set(col_list_feb).intersection(set(col_list_mar))
        return len(list)
    if month == "apr":
        list = set(col_list_mar).intersection(set(col_list_apr))
        return len(list)
    if month == "may":
        list = set(col_list_apr).intersection(set(col_list_may))
        return len(list)
    if month == "jun":
        list = set(col_list_may).intersection(set(col_list_june))
        return len(list)
    
# number of inactive customers
def inactive(month):
    list = set(col_list_jan)
    if month == "jan":
        return 0
    if month == "feb":
        total = 0
        for customer in list:
            if not(customer in col_list_feb):
                total = total + 1
        return total
    list = list.union(set(col_list_feb))
    if month == "mar":
        total = 0
        for customer in list:
            if not(customer in col_list_mar):
                total = total + 1
        return total
    list = list.union(set(col_list_mar))
    if month == "apr":
        total = 0
        for customer in list:
            if not(customer in col_list_apr):
                total = total + 1
        return total
    list = list.union(set(col_list_apr))
    if month == "may":
        total = 0
        for customer in list:
            if not(customer in col_list_may):
                total = total + 1
        return total
    list = list.union(set(col_list_may))
    if month == "jun":
        total = 0
        for customer in list:
            if not(customer in col_list_june):
                total = total + 1
        return total