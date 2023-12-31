from __future__ import annotations
from render_sim.core.frame_gen import LEDFrame, FrameStep, StepList, get_empty_df
from render_sim.core.utils import assert_int_size, intersect_series


class BaseRenderer:
    def __init__(self, N: int) -> None:
        self.N = N
        self.local_df = get_empty_df(N)
        self.steps: StepList = []

    def get_steps(self, led_matrix: LEDFrame) -> StepList:
        '''Inherited class must implement this function'''
        raise NotImplementedError()

    def add_frame_step(self, row_int: int, col_int: int) -> None:
        assert_int_size(row_int, self.N)
        assert_int_size(col_int, self.N)
        self.steps.append((row_int, col_int))

    def build_from_steps(self) -> LEDFrame:
        assert self.steps != []

        base = get_empty_df(self.N)

        for r, c in self.steps:
            base |= intersect_series(r, c, self.N)
        
        print(base.replace(True, "o").replace(False, "."))
        return base

