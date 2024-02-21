from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject

# Coordinate system
crs = 2154
# Geometry type
geom_type = "Polygon"
# Temporary layer with the right coordinate system and geometry type
new_layer = QgsVectorLayer(geom_type + "?crs=epsg:" + str(crs), "New layer", "memory")

# Polygon geometry, WKT format
poly = 'POLYGON((616126.30005647 6328318.90475043, 616126.30005647 6643794.60473103, 1037292.59974799 6643794.60473103, 1037292.59974799 6328318.90475043, 616126.30005647 6328318.90475043))'
# Create a QgsGeometry with the geometry
new_geom = QgsGeometry().fromWkt(poly)

# Create a new feature with the QgsGeometry
new_feature = QgsFeature()
new_feature.setGeometry(new_geom)

# Add the new feature to the temporary layer
new_layer.startEditing()
new_layer.dataProvider().addFeatures([new_feature])
new_layer.updateExtents()
new_layer.commitChanges()
new_layer.triggerRepaint()

# Add layer to QGIS project
QgsProject.instance().addMapLayer(new_layer)




