# This application reads a bundle file and outputs a PLY file with a colored point cloud.
# Available options: -s, --spheres=ARG     Generates a sphere for every point (radius ARG) [0.0]

__version__ = "1.0"

from meshroom.core import desc

class bundle2pset(desc.CommandLineNode):
    commandLine = '"./mve/bundle2pset" {inputValue} {outputValue}'
	
#    category = 'MVE'
    documentation = '''
This node reads a bundle file and outputs a PLY file with a colored point cloud.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="Input Bundle",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output Folder",
            description="Output PLY",
            value=desc.Node.internalFolder,
            uid=[0],
            )
        ]