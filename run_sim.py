from render_sim import *


N = 4
alg = AlgBasic(N)
inFrame = get_random_frame(N)
steps = alg.get_steps(inFrame)

outFrame = alg.show_steps()
assert (outFrame.values == inFrame.values).all()
print()

