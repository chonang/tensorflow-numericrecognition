# tensorflow-numericrecognition
# Tensorflow-Project-Numeric-Recognition
A Numeric Recognition API to recognize user input (Images of handwritten numbers)

#### chonang
Web application with neural network backend for Emerging technologies module, 4th Year software. 

## Project Overview
The application ive developed was designed to create a model based on the input from the MNIST data set and take the user input of an image. It would then attempt to predict the number within the image.
Developed using **Python**, **Keras** , **Tensorflow** and **Jupyter notebooks**, and with the libraries **Flask** for http requests and routing,and **Bootstrap** for user experience.

## Installation Guide
To run this application You will first have to install Python on your windows machine, The package I used was Anaconda 3.5.
You can install Anaconda from [here](https://www.continuum.io/downloads)

Once Python is installed on your machine you will need to install the necessary modules
`
python -m pip install --upgrade pip
`

install flask
`
python pip install Flask
`

install tensorflow
`
python pip install tensorflow
`

install keras
`
python pip install keras
`


install jupyter notebooks
`
python pip install jupyter
`


Now that Flask ,tensorflow and jupyter notebook are installed on your machine you will be able to load the project.
Id advise creating a folder somewhere on your machine and cloning the repository directly from github.
To do that go to that directory
and run this command
`
git clone https://github.com/JohnnyGlynn/Tensorflow-Project-Numeric-Recognition
`
It will clone the entire project to the currently in use directory.

Now, thanks to Keras, the model is quite small so i was able to upload that to github without issues, unlike the behemoth sized models that were being output by tensorflow, I've left all of the notebooks in to demonstrate my work, but id hightly recomend not running either of the tensorflow ones due to their increible ability to be really really slow and to partially computer ventilation systems.


Now, set up flask
`
set FLASK_APP=app.py
`
, this will instance the app.py variable for you so all you have to do is run
`
flask run
`
Now that the python script is running you can use the application at the following address [http://127.0.0.1:5000/]
