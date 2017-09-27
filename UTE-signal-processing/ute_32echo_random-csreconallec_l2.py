### trying to make pipeline with python to take raw data stuck in .mat out for processing

import scipy.io as sio

# sio.whosmat('ute_32echo_random-csreconallec_l2_r0p01.mat')
# mat_contents = sio.loadmat('ute_32echo_random-csreconallec_l2_r0p01.mat')
# print(mat_contents)
## for jupyter in case I wanna make sure

### ^^^ none of this works because matlab 7.3 files can't be opened with scipy

import h5py as hp
import numpy as np
# import matlab.engine
# need to find the proper import for ME, no recognizable input here

# eng = matlab.engine.start_matlab()

mat_contents = hp.File('ute_32echo_random-csreconallec_l2_r0p01.mat')

#get the keys
print(mat_contents.keys())

#sizing the datasets
print(mat_contents['TE'])
print(mat_contents['imallplus'])

arrays ={}
for a, b in mat_contents.items():
    arrays[a] = np.array(b)
#should give the variables within the file with these keys to access a dict

print(arrays['TE'])
print(arrays['imallplus'])

brainmask = hp.File('/.brainmask')
fitting_mapping = hp.File('/truncated_fitting_mapping.m')
fit_results = hp.File('fit_results.mat')
