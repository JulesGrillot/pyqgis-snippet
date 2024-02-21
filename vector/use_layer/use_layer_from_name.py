from qgis.core import QgsProject

# Use the layer called data_layer
layer_name = "data_layer"
layer_selection = QgsProject.instance().mapLayersByName(layer_name)[0]
