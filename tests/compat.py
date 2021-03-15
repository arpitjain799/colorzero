# vim: set et sw=4 sts=4 fileencoding=utf-8:
#
# The colorzero color library
#
# Copyright (c) 2018 Dave Jones <dave@waveform.org.uk>
#
# SPDX-License-Identifier: BSD-3-Clause

import cmath

# Back-ported from python 3.5; see
# github.com/PythonCHB/close_pep/blob/master/is_close.py for original
# implementation
def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
    if rel_tol < 0.0 or abs_tol < 0.0:
        raise ValueError('error tolerances must be non-negative')
    if a == b: # fast-path for exact equality
        return True
    if cmath.isinf(a) or cmath.isinf(b):
        return False
    diff = abs(b - a)
    return (
        (diff <= abs(rel_tol * b)) or
        (diff <= abs(rel_tol * a)) or
        (diff <= abs_tol)
        )
