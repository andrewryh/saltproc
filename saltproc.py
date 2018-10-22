class Simulation():
    """ Class setups parameters for simulation, runs SERPENT, parse output and create input. 
    """

    def __init__(self, cores, nodes, bw, sss_exec_path, restart, timestep, t_0, t_final, input_filename, sss_template_filename, sss_input_filename, sss_output_filename, db_filename, npop, active_cycles, inactive_cycles, connection_graph):
        """ Initializes the class

        Parameters:
        -----------
        cores: int
            number of cores to use for SERPENT run
        nodes: int
            number of nodes to use for SERPENT run
        bw: string
            # !! if 'True', runs saltproc on Blue Waters
        sss_exec_path: string
            path to SERPENT executable
        restart: bool
            if 'True', restarts simulation using existing HDF5  database
        timestep: int
            Duration of each depletion simulation
        t_0: int
            Beggining of simulation moment in time (0 for new run, >0 when restarting)
        t_final: int
            Duration of whole Saltproc simulation
        input_filename: string
            Name of JSON input file with reprocessing scheme and parameters for Saltproc simulation
        sss_template_filename: string
            Name of user SERPENT input file with geometry and initial composition
        sss_input_filename: string
            Name of SERPENT input file
        sss_output_filename: string
            Name of SERPENT output file
        db_file: string
            Name of HDF5 database
        npop: int
            Size of neutron population for SERPENT run
        active_cycles: int
            Number of active cycles for SERPENT run
        inactive_cycles: int
            Number of inactive cycles for SERPENT run
        connection_graph: dict
            key: ???
            value: ???
        """

        def runsim(self):

        def steptime(self):

        def loadinput_sp(self):

        def loadinput_sss(self):

        def outputhandle(self):

        def write_input(self):

        def init_db(self):

        def reopen_db(self):

        def write_db(self):
