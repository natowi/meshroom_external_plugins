# Simplify node plugin for Meshroom
# 
# Simplify (Fast-Quadric-Mesh-Simplification)
# Pre-compiled binaries of Simplify can be downloaded from https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification
#
# Meshroom plugin by natowi (https://github.com/natowi) 11.2019
# Meshroom plugin license: Mozilla Public License Version 2.0
# Plugin folder: meshroom\nodes\aliceVision
# Requires simplify (named alicevision_simplify) in aliceVision\bin
# Requires uncompiled Meshroom and pre-compiled alicevision

__version__ = "3.0"

from meshroom.core import desc


class Meshsimplify(desc.CommandLineNode):
    commandLine = 'alicevision_simplify {inputValue} {outputValue} {ratioValue} {agressValue}'

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
        desc.FloatParam(
            name='ratio',
            label='Ratio for Decimation',
            description='A ratio of 0.2 will decimate 80% of triangles',
            value=0.5,
            range=(0.0, 1.0, 0.01),
            uid=[0],
        ),
		desc.FloatParam(
            name='agress',
            label='Agressiveness',
            description='faster or better decimation, more iterations yield higher quality',
            value=7.0,
            range=(0.0, 100.0, 0.1),
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output mesh",
            description="Output mesh (OBJ file format).",
            value=desc.Node.internalFolder + 'mesh.obj',
            uid=[],
            ),
    ]
