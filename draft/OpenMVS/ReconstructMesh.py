Command line:
Available options:

Generic options:
  -h [ --help ]                         produce this help message
  -w [ --working-folder ] arg           working directory (default current 
                                        directory)
  -c [ --config-file ] arg (=ReconstructMesh.cfg)
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

Reconstruct options:
  -i [ --input-file ] arg               input filename containing camera poses 
                                        and image list
  -o [ --output-file ] arg              output filename for storing the mesh
  -d [ --min-point-distance ] arg (=2.5)
                                        minimum distance in pixels between the 
                                        projection of two 3D points to consider
                                        them different while triangulating (0 -
                                        disabled)
  --constant-weight arg (=1)            considers all view weights 1 instead of
                                        the available weight
  -f [ --free-space-support ] arg (=0)  exploits the free-space support in 
                                        order to reconstruct weakly-represented
                                        surfaces
  --thickness-factor arg (=1)           multiplier adjusting the minimum 
                                        thickness considered during visibility 
                                        weighting
  --quality-factor arg (=1)             multiplier adjusting the quality weight
                                        considered during graph-cut

Clean options:
  --decimate arg (=1)                   decimation factor in range (0..1] to be
                                        applied to the reconstructed surface (1
                                        - disabled)
  --remove-spurious arg (=20)           spurious factor for removing faces with
                                        too long edges or isolated components 
                                        (0 - disabled)
  --remove-spikes arg (=1)              flag controlling the removal of spike 
                                        faces
  --close-holes arg (=30)               try to close small holes in the 
                                        reconstructed surface (0 - disabled)
  --smooth arg (=2)                     number of iterations to smooth the 
                                        reconstructed surface (0 - disabled)
