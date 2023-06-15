from qgis.core import QgsSpatialIndex
from qgis.util import iface


# Function to create spatial index for a layer
def create_index(layer):
    index = QgsSpatialIndex()
    features = {}
    for feature in layer.getFeatures():
        features[feature.id()] = feature
        index.addFeature(feature)
    return index, features


# Use active layer
layer = iface.activeLayer()
# Create spatial index for the layer
layer_index, layer_features = create_index(layer)
