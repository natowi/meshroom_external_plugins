# makescene [ OPTIONS ] INPUT OUT_SCENE**
# Available options:
#   -o, --original        Import original images
# -b, --bundle-id=ARG   Bundle ID (Photosynther and Bundler only) [0]
# -k, --keep-invalid    Keeps images with invalid cameras
# -i, --images-only     Imports images from INPUT_DIR only
# -a, --append-images   Appends images to an existing scene
# -m, --max-pixels=ARG  Limit image size by iterative half-sizing
  
__version__ = "1.0"

from meshroom.core import desc

class makescene(desc.CommandLineNode):
    commandLine = '"./mve/makescene" -i {inputValue} {outputValue}'
	
#    category = 'MVE'
    documentation = '''
This node creates MVE scenes by importing from an external SfM software.
Supported are Noah's Bundler, Photosynther and VisualSfM's compact .nvm
file.

For VisualSfM, makescene expects the .nvm file as INPUT. With VisualSfM, it
is not possible to keep invalid views.

For Noah's Bundler, makescene expects the bundle directory as INPUT, a file
"list.txt" in INPUT and the bundle file in the "bundle" directory.

For Photosynther, makescene expects as INPUT the directory that contains
the "bundle" and the "undistorted" directory. With Photosynther, it is not
possible to keep invalid views or import original images.

With the "images-only" option, all images in the INPUT directory are
imported without camera information. If "append-images" is specified,
images are added to an existing scene.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="Input Scene/Folder",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output",
            description="Output scene",
            value=desc.Node.internalFolder,
            uid=[0],
            )
        ]