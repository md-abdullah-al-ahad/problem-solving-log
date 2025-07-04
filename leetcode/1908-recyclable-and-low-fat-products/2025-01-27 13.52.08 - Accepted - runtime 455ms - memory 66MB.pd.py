import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    low = products[(products['low_fats']=='Y') & (products['recyclable']=='Y')]
    return low[['product_id']]