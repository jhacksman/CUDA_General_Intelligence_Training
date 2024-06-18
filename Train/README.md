# Train Folder

This folder contains scripts necessary for training a general intelligence system. Below is an overview of the contents and instructions on how to use the scripts.

## Contents

### data_preprocessing.py
This script handles dataset loading and preprocessing. It includes functions for:
- Loading datasets from specified directories
- Preprocessing data to ensure it is in the correct format for training
- Splitting data into training, validation, and test sets

## Usage

### data_preprocessing.py
To use the `data_preprocessing.py` script, follow these steps:

1. Ensure you have the necessary dependencies installed. You can install them using the `requirements.txt` file located in the root directory of this repository:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Run the script with the appropriate arguments to load and preprocess your dataset. For example:
   ```bash
   python data_preprocessing.py --data_dir /path/to/dataset --output_dir /path/to/output
   ```

   - `--data_dir`: The directory containing the raw dataset.
   - `--output_dir`: The directory where the preprocessed data will be saved.

3. The script will preprocess the data and save the processed files in the specified output directory.

## Additional Information

For more details on the training process and other scripts that will be added to this folder, please refer to the main README.md file in the root directory of this repository.
