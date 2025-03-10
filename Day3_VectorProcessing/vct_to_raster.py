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

# Now, need to add the vector file path
vct_path = "Vector/geom_humedal_update.vct"

# Raster output path
output_file = 'geom_humedal_update.rst'

# Declare the reference raster 
raster_base = "Abril-2019/Reflectancias/T16QDJ_20190422T160911_B01_DOS_Reflectance.rst"

# =============================================================================
# To transform a vector into an IDRISI raster file, we need two layers:
# - The vector layer containing the polygon
# - A reference raster scene
#
# This process allows us to create a mask for all scenes. 
# In my case, I will apply this transformation to multiple raster scenes.
# =============================================================================

# Create the command
vct_to_rst_command = f"1*3*{vct_path}*{vct_path}*3"

# Check if the file alredy exist-
if not os.path.isfile('C:/Users/Admin/Desktop/Terrset/geom_humedal_update.rst'):
    # Run the IDRISI module
    IDRISI32.RunModule("RASTERVECTOR",vct_to_rst_command, 1, "", "", "", "", 1)

else:
    print("The file already exist.")
