import pandas
import folium
import json


map = folium.Map(location=[23.379379,79.4433265],zoom_start=5,tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="COVID CASES")

df=pandas.read_csv("States.txt")
df1=pandas.read_csv("States_coord.txt")
data=df1.sort_values(by="Place Name")

States=list(df["State"])
States_coord=list(data["Place Name"])
Conf_cases=list(df["Confirmed Cases"])
Act_cases=list(df["Active Cases"])
Cur_cases=list(df["Cured/Discharged"])
Deaths=list(df["Death"])

html = """<h4>COVID INFO:</h4>
Name: %s<br>
Confirmed cases: %s<br>
Active cases: %s<br>
Cured Cases: %s<br>
Deaths: %s<br>

"""

states=sorted(States)
states_coord=sorted(States_coord)

lat=[]
lon=[]

for i in States:
    lat.append(data.loc[data["Place Name"]==i,"Latitude"].iloc[0])
    lon.append(data.loc[data["Place Name"]==i,"Longitude"].iloc[0])

def color_producer(dt,cfs):
    if float(dt/cfs)<0.01 :
        return 'green'
    elif float(dt/cfs)<0.02:
        return 'orange'
    else :
        return 'red'
 

for name,lt,ln,ac,cfs,crc,dt, in zip(states,lat,lon,Act_cases,Conf_cases,Cur_cases,Deaths):
    iframe = folium.IFrame(html=html % (name,cfs,ac,crc,dt), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln],radius=10, 
    popup=folium.Popup(iframe),fill_color=color_producer(dt,cfs),color='black',fill=True,fill_opacity=0.7))


map.add_child(fg)
map.save("covid_map.html")
 
 


    
    
