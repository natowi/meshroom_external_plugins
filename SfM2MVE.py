__version__ = "1.1"

from meshroom.core import desc

class SfM2MVE(desc.CommandLineNode):
    commandLine = 'aliceVision_exportMVE2 {allParams}'

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="SFM input",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output Folder",
            description="Output in MVE format",
            value=desc.Node.internalFolder,
            uid=[0],
            )
        ]
