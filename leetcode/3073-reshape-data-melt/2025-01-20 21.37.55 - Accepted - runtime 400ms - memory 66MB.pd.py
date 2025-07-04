import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], value_name = 'sales', var_name = 'quarter')
    return report