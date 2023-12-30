import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from algorithms.alg_basic import AlgBasic
from algorithms.base_algorithm import get_random_frame


N = 4
alg = AlgBasic(N)
inFrame = get_random_frame(N)
steps = alg.get_steps(inFrame)

outFrame = alg.show_steps()
assert (outFrame.values == inFrame.values).all()
print()

