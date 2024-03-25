#imports for nn
import tensorflow as tf
import keras as kr
import numpy as np
#imports for flask
import flask as fl
from flask import render_template, request,flash, Markup
#imports for images
from PIL import Image
from scipy.misc import imresize, imread
import base64


app = fl.Flask(__name__)

@app.route("/")
def init():
    return render_template('index.html')

@app.route("/uploadfile", methods=['POST', 'GET'])
def uploadfile():

    #adapted from https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model
    #and https://github.com/tensorflow/serving/issues/310
    mnist = kr.models.load_model("./nn/keras_mnist_nn.h5")
    tensorflow_default = tf.get_default_graph()
    #adapted from https://www.tutorialspoint.com/flask/flask_file_uploading.htm
    photo = request.files['photo']
    photo.save("./temp/photototest.png")
    #tf.image.rgb_to_grayscale("./temp/photototest.png", name=None)
    #https://stackoverflow.com/questions/22351254/python-script-to-convert-image-into-byte-array
    image = imread("./temp/photototest.png")
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.imresize.html
    image = imresize(image,(28, 28))
    image = np.array(image).reshape(1, 784).astype(np.float32)
    image = image / 255

    with tensorflow_default.as_default():
        output = mnist.predict(image)
        #maxarg to pick from the numpy array https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.amax.html
        decision = np.array_str(np.argmax(output))

    return render_template('index.html', decision = decision)

if __name__ == "__main__":
    app.run(debug=True)