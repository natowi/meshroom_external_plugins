# computes structure from known poses (sfm file) to ply format. The output ply is not yet compatible with MR (?)

__version__ = "2.0"

import json
import os

from meshroom.core import desc


class StructureFromKnownPoses(desc.CommandLineNode):
    commandLine = 'aliceVision_computeStructureFromKnownPoses {allParams}'
    size = desc.DynamicNodeSize('input')

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='SfMData file.',
            value='',
            uid=[0],
        ),
        desc.ListAttribute(
            elementDesc=desc.File(
                name="featuresFolder",
                label="Features Folder",
                description="",
                value="",
                uid=[0],
            ),
            name="featuresFolders",
            label="Features Folders",
            description="Folder(s) containing the extracted features and descriptors."
        ),
        desc.ListAttribute(
            elementDesc=desc.File(
                name="matchesFolder",
                label="Matches Folder",
                description="",
                value="",
                uid=[0],
            ),
            name="matchesFolders",
            label="Matches Folders",
            description="Folder(s) in which computed matches are stored."
        ),
        desc.ChoiceParam(
            name='describerTypes',
            label='Describer Types',
            description='Describer types used to describe an image.',
            value=['sift'],
            values=['sift', 'sift_float', 'sift_upright', 'akaze', 'akaze_liop', 'akaze_mldb', 'cctag3', 'cctag4', 'sift_ocv', 'akaze_ocv'],
            exclusive=False,
            uid=[0],
            joinChar=',',
        ),

    ]

    outputs = [
        desc.File(
            name='output',
            label='Output Folder',
            description='Output path',
            value=desc.Node.internalFolder + 'sfm.ply',
            uid=[],
        ),

    ]
