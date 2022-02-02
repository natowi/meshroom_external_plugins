# Generic options:
#   -h [ --help ]                         produce this help message
#   -w [ --working-folder ] arg           working directory (default current directory)
# -c [ --config-file ] arg (=TextureMesh.cfg)
#                                         file name containing program options
#   --export-type arg (=ply)              file type used to export the 3D scene (ply or obj)
#   --archive-type arg (=2)               project archive type: 0-text, 1-binary, 2-compressed binary
#   --process-priority arg (=-1)          process priority (below normal by 
#                                         default)
#   --max-threads arg (=0)                maximum number of threads (0 for using 
#                                         all available cores)
#   -v [ --verbosity ] arg (=2)           verbosity level
# 
# Texture options:
#   -i [ --input-file ] arg               input filename containing camera poses and image list
#   -o [ --output-file ] arg              output filename for storing the mesh
#   --decimate arg (=1)                   decimation factor in range [0..1] to be applied to the input surface before refinement (0 - auto, 1 - disabled)
#   --close-holes arg (=30)               try to close small holes in the input surface (0 - disabled)
#   --resolution-level arg (=0)           how many times to scale down the images before mesh refinement
#   --min-resolution arg (=640)           do not scale images lower than this resolution
#   --outlier-threshold arg (=0.0599999987)
#                                         threshold used to find and remove outlier face textures (0 - disabled)
#   --cost-smoothness-ratio arg (=0.100000001)
#                                         ratio used to adjust the preference for more compact patches (1 - best 
#                                         quality/worst compactness, ~0 - worst quality/best compactness)
#   --global-seam-leveling arg (=1)       generate uniform texture patches using 
#                                         global seam leveling
#   --local-seam-leveling arg (=1)        generate uniform texture patch borders 
#                                         using local seam leveling
#   --texture-size-multiple arg (=0)      texture size should be a multiple of 
#                                         this value (0 - power of two)
#   --patch-packing-heuristic arg (=3)    specify the heuristic used when 
#                                         deciding where to place a new patch (0 
#                                         - best fit, 3 - good speed, 100 - best 
#                                         speed)
#   --empty-color arg (=16744231)         color used for faces not covered by any
#                                         image
#   --orthographic-image-resolution arg (=0)
#                                         orthographic image resolution to be generated from the textured mesh - the 
#                                         mesh is expected to be already geo-referenced or at least properly oriented (0 - disabled)

__version__ = "1.0"

from meshroom.core import desc

class TextureMesh(desc.CommandLineNode):
    commandLine = '"./OpenMVS/TextureMesh" {scenedirValue}'
	
#    category = 'MVS'
    documentation = '''
In the case of having a perfect mesh reconstruction and ground-truth camera poses, obtaining the texture is relatively a strait-forward step. In reality however both the mesh and the camera poses contain slight variations/errors at best, and hence the mesh texturing module should be able to cope with them. A very good paper describing such an algorithm, implemented in OpenMVS, is: Let There Be Color! - Large-Scale Texturing of 3D Reconstructions M. Waechter et al. 2014.
## Online
[https://github.com/cdcseacave/openMVS](https://github.com/cdcseacave/openMVS)
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