import collections
import charts
import read_Cannabis

def get_raiting_type(datos):
    '''
    type = input('Quieres saber cual es el tipo de cannabis que hay mas => ')
    datos = list(filter(lambda item : item['Type']for item in datos))
    types = [item(collections.Counter([datos])) for item in datos]
    ratios = [float(item[types])for item in datos]
    return types, ratios 
    '''
    percentages_dict= {item["Type"]: float(item["Rating"]) for item in datos}

    names = percentages_dict.keys()
    per = percentages_dict.values()

    return names, per
if __name__ == '__main__':
    data = read_Cannabis.canna_csv('/home/hector/platzi/fundamentospython/my_proyect1/cannabis.csv')
    types, porcentajes = get_raiting_type(data)
    charts.generate_pie_chart(types, porcentajes)
    