#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
from docx import Document
import os

app = Flask(__name__)
# Max upload file size 16M
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def check_file(file) -> bool:
    return True

@app.route('/convert', methods=['POST'])
def convert():
    upload_files = request.files.getlist('file')
    if not upload_files:
        return jsonify({
            "code": -1,
            "message": "No upload file."
        })
        
    upload_file = upload_files[0]
    if upload_file.filename == '' or not check_file(upload_file):
        return jsonify({
            "code": -2,
            "message": "No vaild file."
        })
    upload_file.filename = secure_filename(upload_file.filename)
    f = pd.read_excel(upload_file)
    print(f)
    
    return jsonify({
        "file_name": upload_file.filename
    })