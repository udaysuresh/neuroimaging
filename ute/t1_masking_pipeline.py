## trying to take the matlab t1 masking protocol and conv w/ nipype
## "mask off"

import os
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe


T1 = "/my/directory/filename.dcm"
directory = os.path.dirname(file_path)

# TODO: convert dcm to nifti here

## T1 masking

bet = pe.MapNode(interface=fsl.BET(), name = 'bet')

## preprocessing params

bet.inputs.vertical_gradient = 0.45
bet.inputs.mask = 0
bet.inputs.robust = True
bet.inputs.frac = 0.5 #default <- change this to adjust mask

## T1 segmentation

fast = pe.MapNode(interface=fsl.FAST(), name='fast')

# TODO: register UTE magnitude to T1

# TODO: apply to frequency map or chemical shift map