# mesh2pset [ OPTS ] IN_MESH OUT_PLY_PSET
#Available options:
# -s, --scale=ARG          Set constant scale for all samples [off]
# -a, --adaptive=ARG       Average distance to neighbors scale factor [1.0]
# -b, --bounding-box=ARG   Six comma separated values used as AABB [off]
# -c, --no-confidences     Do not compute vertex confidences
# -x, --no-scale-values    Do not compute sample scale
# -n, --no-normals         Do not compute sample normals
  
__version__ = "1.0"

from meshroom.core import desc

class mesh2pset(desc.CommandLineNode):
    commandLine = '"./mve/mesh2pset" {inputValue} {outputValue}'
	
#    category = 'MVE'
    documentation = '''
This node creates a PLY point cloud from the input mesh by stripping the
connectivity information. Scale values are computed for each vertex as the
average distance to each neighbor (using the connectivity information).
Confidence values are computed by down-weighting boundary vertices.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input mesh",
                description="Input mesh",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output",
            description="Output scene",
            value=desc.Node.internalFolder,
            uid=[0],
            )
        ]