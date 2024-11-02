# -*- coding: utf-8 -*-
"""ps03_Ishantha_Ex02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/153-Bhr8ATMZ_FVAjxow1TSIvqcutfBx2

Exercise 2: Creating and Customizing a Word Cloud Using Python

This script generates a word cloud from a text file using Python.
The WordCloud library is used to create a visual representation of the most frequently occurring words in the text. The script is designed to be run in Google Colab.

Step 1: Install the WordCloud library
"""

!pip install wordcloud

"""Step 2: Import necessary libraries"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

"""Step 3: Mount Google Drive
This step allows access to files stored in your Google Drive.
"""

from google.colab import drive
drive.mount('/content/drive')

"""Step 4: Load the text file from Google Drive"""

with open('/content/drive/MyDrive/BTU Lecture Materials /Winter 24 25/Conversational AI/JaneEyre.txt', 'r') as file:
    text = file.read()

"""Step 5: Create a WordCloud object"""

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    stopwords=set(STOPWORDS),
    min_font_size=10
).generate(text)

# Display the Word Cloud
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()