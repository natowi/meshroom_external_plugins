# MVE_DepthMap (dmrecon) [draft, WIP]
# MVE DepthMap reconstruction, does not require cuda
# Slower than MR DephMap and might not work with too few images
# convert2mve --> MVE_DepthMap
# 
# TODO: copy inputValue to outputValue and use only the outputValue in cli (so we do not write into the convert2mve node folder)

__version__ = "1.1"

from meshroom.core import desc

class MVE_DepthMap(desc.CommandLineNode):
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
