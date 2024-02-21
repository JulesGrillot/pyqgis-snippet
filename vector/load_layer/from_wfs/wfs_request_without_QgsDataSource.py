from urllib import request, parse
import json
from qgis.core import QgsVectorLayer, QgsProject

# Service url
service_url = "https://wxs.ign.fr/administratif/geoportail/wfs"
# Data name
data = "ADMINEXPRESS-COG-CARTO.LATEST:arrondissement"
# Coordinate System
crs = "4326"
# Rectangle coordinate
boundingbox = [2.0, 46.8, 7.1, 44.1]

# Wfs url
url = '{service_url}?VERSION=2.0.0&TYPENAMES={data}&SRSNAME=EPSG:{crs}&BBOX={xmax},{xmin},{ymax},' \
      '{ymin}&request=GetFeature&outputFormat=json'.format(service_url=service_url, data=data, crs=crs,
                                                           xmax=str(boundingbox[3]), xmin=str(boundingbox[0]),
                                                           ymax=str(boundingbox[1]), ymin=str(boundingbox[2]))

# Request
req = request.Request(url, method="POST")
r = request.urlopen(req)
content = r.read().decode('utf-8')

# Add Layer
layer = QgsVectorLayer(content, "Some Data", "ogr")
QgsProject.instance().addMapLayer(layer)
