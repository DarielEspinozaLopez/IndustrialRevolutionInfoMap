import folium
from folium import plugins
import openrouteservice
from ClientKey import ClientKey


m = folium.Map(
    location=[38.906067936823035, -77.02786521292094],
    zoom_start=6
)

folium.TileLayer(tiles='OpenStreetMap', name='Default').add_to(m)
folium.TileLayer(tiles='CartoDB positron', name='Clean Base').add_to(m)
folium.TileLayer(tiles='CartoDB dark_matter', name='Dark Base').add_to(m)
folium.LayerControl().add_to(m)

folium.Marker(
    location=[42.3314, -82.0458],
    popup="Detroit, Michigan",
    icon=folium.Icon(color='red', icon='cloud')
).add_to(m)

folium.Marker(
    location=[40.4406, -79.9959],
    popup="Pittsburgh, Pennsylvania",
    icon=folium.Icon(color='green', icon='cloud')
).add_to(m)

folium.Marker(
    location=[41.8781, -87.6298],
    popup="Chicago, Illinois",
    icon=folium.Icon(color='green', icon='cloud')
).add_to(m)

folium.Marker(
    location=[40.7128, -74.0060],
    popup="New York City, New York",
    icon=folium.Icon(color='red', icon='cloud')
).add_to(m)

folium.Marker(
    location=[38.906067936823035, -77.02786521292094],
    popup="Destination",
    tooltip="This allows for further information concerning a particular location to be displayed",
    icon=folium.Icon(color="lightblue", icon_color="black", angle=180, icon="cloud"),
    draggable=True
).add_to(m)

folium.plugins.AntPath(
    locations=[[40.7128, -74.0060], [38.906067936823035, -77.02786521292094]],
    color='red',
    pulse_color='yellow',
    weight=5,
    delay=1000
).add_to(m)

client = openrouteservice.Client(key=ClientKey)
cords = [[-74.0060, 40.7128], [-77.02786521292094, 38.906067936823035]]
routes = client.directions(coordinates=cords, profile='driving-car', format='geojson')

geometry = routes['features'][0]['geometry']['coordinates']

route_lines = [[lat, lng] for lng, lat in geometry]

folium.PolyLine(
    locations=route_lines,
    color='blue',
    weight=5,
    opacity=0.8
).add_to(m)


# Save output
m.save('Testing.html')
