from qgis.core import QgsVectorLayer, QgsProject, QgsSpatialIndex


# Function to create spatial index for a layer
def create_index(layer):
    index = QgsSpatialIndex()
    features = {}
    for feature in layer.getFeatures():
        features[feature.id()] = feature
        index.addFeature(feature)
    return index, features


# Add both layers, the one you're gonna select feature from
# and the one used for the comparison.
layer_selection_name = "batiment"
layer_intersection_name = "collectivite_territoriale"
layer_selection = QgsProject.instance().mapLayersByName(layer_selection_name)[0]
layer_intersection = QgsProject.instance().mapLayersByName(layer_intersection_name)[0]

# Create spatial index for the comparison layer
layer_intersection_index, layer_intersection_features = create_index(layer_intersection)

# Go through all feature of the layer you want to do the selection with
for layer_selection_feature in layer_selection.getFeatures():
    # Use the index created on the comparison layer to get the closest features
    layer_intersection_neighbour_ids = layer_intersection_index.intersects(
        layer_selection_feature.geometry().boundingBox()
    )
    # Search through the closest features of the comparison layer
    for layer_intersection_id in layer_intersection_neighbour_ids:
        # If both features intersects,
        # the feature from the selection layer is added to the selection
        layer_intersection_feature = layer_intersection_features[layer_intersection_id]
        if layer_selection_feature.geometry().intersects(
            layer_intersection_feature.geometry()
        ):
            layer_selection.selectByIds(
                [layer_selection_feature.id()], QgsVectorLayer.AddToSelection
            )
