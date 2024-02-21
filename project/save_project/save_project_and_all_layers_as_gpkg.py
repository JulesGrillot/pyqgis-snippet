def saving_vector_gpkg(styled_layer, out_path):
    context = QgsProject.instance().transformContext()
    name = styled_layer.name()
    options = QgsVectorFileWriter.SaveVectorOptions()
    if os.path.isfile(out_path):
        options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer
    options.layerName = name
    options.fileEncoding = styled_layer.dataProvider().encoding()
    options.driverName = "GPKG"
    QgsVectorFileWriter.writeAsVectorFormatV2(styled_layer, out_path, context, options)
    doc = QDomDocument();
    readWriteContext = context = QgsReadWriteContext()
    styled_layer.exportNamedStyle(doc);
    gpkg_layer = QgsVectorLayer(f"{out_path}|layername={name}", name, "ogr")
    gpkg_layer.importNamedStyle(doc)
    gpkg_layer.saveStyleToDatabase(name, "", True, "")
    provider = gpkg_layer.providerType()
    options = gpkg_layer.dataProvider().ProviderOptions()
    styled_layer.setDataSource(f"{out_path}|layername={name}", name, provider, options)
 
def saving_raster_gpkg(raster, path):
    name = raster.name()
    renderer = raster.renderer()
    provider = raster.dataProvider()
    pipe = QgsRasterPipe()
    pipe.set(provider.clone())
    pipe.set(renderer.clone())
    file_writer = QgsRasterFileWriter(path)
    file_writer.Mode(1)
    file_writer.writeRaster(pipe, provider.xSize(), provider.ySize(), provider.extent(), provider.crs())
    gpkg_raster = QgsRasterLayer(f"{path}|layername={name}", name, "gdal")
    provider = gpkg_raster.providerType()
    options = gpkg_raster.dataProvider().ProviderOptions()
    raster.setDataSource(f"{path}|layername={name}", name, provider, options)
 
 
def analyze_group(group, vector_path, raster_path):
    for elem in group.children():
        if elem.nodeType() == 1:
            layer = elem.layer()
            if layer.providerType() == "ogr":
                saving_vector_gpkg(layer, vector_path)
            elif layer.providerType() == "gdal":
                saving_raster_gpkg(layer, raster_path)
        else:
            analyze_group(elem,  vector_path, raster_path)  # all layers of project


path = "/home/jgrillot/Documents/00_test/"
project_filename = "projet"
vector_filename = "vecteurs"
raster_filename = "rasters"


root = QgsProject.instance().layerTreeRoot()

group_name = ""
if group_name != "":
    group = root.findGroup(group_name)
    analyze_group(group, path + vector_filename + ".gpkg", path + raster_filename + ".gpkg")  # layers in a group
else:
   analyze_group(root, path + vector_filename + ".gpkg", path + raster_filename + ".gpkg") 

project_name = "gpkg_project_2"
uri = 'geopackage:{path}{filename}.gpkg?projectName={project_name}'.format(path=path, filename=project_filename, project_name=project_name)
QgsProject.instance().write(uri)
 
 