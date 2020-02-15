# MVE_DepthMap2PointCloud (scene2pset) [draft, WIP]
# scene2pset [ OPTS ] SCENE_DIR MESH_OUT
#
# Available options:
# -d, --depthmap=ARG Name of depth map to use [depth-L0]
# -i, --image=ARG Name of color image to use [undistorted]
# -n, --with-normals Write points with normals (PLY only)
# -s, --with-scale Write points with scale values (PLY only)
# -c, --with-conf Write points with confidence (PLY only)
# -m, --mask=ARG Name of mask/silhouette image to clip 3D points []
# -v, --views=ARG View IDs to use for reconstruction [all]
# -b, --bounding-box=ARG Six comma separated values used as AABB.
# -f, --min-fraction=ARG Minimum fraction of valid depth values [0.0]
# -p, --poisson-normals Scale normals according to confidence
# -S, --scale-factor=ARG Factor for computing scale values [2.5]
# -F, --fssr=ARG FSSR output, sets -nsc and -di with scale ARG

__version__ = "1.1"

from meshroom.core import desc

class MVEDepthMap2PointCloud(desc.CommandLineNode):
    commandLine = 'scene2pset {inputValue} {outputValue}'

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="MVE_DepthMap folder",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output Folder",
            description="Output",
            value="",
            uid=[0],
            )
        ]
