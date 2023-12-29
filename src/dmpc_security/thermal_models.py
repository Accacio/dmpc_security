# [[file:../../docs/dmpc_security/thermal_models.org::+begin_src python][No heading:1]]
#!/usr/bin/env python3

import numpy as np
from scipy import signal

def simulate_system(model,state,input):
    return signal.dlsim(model,input,x0=state)
# No heading:1 ends here

# [[file:../../docs/dmpc_security/thermal_models.org::*Model][Model:1]]
# TODO(accacio): Make model using dimensions/materials
# TODO(accacio): Change resistance names
# TODO(accacio): Verify models
# Model:1 ends here

# [[file:../../docs/dmpc_security/thermal_models.org::*disturbances][disturbances:1]]
def monozone_3R2C_with_external_disturbance(Roaia,Riwia,Rowoa,Cwalls,Cair):
    """Monozone model using 3 resistances and 2 capacitances, sun as external disturbance added as an input

    State is the temperature of the air inside the room and on internal walls.
        """

    A = np.array([[-1/(Cwalls*Roaia)-1/(Cwalls*Riwia), 1/(Cwalls*Riwia)],
                  [ 1/(Cair*Riwia), -1/(Cair*Rowoa)-1/(Cair*Riwia)]])
    B = np.array([[1/Cwalls, 1/(Cwalls*Roaia)],[0, 1/(Cair*Rowoa)]])
    C = np.array([1, 0])
    D = np.array([[0,0]])
    sys=signal.StateSpace(A,B,C,D)
    return sys
# disturbances:1 ends here

# [[file:../../docs/dmpc_security/thermal_models.org::*disturbances][disturbances:2]]
def monozone_3R2C(Roaia,Riwia,Rowoa,Cwalls,Cair):
    """Monozone model using 3 resistances and 2 capacitances, no external disturbances

    State is the temperature of the air inside the room and on internal walls.
    """
    A = np.array([[-1/(Cwalls*Roaia)-1/(Cwalls*Riwia), 1/(Cwalls*Riwia)],
                  [ 1/(Cair*Riwia), -1/(Cair*Rowoa)-1/(Cair*Riwia)]])
    B = np.array([[1/Cwalls],[0]])
    C = np.array([1, 0])
    D = np.array([0])
    sys=signal.StateSpace(A,B,C,D)
    return sys
# disturbances:2 ends here
