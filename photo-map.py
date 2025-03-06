import folium
import pandas as pd
from exif import Image

map = folium.Map(location=(13.7905553,100.323847), zoom_start=100) # muic

countries_border_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)
# folium.GeoJson(countries_border_url).add_to(map)

data = [("2012:04:22 16:51:08",13.7927707,100.3234524),("2015:03:23 20:02:06", 13.7927708,100.3236526), ("2022:02:22 22:22:22", 13.7905553,100.323847)]

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref =='W' :
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def image_coordinates(image_path):

    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
        except AttributeError:
            print ('No Coordinates')
    else:
        print ('The Image has no EXIF information')

    return({"imageTakenTime":img.datetime_original, "geolocation_lat":coords[0],"geolocation_lng":coords[1]})

# image_coordinates('Your image path')

for i in data:
    folium.CircleMarker(location=[i[1], i[2]],radius=2,weight=5, opacity=1, fill_opacity=0.6, fill=True, tooltip=i[0]).add_to(map)


#Set the zoom to the maximum possible
map.fit_bounds(map.get_bounds())


map.save("footprint.html")
