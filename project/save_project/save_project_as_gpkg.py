path = "/home/jgrillot/Documents/00_test/"
filename = "test"
project_name = "gpkg_project"

uri = 'geopackage:{path}{filename}.gpkg?projectName={project_name}'.format(path=path, filename=filename, project_name=project_name)
QgsProject.instance().write(uri)
