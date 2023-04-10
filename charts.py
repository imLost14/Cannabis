import matplotlib.pyplot as plt
import numpy as np


def generate_pie_chart(labels, values):
  colores = ['green', 'gray', 'blue']
  fig, ax = plt.subplots()
  ax.pie(values, labels= labels, autopct='%.1f%%', colors = colores, shadow = True, startangle=90)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.set_ylabel('Raiting', color='black')
  ax.set_xlabel('Tipo de cannabis', color ='green', size =20)
  ax.bar(labels, values,width = 0.8, bottom = 0.1, edgecolor = "black", color = 'gray')
  ax.set_title('Raiting de tipo de Cannabis')
  plt.savefig('bar.png')
  plt.close()
  
  

  
