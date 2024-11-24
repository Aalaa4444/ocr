# Arabic OCR Model

This ocr_pytorch folder contains code for building and training an Optical Character Recognition (OCR) model to recognize Arabic letters and numbers using deep learning techniques. The model is based on a ResNet-inspired architecture and trained on an Arabic dataset containing characters and numbers.

## Requirements
You can install the required dependencies using pip:

```bash
pip install torch torchvision numpy matplotlib opencv-python scikit-learn seaborn
```
## Results
The model achieves the following performance on the test set:

* Test Accuracy: 99.70%
  * with only 10 epochs

## Code Overview
1. Dataset Preprocessing:
The ArabicDataset class loads and processes images from the dataset, converts them to grayscale, resizes them to a target size (32x32), and normalizes the images. Each image is assigned a label corresponding to its Arabic character.

2. Model Architecture:
The ArabicOCRModel is a Convolutional Neural Network (CNN) inspired by ResNet. It includes convolutional layers, batch normalization, residual blocks, and fully connected layers to classify the input images into one of the Arabic characters.

3. Training:
The model is trained using the Adam optimizer and cross-entropy loss. The training process includes validation and evaluation after each epoch, with the goal of achieving high accuracy on the validation set.

4. Evaluation:
After training, the model is tested on a separate test set to evaluate its accuracy. The classification report and confusion matrix are generated using sklearn.metrics to provide insights into the model's performance.

## Dataset

The dataset used in this project consists of images of Arabic letters and numbers. The dataset is organized in directories named after each character, where each image corresponds to a single Arabic character or number.     

## Conclusion
The model successfully recognizes Arabic letters and digits with high accuracy. It demonstrates strong performance on the test dataset, making it suitable for use in Arabic OCR applications.

## Acknowledgements
* The dataset used in this project is publicly available and can be found at <a href="https://www.kaggle.com/datasets/mahmoudreda55/arabic-letters-numbers-ocr/data" target="_blank">Kaggle</a>.
