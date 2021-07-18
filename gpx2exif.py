# WIP - This is a fragment and not ready to be used
# problem: it will update the exif of the input metadata in place, so the image files should be copied to the InternalNodeFolder first
# https://github.com/alicevision/meshroom/blob/develop/meshroom/nodes/aliceVision/Publish.py
# https://github.com/gvellut/gpx2exif
__version__ = "3.0"

from meshroom.core import desc


class InstantMeshes(desc.CommandLineNode):
    commandLine = '{gpx2exifPathValue} image {gpxInputValue} {imageFolder} --delta {minutesValue}m{secondsValue}s'

    cpu = desc.Level.NORMAL
    ram = desc.Level.NORMAL

    inputs = [
		desc.File(
            name="gpx2exifPath",
            label='gpx2exif Path',
            description='Path to gpx2exif',
            value=os.environ.get('gpx2exif',"gpx2exif"),
            uid=[0],
            group='',
            ),
		desc.File(
            name="gpxInput",
            label='GPX input).',
            description='Path to the GPX file',
            value=os.environ.get('GPX file',""),
            uid=[0],
            group='',
            ),
      desc.File(
            name="imageInput",
            label='Image input).',
            description='Path to images',
            value=os.environ.get('images',""),
            uid=[0],
            group='',
            ),

    ]

    outputs = [
        desc.File(
            name="output",
            label="Output mesh",
            description="Output mesh (OBJ file format).",
            value=desc.Node.internalFolder + 'mesh.obj',
            uid=[],
            ),
    ]
