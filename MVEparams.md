Preperation for node implementation


# MVE Bundle to Pointset

This application reads a bundle file and outputs a PLY file with a colored
point cloud.

**bundle2pset.exe [ OPTIONS ] INPUT_BUNDLE OUTPUT_PLY**

Available options:

  -s, --spheres=ARG     Generates a sphere for every point (radius ARG) [0.0]

# MVE Depth Map Reconstruction

**dmrecon.exe [ OPTIONS ] SCENEDIR**

Available options:

  -n, --neighbors=ARG    amount of neighbor views (global view selection)
  
  -m, --master-view=ARG  reconstructs given master view ID only
  
  -l, --list-view=ARG    reconstructs given view IDs (given as string "0-10")
  
  -s, --scale=ARG        reconstruction on given scale, 0 is original
  
  --max-pixels=ARG       Limit master image size [1500000]
  
  -f, --filter-width=ARG  patch size for NCC based comparison [5]
  
  --nocolorscale         turn off color scale
  
  -i, --image=ARG        specify source image embedding [undistorted]
  
  --local-neighbors=ARG  amount of neighbors for local view selection [4]
  
  --keep-dz              store dz map into view
  
  --keep-conf            store confidence map into view
  
  -p, --writeply         use this option to write the ply file
  
  --plydest=ARG          path suffix appended to scene dir to write ply files
  
  --bounding-box=ARG     Six comma separated values used as AABB [disabled]
  
  --progress=ARG         progress output style: 'silent', 'simple' or 'fancy'
  
  --force                Reconstruct and overwrite existing depthmaps
  
# Floating Scale Surface Reconstruction

Samples the implicit function defined by the input samples and produces a
surface mesh. The input samples must have normals and the "values" PLY
attribute (the scale of the samples). Both confidence values and vertex
colors are optional. The final surface should be cleaned (sliver triangles,
isolated components, low-confidence vertices) afterwards.

**fssrecon.exe [ OPTS ] IN_PLY [ IN_PLY ... ] OUT_PLY**

Available options:

  -s, --scale-factor=ARG   Multiply sample scale with factor [1.0]
  
  -r, --refine-octree=ARG  Refines octree with N levels [0]
  
  --min-scale=ARG          Minimum scale, smaller samples are clamped
  
  --max-scale=ARG          Maximum scale, larger samples are ignored
  
  --interpolation=ARG      Interpolation: linear, scaling, lsderiv, [cubic]
  
# MVE Makescene

This utility creates MVE scenes by importing from an external SfM software.
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

**makescene.exe [ OPTIONS ] INPUT OUT_SCENE**
Available options:
  -o, --original        Import original images
  
  -b, --bundle-id=ARG   Bundle ID (Photosynther and Bundler only) [0]
  
  -k, --keep-invalid    Keeps images with invalid cameras
  
  -i, --images-only     Imports images from INPUT_DIR only
  
  -a, --append-images   Appends images to an existing scene
  
  -m, --max-pixels=ARG  Limit image size by iterative half-sizing
  
# MVE FSSR Mesh to Pointset

This app creates a PLY point cloud from the input mesh by stripping the
connectivity information. Scale values are computed for each vertex as the
average distance to each neighbor (using the connectivity information).
Confidence values are computed by down-weighting boundary vertices.

**mesh2pset.exe [ OPTS ] IN_MESH OUT_PLY_PSET**

Available options:

  -s, --scale=ARG          Set constant scale for all samples [off]
  
  -a, --adaptive=ARG       Average distance to neighbors scale factor [1.0]
  
  -b, --bounding-box=ARG   Six comma separated values used as AABB [off]
  
  -c, --no-confidences     Do not compute vertex confidences
  
  -x, --no-scale-values    Do not compute sample scale
  
  -n, --no-normals         Do not compute sample normals
  
# MVE FSSR Mesh Alignment

Generates a combined mesh from Stanford or Meshlab alignment data. The
combined mesh contains all triangulated range images in a global,
consistent coordinate system. Stanford alignments are .conf files with
global camera and a list of meshes with alignment information. Meshlab
alignment are .aln files with a list of meshes and a camera to world
transformation matrix.

meshalign.exe [ OPTS ] ALIGNMENT_FILE [...] OUT_MESH

# MVE FSSR Mesh Cleaning

The application cleans degenerated faces resulting from MC-like algorithms.
Vertices below a confidence threshold and vertices in small isolated
components are deleted as well.

