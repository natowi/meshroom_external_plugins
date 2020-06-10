# Manifold is distributed for free for non-commercial use only an is © 2020 Jingwei Huang. All Rights Reserved
# Binaries can be downloaded from here https://github.com/natowi/ManifoldPlus/releases
# The ManifoldPlus.py node for Meshroom is licensed under MPL2 by natowi


__version__ = "1.1"

from meshroom.core import desc

class ManifoldPlus(desc.CommandLineNode):
    commandLine = 'manifold --input {inputValue} --output {outputValue} --depth {depthValue}'

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
            value="",
            uid=[0],
            )
        ]
