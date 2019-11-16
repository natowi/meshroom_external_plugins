# meshroom_external_plugins
Add support for various external software packages

The Meshroom plugins are licensed under MPL-2.

Tested on Windows only

**List of supported software packages:**

- InstantMeshes (WIP) https://github.com/wjakob/instant-meshes
- Simplify (Fast-Quadric-Mesh-Simplification) https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification
- **ImageMasking** Plugin based on ImageMagick (mogrify) https://github.com/ImageMagick/ImageMagick
  This plugin can create masks for images with white background. ToDo: support for black/green bg, Background subtraction
  **Note** this is WIP has some bugs

**DepthMapMask**

https://github.com/alicevision/meshroom/pull/641

https://github.com/alicevision/meshroom/pull/641/files

**How to use the plugins:**

- download the meshroom repository zip from https://github.com/alicevision/meshroom/
- install requirements: (cli-> navigate in meshroom-develop folder) ´´pip install -r requirements.txt´´
- download the pre-compiled meshroom zip from https://github.com/alicevision/meshroom/releases
- paste the pre-compiled aliceVision and qtPlugins folders and the provided Meshroom.bat in the meshroom folder and use Meshroom.bat (or cli) to start the meshroom gui (*or use your own compiled versions)
- when Meshroom is closed, you can copy the plugin files in the respective folders
- plugin.py in meshroom\nodes\aliceVision (for the MR GUI)
- place the new software (.exe, .py or .bat) in aliceVision\bin (this is for the software package that is called via the MR GUI)



----
**Ideas**

foreground extraction algorithm

http://opensource.graphics/how-to-code-a-nice-user-guided-foreground-extraction-algorithm/

http://opensource.graphics/how-to-code-a-nice-user-guided-foreground-extraction-algorithm-addendum/

-> generate masks
--> it might be possible to use the masks to filter the keypoints, and use the keypoints to detect the object of interest in multiple images
