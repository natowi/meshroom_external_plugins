Place the precompiled .pyc in this folder:
Meshroom\lib\meshroom\nodes\aliceVision

# ImageMasking node plugin for Meshroom
 
- Pre-compiled binaries for imagemagick can be downloaded from https://imagemagick.org/script/download.php
- ImageMagick on github https://github.com/ImageMagick/ImageMagick
- ImageMagick license https://github.com/ImageMagick/ImageMagick/blob/master/LICENSE

- Meshroom plugin by natowi (https://github.com/natowi) 11.2019
- Meshroom plugin license: Mozilla Public License Version 2.0
- Plugin folder (pyc): Meshroom\lib\meshroom\nodes\aliceVision
- Requires mogrify.exe in aliceVision\bin

How to use this plugin:

PrepareDenseScene2 (jpg)->ImageMasking->MaskFolder of DepthMaskFilter

Note: at the moment ImageMasking can only create masks for images with white background (as it is the case for images captured on a turntable in a light box/studio setting)
