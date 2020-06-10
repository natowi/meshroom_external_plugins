# ManifoldPlus is distributed for free for non-commercial use only an is © 2020 Jingwei Huang. All Rights Reserved https://github.com/hjwdzh/ManifoldPlus
# Binaries can be downloaded from here https://github.com/natowi/ManifoldPlus/releases (rename manifoldplus64.exe to manifoldplus.exe)
# The ManifoldPlus.py node for Meshroom is licensed under MPL2 by natowi


__version__ = "1.1"

from meshroom.core import desc

class ManifoldPlus(desc.CommandLineNode):
    commandLine = 'manifoldplus --input {inputValue} --output {outputValue} --depth {depthValue}'

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="obj input",
                value="",
                uid=[0],
                ),
        desc.IntParam(
            name='depth',
            label='depth',
            description='''depth value''',
            value=8,
            range=(0, 20, 1),
            uid=[0],
            advanced=True,
        ),
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output",
            description="Output",
            value=desc.Node.internalFolder + 'manifold-output.obj',
            uid=[0],
            )
        ]
