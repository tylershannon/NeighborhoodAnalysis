
def getNode(data, index):
    node = data[str(index)][0]
    return node

def drawNode(node):
    id = node['NodeID']
    x = float(random(0,width))
    y = float(random(0,height))
    node['NodeX'] = x
    node['NodeY'] = y
    
    textAlign(CENTER, CENTER)
    text(str(s), x,y)
    noFill()
    stroke(255)
    ellipse(x,y,30,30)
    
def drawEdge(node):
    connectionList = node['LevelOneConnections']
    nodeX = node['NodeX']
    nodeY = node['NodeY']
    for i in range(len(connectionList)):
        xX = getNode(data, connectionList[i])['NodeX']
        xY = getNode(data, connectionList[i])['NodeY']
        line(nodeX, nodeY, xX, xY)

def drawNetwork(data):
    for i in range(1,len(data)):
        node = getNode(data, i)
        drawNode(node)
        drawEdge(node)