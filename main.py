import utils
import read_Cannabis
import charts
import collections



    
    #charts.generate_pie_chart(types, repeat)

if __name__ == '__main__':
    data = read_Cannabis.canna_csv('/home/hector/platzi/fundamentospython/my_proyect1/cannabis.csv')
    tipos, raiting = utils.get_raiting_type(data)
    #charts.generate_bar_chart(tipos, raiting)
    charts.generate_pie_chart(tipos, raiting)