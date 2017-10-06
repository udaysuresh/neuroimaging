## quick & basic converter for my own MRI files to swap into nifti from dicoms
## I deserve this for sitting in MRI scanner for an hour

from nipype.interfaces.dcm2nii import Dcm2nii

### workflow to create: BET -> FAST using FSL corresponding to grey and white matter 

converter = Dcm2nii()

# throw inputs here
converter.inputs.source_names = ['NAME.dcm']

# says this is a good idea online bc of size/compression
converter.inputs.gzip_output = True
converter.inputs.output_dir = '.'

converter.cmdline
'dcm2nii -a y -c y -b config.ini -v y -d y -e y -g y -i n -n y -o . -p y -x n -f n NAME.dcm'