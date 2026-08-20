import yaml
from yaml_manager import yaml_writer
import numpy as np
from typing import List


# read yaml file
def read_yaml(file_name):
    try:
        with open(file_name, 'r') as file:
            
            data = yaml.safe_load(file)
            return data
    except (yaml.YAMLError, FileNotFoundError) as e:
        raise ValueError(f"Error reading YAML file: {e}")

# load lights and speakers from yaml file
def load_config_lights(file_name):
    data = read_yaml(file_name)

    if not isinstance(data, list):
        raise ValueError("Invalid YAML format. Expected a list.")
    
    lights = []
    speakers = []
    lights_data = data[0]["lights"]
    speakers_data = data[1]["speakers"]
    
    # check if the id of the light is the same as the index
    for lightId, light in enumerate(lights_data):
        if lightId != light["id"]:
            ValueError(f"Exepected id {lightId}, got { light['id'] }")
        lights.append([light["x"], light["y"], light["z"]])
        
    # check if the id of the speaker is the same as the index
    for speakerId, speaker in enumerate(speakers_data):
        if speakerId != speaker["id"]:
            ValueError(f"Exepected id {speakerId}, got { speaker['id'] }")
        speakers.append([speaker["x"], speaker["y"], speaker["z"]])
    
    return (np.array(lights), np.array(speakers))
        
# load timeline from yaml file
def load_timeline(file_name):
    data = read_yaml(file_name)
    if not isinstance(data, list):
        raise ValueError("Invalid YAML format. Expected a list.")

    try:
        meta_data = {}
        for meta in data[0]["meta"][0]:
            meta_data[meta] = data[0]["meta"][0][meta]

    except KeyError:
        meta_data = None
        print("No meta data in timeline")

    try:
        parts = {}
        for part in data[1]["parts"][0]:
            parts[part] = data[1]["parts"][0][part]
    except KeyError:
        parts = None
        print("No parts in timeline")
    
    try :
        events = {}
        for event in data[2]["events"][0]:
            events[event] = data[2]["events"][0][event]
    except KeyError:
        events = None
        print("No events in timeline")
    
    return (meta_data, parts, events)


meta_data, parts, events = load_timeline(r"./yamls/w1.yaml")

######### BEGINNING MAIN ##################
lights, _ = load_config_lights(r"./yamls/3D_coordinates_device.yml")

import random
# generate random list of id of lights  with no duplicates
random_lights_id = random.sample(range(0, len(lights)), len(lights))

#add to yaml
ym = yaml_writer("where/rand")


for i in range(54):
    a = 1500
    for j in range(40):
        # Überprüfe, ob die Position des Lichts im Kreuzmuster gerade oder ungerade ist
        if a > 4000 and a < 5300 and i%2==0:
            ym.add(i, 4000, 255, 255, 255, 0, 0)
            ym.add(i, 5300, 0, 0, 0, 0, 1)
            a += (60/130*1000)
        elif a > 8000 and a < 9100 and i%2==0:
            ym.add(i, 7800, 255, 255, 255, 0, 0)
            ym.add(i, 9100, 0, 0, 0, 0, 1)
            a += (60/130*1000)
        elif a > 11400 and a < 12700 and i%2==0:
            ym.add(i, 11300, 255, 255, 255, 0, 0)
            ym.add(i, 12700, 0, 0, 0, 0, 1)
            a += (60/130*1000)    
        elif a > 15000 and a < 15800 and i%2==0:
            ym.add(i, 15000, 255, 255, 255, 0, 0)
            ym.add(i, 15800, 0, 0, 0, 0, 1)
            a += (60/130*1000)  
        
        else:
            if j % 2 == 0:
                # Wenn die Position gerade ist
                if i % 6 < 3:
                    ym.add(i, a, 120, 0, 200, 0, 0)  # Licht einschalten
                    ym.add(i, a+500, 0, 0, 0, 0, 1)   # Licht nach 0,5 Sekunden ausschalten
                else:
                    ym.add(i, a, 0, 0, 0, 0, 0)         # Licht ausschalten
                    ym.add(i, a+500, 120, 0, 0, 0, 1)  # Licht einschalten
            else:
                # Wenn die Position ungerade ist
                if i % 6 < 3:
                    ym.add(i, a, 0, 0, 0, 0, 0)         # Licht ausschalten
                    ym.add(i, a+500, 0, 0, 250, 0, 1)  # Licht einschalten
                else:
                    ym.add(i, a, 0, 0, 250, 0, 0)  # Licht einschalten
                    ym.add(i, a+500, 0, 0, 0, 0, 1)   # Licht nach 0,5 Sekunden ausschalten
            a += (60/130*1000)
        if a > 15800:
            break

