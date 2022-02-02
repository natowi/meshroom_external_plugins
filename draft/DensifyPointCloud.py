22:23:07 [App     ] Build date: Feb 14 2020, 19:23:47
22:23:07 [App     ] CPU: Intel(R) Core(TM) i7-7820HK CPU @ 2.90GHz (8 cores)
22:23:07 [App     ] RAM: 31.95GB Physical Memory 128.00TB Virtual Memory
22:23:07 [App     ] OS: Windows 8 x64
22:23:07 [App     ] SSE & AVX compatible CPU & OS detected
22:23:07 [App     ] Command line:
22:23:07 [App     ] Available options:

Generic options:
  -h [ --help ]                         produce this help message
  -w [ --working-folder ] arg           working directory (default current 
                                        directory)
  -c [ --config-file ] arg (=DensifyPointCloud.cfg)
                                        file name containing program options
  --archive-type arg (=2)               project archive type: 0-text, 1-binary,
                                        2-compressed binary
  --process-priority arg (=-1)          process priority (below normal by 
                                        default)
  --max-threads arg (=0)                maximum number of threads (0 for using 
                                        all available cores)
  -v [ --verbosity ] arg (=2)           verbosity level

Densify options:
  -i [ --input-file ] arg               input filename containing camera poses 
                                        and image list
  -o [ --output-file ] arg              output filename for storing the dense 
                                        point-cloud
  --resolution-level arg (=1)           how many times to scale down the images
                                        before point cloud computation
  --max-resolution arg (=3200)          do not scale images higher than this 
                                        resolution
  --min-resolution arg (=640)           do not scale images lower than this 
                                        resolution
  --number-views arg (=5)               number of views used for depth-map 
                                        estimation (0 - all neighbor views 
                                        available)
  --number-views-fuse arg (=3)          minimum number of images that agrees 
                                        with an estimate during fusion in order
                                        to consider it inlier
  --optimize arg (=7)                   filter used after depth-map estimation 
                                        (0 - disabled, 1 - remove speckles, 2 -
                                        fill gaps, 4 - cross-adjust)
  --estimate-colors arg (=2)            estimate the colors for the dense 
                                        point-cloud
  --estimate-normals arg (=0)           estimate the normals for the dense 
                                        point-cloud
  --sample-mesh arg (=0)                uniformly samples points on a mesh (0 -
                                        disabled, <0 - number of points, >0 - 
                                        sample density per square unit)
  --filter-point-cloud arg (=0)         filter dense point-cloud based on 
                                        visibility (0 - disabled)
