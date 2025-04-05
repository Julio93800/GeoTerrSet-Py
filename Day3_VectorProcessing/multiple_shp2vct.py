# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 21:26:09 2025

@author: Admin
"""

"""

In this file, we are going to convert multiple shapefiles into 
IDRISI vector files using the SHAPEIDR module in TerrSet

"""

import win32com.client
import os

# First make a connection to Terrset API 
IDRISI32 = win32com.client.Dispatch('IDRISI32.IdrisiAPIServer')

# Set IDRISI working directory path the data folder. If you are using this code, you must update the file path here. 
IDRISI32.SetWorkingDir("C:/Users/Admin/Desktop/Terrset/Vector")

# Next, we need to retrieve the .shp files using the os library
# Declare the path to the .shp file and the destination path 
shapes_path = 'C:/Users/Admin/Desktop/Terrset/Vector/zonificacion/zonas'
dest_path = 'C:/Users/Admin/Desktop/Terrset/Vector/zonificacion/zonificacion_vct'

for file in os.listdir(shapes_path):
    # Ensure that the files in the paths are .shp files
    if file.endswith('.shp'):
        
        # Build the absolute path from the root and file name
        shape_file = os.path.join(shapes_path, file)
        
        # Create the vector file name using the shapefile's base name
        vct_name = file.split('.')[0]
        
        # Build the absolute path from the root and vector name
        output_vct_file = os.path.join(dest_path, vct_name)
        
        # Create the command
        shp_to_vct_command = f"1*{shape_file}*{output_vct_file}*UTM-16N.REF*m*1"
        
        # Now let´s transform the shape file into IDRISI vector file
        IDRISI32.RunModule("SHAPEIDR",shp_to_vct_command, 1, "", "", "", "", 1)

