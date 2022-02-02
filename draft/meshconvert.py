# meshconvert [ OPTS ] IN_MESH OUT_MESH
# Available options:
# -n, --normals            Compute vertex normals
  
__version__ = "1.0"

from meshroom.core import desc

class meshconvert(desc.CommandLineNode):
    commandLine = '"./mve/meshconvert" {inputValue} {outputValue}'
	
#    category = 'MVE'
    documentation = '''
Converts the mesh given by IN_MESH to the output file OUT_MESH.
The format of the input and output mesh are detected by extension.
Supported file formats are .off, .ply (Stanford), .npts or .bnpts
(Poisson Surface Reconstruction) and .pbrt.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input mesh",
                description="Alignment file",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output",
            description="Output Mesh",
            value=desc.Node.internalFolder,
            uid=[0],
            )
        ]