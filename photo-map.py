import folium
import pandas as pd
from exif import Image
import os

map = folium.Map(location=(13.7905553,100.323847), zoom_start=100) # muic

countries_border_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)
# folium.GeoJson(countries_border_url).add_to(map)

path = "photos\\"
data = [("2012:04:22 16:51:08",13.7927707,100.3234524, "test 1"),("2015:03:23 20:02:06", 13.7927708,100.3236526, "name 2"), ("2022:02:22 22:22:22", 13.7905553,100.323847, "hello")] # fake data

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref =='W' :
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def image_coordinates(image_path):
    try:
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
                # print ('No Coordinates')
                img_no_info += 1
                pass
        else:
            # print ('The Image has no EXIF information')
            img_no_info += 1
            pass

        return (img.datetime_original, coords[0], coords[1], str(image_path).split("\\")[-1])
        # return({"imageTakenTime":img.datetime_original, "geolocation_lat":coords[0],"geolocation_lng":coords[1]})
    except:
        pass
        # return ("0000:00:00 00:00:00", 0, 0, "name")
        # return({"imageTakenTime":"0000:00:00 00:00:00", "geolocation_lat":0,"geolocation_lng":0})

def timeIntSort(time):
    try: 
        time = int(time[0].replace(" ","").replace(":",""))
        return time
    except:
        return 0

img_no_info = 0
for i in os.listdir(path):
    try: 
        data.append(image_coordinates(path + i))
    except: 
        pass

def rgb(hex):
    return tuple(int(hex.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

def hex(rgb):
    return '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])

data.sort(key=timeIntSort)

print("Photos with no information: " + str(img_no_info)) # still not working
# print([item[0] for item in [x for x in data if x is not None]]) # print only time/first element & fake remove all none

for i in data:
    try: 
        popup = "<div><img src=\"" + (path + "\\" +i[3]) + "\" alt=\"" + i[3] + "\" width=\"230\" height=\"172\"><br /><span>" + i[3] + "</span></div>"
        folium.CircleMarker(location=[i[1], i[2]],radius=15,weight=5, opacity=1, fill_opacity=0.6, fill=True,color="#00ffff80" , popup=popup, tooltip=str(i[0] + " : " + i[3])).add_to(map)
    except:
        pass


#Set the zoom to the maximum possible
map.fit_bounds(map.get_bounds())


map.save("index.html")
