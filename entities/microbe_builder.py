import constants
from entities.bacteriophages.b_basic import B_Basic
from entities.macrophages.m_basic import M_Basic
from entities.bacteriophages.b_tank import B_Tank


def build_microbe(unit_id):
    if unit_id == constants.M_BASIC:
        return M_Basic()
    elif unit_id == constants.B_BASIC:
        return B_Basic()
    elif unit_id == constants.B_TANK:
        return B_Tank()
    else:
        raise ValueError("Invalid Unit ID passed to factory build_microbe()")