# ImageMasking node plugin for Meshroom
# 
# Pre-compiled binaries for imagemagick can be downloaded from https://imagemagick.org/script/download.php
# ImageMagick on github https://github.com/ImageMagick/ImageMagick
# ImageMagick license https://github.com/ImageMagick/ImageMagick/blob/master/LICENSE
#
# Meshroom plugin by natowi (https://github.com/natowi) 11.2019
# Meshroom plugin license: Mozilla Public License Version 2.0
# Plugin folder: meshroom\nodes\aliceVision
# Requires mogrify.exe in aliceVision\bin
# Requires uncompiled Meshroom and pre-compiled AliceVision
#
#
# Node for ImageMasking to use with the DepthMapMask node

__version__ = "3.0"

from meshroom.core import desc

# name of the node in Meshroom + call CL with parameters

class ImageMasking(desc.CommandLineNode):
    commandLine = 'mogrify -format png -path {outputValue} -type Grayscale -negate -fill black -fuzz {fuzzValue}% +opaque "#ffffff" -blur {radiusValue}x{sigmaValue} -type Bilevel -depth 1 {inputValue}/*jpg'

# Default node parameters demo:
# mogrify -format png -path "path/to/output/dir" -type Grayscale -negate -fill black -fuzz 9% +opaque "#ffffff" -blur 0x6 -type Bilevel -depth 1 "path/to/input/dir"/*.jpg

    cpu = desc.Level.NORMAL
    ram = desc.Level.NORMAL

#define node inputs, use PrepareDenseScene node to convert the input images to jpg

    inputs = [
        desc.File(
            name="input",
            label='Input Image Folder',
            description='',
            value='',
            uid=[0],
            ),
    
    
# wip black/white/green/* background, background pattern
	
		desc.IntParam(
			name='fuzz',
			label='fuzz',
			description='',
			value=60,
			range=(0, 100, 1),
			uid=[0],
			),

# Documentation: http://www.imagemagick.org/Usage/blur/
	
		desc.IntParam(
			name='radius',
			label='Blur radius',
			description='larger value=larger blur radius, 0=auto value (default)',
			value=0,
			range=(0, 100, 1),
			uid=[0],
			),
	
		desc.FloatParam(
			name='sigma',
			label='Blur Sigma',
			description='blur intensity',
			value=6,
			range=(0.0, 100.0, 0.01),
			uid=[0],
			),
	
	]

# define node outputs
    outputs = [
        desc.File(
            name="output",
            label="Output Masks",
            description="Output Masks folder (monochrome PNG)",
            value=desc.Node.internalFolder,
            uid=[],
            ),
    ]
