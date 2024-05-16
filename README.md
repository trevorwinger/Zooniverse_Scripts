# Zooniverse Scripts

This repository contains scripts for processing images and uploading subject sets to Zooniverse projects. These scripts are designed to automate the workflow of preparing images for a Zooniverse project and programmatically uploading them as a subject set. Additionally, these scripts are accessible as Google Colab notebooks, providing an easy-to-use, cloud-based environment for running the scripts.
## Contents

1. **image_processing.py** - This script processes images in a specified folder, preparing them for upload. It supports images in .jpg and .png formats. Also available as a Google Colab notebook.

2. **subject_set_upload.py** - This script uploads the processed images as a subject set to a specific Zooniverse project. It requires Zooniverse credentials and project ID to function. Also available as a Google Colab notebook.

3. **subject_wrapper.py** - A utility script that sequentially runs the above scripts, taking care of processing images and then uploading them as a subject set to a Zooniverse project.

4.**transform_export.py** - A utility script that takes a project's classification export (entire project or specific workflow) and transforms the JSON for each task and workflow to be a column x row representation. Each workflow is then saved as an independent CSV file.  

## Prerequisites
1. Python 3.x
2. Required Python packages: argparse, subprocess, tqdm, panoptes-client.
3. ImageMagick for image processing.

## Installation

1. Clone the repository

Clone this repository to your local machine using:

```bash 
git clone https://github.com/trevorwinger/Zooniverse_Scripts.git
```

2. Install Python dependencies

Navigate to the cloned repository's directory and install the required Python packages:

```bash

pip install -r requirements.txt 
```

3. Install ImageMagick
- For Windows, download and install from ImageMagick Download.
- For macOS, install using Homebrew with brew install imagemagick.
- For Linux (Debian/Ubuntu), install using sudo apt-get install imagemagick.

## Usage
### Image Processing

To process images in a folder, run:

```bash

python image_processing.py <path_to_folder>
```

Ensure the path points to a folder containing .jpg or .png images.
Subject Set Uploading

To upload a subject set to a Zooniverse project, run:

```bash

python subject_set_upload.py <path_to_folder> <username> <password> <project_id>
```

Replace <path_to_folder>, <username>, <password>, and <project_id> with your specific details.
Running Both Scripts Sequentially

To process images and upload them as a subject set in one go, use:

```bash

python subject_wrapper.py <path_to_folder> <username> <password> <project_id>
```

This command sequentially processes the images in the specified folder and uploads them to the Zooniverse project identified by <project_id> using the provided credentials.

### Classification processing
```
python transform_export <path_to_export_csv>
```
Google Colab Notebooks

For those preferring to run these scripts in a cloud environment, Google Colab versions are available:
1. [Image Processing Notebook](https://colab.research.google.com/drive/1G2ME0Oxa7HSW3pLLD5Rz6EGX9IHLNG_s)
2. [Subject Set Uploading Notebook](https://colab.research.google.com/drive/1DbNXWxlYhwu7RK-Uixu3-KtRFFCpR1Tk)
3. [Classification Transformation Notebook](https://colab.research.google.com/drive/12GoWU1Vox0AjAdZecAvr0VJQd4pbEM55?usp=sharing)

## Contributing
Contributions to improve the scripts or add new features are welcome. Please fork the repository and submit a pull request with your changes.
