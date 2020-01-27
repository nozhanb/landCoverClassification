#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:48:03 2019

@author: nozhan
"""
import os
import ml 
import visual
import convert
import pathlib
from flask import Flask, flash, url_for, redirect
from flask import request
from flask import render_template
from werkzeug import secure_filename


#from visual import cityMap

api = Flask(__name__)
UPLOAD_FOLDER = pathlib.Path(uploads)
api.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@api.route('/', methods = ['GET', 'POST'])
def hello_worls():
    if request.method == 'GET':
            return render_template('index.html')
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        file  = request.files['file']
        if file == '':
            flash("No selected file")
            return redirect(request.url)
        images = request.files.getlist("file")

        for image in images:
            image.save(os.path.join(api.config['UPLOAD_FOLDER'], secure_filename(image.filename)))

        data, height, width = convert.data_frame()  #   The data_frame method goes to the uploads directory and fetches the images.
        print('-------------> Conversion Done!')
        y_pred = ml.map_ml(data)    #   This module and method will take the data and runs a pre-trained ML model.
        print('-------------> Prediction Done!')
        visual.city_map(y_pred, height, width)
        print('-------------> Map Creation Done!')
#               return render_template('result.html')
        return 'Files uploaded and mapping was done successfully!!!'

if __name__ == '__main__':
        api.run(debug=False, host = '0.0.0.0')
