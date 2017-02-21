__author__ = 'sf713420'


import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio
from nipype.interfaces.utility import IdentityInterface
import os
from doit_spm import Doit


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
    data_ref = glob("/data/henry1/tristan/LST/FLAIR-MPRAGE/*/*_bin_lesion_map.nii")
    dwf = doit_workflow(data_ref, 0.3)
    dwf.run()
