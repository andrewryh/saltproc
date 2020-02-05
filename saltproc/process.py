from saltproc import Materialflow
from pyne import nucname as pyname
import numpy as np


class Process():
    """Class describes process which must be applied to Materialflow to change
     burnable material composition.
     """

    def __init__(self,
                 mass_flowrate=0.0,
                 capacity=0.0,
                 volume=0.0,
                 efficiency=1.0,
                 ):
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
        self.mass_flowrate = mass_flowrate
        self.capacity = capacity
        self.volume = volume
        self.efficiency = efficiency

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

        waste_nucvec = {}
        out_nucvec = {}
        print("Xe concentration in inflow before % f g" % inflow['Xe136'])
        for iso in inflow.comp.keys():
            el_name = pyname.serpent(iso).split('-')[0]
            if el_name in self.efficiency:
                out_nucvec[iso] = \
                    float(inflow.comp[iso]) * \
                    float(1.0 - self.efficiency[el_name])
                waste_nucvec[iso] = \
                    float(inflow[iso]) * float(self.efficiency[el_name])
            else:
                out_nucvec[iso] = float(inflow.comp[iso])
                waste_nucvec[iso] = 0.0  # zeroes everywhere else
        waste = Materialflow(waste_nucvec)
        inflow.mass = float(inflow.mass - waste.mass)
        inflow.comp = out_nucvec
        inflow.norm_comp()
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
