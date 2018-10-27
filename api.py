def currencyConverter(country,money,conversionFactor):
    import requests
    webd=requests.get("https://restcountries.eu/rest/v2/all")
    data=webd.json()
    count=0
    for item in range(len(data)):
        if data[item]["name"].lower()==country.lower() or country.title() in data[item]["altSpellings"]:
            cd=data[item]["currencies"][0]["code"]
            symb=data[item]["currencies"][0]["symbol"]
            conv=money*conversionFactor
            conv=round(conv,2)
            count+=1
    if count!=1:
        return "{} is not a valid country.".format(country)
    else:
        return "In {}, ${} USD is worth {}{} {}.".format(country,money,symb,conv,cd)

def translator(codeList):
    import requests
    webd=requests.get("https://restcountries.eu/rest/v2/all")
    data=webd.json()
    newdict={}
    for item in codeList:
        for num in range(len(data)):
            if data[num]["alpha3Code"].lower()==item.lower():
                a=data[num]["name"]
                b=data[num]["languages"][0]["iso639_1"]
                c=data[num]["translations"][b]
                newdict[a]=c
    return newdict

def nearbyLocations(codeList):
    import requests
    list1=[]
    list2=[]
    list3=[]
    count=0
    num1=0
    codeList=sorted(codeList,reverse=True)
    for item in codeList:
        tup=()
        webd=requests.get("https://restcountries.eu/rest/v2/all")
        data=webd.json()
        for num in range(len(data)):
            if data[num]["alpha3Code"].lower()==item.lower():
                list1.append(data[num]["borders"])
        for i in range(len(list1)):
            if len(list1[i])>count:
                count=len(list1[i])
                num1=i
        list2=list1[num1]
    for element in list2:
        tup=()
        webd=requests.get("https://restcountries.eu/rest/v2/all")
        data=webd.json()
        for num in range(len(data)):
            if data[num]["alpha3Code"].lower()==element.lower():
                tup+=data[num]["latlng"][0],data[num]["latlng"][1]
        list3.append(tup)
    return list3

def humidityCheck(locationList,maxHumidity):
    import requests
    list1=[]
    for city in locationList:
        webd=requests.get("https://api.openweathermap.org/data/2.5/weather?id="+str(city)+"&APPID=91ad2aac3c6eedf805c30109bc807d56")
        data=webd.json()
        try:
            if data["main"]["humidity"]<maxHumidity:
                list1.append(data["name"])
        except:
            return "{} is not a valid ID.".format(city)

    return list1 
                

def locationTemps(coordinatesList):
    import requests
    newlist=[]
    for item in coordinatesList:
        tup=()
        webd=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(item[0])+"&lon="+str(item[1])+"&APPID=91ad2aac3c6eedf805c30109bc807d56")
        data=webd.json()
        a=data["name"]
        temp=data["main"]["temp"]
        tup+=a,temp
        newlist.append(tup)
    return sorted(newlist, key=lambda tup:tup[1])

def typesOfWeather(locationList):
    import requests
    newdict={}
    for city in locationList:
        try:
            webd=requests.get("https://api.openweathermap.org/data/2.5/weather?id="+str(city)+"&APPID=91ad2aac3c6eedf805c30109bc807d56")
            data=webd.json()
            wtype=data["weather"][0]["main"]
            if wtype not in newdict:
                newlist=[]
                newlist.append(data["name"])
                newdict[wtype]=newlist
            else:
                newdict[wtype].append(data["name"])
        except:
            return "{} is not a valid ID.".format(city)
    return newdict

    





                
            
       
        
        
                
        
                

                                    
