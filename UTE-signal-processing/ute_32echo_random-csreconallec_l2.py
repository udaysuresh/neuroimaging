### trying to make pipeline with python to take raw data stuck in .mat out for processing

import scipy.io as sio

sio.whosmat('ute_32echo_random-csreconallec_l2_r0p01.mat')
mat_contents = sio.loadmat('ute_32echo_random-csreconallec_l2_r0p01.mat')
# print(mat_contents)
## for jupyter in case I wanna make sure
