### Grey Matter / White Matter post processing pipeline for T1/T2 weighted images
## based on commandline protocol

from nipype.interfaces.dcm2nii import Dcm2nii
import nipype.interfaces.fsl as fsl
import nipype.pipeline.engine as pe


converter = Dcm2nii()

converter.inputs.source_names = ['NAME.dcm']
