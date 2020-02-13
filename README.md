# meshroom_external_plugins
Add support for various external software packages

The Meshroom plugins are licensed under MPL-2.

Tested on Windows only

**List of supported software packages:**

- InstantMeshes (Implemented: smooth, crease, rosy, posy) https://github.com/wjakob/instant-meshes
- Simplify (Fast-Quadric-Mesh-Simplification) https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification
- **ImageMasking** Plugin based on ImageMagick (mogrify) https://github.com/ImageMagick/ImageMagick
  This plugin can create *masks for images with white background*. ToDo: support for black/green bg, Background subtraction
  **Usage** PrepareDenseScene2(jpg)->ImageMasking->ImagesFolder(PrepareDenseScene3)->DepthMaskFilter

**DepthMapMask**

https://github.com/alicevision/meshroom/pull/641

https://github.com/alicevision/meshroom/pull/641/files

**MVE support**

https://www.gcc.tu-darmstadt.de/home/proj/mve/

- Convert2MVE convert Mesroom SfM to MVE data file format
- MVEparams.md notes for node implementation

**How to use the plugins:**

The binary windows distribution of Meshroom can use uncompiled python source (*.py) files.
(It compiles these files on-the-fly and creates a _pycache_ folder.)
So the only two things you need to do is:
- copy the executable (InstantMeshes.exe) into aliceVision/bin folder and rename to 'external_instantMeshes.exe'
- put the python file (InstantMeshes.py) into the libs/meshroom/nodes/aliceVision folder

For alternative methods, read the wiki


**Software packages with Meshroom addons**

Blender:

https://github.com/tibicen/meshroom2blender

https://github.com/tibicen/meshroom2blender

https://github.com/SBCV/Blender-Addon-Photogrammetry-Importer

https://github.com/s-leger/Meshroom_tracking_for_blender

( https://github.com/Stwend/MeshroomTools )

OrtogOnBlender
https://www.blendernation.com/2019/07/29/meshroom-on-ortogonblender/

implementation:

https://github.com/cogitas3d/OrtogOnBlender/blob/08bb76a734d2c1e1af9aedcce15fbb1232d2e5ff/FotogrametriaMeshroom.py


