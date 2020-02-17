from saltproc import Materialflow
from saltproc import Process
import numpy as np


class Separator(Process):
    """Class describes salt processing system `separator`. It inherits from the
    process class and has attributes and methods intrinsics to separator,
     """

    def __init__(self,
                 mass_flowrate=0.0,
                 capacity=0.0,
                 volume=0.0,
                 efficiency={'Xe135': 1.0},
                 interf_area=0.0,
                 ):
        super().__init__(self,
                         mass_flowrate,
                         capacity,
                         volume,
                         efficiency)
        """ Initializes the Process object.

        Parameters
        ----------
        mass_flowrate : float
            mass flow rate of the material flow (g/s)
        capacity : float
            maximum mass flow rate of the material flow which current process
            can handle (g/s)
        volume : float
            total volume of the current facility (:math:`cm^3`)
        efficiency : dict

            ``key``
                element name for removal (not isotope)
            ``value``
                removal efficency for the isotope (weight fraction)
        """
        # initialize all object attributes
        self.a = interf_area

    def rem_elements(self, inflow):
        """Updates Materialflow object `inflow` after removal target isotopes
        with specific efficiency in single component of fuel reprocessing
        system and returns waste stream Materialflow object.

        Parameters
        ----------
        inflow : Materialflow obj
            Target material stream to remove poisons from.

        Returns
        -------
        Materialflow object
            Waste stream from the reprocessing system component.

        """
        # To match with variable name in the JSON file
        capacity = self.capacity
        waste_nucvec = {}
        out_nucvec = {}
        print("Xe concentration in inflow before % f g" % inflow['Xe134'])
        print("Xe concentration in inflow before % f g" % inflow['Xe135'])
        print("Xe concentration in inflow before % f g" % inflow['Xe136'])
        for iso in inflow.comp.keys():
            el_name = pyname.serpent(iso).split('-')[0]
            if el_name in self.efficiency:
                print("Efficiency string", self.efficiency[el_name], type(self.efficiency[el_name]))
                out_nucvec[iso] = \
                    float(inflow.comp[iso]) * \
                    float(1.0 - eval(self.efficiency[el_name]))
                waste_nucvec[iso] = \
                    float(inflow[iso]) * float(eval(self.efficiency[el_name]))
            else:
                out_nucvec[iso] = float(inflow.comp[iso])
                waste_nucvec[iso] = 0.0  # zeroes everywhere else
        waste = Materialflow(waste_nucvec)
        inflow.mass = float(inflow.mass - waste.mass)
        inflow.comp = out_nucvec
        inflow.norm_comp()
        print("Xe concentration in inflow after %f g" % inflow['Xe134'])
        print("Xe concentration in inflow after %f g" % inflow['Xe135'])
        print("Xe concentration in inflow after %f g" % inflow['Xe136'])
        print("Waste mass %f g\n" % waste.mass)
        del out_nucvec, waste_nucvec, el_name
        return waste

    def check_mass_conservation(self):
        """Checking that Process.outflow + Process.waste_stream is equal
        Process.inflow and the total mass is being conserved. Returns `True` if
        the mass conserved or `False` if its mismatched.
        """
        out_stream = self.outflow + self.waste_stream
        np.testing.assert_array_equal(out_stream, self.inflow)
