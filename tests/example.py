#!/usr/bin/python

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'malla'))
import directed_edge as de
import off
from dataclasses import dataclass

@dataclass
class Vertex:
    x: float
    y: float
    z: float

v, f = off.read('cubo.off')
m = de.mesh([Vertex(*P) for P in v], f)
for i in range(m.number_of_vertices()):
    s = f'Vertex {i}:'
    for p in m.vertex_halfedges(i):
        s += f' {p}'
    print(s)

# off.write('cubo-out.off', m)
