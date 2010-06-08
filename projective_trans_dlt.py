#!/usr/bin/env python
# (C) Copyright 2010 Brandyn A. White
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Example of computing a Projective Transformation using DLT
See Multiview Geometry p. 89-90
"""
__author__ = 'Brandyn A. White <bwhite@cs.umd.edu>'
__license__ = 'GPL V3'

import numpy as np

# Input Points
ps0 = np.array([(0., 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)])
ps1 = np.array([(1., 0, 1), (1, 1, 1), (0, 1, 1), (0, 0, 1)])

# Compute a matrix
a = []
for p0, p1 in zip(ps0, ps1):
    a.append(np.concatenate((np.zeros(3), -p0, p1[1] * p0)))
    a.append(np.concatenate((p0, np.zeros(3), -p1[0] * p0)))

# Find right null space vector and normalize
h = np.linalg.svd(a)[2][-1].reshape((3, 3))
h = h / h[2][2]

# Done
print(h)
