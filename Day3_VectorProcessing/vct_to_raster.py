# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:03:30 2025

@author: Admin
"""

"""
This script transforms a vector into a raster to create a mask for a larger raster, 
extracting only the Region of Interest (ROI).
"""

import win32com.client
import os

# First make a connection to Terrset API 
IDRISI32 = win32com.client.Dispatch('IDRISI32.IdrisiAPIServer')

# Set IDRISI working directory path the data folder. If you are using this code, you must update the file path here. 
IDRISI32.SetWorkingDir("C:/Users/Admin/Desktop/Terrset")

# Now, need to add the file path
vct_path = "geom_humedal_update.vct"

# Declare the output vector file
output_rst_file = "Abril-2019/Reflectancias/T16QDJ_20190422T160911_B01_DOS_Reflectance.rst"

# =============================================================================
# To transform a vector into an IDRISI raster file, we need two layers:
# - The vector layer containing the polygon
# - A reference raster scene
#
# This process allows us to create a mask for all scenes. 
# In my case, I will apply this transformation to multiple raster scenes.
# =============================================================================

# Create the command
vct_to_rst_command = f"1*3*{vct_path}*{output_rst_file}*1"

# Check if the file alredy exist-
if not os.path.isfile('C:/Users/Admin/Desktop/Terrset/geom_humedal_update.rst'):
    # Run the IDRISI module
    # FIXME: The code runs successfully, but a warning appears indicating that the geodatabase could not be created.  
    # However, the vector file is generated in the correct path.
    IDRISI32.RunModule("RASTERVECTOR",vct_to_rst_command, 1, "", "", "", "", 1)

else:
    print("The file already exist.")
