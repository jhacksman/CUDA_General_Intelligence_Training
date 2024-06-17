# CUDA General Intelligence Training

## Non-Synthetic Datasets for Training General Model

1. [HICO-DET: Human-Object Interaction Detection](https://paperswithcode.com/dataset/hico-det)
2. [V-COCO: Verbs in COCO](https://paperswithcode.com/dataset/v-coco)
3. [FineGym: Action Recognition Dataset](https://paperswithcode.com/dataset/finegym)
4. [RICH: Real scenes, Interaction, Contact and Humans](https://paperswithcode.com/dataset/rich)
5. [BEHAVE: Full Body Human-Object Interaction Dataset](https://paperswithcode.com/dataset/behave)
6. [HOI4D: Large-scale 4D Egocentric Dataset](https://paperswithcode.com/dataset/hoi4d)
7. [HICO: Humans Interacting with Common Objects](https://paperswithcode.com/dataset/hico)
8. [H2O: Human-to-Human-or-Object Interaction Dataset](https://paperswithcode.com/dataset/h2o)
9. [MPHOI-72: Multi-person Human-object Interaction Dataset](https://paperswithcode.com/dataset/mphoi-72)
10. [TREK-100: Video Sequences Dataset](https://paperswithcode.com/dataset/trek-100)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jhacksman/CUDA_General_Intelligence_Training.git
   cd CUDA_General_Intelligence_Training
   ```

2. **Install Anaconda or Miniconda**:
   Follow the official [Anaconda installation guide](https://docs.anaconda.com/anaconda/install/) or [Miniconda installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) to install Anaconda or Miniconda.

3. **Create and Activate Conda Environment**:
   Create a new conda environment specific to this project and activate it:
   ```bash
   conda create --name cuda_general_intelligence python=3.8
   conda activate cuda_general_intelligence
   ```

4. **Install Dependencies**:
   Ensure you have the following software and libraries installed:
   - **Operating System**: Ubuntu 20.04 LTS
   - **CUDA Toolkit**: Version 11.4
   - **TensorFlow**: Version 2.5
   - **PyTorch**: Version 1.9
   - **Hugging Face Transformers**: Version 4.9
   - **Diffusers**: Version 0.4
   - **JupyterLab**: Version 3.0
   - **Docker**: Version 20.10
   - **Git**: Version 2.32

   You can install these dependencies using the following commands:
   ```bash
   sudo apt update
   sudo apt install -y docker.io git
   pip install tensorflow==2.5 torch==1.9 transformers==4.9 diffusers==0.4 jupyterlab==3.0
   ```

## Environment Setup

1. **CUDA Toolkit**:
   Follow the official [CUDA Toolkit installation guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) to install CUDA 11.4.

2. **Docker**:
   Ensure Docker is installed and running. You can follow the official [Docker installation guide](https://docs.docker.com/engine/install/ubuntu/) for Ubuntu.

3. **Environment Variables**:
   Set up the necessary environment variables for CUDA:
   ```bash
   export PATH=/usr/local/cuda-11.4/bin${PATH:+:${PATH}}
   export LD_LIBRARY_PATH=/usr/local/cuda-11.4/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
   ```

## Running the Project

1. **Start JupyterLab**:
   Launch JupyterLab to interact with the project notebooks:
   ```bash
   jupyter lab
   ```

2. **Run Training Scripts**:
   Follow the instructions in the project notebooks to run the training scripts. Ensure you have the necessary datasets downloaded and placed in the appropriate directories.

3. **Docker Containers**:
   If using Docker, build and run the Docker containers as specified in the Dockerfile:
   ```bash
   docker build -t cuda_general_intelligence_training .
   docker run --gpus all -it cuda_general_intelligence_training
   ```

## Conclusion

The above instructions provide a comprehensive guide to setting up and running the CUDA General Intelligence Training project. Ensure all dependencies are installed, environment variables are set, and follow the steps to run the project successfully.
