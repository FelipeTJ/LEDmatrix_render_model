import pandas as pd
import numpy as np


class FrameStep(pd.DataFrame):
    '''Simple return type name for matrix representations'''
    pass


def get_empty_df(N: int) -> FrameStep:
    df = pd.DataFrame(np.zeros((N, N), dtype=bool))
    df.columns.name = "cols"
    df.index.name = "rows"
    return df


def get_random_frame(N: int) -> FrameStep:
    df = get_empty_df(N)
    return df | np.random.choice([0, 1], (N, N)).astype(bool)