import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge=pd.merge(left=customers,right=orders,how='left',left_on='id',right_on='customerId')
    result=merge[merge['customerId'].isna()][['name']]
    result.columns=['Customers']
    return result
    
    
