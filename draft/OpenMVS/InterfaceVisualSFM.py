Command line:
Available options:

Generic options:
  -h [ --help ]                         produce this help message
  -w [ --working-folder ] arg           working directory (default current 
                                        directory)
  -c [ --config-file ] arg (=InterfaceVisualSFM.cfg)
                                        file name containing program options
  --archive-type arg (=2)               project archive type: 0-text, 1-binary,
                                        2-compressed binary
  --process-priority arg (=-1)          process priority (below normal by 
                                        default)
  --max-threads arg (=0)                maximum number of threads (0 for using 
                                        all available cores)
  -v [ --verbosity ] arg (=2)           verbosity level

Main options:
  -i [ --input-file ] arg               input filename containing camera poses 
                                        and image list
  -o [ --output-file ] arg              output filename for storing the mesh
  --output-image-folder arg (=undistorted_images)
                                        output folder to store undistorted 
                                        images
