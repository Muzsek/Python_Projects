import requests
import json
ISS_url = "http://api.open-notify.org/iss-now.json"


#Not ready yet
def ISS_test() -> None:
    try:
        ISS_req = requests.get(ISS_url)
        print("Requesting from URL: " + ISS_req.reason)
        data = ISS_req.json()
        #clean_data = json.dumps(data,indent=4,ensure_ascii=False) # String, only for visualization
        # {'timestamp': 1766868387, 'iss_position': {'longitude': '-123.5724', 'latitude': '-37.2624'}, 'message': 'success'}
        longitude = data['iss_position']['longitude']
        latitude = data['iss_position']['latitude']
        print(f"Langitude: {data['iss_position']['longitude']}") 
        print(f"Latitude: {data['iss_position']['latitude']}")

        # 2. LÉPÉS: Koordináta átváltása helyszínné (Nominatim API)
    # Fontos: A 'format=json' mondja meg, hogy milyen formátumban kérjük az adatot
        geo_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
        
        # Itt adjuk meg a User-Agentet, hogy tudják, ki kérdez (bármilyen nevet írhatsz)
        fejlec = {'User-Agent': 'SajatISSKovetoApp/1.0'}
        
        geo_valasz = requests.get(geo_url, headers=fejlec).json()

        # 3. LÉPÉS: Az eredmény megjelenítése
        # Mivel az ISS gyakran van az óceán felett, nem biztos, hogy lesz címe
        if 'address' in geo_valasz:
            cim = geo_valasz['display_name']
            print(f"Az ISS éppen e felett jár: {cim}")
        else:
            # Ha nincs a közelben szárazföld, az API nem ad vissza 'address' kulcsot
            print("Az ISS jelenleg az óceán vagy lakatlan terület felett jár.")
    except Exception as e:
        print("Error: "+ e)
if __name__ == "__main__":
    ISS_test()