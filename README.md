Simple Directed Edge Python implementation for triangle meshes

Example:

```
# import modules
from malla import directed_edge as de
from malla import off
from dataclasses import dataclass

# create a class for vertex data
@dataclass
class Vertex:
    x: float
    y: float
    z: float

# read mesh from off file
v, f = off.read('model.off')

# create a mesh
m = de.mesh([Vertex(*P) for P in v], f)

# write mesh to off file
off.write('output-model.off', m)
```
