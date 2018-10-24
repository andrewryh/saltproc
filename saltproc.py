class Simulation():
    """ Class setups parameters for simulation, runs SERPENT, parse output and create input. 
    """

    def __init__(self, sim_name, cores, nodes, bw, sss_exec_path, restart, timestep, t_0, t_final, input_filename, db_filename, connection_graph):
        """ Initializes the class

        Parameters:
        -----------
        sim_name: string
            name of simulation may contain number of reference case, paper name or other specific information to identify simulation
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
            duration of each depletion simulation
        t_0: int
            beggining of simulation moment in time (0 for new run, >0 when restarting)
        t_final: int
            duration of whole Saltproc simulation
        input_filename: string
            name of JSON input file with reprocessing scheme and parameters for Saltproc simulation
        db_file: string
            name of HDF5 database
        connection_graph: dict
            key: ???
            value: ???
        """

    def runsim(self):

    def steptime(self):

    def loadinput_sp(self):

    def init_db(self):

    def reopen_db(self):

    def write_db(self):

class Materialflow ():
    """ Class contains information about material flow and methods how insert and extract elements to|from the flow.
    """

    def __init__(self, mat_name, n_iso, mass, rho, mass_flowrate, vol_flowrate):
        """ Initializes the class

        Parameters:
        -----------
        mat_name: string
            name of material from SERPENT input file
        n_iso: int
            number of isotopes in the material flow
        mass: 1D ndarray of size n_iso
            mass of isotopes in the material flow (g)
        rho: float
            density of the material flow (g/cm**3)
        mass_flowrate: float 
            mass flow rate of the material flow (g/s)
        vol_flowrate: float
            volumetric flow rate of the material flow through reactor  (cm**3/s)
        """

    def conservationchecker(self):

    def insert(self):

    def extrac(self):

class Reactor ():
    """ Class contains information about current state of the reactor and initiate the reactor depletion. """

    def __init__(self, name, volume, mass_flowrate, power_level, fp_powdens, composition, mthm, sss_template_filename, sss_input_filename, sss_output_filename, npop, active_cycles, inactive_cycles):
        """ Initializes the class

        Parameters:
        -----------
        name: string
            name of the reactor design
        volume: float
            total volume of reactor core
        mass_flowrate: float
            total mass flowrate through reactor
        power_level: array [Tx1]
            normalized power level in percents (%) for each depletion step
        fp_powdens: float
            full power density (kW/g) in depletion simulation (SERPENT)
        composition: array [iso x T x number of depleted materials]
            mass of each isotope for the end of each timestep for every fluid (g)
        mthm: array [Tx1]
            metric tons of heavy metals for the end of each time step (MTHM)
        sss_template_filename: string
            name of user SERPENT input file with geometry and initial composition
        sss_input_filename: string
            name of SERPENT input file
        sss_output_filename: string
            name of SERPENT output file
        npop: int
            size of neutron population for SERPENT run
        active_cycles: int
            number of active cycles for SERPENT run
        inactive_cycles: int
            number of inactive cycles for SERPENT run
        """

    def run_serpent(self):

    def load_input(self):

    def outputhandle(self):

    def write_input(self):
