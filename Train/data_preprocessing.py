import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from torchvision import transforms
from PIL import Image

def load_dataset(dataset_path):
    """
    Load dataset from the specified path.
    """
    data = pd.read_csv(dataset_path)
    return data

def clean_data(data):
    """
    Clean the dataset by handling missing values and removing duplicates.
    """
    data = data.dropna()
    data = data.drop_duplicates()
    return data

def augment_data(image):
    """
    Perform data augmentation on the given image.
    """
    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
        transforms.ToTensor()
    ])
    augmented_image = transform(image)
    return augmented_image

def preprocess_data(data, image_column):
    """
    Preprocess the dataset by applying data augmentation to images.
    """
    data[image_column] = data[image_column].apply(lambda x: augment_data(Image.open(x)))
    return data

def split_data(data, test_size=0.2, random_state=42):
    """
    Split the dataset into training and validation sets.
    """
    train_data, val_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, val_data

def save_preprocessed_data(train_data, val_data, output_dir):
    """
    Save the preprocessed training and validation data to the specified directory.
    """
    os.makedirs(output_dir, exist_ok=True)
    train_data.to_csv(os.path.join(output_dir, 'train_data.csv'), index=False)
    val_data.to_csv(os.path.join(output_dir, 'val_data.csv'), index=False)

if __name__ == "__main__":
    dataset_path = "path/to/dataset.csv"
    output_dir = "path/to/output_dir"
    image_column = "image_path"

    data = load_dataset(dataset_path)
    data = clean_data(data)
    data = preprocess_data(data, image_column)
    train_data, val_data = split_data(data)
    save_preprocessed_data(train_data, val_data, output_dir)
