# meshclean [ OPTS ] IN_MESH OUT_MESH
# -t, --threshold=ARG      Threshold on the geometry confidence [1.0]
# -p, --percentile=ARG     Use the nth percentile (0 - 100) as confidence threshold [disabled]
# -c, --component-size=ARG  Minimum number of vertices per component [1000]
# -n, --no-clean           Prevents cleanup of degenerated faces
# --delete-scale           Delete scale attribute from mesh
# --delete-conf            Delete confidence attribute from mesh
# --delete-color           Delete color attribute from mesh

__version__ = "1.0"

from meshroom.core import desc

class meshclean(desc.CommandLineNode):
    commandLine = '"./mve/meshclean" {inputValue} {outputValue}'
	
#    category = 'MVE'
    documentation = '''
The application cleans degenerated faces resulting from MC-like algorithms.
Vertices below a confidence threshold and vertices in small isolated
components are deleted as well.
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