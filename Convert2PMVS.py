# MR Sfm node -> convert2PMVS  (draft, WIP)

# Optional parameters:
#   --resolution arg (=1)              Divide image coefficient
#   --nbCore arg (=8)                  Nb core
#   --useVisData arg (=1)              Use visibility information.

# Log parameters:
#   -v [ --verboseLevel ] arg (=info)  verbosity level (fatal,  error, warning, info, debug, trace).

__version__ = "1.1"

from meshroom.core import desc

class Convert2PMVS(desc.CommandLineNode):
    commandLine = 'aliceVision_exportPMVS {allParams}'

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="SFMData input",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output Folder",
            description="Output path for keypoints",
            value=desc.Node.internalFolder,
            uid=[0],
            )
        ]
