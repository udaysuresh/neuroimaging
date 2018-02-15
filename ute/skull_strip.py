
from nipype.interfaces.dcm2nii import Dcm2nii
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio

converter = Dcm2nii()
converter.source_dir = '2'



# skull stripping

bet = pe.Node(interface=fsl.BET(), name = 'bet')
bet.inputs.in_file = '20170929_dti_FA.nii.gz'

# segmentation
fast = pe.Node(interface=fsl.FAST(), name='fast')

ds = pe.Node(interface=nio.DataSink(), name="ds")

ds.inputs.base_directory = '.'

workflow = pe.Workflow(name='bet_fast')
workflow.base_dir = './output'

workflow.connect([(bet, fast, [('out_file', 'in_files')]), (fast, ds, [('mixeltype', 'in_files')])])

workflow.run()
