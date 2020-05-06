import folium
import pandas


map = folium.Map(location = [31.430646, 74.288592],tiles="Stamen Terrain", zoom_start=4)
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name = "Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
     fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=el, fill = True, fill_color = color_producer(el), fill_opacity = 0.7))
print(data)

fgp = folium.FeatureGroup(name = 'Population')
# adding polygon layer
# This will change color of polygon if population of countries is given below
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'} ))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map.html")

