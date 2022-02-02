# meshalign [ OPTS ] ALIGNMENT_FILE [...] OUT_MESH

__version__ = "1.0"

from meshroom.core import desc

class meshalign(desc.CommandLineNode):
    commandLine = '"./mve/meshalign" {inputValue} {outputValue}'
	
#    category = 'MVE'
    documentation = '''
Generates a combined mesh from Stanford or Meshlab alignment data. The
combined mesh contains all triangulated range images in a global,
consistent coordinate system. Stanford alignments are .conf files with
global camera and a list of meshes with alignment information.
Meshlab alignment are .aln files with a list of meshes and a camera to world transformation matrix.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input",
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