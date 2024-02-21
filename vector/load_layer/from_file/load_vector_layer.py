from qgis.utils import iface

# Path to the layer
path = r"D:\data\shape"
# layer file name with extension
layer_file = "data.shp"

# layer name to show in QGIS, file name minus the extension
layer_file_element = layer_file.split(".")
layer_file_element.pop(-1)
layer_name = '.'.join(layer_file_element)

# Add layer to QGIS Project
iface.addVectorLayer(path + '/' + layer_file, layer_name, 'ogr')
