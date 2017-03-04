__author__ = 'sf713420'


import nipype.pipeline.engine as pe
import nipype.interfaces.io as nio
from nipype.interfaces.utility import IdentityInterface
import os
import sys
print(__file__)
print(sys.path)
sys.path.append(os.path.dirname(__file__))
import numpy as np
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

    count = 0


    # inputs
    inputspec = pe.Node(IdentityInterface(fields = ['data_ref', 'thresh']), name = 'inputspec')
    inputspec.inputs.mandatory_inputs = True
    inputspec.inputs.data_ref = data_ref
    inputspec.inputs.thresh = bin_thresh


    # doit_node
    doit_node = pe.Node(name = 'doit_node',
                           interface = Doit(),
                           #iterfield = ['data_ref']
                           )
    doit_node.iterables = ("bin_thresh", thresh_array)
    # TODO
    #doit_node.inputs.in_file = doit_node.inputs.data_ref
    print(doit_node.iterables)
    print(doit_node.inputs.bin_thresh)

    #datasink

    """ # This is not necessary
    print(count)
    thresh_str = '%.2f' % doit_node.iterables[1][count]
    count += 1
    """

    data_sink = pe.Node(nio.DataSink(), name = 'sinker')
    data_sink.inputs.base_directory = sink_dir
    data_sink.inputs.container = '.'

    # Pipeline assembly
    pipeline = pe.Workflow(name = 'pipeline_doit')
    pipeline.base_dir = base_dir

    pipeline.connect(inputspec, 'data_ref', doit_node, 'data_ref')
    pipeline.connect(inputspec, 'thresh', doit_node, 'bin_thresh')
    pipeline.connect(doit_node, 'csv_file', data_sink, '@LST_doit')

    pipeline.write_graph(graph2use = 'orig')
    pipeline.config['Execution'] = {'keep_inputs': True, 'remove_unnecessary_outputs': False}

    return pipeline

"""
if __name__ == '__main__':
    from glob import glob
    data_ref = glob("/data/henry1/tristan/LST/FLAIR-MPRAGE/*/*_bin_lesion_map.nii")
    FLAIR_T1_name = data_ref[0].split('/')[5]
    sk_dir = os.path.join('/data/henry1/tristan/LST/opt_thresh_results', FLAIR_T1_name)
    thresh_array = np.linspace(0.05, 1.00, num=20)
    dwf = doit_workflow(data_ref, thresh_array, sink_dir=sk_dir)

    dwf.run()
"""
