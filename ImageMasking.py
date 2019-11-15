# Instant Meshes node plugin for Meshroom
# 
# Pre-compiled binaries for Instant Meshes can be downloaded from https://github.com/wjakob/instant-meshes
# Instant Meshes, created by  Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung
#
# Meshroom plugin by natowi (https://github.com/natowi) 11.2019
# Meshroom plugin license: Mozilla Public License Version 2.0
# Plugin folder: meshroom\nodes\aliceVision
# Requires .... in aliceVision\bin
# Requires uncompiled Meshroom and pre-compiled alicevision
#
# Note: not all options are implemented yet

__version__ = "3.0"

from meshroom.core import desc


class InstantMeshes(desc.CommandLineNode):
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
