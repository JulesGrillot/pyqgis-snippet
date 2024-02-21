from qgis.core import QgsDataSourceUri
from qgis.util import iface

# Service url
service_url = "https://wxs.ign.fr/administratif/geoportail/wfs"
# Data name
data = "ADMINEXPRESS-COG-CARTO.LATEST:arrondissement"
# Coordinate System
crs = "4326"

# Create the data source uri with parameters
uri = QgsDataSourceUri()
uri.setParam('service', 'wfs')
uri.setParam('version', 'auto')
uri.setParam('request', 'GetFeature')
uri.setParam('typename', data)
uri.setParam('srsName', crs)
uri.setParam('url', service_url)

# Add layer from the WFS
layer = iface.addVectorLayer(uri.uri(False), 'Some Data', 'WFS')
