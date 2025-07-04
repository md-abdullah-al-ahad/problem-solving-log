import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rw,clm = players.shape
    return [rw,clm]