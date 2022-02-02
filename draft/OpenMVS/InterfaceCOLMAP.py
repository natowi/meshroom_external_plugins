Command line: InterfaceCOLMAP

Import/export 3D reconstruction from/to COLMAP format as TXT (the only documented format).
In order to import a scene, run COLMAP SfM and next undistort the images (only PINHOLE
camera model supported for the moment); and convert the BIN scene to TXT by importing in
COLMAP the sparse scene stored in 'dense' folder and exporting it as TXT.

Available options:

Generic options:
  -h [ --help ]                         produce this help message
  -w [ --working-folder ] arg           working directory (default current 
                                        directory)
  -c [ --config-file ] arg (=InterfaceCOLMAP.cfg)
                                        file name containing program options
  --archive-type arg (=2)               project archive type: 0-text, 1-binary,
                                        2-compressed binary
  --process-priority arg (=-1)          process priority (below normal by 
                                        default)
  --max-threads arg (=0)                maximum number of threads (0 for using 
                                        all available cores)
  -v [ --verbosity ] arg (=2)           verbosity level

Main options:
  -i [ --input-file ] arg               input COLMAP folder containing cameras,
                                        images and points files OR input MVS 
                                        project file
  -o [ --output-file ] arg              output filename for storing the MVS 
                                        project
  --image-folder arg (=images/)         folder to the undistorted images
  -f [ --normalize ] arg (=1)           normalize intrinsics while exporting to
                                        MVS format
