# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 21:06:50 2025

@author: Admin

"""
"""
This script performs raster operations using GDAL in TerrSet. 
It applies a mask raster to multiple raster datasets and saves 
the results as new raster files with a '_pol' suffix.

Steps:
1. Identify raster files based on a naming pattern (e.g., 'evi_oct_2022.rst').
2. Load each raster and a mask raster.
3. Multiply the raster values by the mask.
4. Save the processed raster in the specified output directory.

Requirements:
- GDAL library installed.
- A valid mask raster file.
"""

from osgeo import gdal
import numpy as np
import os
import re

# Define the base directory where raster data is located
base_dir = "C:/Users/Admin/Desktop/Terrset"

# Define the path of the mask
mask_path = "C:/Users/Admin/Desktop/Terrset/Vector/geom_humedal_update.rst"

# Load the mask raster
mask_dataset = gdal.Open(mask_path, gdal.GA_ReadOnly)
mask_array = mask_dataset.GetRasterBand(1).ReadAsArray().astype(np.float32)

# Define index names to search for in raster filenames
indices = ["evi", "lswi", "ndvi", "ndwi"]  # Add more indices if necessary

# Define month names (in Spanish) used in the filenames
months = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio", 
    "julio", "agosto", "septiembre", "oct", "nov", "dic"
]

# Create a regex pattern to match raster filenames (e.g., 'evi_oct_2022.rst')
pattern = re.compile(rf"^({'|'.join(indices)})_({'|'.join(months)})_\d{{4}}\.rst$", re.IGNORECASE)

# Define the output directory where processed rasters will be saved
output_dir = "C:/Users/Admin/Desktop/Terrset/productos_finales"
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# List to store identified raster file paths
full_scene_indices = []

# Traverse the directory structure to find matching raster files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if pattern.match(file):  # Check if the filename matches the pattern
            rst_file = os.path.join(root, file)
            full_scene_indices.append(rst_file)

            # Open the raster file
            dataset = gdal.Open(rst_file, gdal.GA_ReadOnly)
            raster_array = dataset.GetRasterBand(1).ReadAsArray().astype(np.float32)

            # Apply the mask using element-wise multiplication
            multiplied_array = raster_array * mask_array

            # Define the output filename by appending '_pol' before the extension
            output_rst = os.path.join(output_dir, file.replace(".rst", "_pol.rst"))

            # Save the processed raster as a new .rst file
            driver = gdal.GetDriverByName("RST")
            out_dataset = driver.Create(output_rst, dataset.RasterXSize, dataset.RasterYSize, 1, gdal.GDT_Float32)
            out_dataset.GetRasterBand(1).WriteArray(multiplied_array)

            # Copy geospatial metadata (projection & transformation) from the original raster
            out_dataset.SetGeoTransform(dataset.GetGeoTransform())
            out_dataset.SetProjection(dataset.GetProjection())

            # Close datasets to free memory
            dataset = None
            out_dataset = None

            print(f"Processed: {rst_file} -> {output_rst}")

print("\nAll raster operations completed. Results saved in:", output_dir)



