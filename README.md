# Land Cover Classification

The purpose of this process is to train a simple land cover classification model that is capable of classifing 5 different classes given a set of satellite images..

# 1. Introduction

The land cover classification repository contains two different directories; ___trainingModel___ and ___workingModel___. If you are not interested in training a new model then you should navigate to the workingModel directory as this directory conains all the necessary parts of running a land model classification on a local browser through a Docker container. However, if you are intersted in training your own model, then you should navigate to the trainingModel directory and there you can train your model by replacing the already existing images with your own images (read 2.1 for more details on making a training data set).

# 2. Model Training

In order to train the land cover classification model, one needs a training set and a test set. Below you can find a short description of the processes through which a training set and a test set were prepared.

## 2.1 Satellite Imagery Acquisition

All the acquired satellite imageries in this work were collected from [EO Browser](https://www.sentinel-hub.com/explore/eobrowser). However, for the purpose of this work the required satellite imageries are provided in the ___trainingImage___ directory under the ___trainingModel___ directory (see 3 for file system structure of this repository).

## 2.2 Training Data Set

The aim is to create a ___CSV___ file with 5 different columns including ___red___, ___green___, ___blue___, ___infrared___ intensities, and ___land cover type___. (See section 2.1.2 for more details on infrared intensity.) Each row in this CSV file represents a pixel in the moochoromatic (single band/color) training images. Pixel values of all four images/bands are read simultaneously and stored in each row and column of the traingingSet.CSV file. For instance, the water image in the training directory contains 1265 x 810 pixels. This means at the end of the process there will be a dataframe with 1,024,650 (1265 x 810) rows each for a pixel and five columns of which four showing band intensities and the last one filled with letter ___w___ that stands for water. This process is done for five different classes of image each representing a land cover type.

### 2.3 Test Data Set

Test set preparation process is similar to the training set preparation process with the exception that there is no class column as we are going to predict the class of each pixel based on the given intensity values of each pixel (see 2.2. for more details on data set preparation process). The image used for test set preparation is stored in the ___testImage___ directory under the ___trainingModel___ directory (see 3 for file system structure of this repository).


# 3. Land Cover Classification Repository Tree

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

___templates___: is a directory that contains two html files; ___index.html___ and ___result.html___. The two files are used in the ___api.py___ code to create an html page and give the ability to load the required images to run the classificatoin model. 

___uploads___: is a directory that contains the images to be uploaded into our model via html page.

___api.py___: this file will provide the interface between our docker container and the user. It provides an html page where the usesr can upload their images. Once the images have uploaded by the user it calls the convert.py file for creating a dataframe out of the uploaded images. Once the dataframe is ready it will call the ml.py to run the trained land model calssification on the prepared dataframe. Finally, it will call the visual.py to create a semantic map of the uploaded images based on the output of the ml.py. 

___model.pk___: this is our ___trained___ machine learning/land cover classification model. The ___.pk___ extension shows the model has been pickled to be transferable. (The pickling process has been done using ___pickle___ package in python.) 

___Dockerfile___: this is the Dockerfile where we use to create an ubuntu 18.04 slim version. Once the ubuntu image has been created it will automatically set up a container with all the required specifications such as the ability to connect to the local host. For further information read the content of the Dockerfile (see 3 for the location of the Dockerfile).



## 4. Running the Model

Once you have downloaded/cloned the repository, use the ___Dockerfile___ to create the required docker image and then run the docker image to create the container. Next, just type in the browser "0.0.0.3000". This will connect you to the container. Then the an html page will pop up and asks you to upload your images. Up load your images and click on ___upload___ button. Once uploaded the images will be sent to the container where our classificaton model is running. After a few minutes (depending on how big your image is) you will receive a message stating "Processing done!". This means the classification is over. The user needs to remember that the image should be transfered from the container to local machine as this process will not happen automatically. This can be done in two way SCP or mannually (see the command below).

> docker_container_id scp path_to_image_in_docker_container path_to_desired_location_on_local_machine

> e.g. ===> 123456789f scp dev:/home/docker/foo.txt .

The above line in the example transfers ___foo.txt___ stored at ___dev:/home/docker/___ inside the container with the id ___123456789f___ to ___.___ the current directory on our local machine.


## 5. Performance

It
