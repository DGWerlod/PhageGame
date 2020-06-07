import constants
from entities.microbes.bacteriophages.b_basic import B_Basic
from entities.microbes.macrophages.m_basic import M_Basic
from entities.microbes.bacteriophages.b_tank import B_Tank
from entities.microbes.macrophages.m_beach import M_Beach
from entities.microbes.bacteriophages.b_pult import B_Pult


def build_microbe(name):
    if name == constants.M_BASIC:
        return M_Basic()
    elif name == constants.B_BASIC:
        return B_Basic()
    elif name == constants.B_TANK:
        return B_Tank()
    elif name == constants.M_BEACH:
        return M_Beach()
    elif name == constants.B_PULT:
        return B_Pult()
    else:
        raise ValueError("Invalid Unit ID passed to factory build_microbe()")
