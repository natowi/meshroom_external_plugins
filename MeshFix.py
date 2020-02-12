# MeshFix
# https://github.com/MarcoAttene/MeshFix-V2.1

# MeshFix node plugin for Meshroom
# 
# Pre-compiled binaries for MeshFix can be downloaded from https://github.com/MarcoAttene/MeshFix-V2.1
# MeshFix, created by Marco Attene

# Meshroom plugin by natowi (https://github.com/natowi) 11.2019
# Meshroom plugin license: Mozilla Public License Version 2.0
# Plugin folder: meshroom\nodes\aliceVision
# Requires Instant Meshes (named alicevision_InstantMeshes) in aliceVision\bin
# Requires uncompiled Meshroom and pre-compiled alicevision

# Option '-a' = joins multiple open components before starting
# Option '-j' = output files in STL format insted of OFF

__version__ = "3.0"

from meshroom.core import desc


class MeshFix(desc.CommandLineNode):
    commandLine = 'MeshFix {inputValue} {outputValue} -j'

    cpu = desc.Level.NORMAL
    ram = desc.Level.NORMAL

    inputs = [
        desc.File(
            name="input",
            label='Input Mesh (OBJ file format).',
            description='',
            value='',
            uid=[0],
            ),
]

    outputs = [
        desc.File(
            name="output",
            label="Output mesh",
            description="Output mesh (OBJ file format).",
            value=desc.Node.internalFolder + 'mesh_fixed.stl',
            uid=[],
            ),
    ]
