# Note: This node is outdated and archived as Meshroom python node example
#
# Requirements:
# enum34;python_version<"3.4"
# PySide2==5.13.0
# markdown==2.6.11
# numpy
# Pillow
# Imath
# OpenEXR
# 
# https://github.com/alicevision/meshroom/pull/641
# Node by ALfuhrmann https://github.com/ALfuhrmann
# 
# This node includes the minor fix by tpontin https://github.com/alicevision/meshroom/pull/641#issuecomment-603876386
# As this node was intended as Meshroom contribution, it is licensed under MPLv2
# 
# Node inputs:
# Input: cameraInit.sfm for input image file names (.sfm only, no alembic)
# Filtered Depth Maps Folder: depth maps folder output of DepthMaskFilter
# Mask Folder: folder containing b/w mask .PNG images with the same names as the associated input files
# The masks have to be rectified, so you cannot use your generated masks directly, but have to run them through a PrepareDenseScene node
# (https://github.com/alicevision/meshroom/pull/641)
#
# See https://github.com/alicevision/meshroom/pull/708 for the latest DepthMaskFilter implementation in Meshroom


from __future__ import print_function

__version__ = "1.0"

from meshroom.core import desc
import json, shutil, glob
import OpenEXR
import Imath
import numpy as np
from PIL import Image
import os.path
import logging

class DepthMaskFilter(desc.Node):

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='SfMData file.',
            value='',
            uid=[0],
        ),   
        desc.File(
            name="depthMapsFilterFolder",
            label='Filtered Depth Maps Folder',
            description='Input filtered depth maps folder',
            value='',
            uid=[0],
        ),        
        desc.File(
            name="MasksFolder",
            label="Masks Folder",
            description="Input masks folder",
            value="",
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='Output folder for masked depth maps.',
            value=desc.Node.internalFolder,
            uid=[],
        ),
    ]


    def maskEXR(self, filename, maskname, fill_value):
        (basename, extension) = os.path.splitext(filename)

        infile = OpenEXR.InputFile(filename) # read depth map
        header = infile.header()

        if (header['channels']['Y'].type == Imath.PixelType(Imath.PixelType.FLOAT)):
            pt = Imath.PixelType(Imath.PixelType.FLOAT)
            dt = np.float32
        elif (header['channels']['Y'].type == Imath.PixelType(Imath.PixelType.HALF)):
            pt = Imath.PixelType(Imath.PixelType.HALF)
            dt = np.float16
        else:
            print('Integer images not supported!')
            exit(-1)

        dw = header['dataWindow']
        size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
        Ystr = infile.channel('Y', pt)
        Y = np.frombuffer(Ystr, dtype=dt)
        Y.shape = (size[1], size[0])  

        maskImage = Image.open(maskname)
        if (size != maskImage.size): # check if depthmaps were downsampled
                print("Resizing mask: {}".format(maskname))
                maskImage = maskImage.resize(size, Image.NEAREST)
                
        imgmask = np.array(maskImage)[:, :, 0]  # read only greyscale images

        Y_masked = np.ma.array(Y, mask=(imgmask == 0)).filled(fill_value) # fill masked areas
        infile.close()

        # write masked depth map
        exr = OpenEXR.OutputFile(filename, header)
        exr.writePixels({'Y': Y_masked})
        exr.close()

    
    def processChunk(self, chunk):
    
        print("DepthMask Node start\n")

        with open(chunk.node.input.value, 'r') as f:
            sfm = json.load(f)
            for view in sfm["views"]:  # loop over all views/images
                viewId = view["viewId"]
                source_image_path = view["path"]
                (src_path, src_name) = os.path.split(source_image_path)
                (filename, ext) = os.path.splitext(src_name)
                depth_map_name = os.path.join(chunk.node.output.value, viewId+"_depthMap.exr")
                mask_name = os.path.join(chunk.node.MasksFolder.value, viewId+".png")

                # duplicate all maps
                files = glob.glob(os.path.join(chunk.node.depthMapsFilterFolder.value, viewId+"_*Map.*"))
                for f in files:
                    shutil.copy(f, chunk.node.output.value)
                
                # masking depth maps
                print("Masking depth map: {}".format(depth_map_name))
                if os.path.exists(mask_name): self.maskEXR(depth_map_name, mask_name, -1.0)
        print('DepthMask Node end')
