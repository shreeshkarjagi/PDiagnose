#import libs
from imutils import paths
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from skimage import feature
import cv2
import numpy as np
import os

## func to extract Histogram of Oriented Gradients (HOG) (https://towardsdatascience.com/hog-histogram-of-oriented-gradients-67ecd887675f) features from an image
def hog_quantifier(image):
    features = feature.hog(image, orientations=9,
                           pixels_per_cell=(10, 10), cells_per_block=(2, 2),
                           transform_sqrt=True, block_norm="L1")
    return features

# func to preprocess and split images into data and labels
def processing_split(path):
    # get a list of image file paths in the specified directory
    imagePaths = list(paths.list_images(path))
    data = []  # list to store HOG features of images
    labels = [] # list to store corresponding labels
    for imagePath in imagePaths:
        # extract label from the file path
        label = imagePath.split(os.path.sep)[-2]
        # read image, convert to grayscale, resize, and apply thresholding
        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (250, 250), fx=0.5, fy=0.5)
        img = cv2.threshold(img, 0, 255,
                              cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        # extract HOG features and append to the data list
        features = hog_quantifier(img)
        data.append(features)
        labels.append(label)
    return (np.array(data), np.array(labels))


def train(data):
    model = RandomForestClassifier(random_state = 2)
    path = "/Users/shreeshkarjagi/Documents/PDiagnose/PDiagnose/drawings" + data
    trainingPath = os.path.sep.join([path, "training"])
    testingPath = os.path.sep.join([path, "testing"])
    if trainX.size == 0:
        print("No training data found or porcessing failed.")
        return None
    print("Shape of train:", trainX.shape)
    (trainX, trainY) = processing_split(trainingPath)
    
    (testX, testY) = processing_split(testingPath)
    encoder = LabelEncoder()
    trainY = encoder.fit_transform(trainY)
    testY = encoder.transform(testY)
    model.fit(trainX, trainY)
    print("Shape of trainY:", trainY.shape)
    predictions = model.predict(testX)
    accuracy = accuracy_score(testY, predictions)
    return model


def predictionTester(model, testingPath):    
    img = cv2.imread(testingPath)
    # The image being displayed still needs to be the original saved here
    # Converts images to greyscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (250, 250), fx=0.5, fy=0.5)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # Make prediction here as Normal or Abnormal
    modelsetter = hog_quantifier(img)
    prediction = model.predict([modelsetter])
    return prediction
