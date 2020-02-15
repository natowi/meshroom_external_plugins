# MVE_DepthMap (dmrecon) [draft, WIP]
# MVE DepthMap reconstruction, does not require cuda
# Slower than MR DephMap and might not work with too few images
# convert2mve --> MVE_DepthMap
# 
# TODO: copy inputValue to outputValue and use only the outputValue in cli (so we do not write into the convert2mve node folder)
#
# Available options:
# -n, --neighbors=ARG amount of neighbor views (global view selection)
# -m, --master-view=ARG reconstructs given master view ID only
# -l, --list-view=ARG reconstructs given view IDs (given as string "0-10")
# -s, --scale=ARG reconstruction on given scale, 0 is original
# --max-pixels=ARG Limit master image size [1500000]
# -f, --filter-width=ARG patch size for NCC based comparison [5]
# --nocolorscale turn off color scale
# -i, --image=ARG specify source image embedding [undistorted]
# --local-neighbors=ARG amount of neighbors for local view selection [4]
# --keep-dz store dz map into view
# --keep-conf store confidence map into view
# -p, --writeply use this option to write the ply file
# --plydest=ARG path suffix appended to scene dir to write ply files
# --bounding-box=ARG Six comma separated values used as AABB [disabled]
# --progress=ARG progress output style: 'silent', 'simple' or 'fancy'
# --force Reconstruct and overwrite existing depthmaps

__version__ = "1.1"

from meshroom.core import desc

class MVEDepthMap(desc.CommandLineNode):
    commandLine = 'dmrecon {outputValue}'

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="MVE project folder",
                value="",
                uid=[0],
		)
    ]

   # outputs = [
   #     desc.File(
   #         name="output",
   #         label="Output Folder",
   #         description="Output",
   #         value="",
   #         uid=[0],
   #         )
   #     ]
