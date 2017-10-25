#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from builtins import str
from builtins import range

import os                                    # system functions

import nipype.interfaces.io as nio           # Data i/o
import nipype.interfaces.fsl as fsl          # fsl
import nipype.interfaces.utility as util     # utility
import nipype.pipeline.engine as pe          # pypeline engine
import nipype.algorithms.modelgen as model   # model generation
import nipype.algorithms.rapidart as ra      # artifact detection


#setup output
fsl.FSLCommand.set_default_output_type('NIFTI_GZ')

preproc = pe.Workflow(name='preproc')

inputnode = pe.Node(interface=util.IdentityInterface(fields=['func', 'struct', ]), name='inputspec')
