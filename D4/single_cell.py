from bmtk.builder import NetworkBuilder
from bmtk.utils.sim_setup import build_env_bionet

net = NetworkBuilder("biophysical")

# This works with PNs
net.add_nodes(N=1, pop_name='PyrA',
        mem_potential='e',
        model_type='biophysical',
        model_template='hoc:SOM_Cell',
        morphology=None)

#net.add_nodes(N=1, pop_name='SOM',
#        mem_potential='e',
#        model_type='biophysical',
#        model_template='hoc:SOM_Cell',
#        morphology=None)

net.build()
net.save_nodes(output_dir='network')

build_env_bionet(
    base_dir='./',       # Where to save the scripts and config files
    config_file='config.json', # Where main config will be saved.
    network_dir='./network',
    components_dir='biophys_components',
    tstop=400.0, dt=0.1,      # Run a simulation for 2000 ms at 0.1 ms intervals
    report_vars=['v'],  # Tells simulator we want to record membrane potential and calcium traces
    current_clamp={            # Creates a step current from 500.ms to 1500.0 ms
        'amp': 0.400,
        'delay': 100.0,
        'duration': 200.0
    },
    compile_mechanisms=False   # Will try to compile NEURON mechanisms
)

