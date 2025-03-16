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
IDRISI32.SetWorkingDir("C:/Users/Admin/Desktop/Terrset/Vector")

# Now, need to add the vector file path
vct_path = "geom_humedal_update.vct"

# Raster output path
output_file = 'geom_humedal_update.rst'

# Declare the reference raster 
raster_base = "Abril-2019/Indices/ndwi_abril_2019.rst"

# =============================================================================
# To transform a vector into an IDRISI raster file, we need two layers:
# - The vector layer containing the polygon
# - A reference raster scene
#
# This process allows us to create a mask for all scenes. 
# In my case, I will apply this transformation to multiple raster scenes.
# =============================================================================

# Create the command
vct_to_rst_command = f"1*3*{vct_path}*{output_file}*1"
initial_command = f"{output_file}*1*1*0*1*{raster_base}*m"

# Check if the file alredy exist-
# If the raster file doesn't exist, we're going to create an empty raster with the module: INITIAL
# This beacuse we need a raster to update with the RASTERVECTOR module
if not os.path.isfile('C:/Users/Admin/Desktop/Terrset/Vector/geom_humedal_update.rst'):
    # Run the IDRISI module
    IDRISI32.RunModule("INITIAL",initial_command, 1, "", "", "", "", 1)

else:
    print("The file already exist, let's update it.")
    IDRISI32.RunModule("RASTERVECTOR",vct_to_rst_command, 1, "", "", "", "", 1)
    

