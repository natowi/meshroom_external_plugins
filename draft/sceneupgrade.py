# sceneupgrade [ OPTIONS ] INPUT
# Available options:
# -k, --keep-original   Keep original files
  
__version__ = "1.0"

from meshroom.core import desc

class sceneupgrade(desc.CommandLineNode):
    commandLine = '"./mve/sceneupgrade" {inputValue}'
	
#    category = 'MVE'
    documentation = '''
This utility upgrades an MVE view, a prebundle file, or an MVE scene to the
new format. See the Github wiki for more details about the new formats.
INPUT can either be a single .mve view, a single .sfm prebundle file, or a
scene directory. In the latter case, all views and the prebundle.sfm are upgraded.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="Input",
                value="",
                uid=[0],
		)
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