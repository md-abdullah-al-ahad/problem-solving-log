import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    shape = players.shape
    return list(shape)