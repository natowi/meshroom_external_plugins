# Shading aware Multi-View Stereo
# Usage: smvsrecon [ OPTS ] SCENE_DIR
# Available options:
# -a, --alpha=ARG          Regularization parameter, a higher alpha leads to smoother surfaces [1]
# -s, --scale=ARG          Scale of input images [estimated to reduce images to a maximum of ~1.5MP]
# -i, --image=ARG          Image embedding [undistorted]
# -n, --neighbors=ARG      Number of neighbors for recon [6]
# -o, --output-scale=ARG   Scale of output depth [2]
# -l, --list-view=ARG      Reconstructs given viewIDs (given as string "0-10")
# -t, --threads=ARG        Number of threads [Num CPU cores]. Peak memory requirement is ~1GB per thread and 2 megapixel image resolution
# -d, --debug-lvl=ARG      Debug level [0]
# -r, --recon-only         Generate only depth maps and no output ply. [off]
# -M, --max-pixels=ARG     Maximal number of pixels for reconstruction. Images will be rescaled to be below this value. [1700000]
# -S, --shading            Use shading-based optimization. [off]
# -R, --regularize-lighting=ARG  Use additional basic surface regularization when lighting is turned on. This is untested but may improve results for scenes with complex lighting (0 = off, 100 = use full basic regularizer). [0]
# -g, --gamma-srgb         Apply inverse SRGB gamma correction. [off]
# -m, --mesh               Create Triangle mesh instead of simple point cloud (WIP). [off]
# -y, --simplify           Create simplified triangle mesh (WIP). [off]
# -f, --force              Force reconstruction of result embeddings
# --no-cut                 Turn off surface cutting and export fill pointcloud from all depth values. [on]
# --aabb=ARG               Comma separated AABB for output: min,min,min,max,max,max
# --min-neighbors=ARG      Minimal number of neighbors for reconstruction. [3]
# --no-sgm                 Turn off semi-global matching.
# --force-sgm              Force reconstruction of SGM embeddings.
# --sgm-scale=ARG          Scale of reconstruction of SGM embeddings relative to input scale. [1]
# --sgm-range=ARG          Range for SGM depth sweep, given as string "0.1,3.5". [estimated from SfM pointcloud] (this option is untested please report any issues)
# --full-opt               Run full optimization on all nodes (otherwise it only runs on non converged nodes) [off]
# --clean                  Clean scene and remove all result embeddings

__version__ = "1.0"

from meshroom.core import desc

class smvsrecon(desc.CommandLineNode):
    commandLine = '"./mve/smvsrecon" {scenedirValue}'
	
#    category = 'MVE'
    documentation = '''
This node is intended as an alternative multi-view stereo step and replaces dmrecon and scene2pset
(smvsrecon needs to be placed within the mve folder)
## Online
[https://github.com/flanggut/smvs](https://github.com/flanggut/smvs)
'''

    inputs = [
        desc.File(
                name="scenedir",
                label="Scene directory",
                description="Scene directory",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output Folder",
            description="Output PLY",
            value="",
            uid=[0],
            )
        ]