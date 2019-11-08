import re
from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Range1d, PanTool, WheelZoomTool, Circle


def map_plotting():
    file = open('message_new_pen.txt')
    patter = re.compile(r'[-]?[\d]+.[\d]+')
    string = file.read()
    count = 0
    longtitude = []
    latitude = []
    for match in re.finditer(patter, string):
        if count % 2 == 0:
            latitude.append(match.group())
        else:
            longtitude.append(match.group())
        count += 1
    file.close()

    map_options = GMapOptions(lat=0, lng=0, zoom=3)
    plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
    plot.title.text = 'Mission Violet'
    plot.api_key = 'AIzaSyDqEjjYJHbEMAjw-tx1PCFv93E_imu1wvQ'
    source = ColumnDataSource(data=dict(lat=latitude, lon=longtitude))
    circle = Circle(x='lon', y='lat', size=15, fill_color='red')
    plot.add_glyph(source, circle)
    plot.add_tools(PanTool(), WheelZoomTool())
    output_file('Mission Violet.html')
    show(plot)

from cryptography.fernet import Fernet
import hashlib
import base64
def decrypt():
    key_word =b'TRUTH'
    key = hashlib.sha3_256(key_word)
    key_bytes = key.digest()
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    cipher = Fernet(fernet_key)
    text = b'gAAAAABaUXStIpjRWJTrbWGOB45IyRpbb8Zyl1sdktcSeOL0zpH-_Oxd2nXVjeph_fGybthCci75lTd0z5SycthFo-5uoFxZqeBTdDc_n9uq3FdZk75gYFAWIRSGlAqlBQlcqkNhVx3W3w7rTaCAhCrHijeyTtxq53S3ab6fLHUw3KPHx2LtdurISe5ArhrmG9IOepnzGzBBTaTgCfoAmbITCWbp_5cdQQ=='
    print(cipher.decrypt(text))

decrypt()