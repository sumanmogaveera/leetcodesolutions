import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    bigcountries_filter=(world['area']>=3000000) |(world['population']>=25000000)

    return world.loc[bigcountries_filter,['area','population','name']]
