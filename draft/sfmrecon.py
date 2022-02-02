# sfmrecon [ OPTIONS ] SCENE
# Available options:
# -o, --original=ARG     Original image embedding [original]
# -e, --exif=ARG         EXIF data embedding [exif]
# -m, --max-pixels=ARG   Limit image size by iterative half-sizing [6000000]
# -u, --undistorted=ARG  Undistorted image embedding [undistorted]
# --prebundle=ARG        Load/store pre-bundle file [prebundle.sfm]
# --log-file=ARG         Log some timings to file []
# --no-prediction        Disable matchability prediction
# --normalize            Normalize scene after reconstruction
# --skip-sfm             Compute prebundle, skip SfM reconstruction
# --always-full-ba       Run full bundle adjustment after every view
# --video-matching=ARG   Only match to ARG previous frames [0]
# --fixed-intrinsics     Do not optimize camera intrinsics
# --shared-intrinsics    Share intrinsics between all cameras
# --intrinsics-from-views  Use intrinsics from MVE views [use EXIF]
# --track-error-thres=ARG  Error threshold for new tracks [10]
# --track-thres-factor=ARG  Error threshold factor for tracks [25]
# --use-2cam-tracks      Triangulate tracks from only two cameras
# --initial-pair=ARG     Manually specify initial pair IDs [-1,-1]
# --cascade-hashing      Use cascade hashing for matching [false]

__version__ = "1.0"

from meshroom.core import desc

class sfmrecon(desc.CommandLineNode):
    commandLine = '"./mve/sfmrecon" {inputValue}'
	
#    category = 'MVE'
    documentation = '''
Reconstruction of camera parameters for MVE scenes using Structure from
Motion. Note: The prebundle and the log file are relative to the scene
directory.
## Online
[https://github.com/simonfuhrmann/mve](https://github.com/simonfuhrmann/mve)
'''

    inputs = [
        desc.File(
                name="input",
                label="Input",
                description="Input",
                value="",
                uid=[0],
		)
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output",
            description="Output",
            value="",
            uid=[0],
            )
        ]