#4000-5300
for i in range(54):
    a = 15800
    while a < 27000:
        if a < 17800:
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 220, 150, 230, 0, 0) # Licht einschalten 
                ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*1000)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+500, 0, 150, 230, 0, 1) # Licht einschalten
                a += (60/130*1000)
        if a > 17800 and a < 19500:
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 255, 0, 127, 0, 0) # Licht einschalten 
                ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*1000)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+500, 255, 0, 127, 0, 1) # Licht einschalten
                a += (60/130*1000)
  
        if a > 19500 and a < 23000:
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 123, 123, 255, 0, 0) # Licht einschalten
                ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*1000)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+500, 255, 0, 255, 0, 1) # Licht einschalten
                a += (60/130*1000)
        if a > 23000:
            #schwarz weiß
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 123, 123, 255, 0, 0) # Licht einschalten
                ym.add(i, a+300, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*500)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+300, 255, 0, 255, 0, 1) # Licht einschalten
                a += (60/130*500)

for i in range(54):
    a= 27000
    while a < 30750:
        if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
            ym.add(i, a, 255, 255, 255, 0, 0) # Licht einschalten
            ym.add(i, a+150, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
            a += (60/130*250)
        else:
            ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
            ym.add(i, a+150, 255, 255, 255, 0, 1) # Licht einschalten
            a += (60/130*250)
    ym.add(i, a, 0, 0, 0, 0, 0)

zeit = [30750, 31200, 31650, 31900, 32100, 32550, 33000, 33750, 34250, 34750, 35250, 36250, 36550]    

außenring = [0,1,2,3,4,5,6,12,18,24,30,36,42,48,49,50,51,52,53,47,41,35,29,23,17,11]
innenring = [7,8,9,10,16,22,28,34,40,46,45,44,43,37,31,25,19,13]
kleinring = [14,15,21,20,26,27,33,32,38,39]

for i in außenring:
    a=30750
    while a < 49250:
        if ((a > 33500 and a < 34750)or (a > 37000 and a < 38500)or (a > 40500 and a < 42000) or (a>44500 and a<45500)):
            ym.add(i, a, 255, 255, 255, 0, 0)
            ym.add(i, a+500, 0, 0, 0, 0, 1)
        else:
            ym.add(i, a, 0, 0, 255, 0, 0) # Licht einschalten
            ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
        a += (60/130*1000)
 
        
for i in innenring:
    a=30750
    while a < 49250:
        if ((a > 33500 and a < 34750)or (a > 37000 and a < 38500)or (a > 40500 and a < 42000) or (a>44500 and a<45500)):
            ym.add(i, a, 0, 0, 0, 200, 0)
            ym.add(i, a+500, 255, 255, 255, 0, 1)
        else:
            ym.add(i, a, 127, 0, 255, 0, 0) # Licht einschalten
            ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
        a += (60/130*1000)
    
        
for i in kleinring:
    a=30750
    while a < 50500:
        if ((a > 33500 and a < 34750)or (a > 37000 and a < 38500) or (a > 40500 and a < 42000) or (a>44500 and a<45500)):
            ym.add(i, a, 255, 255, 255, 0, 0)
            ym.add(i, a+500, 0, 0, 0, 0, 1)
        else:
            ym.add(i, a, 255, 51, 255, 0, 0) # Licht einschalten
            ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
        a += (60/130*1000)

for i in range(54):
    a=50500
    ym.add(i, a, 255, 255, 200, 0, 0)
    ym.add(i, a+500, 0, 0, 0, 0, 1)
    a=51000
    ym.add(i, a, 255, 255, 255, 0, 0)
    ym.add(i, 51300, 255, 102, 255, 0, 1)
    ym.add(i, 51700, 0, 0, 0, 0, 0)
    ym.add(i, 52500, 255, 255, 255, 0, 1)
        
for x in außenring:
    a=52600
    while a< 59900:
        ym.add(x, a, 255, 51, 255, 0, 0) # Licht einschalten
        ym.add(x, a+500, 0, 0, 0, 0, 1)
        a += (60/130*1000)
        
for x in innenring:
    a=52600
    while a< 59900:
        ym.add(x, a, 127, 0, 255, 0, 0) # Licht einschalten
        ym.add(x, a+500, 0, 0, 0, 0, 1)
        a += (60/130*1000)
        
for x in kleinring:
    a=52600
    while a< 59900:
        ym.add(x, a, 0, 0, 255, 0, 0) # Licht einschalten
        ym.add(x, a+500, 0, 0, 0, 0, 1)
        a += (60/130*1000)

a=59900
for i in range(5): #nicki minaj so many boys
    for y in range(6):
        ym.add((i*12)+y, a,0,0,255,0,0)
    a += (60/130*1000)
    if a >63400:
        break

for i in range(54): #ohohoh
    a=63400
    ym.add(i,a,0,20,255,0,0)
    ym.add(i,a+500, 0,0,0,0,1)
    ym.add(i,a+1000,0,20,255,0,1)
    ym.add(i,a+1100, 0,0,0,0,1)
    
a=64500
for i in range(5): #nicki minaj so many boys
    for y in range(6):
        ym.add((i*12)+y, a,0,20,255,0,0)
    a += (60/130*1000)
    if a >67400:
        break

for i in range(54): #ohohoh
    a=67400
    ym.add(i,a,0,20,255,0,0)
    ym.add(i,a+500, 0,0,0,0,1)
    ym.add(i,a+1000,0,20,255,0,1)
    ym.add(i,a+1100, 0,0,0,0,1)

a=68500   
for i in range(5): #nicki minaj so many boys
    for y in range(6):
        ym.add((i*12)+y, a,255,0,255,0,0)
    a += (60/130*1000)
    if a >71000:
        break
    
for i in range(54): #ohohoh
    a=71000
    ym.add(i,a,255,0,255,0,0)
    ym.add(i,a+500, 0,0,0,0,1)
    ym.add(i,a+1000,255,0,255,0,1)
    ym.add(i,a+1100, 0,0,0,0,1)

    
a=72100   
for i in range(5): #nicki minaj so many boys
    for y in range(6):
        ym.add((i*12)+y, a,255,0,0,0,0)
    a += (60/130*1000)
    if a >74750:
        break
    
for i in range(54):
    a = 74750 #15800
    while a < 85950:
        if a < 76750:
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 220, 150, 230, 0, 0) # Licht einschalten 
                ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*1000)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+500, 0, 150, 230, 0, 1) # Licht einschalten
                a += (60/130*1000)
        if a > 76750 and a < 78450:
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 255, 0, 127, 0, 0) # Licht einschalten 
                ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*1000)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+500, 255, 0, 127, 0, 1) # Licht einschalten
                a += (60/130*1000)
  
        if a > 78450 and a < 81950:
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 255, 0, 255, 0, 0) # Licht einschalten
                ym.add(i, a+500, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*1000)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+500, 123, 123, 255, 0, 1) # Licht einschalten
                a += (60/130*1000)
        if a > 81950:
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
                ym.add(i, a, 123, 123, 255, 0, 0) # Licht einschalten
                ym.add(i, a+300, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
                a += (60/130*500)
            else:
                ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
                ym.add(i, a+300, 255, 0, 255, 0, 1) # Licht einschalten
                a += (60/130*500)
                
for i in range(54):
    a= 85950
    while a < 90000:
        if i == 0 or i == 2 or i == 4 or i == 7 or i == 9 or i == 11 or i == 12 or i == 14 or i ==16 or i ==19 or i ==21 or i ==23 or i ==24 or i ==26 or i ==28 or i ==31 or i ==33 or i ==35 or i ==36 or i ==38 or i ==40 or i == 43 or i ==45 or i ==47 or i ==48 or i ==50 or i ==52:
            ym.add(i, a, 255, 255, 255, 0, 0) # Licht einschalten
            ym.add(i, a+150, 0, 0, 0, 0, 1) # Licht nach 0,5 Sekunden ausschalten
            a += (60/130*250)
        else:
            ym.add(i, a, 0, 0, 0, 0, 0) # Licht ausschalten
            ym.add(i, a+150, 255, 255, 255, 0, 1) # Licht einschalten
            a += (60/130*250)
    ym.add(i, a, 0, 0, 0, 0, 0)
    

            
    
    
        
        
    
        
    
#30750 hey
#31200 bring
#31650
#31900
#32100
#32550
#33000
#33750 bodyy
#34250bodyy
#34750
#35250
#36250
#36550

 
 

# Speichern der YAML-Datei
ym.write()
