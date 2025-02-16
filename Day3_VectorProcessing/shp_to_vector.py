# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:37:24 2025

@author: jguevara
"""

"""
This code transforms a .shp file into a vector format, 
enabling more geoprocessing tasks within the TerrSet Libra GIS environment.
"""

import win32com.client
import os

# First make a connection to Terrset API 
IDRISI32 = win32com.client.Dispatch('IDRISI32.IdrisiAPIServer')

# Set IDRISI working directory path the data folder. If you are using this code, you must update the file path here. 
IDRISI32.SetWorkingDir("C:/Users/Admin/Desktop/Terrset")

# Now, need to add the file path
shp_path = "Vector/Humedal_vector.shp"

# Declare the output vector file
output_vct_file = "geom_humedal_update.vct"

# =============================================================================
# To transform a .shp file into an IDRISI vector file, we need the SHAPEIDR module.
# First, create the command that the TerrSet API requires to perform the transformation using the IDRISI API with the RunModule method.
# Then, pass the module name in uppercase, followed by the command and the necessary flags.
# The ‘ 1, '','','','',1 ‘ at the end of the line must be included with every operation.  
# The parameters for each module can be found in the ‘macro command’ link in the help of each module. 
# eg. IDRISI32.RunModule("MODULE",'your_command_here', 1, "", "", "", "", 1) 
# =============================================================================

# Create the command
shp_to_vct_command = f"1*{shp_path}*{output_vct_file}*Utm-16n*m*1"

# Check if the file alredy exist-
if not os.path.isfile('C:/Users/Admin/Desktop/Terrset/geom_humedal_update.vct'):
    # Run the IDRISI module
    # FIXME: The code runs successfully, but a warning appears indicating that the geodatabase could not be created.  
    # However, the vector file is generated in the correct path.
    IDRISI32.RunModule("SHAPEIDR",shp_to_vct_command, 1, "", "", "", "", 1)

else:
    print("The file already exist.")





