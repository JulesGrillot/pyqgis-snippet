from qgis.core import QgsProject

# Get the layer tree at root
root = QgsProject.instance().layerTreeRoot()

# Get desired group
group_name = ""
group = root.findGroup(group_name)

# Go through all elements of the group
for elem in group.children():
    # if element is a layer
    if elem.nodeType() == 1:
        layer = elem.layer()
        pass  # do something
    else:
        pass
