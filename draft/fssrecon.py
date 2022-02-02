# fssrecon [ OPTS ] IN_PLY [ IN_PLY ... ] OUT_PLY
# -s, --scale-factor=ARG   Multiply sample scale with factor [1.0]
# -r, --refine-octree=ARG  Refines octree with N levels [0]
# --min-scale=ARG          Minimum scale, smaller samples are clamped
# --max-scale=ARG          Maximum scale, larger samples are ignored
# --interpolation=ARG      Interpolation: linear, scaling, lsderiv, [cubic]
  
__version__ = "1.0"

from meshroom.core import desc

class fssrecon(desc.CommandLineNode):
    commandLine = '"./mve/fssrecon" {inputValue} {outputValue}'
	
#    category = 'MVE'
    documentation = '''
To reconstruct a final surface from the dense point could, the fssrecon tool can be used. 
You might also want to consider using Poisson Surface Reconstruction for reconstruction,
which often creates more complete and smoother geometry,
but doesn't work as well with varying surface detail and doesn't produce colored output.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input PLY",
                description="Input sparse pointcloud (PLY)",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output PLY",
            description="Input dense pointcloud (PLY)",
            value=desc.Node.internalFolder + 'densepointcloud.ply',
            uid=[0],
            )
        ]