# Human Action Recognition System

## Project Overview

This project implements a Human Action Recognition (HAR) system that classifies human actions such as clapping, running, and more from images. It uses deep learning techniques with transfer learning leveraging MobileNetV2, data augmentation to increase model robustness, and early stopping to prevent overfitting.

The system is deployed as a Streamlit web app where users can upload images and get real-time action predictions.

## Features

- Load and preprocess images from structured train/test folders.
- Uses MobileNetV2 as a pre-trained feature extractor with custom classification layers.
- Data augmentation applied to training images for better generalization.
- Dropout layers and early stopping callbacks to reduce overfitting.
- Streamlit app for user-friendly interaction.

## Dataset

The dataset contains approximately 300 images per class across 16 classes, split into train and test folders.

## Installation

### Prerequisites

- Python 3.8 or higher
- Conda or pip

### Setup Instructions

Clone the repo
git clone <your-repo-url>
cd <your-project-folder>

Create and activate environment
conda create -n actionrecognition python=3.8 -y
conda activate actionrecognition

Install dependencies
pip install -r requirements.txt

## Usage

### Train the Model

Run the training notebook or script to train the model with augmentation and early stopping:

python train_model.py


### Run Streamlit App

Launch the Streamlit app to test predictions on your images:
streamlit run app.py

Upload images via the web interface to see predicted actions.

## Model Performance

- Initial model training shows modest accuracy due to limited dataset size.
- Use of transfer learning, augmentation, and early stopping helps improve performance.
- Future improvements include dataset expansion, fine-tuning MobileNetV2, and experimenting with input sizes.
Upload images via the web interface to see predicted actions.

## Model Performance

- Initial model training shows modest accuracy due to limited dataset size.
- Use of transfer learning, augmentation, and early stopping helps improve performance.
- Future improvements include dataset expansion, fine-tuning MobileNetV2, and experimenting with input sizes.

## Future Work

- Collect larger and more diverse datasets.
- Fine-tune base model layers for better adaptation.
- Increase input image resolution for stronger feature extraction.
- Explore advanced architectures and multi-modal approaches.

## Contributing

Contributions, bug reports, and feature requests are welcome!

## License

Specify your license here.

## Contact

Your Name – omyadao1706@gamil.com  
Project Link: <>