**meshclean.exe [ OPTS ] IN_MESH OUT_MESH**

Available options:

  -t, --threshold=ARG      Threshold on the geometry confidence [1.0]
  
  -p, --percentile=ARG     Use the nth percentile (0 - 100) as confidence threshold [disabled]
  
  -c, --component-size=ARG  Minimum number of vertices per component [1000]
  
  -n, --no-clean           Prevents cleanup of degenerated faces
  
  --delete-scale           Delete scale attribute from mesh
  
  --delete-conf            Delete confidence attribute from mesh
  
  --delete-color           Delete color attribute from mesh
  
# MVE Mesh Conversion

Converts the mesh given by IN_MESH to the output file OUT_MESH. The format
of the input and output mesh are detected by extension. Supported file
formats are .off, .ply (Stanford), .npts or .bnpts (Poisson Surface
Reconstruction) and .pbrt.

**meshconvert.exe [ OPTS ] IN_MESH OUT_MESH**

Available options:

  -n, --normals            Compute vertex normals
  
# MVE SfM Prebundle

Statistics generator for prebundle files. The graph mode outputs the
matching graph in Graphviz DOT format.

**prebundle.exe [ MODES ] PREBUNDLE_FILE**

Available options:

  -g, --graph-mode=ARG   Graph mode: Output matching graph file for DOT
  
# MVE Scene to Pointset

Generates a pointset from the scene by projecting reconstructed depth
values in the world coordinate system.

**scene2pset [ OPTS ] SCENE_DIR MESH_OUT**

Available options:

  -d, --depthmap=ARG       Name of depth map to use [depth-L0]
  
  -i, --image=ARG          Name of color image to use [undistorted]
  
  -n, --with-normals       Write points with normals (PLY only)
  
  -s, --with-scale         Write points with scale values (PLY only)
  
  -c, --with-conf          Write points with confidence (PLY only)
  
  -m, --mask=ARG           Name of mask/silhouette image to clip 3D points []
  
  -v, --views=ARG          View IDs to use for reconstruction [all]
  
  -b, --bounding-box=ARG   Six comma separated values used as AABB.
  
  -f, --min-fraction=ARG   Minimum fraction of valid depth values [0.0]
  
  -p, --poisson-normals    Scale normals according to confidence
  
  -S, --scale-factor=ARG   Factor for computing scale values [2.5]
  
  -F, --fssr=ARG           FSSR output, sets -nsc and -di with scale ARG
  
# MVE Scene Upgrade

This utility upgrades an MVE view, a prebundle file, or an MVE scene to the
new format. See the Github wiki for more details about the new formats.
INPUT can either be a single .mve view, a single .sfm prebundle file, or a
scene directory. In the latter case, all views and the prebundle.sfm are
upgraded.

**sceneupgrade.exe [ OPTIONS ] INPUT**

Available options:

  -k, --keep-original   Keep original files
  
# MVE SfM Reconstruction

Reconstruction of camera parameters for MVE scenes using Structure from
Motion. Note: The prebundle and the log file are relative to the scene
directory.

**sfmrecon.exe [ OPTIONS ] SCENE**

Available options:

  -o, --original=ARG     Original image embedding [original]
  
  -e, --exif=ARG         EXIF data embedding [exif]
  
  -m, --max-pixels=ARG   Limit image size by iterative half-sizing [6000000]
  
  -u, --undistorted=ARG  Undistorted image embedding [undistorted]
  
  --prebundle=ARG        Load/store pre-bundle file [prebundle.sfm]
  
  --log-file=ARG         Log some timings to file []
  
  --no-prediction        Disable matchability prediction
  
  --normalize            Normalize scene after reconstruction
  
  --skip-sfm             Compute prebundle, skip SfM reconstruction
  
  --always-full-ba       Run full bundle adjustment after every view
  
  --video-matching=ARG   Only match to ARG previous frames [0]
  
  --fixed-intrinsics     Do not optimize camera intrinsics
  
  --shared-intrinsics    Share intrinsics between all cameras
  
  --intrinsics-from-views  Use intrinsics from MVE views [use EXIF]
  
  --track-error-thres=ARG  Error threshold for new tracks [10]
  
  --track-thres-factor=ARG  Error threshold factor for tracks [25]
  
  --use-2cam-tracks      Triangulate tracks from only two cameras
  
  --initial-pair=ARG     Manually specify initial pair IDs [-1,-1]
  
  --cascade-hashing      Use cascade hashing for matching [false]
  
  
