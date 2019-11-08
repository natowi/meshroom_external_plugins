# meshroom_external_plugins
Add support for various external software packages

Tested on Windows only

List of supported software packages:

- InstantMeshes (WIP) https://github.com/wjakob/instant-meshes
- Simplify (Fast-Quadric-Mesh-Simplification) https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification

How to use the plugins:

- download the meshroom repository zip from https://github.com/alicevision/meshroom/
- download the pre-compiled meshroom zip from https://github.com/alicevision/meshroom/releases
- paste the pre-compiled aliceVision and qtPlugins folders and the provided Meshroom.bat in the meshroom folder and use Meshroom.bat (or cli) to start the meshroom gui (*or use your own compiled versions)
- when Meshroom is closed, you can copy the plugin files in the respective folders
- plugin.py in meshroom\nodes\aliceVision 
- software.exe (rename as required) in aliceVision\bin
