
class _hotelBase:



    def __init__(self,
    name : str, 
    classification,
    taxaSemanaNorm, 
    taxaFdsNorm,
    taxaSemanaReward, 
    taxaFdsReward):
        self.taxaNorm = []
        self.taxaReward = []
        self.name = name
        self.classification = classification
        self.taxaNorm.append(taxaSemanaNorm)
        self.taxaNorm.append(taxaFdsNorm)
        self.taxaReward.append(taxaSemanaReward)
        self.taxaReward.append(taxaFdsReward) 
    
    def __str__(self):
        return self.name
    
    def calculatePrice(self, daysList,isReward : bool):
        pricePerDay = []

        if isReward:  
                pricePerDay = self.taxaReward 
        else: 
                pricePerDay = self.taxaNorm

        price = 0
        for day in daysList:
            if( day == 'sun' or day == 'sat'):
                price += pricePerDay[1]
            else:
                price += pricePerDay[0]

        return price


class Hoteis:

    LAKEWOOD =_hotelBase("Lakewood", 3,110,90,80,80)
    BRIDGEWOOD = _hotelBase("Bridgewood", 4,160,60,110,50)
    RIDGEWOOD = _hotelBase('Ridgewood',5,220,150,100,40)

    hotelList = [BRIDGEWOOD,RIDGEWOOD,LAKEWOOD]

    
    def calculateCheapest(self,tipoCliente, daysList):
        cheapestone = _hotelBase("dummy",0,0,0,0,0)
        price = 99999
        for hotel in self.hotelList:
            instancePrice = hotel.calculatePrice(daysList= daysList,isReward=tipoCliente)
            if instancePrice < price:
                price = instancePrice
                cheapestone = hotel
                
        print(cheapestone)
        return cheapestone.name
