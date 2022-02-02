# prebundle [ MODES ] PREBUNDLE_FILE
# Available options:
# -g, --graph-mode=ARG   Graph mode: Output matching graph file for DOT
  
__version__ = "1.0"

from meshroom.core import desc

class prebundle(desc.CommandLineNode):
    commandLine = '"./mve/prebundle" {inputValue}'
	
#    category = 'MVE'
    documentation = '''
Statistics generator for prebundle files. The graph mode outputs the
matching graph in Graphviz DOT format.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input mesh",
                description="Prebundle file",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output",
            description="Graphviz DOT Output",
            value="",
            uid=[0],
            )
        ]