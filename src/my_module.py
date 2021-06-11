
import re
from . import hotels

def cheapest(busca : str) :

    hoteis = hotels.Hoteis()

    tipoCliente, dias = cleanString(busca)

    return hoteis.calculateCheapest(tipoCliente= tipoCliente,daysList= dias)
    

def cleanString(entrada : str) :
    isReward = True
    daylist = []

    divide = entrada.split(':')

    tipoCliente = divide[0]

    if tipoCliente == 'Regular':
        isReward = False

    pattern = "\(.*?\)"

    secondDivide = divide[1].split(',')

    for day in secondDivide:
        daylist.append(re.sub("[(,)]","",re.search(pattern, day).group()))


    return isReward, daylist



