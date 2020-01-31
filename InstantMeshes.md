InstantMeshes Options:

Implemented:

-o, --output <output>     Writes to the specified PLY/OBJ output file in batch mode
   
-S, --smooth <iter>       Number of smoothing & ray tracing reprojection steps (default: 2)

-c, --crease <degrees    Dihedral angle threshold for creases

-r, --rosy <number       Specifies the orientation symmetry type (2, 4, or 6)

-p, --posy <number       Specifies the position symmetry type (4 or 6)


To Do:

-t, --threads <count     Number of threads used for parallel computations

-s, --scale <scale       Desired world space length of edges in the output

-f, --faces <count       Desired face count of the output mesh

-v, --vertices <count    Desired vertex count of the output mesh

-k, --knn <count         Point cloud mode: number of adjacent points to consider

......

-d, --deterministic       Prefer (slower) deterministic algorithms

-D, --dominant            Generate a tri/quad dominant mesh instead of a pure tri/quad mesh

-i, --intrinsic           Intrinsic mode (extrinsic is the default)

-b, --boundaries          Align to boundaries (only applies when the mesh is not closed)

-F, --fullscreen          Open a full-screen window


