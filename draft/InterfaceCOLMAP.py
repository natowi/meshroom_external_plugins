22:10:07 [App     ] Build date: Feb 14 2020, 19:23:47
22:10:07 [App     ] CPU: Intel(R) Core(TM) i7-7820HK CPU @ 2.90GHz (8 cores)
22:10:07 [App     ] RAM: 31.95GB Physical Memory 128.00TB Virtual Memory
22:10:07 [App     ] OS: Windows 8 x64
22:10:07 [App     ] SSE & AVX compatible CPU & OS detected
22:10:07 [App     ] Command line: InterfaceCOLMAP
22:10:07 [App     ] 
Import/export 3D reconstruction from/to COLMAP format as TXT (the only documented format).
In order to import a scene, run COLMAP SfM and next undistort the images (only PINHOLE
camera model supported for the moment); and convert the BIN scene to TXT by importing in
COLMAP the sparse scene stored in 'dense' folder and exporting it as TXT.

22:10:07 [App     ] Available options:

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
