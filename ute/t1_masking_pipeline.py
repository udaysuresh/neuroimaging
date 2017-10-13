## trying to take the matlab t1 masking protocol and conv w/ nipype
## "mask off"

import os
import nipype.interfaces.fsl as fsl

T1 = "/my/directory/filename.dcm"
directory = os.path.dirname(file_path)

# TODO: convert dcm to nifti here

## preprocessing params

bet = pe.MapNode(interface=fsl.BET(), name = 'bet')

bet.inputs.vertical_gradient = 0.45
bet.inputs.mask = 0
bet.inputs.robust = True
bet.inputs.frac = 0.5 #default <- change this to adjust mask

## T1 masking
