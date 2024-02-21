from qgis.utils import iface
from qgis.core import QgsVectorLayer

# Use active layer in layer tree
layer = iface.activeLayer()

## Selection based on id
# Select features with id 0 and 1
layer.selectByIds([0, 1])
