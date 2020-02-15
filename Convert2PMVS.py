# MR Sfm node -> convert2PMVS  (draft, WIP)

__version__ = "1.1"

from meshroom.core import desc

class Convert2PMVS(desc.CommandLineNode):
    commandLine = 'aliceVision_exportPMVS {allParams}'

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
            description="Output in PMVS format",
            value=desc.Node.internalFolder,
            uid=[0],
            )
        ]
