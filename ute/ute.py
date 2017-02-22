__author__ = 'usuresh'

from nipype.interfaces.base import (BaseInterface, TraitedSpec, traits, File,
                                    OutputMultiPath, BaseInterfaceInputSpec,
                                    isdefined, InputMultiPath)

from ...config import config
from glob import glob
import os
from ...base import register_workflow, PBRBaseInputSpec, PBRBaseInterface

class UteInputSpec(PBRBaseInputSpec):
    foo = InputMultiPath(File(exists=True))
    # for now, using flair, but later will switch to UTE

class UteOutputSpec(TraitedSpec):
    pass
    # for now, nothing is output, but later there will be outputs

class Ute(PBRBaseInterface):
    """
    """
    input_spec = UteInputSpec
    output_spec = UteOutputSpec #fix
    #stuff AK added to the Nipype stuff
    flag = "ute" #this is for pbr mse# -w interfacename
    connections = [("nifti", "t1_files", "foo")]
    # auto-assemble connections: take the nifti interface's output called "t1_files" 
    # and connect to the this interfaces input called "foo"

    def _run_interface_pbr(self, runtime):
        #eventually, a nipype workflow will run in here, but for now
        print(self.inputs)
        return runtime


    def _get_output_folder(self):
        return "ute"

    def _list_outputs(self):
        outputs = self._outputs().get()
        #we don't have any outputs yet, but when you do, you
        # need to define how to find them
        #outputs["bar"] = glob()  

        return outputs

register_workflow(Ute)
