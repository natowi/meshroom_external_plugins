# ImageMasking node plugin for Meshroom
# 
# Pre-compiled binaries for .... can be downloaded from ....
# ...., created by  ....
#
# Meshroom plugin by natowi (https://github.com/natowi) 11.2019
# Meshroom plugin license: Mozilla Public License Version 2.0
# Plugin folder: meshroom\nodes\aliceVision
# Requires .... in aliceVision\bin
# Requires uncompiled Meshroom and pre-compiled alicevision
#
# Note: not all options are implemented yet

# This node will create image masks for the DepthMapMask node (also wip)

__version__ = "3.0"

from meshroom.core import desc


class ImageMasking(desc.CommandLineNode):
    commandLine = 'alicevision_......'

    cpu = desc.Level.NORMAL
    ram = desc.Level.NORMAL

    inputs = [
        desc.File(
            name="input",
            label='Input Image Folder',
            description='',
            value='',
            uid=[0],
            ),

    outputs = [
        desc.File(
            name="output",
            label="Output Masks",
            description="Output Masks folder (monochrome PNG)",
            value=desc.Node.internalFolder + 'img.png', #note: image name = input
            uid=[],
            ),
    ]
