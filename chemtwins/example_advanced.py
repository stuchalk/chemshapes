""" code to validate jsonld using shacl """
from pyshacl import validate
from os import path

data_file = '../static/twins/ethanal_min.jsonld'
data_file = path.abspath(data_file)
data_file_format = 'json-ld'

shapes_file = 'ShapesChemTwinAdvanced.ttl'
shapes_file = path.abspath(shapes_file)
shapes_file_format = 'turtle'

conforms, v_graph, v_text = validate(data_file, shacl_graph=shapes_file,
                                     data_graph_format=data_file_format,
                                     shacl_graph_format=shapes_file_format,
                                     inference='rdfs', debug=True,
                                     serialize_report_graph=True)
print(v_text)
