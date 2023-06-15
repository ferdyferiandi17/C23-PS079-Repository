
from flask import Flask, request, jsonify
from keras.models import load_model

import tensorflow as tf
from tensorflow import keras
from skimage import transform, io
import numpy as np
import os
from PIL import Image
from datetime import datetime
from keras.preprocessing import image
from flask_cors import CORS
import keras.utils as image

app = Flask(__name__)

# load model for prediction
modelnasnet = load_model("acnelevel.h5")



UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tiff', 'webp', 'jfif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/ping', methods=['GET'])
def main():
    return jsonify(message='Hello, World!')

@app.route('/submit', methods=['POST'])
def predict():
    if 'file' not in request.files:
        resp = jsonify({'message': 'No image in the request'})
        resp.status_code = 400
        return resp
    files = request.files.getlist('file')
    filename = "temp_image.png"
    errors = {}
    success = False
    for file in files:
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors["message"] = 'File type of {} is not allowed'.format(file.filename)

    if not success:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp
    img_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # convert image to RGB
    img = Image.open(img_url).convert('RGB')
    now = datetime.now()
    predict_image_path = 'static/uploads/' + now.strftime("%d%m%y-%H%M%S") + ".png"
    image_predict = predict_image_path
    img.convert('RGB').save(image_predict, format="png")
    img.close()

    # prepare image for prediction
    img = image.load_img(predict_image_path, target_size=(128, 128, 3))
    x = image.img_to_array(img)
    x = x/127.5-1 
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    # predict
    prediction_array = modelnasnet.predict(images)
 

    # prepare api response
    class_names = ['level_1', 'level_2', 'level_3', 'level_4']
    result = {
        "prediction": class_names[np.argmax(prediction_array)],
        "confidence": '{:2.0f}%'.format(100 * np.max(prediction_array))
    }

    return jsonify(isError=False, message="Success", statusCode=200, data=result), 200
   


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
