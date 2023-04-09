import matplotlib.pyplot as plt


def generate_pie_chart(labels, values):
  colores = ['green', 'gray', 'blue']
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels, colors = colores)
  ax.axis('equal')
  plt.show()


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.set_ylabel('Raiting', color='black')
  ax.set_xlabel('Tipo de cannabis', color ='green', size =20)
  ax.bar(labels, values,width = 0.8, bottom = 0.1, edgecolor = "black", color = 'gray')
  ax.set_title('Raiting de tipo de Cannabis')
  plt.show()