from qgis.util import iface

# Type of WMTS, url and name
type = "xyz"
url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}.png"
name = 'ESRI World Imagery'

# Uri's creation based on type and url
uri = "type=" + type + "&url=" + url

# Add WMTS to the QgsProject
iface.addRasterLayer(uri, name, 'wms')
