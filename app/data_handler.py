import requests 

def get_character():
    r = requests.get('https://swapi.co/api/people/')
    data = str(r.json())
    print(data) 

get_character()
