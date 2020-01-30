# Instant Meshes node plugin for Meshroom
# 
# Pre-compiled binaries for Instant Meshes can be downloaded from https://github.com/wjakob/instant-meshes
# Instant Meshes, created by  Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung
#
# Meshroom plugin by natowi (https://github.com/natowi) 11.2019
# Meshroom plugin license: Mozilla Public License Version 2.0
# Plugin folder: meshroom\nodes\aliceVision
# Requires Instant Meshes (named alicevision_InstantMeshes) in aliceVision\bin
# Requires uncompiled Meshroom and pre-compiled alicevision
#
# Note: not all options are implemented yet

__version__ = "3.0"

from meshroom.core import desc


class InstantMeshes(desc.CommandLineNode):
    commandLine = 'alicevision_InstantMeshes {inputValue} -S {smoothValue} -c {creaseValue} -r {rosyValue} -p {posyValue} --output {outputValue}'

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
        desc.IntParam(
            name='smooth',
            label='Number of smoothing',
            description='Number of smoothing & ray tracing reprojection steps (default: 2)',
            value=2,
            range=(0, 100, 1),
            uid=[0],
            ),
		desc.IntParam(
            name='crease',
            label='Dihedral angle threshold for creases',
            description='Dihedral angle threshold for creases in degrees',
            value=0,
            range=(0, 360, 1),
            uid=[0],
            ),
		desc.IntParam(
            name='rosy',
            label='Orientation symmetry',
            description='Specifies the orientation symmetry type',
            value=2,
            range=(2, 6, 2),
            uid=[0],
            ),
		desc.IntParam(
            name='posy',
            label='Position symmetry',
            description='Specifies the position symmetry type',
            value=4,
            range=(4, 6, 2),
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
