from qgis.utils import iface
from qgis.core import QgsVectorLayer

# Use active layer in layer tree
layer = iface.activeLayer()

## Selection based on attributes
# Attribute name
field_1 = 'FIELD1'
field_2 = 'FIELD2'

# Attribute value
value_1 = 'value1'
value_2 = 'value2'

# Create an expression with format
expr = "\"{field_1}\" = '{value_1}' AND \"{field_2}\" = '{value_2}'".format(field_1=field_1, value_1=value_1,
                                                                            field_2=field_2, value_2=value_2)
# Use the expression to select features
layer.selectByExpression(expr)
