# Human-Action-Recognition
Deep Learning-based Human Action Recognition using CNN and OpenCV
Project Overview
This project implements a Human Action Recognition system using deep learning techniques. It classifies human actions such as clapping, running, and other activities from images/videos. The system uses transfer learning with a MobileNetV2 backbone, enhanced by data augmentation and early stopping to improve model generalization.

Features
Data loading and preprocessing from structured folders.

Use of MobileNetV2 pre-trained model for transfer learning.

Data augmentation for improved variability and model robustness.

Dropout and early stopping to reduce overfitting.

Streamlit application for real-time image upload and action prediction.

Dataset
The dataset contains ~300 images per class, organized into 16 classes such as clapping, running, etc. Data is split into train and test folders for training and evaluation.

Installation
Prerequisites:
Python 3.8 or above

Conda or pip for environment management

Setup:
bash
# Clone repository
git clone <your-repo-url>
cd <your-project-folder>

# Create and activate virtual environment (using Conda)
conda create -n actionrecognition python=3.8 -y
conda activate actionrecognition

# Install dependencies
pip install -r requirements.txt
Running the Project
Training Model
Run your Jupyter notebook or Python script for training:

bash
python train_model.py
Streamlit App
To launch the web app for action recognition:

bash
streamlit run app.py
Upload an image to get predicted human action results.

Model Performance
The model achieved modest accuracy due to limited dataset size.

Data augmentation, transfer learning, and early stopping were used to improve robustness.

Expect gradual improvement with more data and fine-tuning.

Future Work
Increase dataset size with more diverse images.

Fine-tune MobileNetV2 by unfreezing layers for better task adaptation.

Experiment with larger image input sizes (96x96 or 224x224).

Add more augmentation techniques.

Explore alternative architectures and multimodal inputs.

Contributing
Anyone is welcome to contribute improvements or report issues.

License
Specify your license here.

Contact
Your Name – your.email@example.com
Project Link: <your-repo-url>
