import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from base_algorithm import FrameStep, BaseRenderer, pd


class AlgBasic(BaseRenderer):
    def get_steps(self, led_matrix: pd.DataFrame) -> FrameStep:
        """Generate steps naively"""
        assert (
            led_matrix.index.size == self.N
        ), f"Incompatible N! {led_matrix.index.size} != {self.N}"

        for ix, pow2 in enumerate(self.get_2powerN(self.N)):
            
            self.add_frame_step(pow2, self.get_series_value(led_matrix.loc[ix, :]))

        return self.steps
