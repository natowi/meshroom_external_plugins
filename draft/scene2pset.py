# scene2pset [ OPTS ] SCENE_DIR MESH_OUT
# Available options:
# -d, --depthmap=ARG       Name of depth map to use [depth-L0]
# -i, --image=ARG          Name of color image to use [undistorted]
# -n, --with-normals       Write points with normals (PLY only)
# -s, --with-scale         Write points with scale values (PLY only)
# -c, --with-conf          Write points with confidence (PLY only)
# -m, --mask=ARG           Name of mask/silhouette image to clip 3D points []
# -v, --views=ARG          View IDs to use for reconstruction [all]
# -b, --bounding-box=ARG   Six comma separated values used as AABB.
# -f, --min-fraction=ARG   Minimum fraction of valid depth values [0.0]
# -p, --poisson-normals    Scale normals according to confidence
# -S, --scale-factor=ARG   Factor for computing scale values [2.5]
# -F, --fssr=ARG           FSSR output, sets -nsc and -di with scale ARG
  
__version__ = "1.0"

from meshroom.core import desc

class scene2pset(desc.CommandLineNode):
    commandLine = '"./mve/scene2pset" {inputValue}'
	
#    category = 'MVE'
    documentation = '''
Generates a pointset from the scene by projecting reconstructed depth
values in the world coordinate system.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="Input",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output",
            description="Output",
            value="",
            uid=[0],
            )
        ]