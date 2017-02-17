from nipype.interfaces.spm.base import SPMCommand, SPMCommandInputSpec
from nipype.interfaces.base import (BaseInterface, TraitedSpec, traits, File,
                                    OutputMultiPath, BaseInterfaceInputSpec,
                                    isdefined, InputMultiPath)
import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio
from nipype.interfaces.utility import IdentityInterface
import os


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

def doit_workflow(data_ref, bin_thresh, base_dir = None, sink_dir = None):
    # data_ref should be a list of pathname
    # base_dir is the working directory
    # sink_dir is where the data is sinking
    if base_dir is None:
        base_dir = os.getcwd()
        print("base_dir is: ", base_dir)
    if sink_dir is None:
        sink_dir = base_dir
        print("sink_dir is: ", sink_dir)

    # inputs
    inputspec = pe.Node(IdentityInterface(fields = ['data_ref', 'thresh']), name = 'inputspec')
    inputspec.inputs.mandatory_inputs = True
    inputspec.inputs.data_ref = data_ref
    inputspec.inputs.thresh = bin_thresh


    # doit_node
    doit_node = pe.MapNode(name = 'doit_node',
                           interface = Doit(),
                           iterfield = ['data_ref'])
    #doit_node.inputs.in_file =

    #datasink
    data_sink = pe.Node(nio.DataSink(), name = 'sinker')
    data_sink.inputs.base_directory = sink_dir
    data_sink.inputs.container = 'doit_output'

    # Pipeline assembly
    pipeline = pe.Workflow(name = 'pipeline_doit')
    pipeline.base_dir = base_dir

    pipeline.connect(inputspec, 'data_ref', doit_node, 'data_ref')
    pipeline.connect(inputspec, 'thresh', doit_node, 'bin_thresh')
    pipeline.connect(doit_node, 'csv_file', data_sink, 'doit_output')

    pipeline.write_graph(graph2use = 'orig')
    pipeline.config['Execution'] = {'keep_inputs': True, 'remove_unnecessary_outputs': False}

    return pipeline


if __name__ == '__main__':
    from glob import glob

    foo = Doit()
    print("The default value is: ", foo.inputs.bin_thresh)
    foo.inputs.data_ref = glob("/data/henry1/tristan/LST/FLAIR-MPRAGE/*/*_bin_lesion_map.nii")
    print("data_ref: ", foo.inputs.data_ref)

    foo.inputs.bin_thresh = 0.3
    print("The threshold is: ", foo.inputs.bin_thresh)
    ## Make a workflow here


    data_ref = glob("/data/henry1/tristan/LST/FLAIR-MPRAGE/*/*_bin_lesion_map.nii")
    dwf = doit_workflow(data_ref, 0.3)
    dwf.run()