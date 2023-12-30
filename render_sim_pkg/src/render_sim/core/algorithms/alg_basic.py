from render_sim.core.frame_gen import pd, FrameStep
from render_sim.core.utils import get_2powerN, get_series_value
from render_sim.core.algorithms.base_algorithm import BaseRenderer


class AlgBasic(BaseRenderer):
    def get_steps(self, led_matrix: pd.DataFrame) -> FrameStep:
        """Generate steps naively"""
        assert (
            led_matrix.index.size == self.N
        ), f"Incompatible N! {led_matrix.index.size} != {self.N}"

        for ix, pow2 in enumerate(get_2powerN(self.N)):
            col_val = get_series_value(led_matrix.loc[ix, :])
            
            if col_val != 0:
                self.add_frame_step(pow2, col_val)

        return self.steps
