# Land Cover Classification

The purpose of this process is to train a simple land cover classification model that is capable of classifing 5 different classes given a set of satellite images.

# 1. Introduction

The land cover classification repository contains two different directories; ___trainingModel___ and ___workingModel___. If you are not interested in training a new model then you should navigate to the workingModel directory as this directory conains all the necessary parts of running a land model classification on a local browser via Docker containers. However, if you are intersted to train your own model, then you should navigate to the trainingModel directory and their you can train your model by replacing the already existing images with your own images (read 2.1 for more details on making a training data set).

# 2. Model Training

In order to train land model classification, one needs a training set and a test set. The following sections show how a training set and a test set were created.

## 2.1 Training Dataset

The aim is to create a ___CSV___ file with 5 different columns in it including ___red___, ___green___, ___blue___, ___infrared___ intensities, and ___land cover type___. (See section 2.1.2 for more details on infrared intensity.) Each row in this CSV file represents a pixel. Each pixel belongs to the cropped out pieces of the satellite imageries. In the following the process of creating the CSV file will be explained.

### 2.1.1 Satellite Imagery Acquisition

All the acquired satellite imageries in this work were collected from [EO Browser](https://www.sentinel-hub.com/explore/eobrowser). However, for the purpose of this work the required satellite imageries are provided in the image directory.

### 2.1.2 Training Set, Test Set, and Model Preparation

In order to train a land cover classification model one needs a training dataset. To prepare your training and test datasets one has to run the first block and the second block of the notebook.

___Method 1___: ___ONLY___ uses the red, green, and blue intensity values of the images. While with this method a CSV table can be easily made it comes at the price of excluding infrared values. Lack of infrared data may result in a less accurate classification model. This may prove particularly true for classes such as vegetation and water where infrared can provide very distinctive values compared to other channels for the same classes. If this method is chosen, the user can simply download the AOI from the [EO Browser](https://www.sentinel-hub.com/explore/eobrowser) and download the image as a RGB image. Then, using a image editing tools (e.g. paint in windows) one can crop the different types of land cover from the original image and save them in a directory. Next, using a python library for image processing sush as ___PIL___ the user can read in the pixels of each cropped land type (e.g. vegetation, water) and add the RGB values to the CSV file along with the class of the pixel.

___Method 2___: Includes the infrared values too. If this method is chosen, the user needs to download the images (of the area to be classified) in the form of ___tiff___ images from the [EO Browser](https://www.sentinel-hub.com/explore/eobrowser). Note that unlike method 1 that there is only one true color image with three channels, in method 2 there needs to be one true color image and four different ___tiff___ images of the same aera each for one of the channels (as provided in the images directory???). (Note that to be able to download ___monochoromatic tiff___ images you need to create an account in EO Browser.) Similar to method 1, the areas of interest need to be cropped out of the original true color image and the cropped out areas should be collected and stored in a folder called ___cropped___.

Next, one has to use the ___trainingTest.py___ code. This code is only applicable to method 2! Also, note that this code contains all the training set, test set, and model preparation steps. In the first part, ___trainingTest.py___ reads in four monochoromatic images. Next, it uses the meta data of the tiff images and an ___affine___ matrix to build and assign a pair of ___longitude___ and ___latitude___ values to each and every single pixels of these images. These longitudes and latitudes, later, will be used to find a relation between the ord


# 2. Land Cover Classification Repository Tree

The following tree shows the contents of this repository, 

```bash
root(landCoverClassifiation)
|   
|___ /workingModel
|   |
|   |___ /templates
|   |    |___ index.html
|   |    |___ resutl.html
|   |
|   |___ /uploads
|   |    |___ .png images
|   |
|   |___ ml.py
|   |
|   |___ api.py
|   |
|   |___ visual.py
|   |
|   |___ convert.py
|   |
|   |___ model.pk
|   |
|   |___ Dockerfile
|   |
|   |___ requirements.txt
|      
|___/trainingModel
|   |
|   |___ landCover.ipynb
|   |
|   |___/trainingImage
|   |   |___some images for training
|   |
|   |___/testImage
|   |   |___some images for testing

```

Where in the following each of the contents is briefly explained.

## 2.1 Content Description

___templates___: Is a directory that contains two html files; ___index.html___ and ___result.html___. The two files are used in the ___api.py___ code to create an html page and give the ability to load the required images to run the classificatoin model. 

___uploads___: Is a directory that contains the images to be uploaded into our model via html page.

___api.py___: This file will provide the interface between our docker container and the user. It provides an html page where the usesd can upload images.

___model.pk___: This is our ___trained___ machine learning/land cover classification model. The ___.pk___ extension shows the model has been pickled to be transferable. (The pickling process has been done using the pcikle package in python.)

___Dockerfile___: This is the Dockerfile where we use to create an ubuntu 18.04 slim version. Once that ubuntu image has been created it will automatically set up a container with all the required specifications such as ability to connect to the local host. For dfurther information read the content of the Dockerfile.



# ??. Running the Model

Once you have downloaded/cloned the repository, use the ___Dockerfile___ to create the required docker image and then run the docker image to create the container. Next, just type in the browser "0.0.0.3000". This will connect you to the container. Then the an html page will pop up and asks you for your images to be uploaded. Up load your images and click on ___upload___ button. Once uploaded the images will be sent to the container where our classificaton model is. After a few minutes (depending on how big your image is) you willl receive a message stating "Processing done!". This means the classification is over. The user needs to remember that the image should be tranfered from the container to local machine as this process will not happen automatically. This can be done in two way SCP or mannually.



# 2. Satellite Imagery Acquisition

All the acquired satellite imageries in this work were collected from [EO Browser](https://www.sentinel-hub.com/explore/eobrowser). However, for the purpose of this work the processed satellite imageries are provided in the image repository.


# 3. Codes' Description


There are two ...
# 4. Docker Container


# 5. Python Flask

