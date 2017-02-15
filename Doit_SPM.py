from nipype.interfaces.spm.base import SPMCommand, SPMCommandInputSpec
from nipype.interfaces.base import (BaseInterface, TraitedSpec, traits, File,
                                    OutputMultiPath, BaseInterfaceInputSpec,
                                    isdefined, InputMultiPath)
import nipype.pipeline.engine as pe


class DoitInputSpec(SPMCommandInputSpec):
    data_ref = traits.List(File(exists=True), field="doit.data_ref")
    bin_thresh = traits.Float(0.5, field="doit.bin_thresh", usedefault=True)


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
        outputs = self._list_outputs().get()
        outputs["csv_file"] = glob("*.csv")[0]
        return outputs


if __name__ == '__main__':
    from glob import glob

    foo = Doit()
    foo.inputs.data_ref = glob("/data/henry1/tristan/LST/FLAIR-MPRAGE/*/*_bin_lesion_map.nii")
    foo.inputs.bin_thresh = 0.3


    res = foo.run()