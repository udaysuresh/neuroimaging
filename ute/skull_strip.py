
import nipype.interfaces.dcm2nii as dcm2nii
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio

dcm2nii = pe.Node(interface=dcm2nii(), name = 'dcm2nii')
dcm2nii.source_dir = '3'

# skull stripping

bet = pe.Node(interface=fsl.BET(), name = 'bet')

# segmentation
# fast = pe.Node(interface=fsl.FAST(), name='fast')

# ds = pe.Node(interface=nio.DataSink(), name="ds")

ds.inputs.base_directory = '.'

workflow = pe.Workflow(name='conv_bet')
workflow.base_dir = './output'

workflow.connect([(dcm2nii, bet, [('converted_files', 'in_file')])])
# workflow.connect([(dcm2nii, bet, [('converted_files', 'in_file')]), (bet, fast, [('out_file', 'in_files')])])


workflow.run()
