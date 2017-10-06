### Grey Matter / White Matter post processing pipeline for T1/T2 weighted images
## based on commandline protocol

from nipype.interfaces.dcm2nii import Dcm2nii
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio

converter.inputs.source_names = ['NAME.dcm']

convert = pe.MapNode(interface=Dcm2nii(), name='conv', iterfield=['source_names'])

fast = pe.MapNode(interface=fsl.FAST(), name='fast', iterfield=['in_files'])

ds = pe.Node(interface=nio.DataSink(), name="ds", iterfield=['in_files'])

ds.inputs.base_directory = '.'

workflow = pe.Workflow(name='T1/T2_GM/WM_Segmentation')
workflow.base_dir = '.'

workflow.connect([(conv, fast, [('out_file', 'in_files')]), (fast, ds,[('mixeltype', 'in_files')])])

workflow.run()
