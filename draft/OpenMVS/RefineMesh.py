Command line:
Available options:

Generic options:
  -h [ --help ]                         produce this help message
  -w [ --working-folder ] arg           working directory (default current 
                                        directory)
  -c [ --config-file ] arg (=RefineMesh.cfg)
                                        file name containing program options
  --export-type arg (=ply)              file type used to export the 3D scene 
                                        (ply or obj)
  --archive-type arg (=2)               project archive type: 0-text, 1-binary,
                                        2-compressed binary
  --process-priority arg (=-1)          process priority (below normal by 
                                        default)
  --max-threads arg (=0)                maximum number of threads (0 for using 
                                        all available cores)
  -v [ --verbosity ] arg (=2)           verbosity level

Refine options:
  -i [ --input-file ] arg               input filename containing camera poses 
                                        and image list
  -o [ --output-file ] arg              output filename for storing the mesh
  --resolution-level arg (=0)           how many times to scale down the images
                                        before mesh refinement
  --min-resolution arg (=640)           do not scale images lower than this 
                                        resolution
  --max-views arg (=8)                  maximum number of neighbor images used 
                                        to refine the mesh
  --decimate arg (=0)                   decimation factor in range [0..1] to be
                                        applied to the input surface before 
                                        refinement (0 - auto, 1 - disabled)
  --close-holes arg (=30)               try to close small holes in the input 
                                        surface (0 - disabled)
  --ensure-edge-size arg (=1)           ensure edge size and improve vertex 
                                        valence of the input surface (0 - 
                                        disabled, 1 - auto, 2 - force)
  --max-face-area arg (=64)             maximum face area projected in any pair
                                        of images that is not subdivided (0 - 
                                        disabled)
  --scales arg (=3)                     how many iterations to run mesh 
                                        optimization on multi-scale images
  --scale-step arg (=0.5)               image scale factor used at each mesh 
                                        optimization step
  --reduce-memory arg (=1)              recompute some data in order to reduce 
                                        memory requirements
  --alternate-pair arg (=0)             refine mesh using an image pair 
                                        alternatively as reference (0 - both, 1
                                        - alternate, 2 - only left, 3 - only 
                                        right)
  --regularity-weight arg (=0.200000003)
                                        scalar regularity weight to balance 
                                        between photo-consistency and 
                                        regularization terms during mesh 
                                        optimization
  --rigidity-elasticity-ratio arg (=0.899999976)
                                        scalar ratio used to compute the 
                                        regularity gradient as a combination of
                                        rigidity and elasticity
  --gradient-step arg (=45.0499992)     gradient step to be used instead (0 - 
                                        auto)
  --planar-vertex-ratio arg (=0)        threshold used to remove vertices on 
                                        planar patches (0 - disabled)
