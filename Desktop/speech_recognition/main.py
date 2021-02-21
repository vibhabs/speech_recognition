#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os
import speech_recognition as sr
import datetime
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import numpy as np
from PIL import Image, ImageOps
from scipy.ndimage import gaussian_gradient_magnitude

app = Flask(__name__)
r=sr.Recognizer()

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route('/index2', methods=['GET', 'POST'])
def index2():
	transcript = ""
	if request.method == 'POST':
		print("FORM DATA RECEIVED")

		if "file" not in request.files:
			return redirect(request.url)

		file = request.files["file"]
		if file.filename == "":
			return redirect(request.url)

		if file:
		
			recognizer = sr.Recognizer()
			audioFile = sr.AudioFile(file)
			with audioFile as source:
				r.adjust_for_ambient_noise(source)
				audio=r.record(source)
			transcript=r.recognize_google(audio)
		               
			filename= datetime.datetime.now()
			with open(filename.strftime("%d %B %Y")+".txt", "w") as file: 
				file.write(transcript)			
			file.close()
			file=open(filename.strftime("%d %B %Y")+".txt", "r") 
			text=file.read()
			print(text)
			print(r.recognize_google(audio))
			canvas_width=1920
			canvas_height=1080  
			wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
			wordcloud.to_file(filename.strftime("%d %B %Y")+".png")
			plt.imshow(wordcloud, interpolation='bilinear')
			plt.axis("off")
		
			
			
				
				

	return render_template('index2.html', transcript=transcript)
			


if __name__ == "__main__":
    app.run(debug=True)
