from __future__ import annotations
import pandas as pd
import numpy as np


class FrameStep:
    pass


class BaseRenderer:
    def __init__(self, N: int) -> None:
        self.N = N
        self.local_df = self.get_empty_df(N)
        self.steps = []

    def add_frame_step(self, row_int: int, col_int: int):
        self.assert_int_size(row_int, self.N)
        self.assert_int_size(col_int, self.N)
        self.steps.append((row_int, col_int))

    def show_steps(self):
        assert self.steps != []

        for r, c in self.steps:
            step = self.intersect_series(r, c, self.N)
            pass

    @staticmethod
    def get_2powerN(N: int) -> pd.Series:
        return pd.Series([2**i for i in range(N)])

    @staticmethod
    def get_series_value(row: pd.Series) -> int:
        return BaseRenderer.get_2powerN(row.size).loc[row].sum()

    @staticmethod
    def value_to_series(val: int, N: int) -> pd.Series:
        BaseRenderer.assert_int_size(val, N)
        return pd.Series(list(f"{val:0{N}b}"), dtype=int).astype(bool)

    @staticmethod
    def get_empty_df(N: int) -> pd.DataFrame:
        df = pd.DataFrame(np.zeros((N, N), dtype=bool))
        df.columns.name = "cols"
        df.index.name = "rows"
        return df

    @staticmethod
    def assert_int_size(int: int, N: int) -> None:
        assert 0 <= int < 2 ** (N + 1), f"Out of range {int} > {N}"


def get_random_frame(N: int):
    df = BaseRenderer.get_empty_df(N)
    return df | np.random.choice([0, 1], (N, N)).astype(bool)
