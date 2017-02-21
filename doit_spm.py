from nipype.interfaces.spm.base import SPMCommand, SPMCommandInputSpec
from nipype.interfaces.base import (BaseInterface, TraitedSpec, traits, File,
                                    OutputMultiPath, BaseInterfaceInputSpec,
                                    isdefined, InputMultiPath)
import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio
from nipype.interfaces.utility import IdentityInterface
import os
#from utils import doit_workflow


class DoitInputSpec(SPMCommandInputSpec):
    data_ref = traits.List(File(exists=True), field="doit.data_ref")
    bin_thresh = traits.Float(0.5, field="doit.bin_thresh", usedefault=True) #default is 0.5?


class DoitOutputSpec(TraitedSpec):
    csv_file = File(exists=True)


class Doit(SPMCommand):
    input_spec = DoitInputSpec
    output_spec = DoitOutputSpec
    _jobtype = 'tools'
    _jobname = 'LST'

    def _format_arg(self, opt, spec, val):
        """Convert input to appropriate format for spm
        """
        # import numpy as np
        # from nipype.utils.filemanip import copyfiles

        # if opt in ['t1_files', 'flair_files']:
        #    val2 = copyfiles(val, os.path.abspath("."))
        #    return np.array(val2, dtype=object)

        return super(Doit, self)._format_arg(opt, spec, val)

    def _list_outputs(self):
        from nipype.utils.filemanip import fname_presuffix
        from glob import glob
        from os.path import join
        outputs = self._list_outputs().get()

        outputs["csv_file"] = glob(join(os.path.abspath('.'), "*.csv")) # ??
        print(outputs)
        return outputs

"""
if __name__ == '__main__':
    from glob import glob

    foo = Doit()
    print("The default value is: ", foo.inputs.bin_thresh)
    foo.inputs.data_ref = glob("/data/henry1/tristan/LST/FLAIR-MPRAGE/*/*_bin_lesion_map.nii")
    print("data_ref: ", foo.inputs.data_ref)

    foo.inputs.bin_thresh = 0.3
    print("The threshold is: ", foo.inputs.bin_thresh)
    ## Make a workflow here
"""




