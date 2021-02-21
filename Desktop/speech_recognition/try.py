import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import datetime
from scipy.ndimage import gaussian_gradient_magnitude
filename= datetime.datetime.now()
file=open(filename.strftime("%d %B %Y")+".txt", "r") 
text=file.read()
canvas_width=1920
canvas_height=1080  
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png")
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
"""plt.show()"""



