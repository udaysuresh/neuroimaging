### Grey Matter / White Matter post processing pipeline for T1/T2 weighted images
## based on commandline protocol

from nipype.interfaces.dcm2nii import Dcm2nii
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio

converter = Dcm2nii()

converter.inputs.source_names = ['E5466S1I1.DCM']

convert = pe.MapNode(interface=Dcm2nii(), name='conv', iterfield=['source_names'])

# skull stripping
bet = pe.MapNode(interface=fsl.BET(), name = 'bet', iterfield=['frac'])

bet.inputs.frac = [0.8, 0.5, 0.2]

# segmentation
fast = pe.MapNode(interface=fsl.FAST(), name='fast', iterfield=['in_files'])

# registration
flirt = pe.MapNode(interface=fsl.FLIRT(), name='flirt', iterfield=['in_file'])

ds = pe.Node(interface=nio.DataSink(), name="ds", iterfield=['in_files'])

ds.inputs.base_directory = '.'

workflow = pe.Workflow(name='T1_T2_Segmentation')
workflow.base_dir = './output'

workflow.connect([(convert, bet, [('converted_files', 'in_file')]), (bet, fast, [('out_file', 'in_files')]), (fast, flirt, [('mixeltype', 'in_file')]), (flirt, ds, [('out_file', 'in_files')])])

workflow.run()


## scatterplotting
# voxel wise analysis, might need interpolation
# grey vs white matter masks
# regional analysis & atlas
# write up a few pages on what avenue to follow

## identify one of the strats and follow it, make sure you have enough data and then email peder
