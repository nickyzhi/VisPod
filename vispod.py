import flask
from flask import Flask, request, redirect, url_for, jsonify, render_template
from werkzeug import secure_filename
from flask import send_from_directory
import os
from os import walk
import json
import numpy as np
from scipy import spatial
import textmining
import numpy as np
from pythonLibrary.rake import Rake
from pythonLibrary.rake_nltk import Rake_nltk
from pythonLibrary.texttiling import textTiling

UPLOAD_FOLDER = './static/uploadedfile'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'mp3', 'wav', 'flac'])


app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


    #         f = textTiling(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         data = f.run()
    # jsondata =  json.dumps(data)

@app.route('/<filename>')
def index(filename):
    [audioFile, transcriptFile] = filename.split("+")
    f = textTiling(os.path.join(app.config['UPLOAD_FOLDER'], transcriptFile))
    data = f.run()
    jsondata =  json.dumps(data)
    audioPath = os.path.join(app.config['UPLOAD_FOLDER'], audioFile)
    return render_template('index.html', data=jsondata, audioPath = audioPath)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("file[]")
        print files
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        for file in files:
            filename = secure_filename(file.filename)
            if "txt" in filename:
                transcriptFile = filename
            else:
                audioFile = filename
        returnFilesName = audioFile + "+" +transcriptFile
        return redirect(url_for('index', filename=returnFilesName))
            #return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')

# @app.route('/data')
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     print filename
#     f = textTiling(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     data = f.run()
#     jsondata =  json.dumps(data)
#     return jsondata



    

# @app.route("/data")
# @app.route("/data/<filename>")
# def data_process(filename):
#     f = datasetLDA(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     data = f.run()
#     return json.dumps(data)




if __name__ == "__main__":
    # Set up the development server on port 8000.
    app.debug = True
    app.run()