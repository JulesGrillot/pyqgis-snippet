from qgis.core import QgsProject

for layer in QgsProject.instance().mapLayers().values():
    pass  # do something
