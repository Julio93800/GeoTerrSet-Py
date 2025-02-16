# GeoTerrSet-Py

## Overview
This repository is dedicated to using **TerrSet** with **Python**. The goal is to explore different functionalities of TerrSet while automating geospatial analysis with Python scripts.

## Structure
The project is divided into a daily workflow, where each day focuses on a specific feature or automation task with TerrSet.

```
📂 GeoTerrSet-Py
 ├── 📂 Day1_Setup            # Installing and configuring TerrSet for Python, includes Conda environment
 ├── 📂 Day2_RasterAnalysis   # Working with raster data in TerrSet
 ├── 📂 Day3_VectorProcessing # Handling vector data with Python
 ├── 📂 Day4_ModelAutomation  # Automating workflows using Python scripts
 ├── 📂 Day5_MachineLearning  # Exploring ML capabilities within TerrSet
 ├── 📂 Resources             # Additional guides, datasets, and references
 └── README.md                # This file
```

## Installation
Before running the scripts, ensure you have **TerrSet** installed along with Python. The project uses a **Conda environment with Python 3.10**. To set up the environment, navigate to `Day1_Setup` and run:

```bash
conda env create -f Day1_Setup/geoterrser-py_env.yml
conda activate geoterrset
```



## Getting Started
Each day's folder contains Python scripts and Jupyter Notebooks explaining the functionality. Simply navigate to the desired day and run the scripts.

Example:
```bash
cd Day1_Setup
python setup_terrset.py
```

## Contributions
Contributions are welcome! Feel free to fork the repo and submit a pull request if you have improvements or additional use cases to share.

## License
This project is licensed under the MIT License.

---
### Notes
- The Conda environment is defined in `Day1_Setup/environment.yml` and includes all necessary dependencies.
- Ensure you have the correct version of Python (3.10) before running the scripts.
- If you have additional dependencies for machine learning or automation, include them in `requirements.txt`.

## License
This project is licensed under the MIT License.

---
### Notes
- If you have a specific dataset or version requirement, please mention it in the setup guide.
- If you have additional dependencies for machine learning or automation, include them in `requirements.txt`.
