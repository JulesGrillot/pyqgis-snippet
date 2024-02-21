import glob
from qgis.util import iface

# absolute path to search all text files inside a specific folder
path = r'D:\data\**\*.shp'
# Set recursive = True to check sub-folders
files = glob.glob(path, recursive=True)
# Add every shp to QgsProject with his name
for shp in files:
    file = shp.split('\\')[len(shp.split('\\')) - 1]
    name = file.split('.shp')[0]
    iface.addVectorLayer(shp, name, 'ogr')
