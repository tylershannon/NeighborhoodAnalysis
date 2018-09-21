import json
import NetworkMap as map

def setup():
    background(200)
    size(640, 360)
    
    nodeData = open("NetworkMap.json").read()
    nodeData = json.loads(nodeData)
    
    map.drawNetwork(nodeData)
    
def draw():
    pass
