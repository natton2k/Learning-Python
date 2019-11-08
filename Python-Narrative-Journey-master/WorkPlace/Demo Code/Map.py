import csv

f = open('countries.csv')
map = csv.reader(f)
latitude = []
longtitude = []
for country, lat, long, name in list(map)[1:]:
    latitude.append(float(lat))
    longtitude.append(float(long))

from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool

map_options = GMapOptions(lat=0, lng=0, zoom=3)
plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = 'Example Plot'
plot.api_key = 'AIzaSyDqEjjYJHbEMAjw-tx1PCFv93E_imu1wvQ'
source = ColumnDataSource(data=dict(lat=latitude, lon=longtitude))
circle = Circle(x='lon', y='lat', size=15, fill_color='red')
plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file('abc.html')
show(plot)
