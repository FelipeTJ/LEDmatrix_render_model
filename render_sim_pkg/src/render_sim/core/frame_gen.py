import pandas as pd
import numpy as np
from typing import TypeAlias


'''Alias for DataFrame representing final rendered image'''
LEDFrame: TypeAlias =  pd.DataFrame

'''Alias for DataFrame representing single-step of LED matrix image'''
FrameStep: TypeAlias = pd.DataFrame

'''Alias for list of steps needed to display an LEDFrame [(rows, cols)]'''
StepList: TypeAlias = list[tuple[int, int]]


def get_empty_df(N: int) -> LEDFrame:
    df = pd.DataFrame(np.zeros((N, N), dtype=bool))
    df.columns.name = "cols"
    df.index.name = "rows"
    return df


def get_random_frame(N: int) -> LEDFrame:
    df = get_empty_df(N)
    return df | np.random.choice([0, 1], (N, N)).astype(bool)