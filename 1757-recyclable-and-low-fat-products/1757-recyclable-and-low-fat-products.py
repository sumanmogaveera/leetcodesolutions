import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filter = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    
    return products.loc[filter, ['product_id']]