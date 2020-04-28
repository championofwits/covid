import requests
from bs4 import BeautifulSoup





##gt covid data daily
def get_covid_country(country):
    site = "https://www.worldometers.info/coronavirus/country/" + country

    source = requests.get(site).text
    soup = BeautifulSoup(source,'lxml')
    c1 = soup.find('div',class_='maincounter-number')
    k = c1.text
    k = str(k.strip().replace(',',''))
    return (int(k))

#c1 = get_covid_country("India")
#c2 = get_covid_country("us")
#c3 = get_covid_country("china")
#print(c1,c2,c3)


def get_sensex():
    site = "https://www.moneycontrol.com/indian-indices/sensex-4.html"
    source = requests.get(site).text
    soup = BeautifulSoup(source,'lxml')
    k1 = soup.find('span',class_='lastprice')
    k = str(k1.text).strip()
    return(float(k))


def curr_comp(curr1,curr2):
    site = "https://api.exchangeratesapi.io/latest?sy=" 
    source = requests.get(site+curr1+","+curr2).json
    return(source)




