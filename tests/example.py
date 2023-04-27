#!/usr/bin/python

from malla import directed_edge as de
from malla import off
from dataclasses import dataclass

@dataclass
class Vertex:
    x: float
    y: float
    z: float

    def __str__(self):
        return f'{x} {y} {z}'

v, f = off.read('/home/dimas/programs-python/mesh/cubo.off')
m = de.mesh([Vertex(*P) for P in v], f)

off.write('cubo.off', m.vertex_strings(), m.face_strings())
