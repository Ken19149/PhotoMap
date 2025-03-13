import sys

sys.set_int_max_str_digits(231508122)

data = [("2015:03:23 20:02:06", 13.7927708,100.3236526, "name 2"),("2012:04:22 16:51:08",13.7927707,100.3234524, "test 1"), ("2022:02:22 22:22:22", 13.7905553,100.323847, "hello")] # fake data

# time = list(map(int, data[0][0].split(" ")[0].split(":") + data[0][0].split(" ")[1].split(":")))                  # [2012, 4, 22, 16, 51, 8]
# time = time[0]*365*24*60*60 + time[1]*30*24*60*60 + time[2]*24*60*60 + time[3]*60*60 + time[4]*60 + time[5]       # A VERY BIG NUMBER

# time = int(data[0][0].replace(" ","").replace(":",""))  # 20120422165108 # a smaller big number

# sort list by time
def timeIntSort(time):
    time = int(time[0].replace(" ","").replace(":",""))
    return time

data.sort(key=timeIntSort)
print([item[0] for item in data])
print([timeIntSort(item) for item in data])
print([timeIntSort(item) for item in data][-1] - [timeIntSort(item) for item in data][0]) # print newest time - oldest time

def rgb(hex):
    return tuple(int(hex.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

def hex(rgb):
    return '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])

print(hex((25,255,200)))

'''
// gradient colors
vars:
- from colorX -> colorY
- time range: newest time - oldest time
- number of photos // exclude none



'''
