Generic options:
  -h [ --help ]                         produce this help message
  -w [ --working-folder ] arg           working directory (default current
                                        directory)
  -c [ --config-file ] arg (=Viewer.cfg)
                                        file name containing program options
  --export-type arg                     file type used to export the 3D scene
                                        (ply or obj)
  --archive-type arg (=2)               project archive type: 0-text, 1-binary,
                                        2-compressed binary
  --process-priority arg (=0)           process priority (normal by default)
  --max-threads arg (=0)                maximum number of threads that this
                                        process should use (0 - use all
                                        available cores)
  --max-memory arg (=0)                 maximum amount of memory in MB that
                                        this process should use (0 - use all
                                        available memory)
  --log-file arg (=0)                   dump log to a file
  -v [ --verbosity ] arg (=2)           verbosity level

Viewer options:
  -i [ --input-file ] arg               input project filename containing
                                        camera poses and scene
                                        (point-cloud/mesh)
  -o [ --output-file ] arg              output filename for storing the mesh
  --texture-lossless arg (=0)           export texture using a lossless image
                                        format