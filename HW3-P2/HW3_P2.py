import random
import math
from vertex import vertex
from matrix import matrix
from edge import edge

def calculateWeight(pt1, pt2):
    x = random.randint(0, 100)
    return x

def createEdgeObjects(verticeList):
    edgeList =[]
    for u in verticeList:
        neighborList = u.get_neighbors()
        for n in neighborList:
            newEdge = edge(u, n[0], n[1])
            edgeList.append(newEdge)
    return edgeList

def generateGraph():
    graph = []
    vertices = []
    counter = 1
    while counter<20:
        new_vertex = vertex(counter)
        new_vertex.set_matrixPos(counter)
        vertices.append(new_vertex)
        counter += 1
    for v in vertices:
        numNeighbors = random.randint(0, len(vertices))
        neighbors = []
        neighborIndexOptions = []
        i = len(vertices) - 1
        while i>=0:
            neighborIndexOptions.append(i)
            i -= 1
        while numNeighbors > 0:
            random.shuffle(neighborIndexOptions)
            neighborIndex = neighborIndexOptions.pop(0)
            edge = (v, vertices[neighborIndex])
            weight = calculateWeight(v.get_data(), vertices[neighborIndex].get_data())
            neighbors.append((vertices[neighborIndex], weight))
            numNeighbors -= 1
        v.set_neighbors(neighbors)
    graph.append(vertices)
    edgeList = createEdgeObjects(vertices)
    graph.append(edgeList)
    return graph

def createAdjacencyMatrix(graph):
    #note that the vertices were added to the graph in the same order that they were assigned their matrixPos
    W = []
    P = []
    count = 1
    topLine = [0]
    W.append(topLine)
    P.append(topLine)
    while count < (len(graph[0])+1):
        topLine.append(count)
        additionalLineW = [count]
        additionalLineP = [count]
        for i in graph[0]:
            additionalLineW.append(float("inf"))
            additionalLineP.append(None)
        W.append(additionalLineW)
        P.append(additionalLineP)
        count +=1
    graphIndex = 0
    matPos = 1
    while graphIndex<len(graph[0]):
        vertice = graph[0][graphIndex]
        neighbors =  vertice.get_neighbors()
        for n in neighbors:
            W[matPos][n[0].get_matrixPos()]=n[1]
            P[matPos][n[0].get_matrixPos()]=vertice.get_matrixPos()
        graphIndex+=1
        matPos+=1
    #set diagonal to 0
    d = 0
    while d <len(W[0]):
        W[d][d] = 0
        P[d][d] = None
        d+=1
    return (W, P)

def sortTemp(temp):
    j = 1
    while j < len(temp):
        key = temp[j]
        i = j-1
        while (i >= 0):
            if temp[i][0] > key[0]:
                switch1 = (temp[i][0], temp[i][1])
                switch2 = (temp[i+1][0], temp[i+1][1])
                temp[i] = switch2
                temp[i+1] = switch1
                key = temp[i]
            i = i-1
        j += 1
    return temp

def createFile(graph):
    file = open("graph.txt", "w")
    for u in graph[0]:
        file.write("v{}: ".format(u.get_data()))
        neighbors = u.get_neighbors()
        temp = []
        for n in neighbors:
            neighborValue = n[0].get_data()
            edgeWeight = n[1]
            temp.append((neighborValue, edgeWeight))
        temp = sortTemp(temp)
        count = 1
        while count <= len(graph[0]):
            if len(temp) == 0:
                file.write("0, ")
            elif count == temp[0][0]:
                file.write("{}, ".format(temp[0][1]))
                temp.pop(0)
            else:
                file.write("0, ")
            count += 1
        file.write('\n')
    file.close

def extractMin(Q):
    #inefficient, consider creating a heap?
    minQ = Q[0]
    for q in Q:
        if q.get_distance() < minQ.get_distance():
            minQ = q
    Q.remove(minQ)
    return minQ

def relax(u, v, w):
    if v.get_distance() > (u.get_distance()+w):
        v.set_distance(u.get_distance()+w)
        v.set_parent(u)

def dijkstra(graph):
    #vertices have already been initialized with parent none and distance infinity at creation of vertex object
    source = graph[0][0]
    source.set_distance(0)
    S = []
    Q = []
    for q in graph[0]:
        Q.append(q)
    while len(Q) > 0:
        u = extractMin(Q)
        S.append(u)
        #Is this what is meant by S = S U {u}?
        adjacentV = u.get_neighbors()
        for v in adjacentV:
            relax(u, v[0], v[1])
    #extract info from S before messing with Nodes in next part
    shortestPath = []
    for s in S:
        newS = vertex(s.get_data(), s.get_neighbors(), s.get_distance(), s.get_parent())
        shortestPath.append(newS)
    return shortestPath

def translateFloydWarshal(finalD, finalP):
    answer = []
    i = 1
    while i < len(finalD):
        j = 1
        while j < len(finalD):
            if i == j:
                pass
            elif finalP[i][j] == None:
                newList = ["There is no path from {} to {}".format(i, j)]
                answer.append(newList)
            else:
                m = i
                newList = []
                newList.append(j)
                while finalP[m][j] != m:
                    m = finalP[m][j]
                    newList.insert(len(newList)-1, m)
                newList.insert(0, i)
                answer.append("The shortest path from {} to {} is: {}".format(i, j, newList))
            j += 1
        i+= 1
    for a in answer:
        print (a)
    return answer

def floydWarshall(W, P):
    n = len(W)-1
    Dlist = []
    Plist = []
    D0 = matrix(0, W, W)
    P0 = matrix(0, P, P)
    Dlist.append(D0)
    Plist.append(P0)
    k =1
    while k <= n:
        #initialize new matrix Dk and Pk
        parentD = Dlist[k-1]
        Dk = matrix(k, parentD)
        parentP = Plist[k-1]
        Pk = matrix (k, parentP)
        Dk_newData = []
        Dk_newData.append(parentD.get_data()[0])
        Pk_newData = []
        for p in parentP.get_data():
            Pk_newData.append(p)
        t = 1
        while t<=n:
            newlistD = []
            newlistD.append(t)
            z = 1
            while z<=n:
                newlistD.append(0)
                z+=1
            Dk_newData.append(newlistD)
            t+=1
        #fill Dk and Pk with real data
        i=1
        while i<=n:
            j=1
            while j<=n:
                Dk_newData[i][j] = min(parentD.get_data()[i][j], (parentD.get_data()[i][k]+parentD.get_data()[k][j]))
                if (parentD.get_data()[i][k]+parentD.get_data()[k][j]) < parentD.get_data()[i][j]: 
                    Pk_newData[i][j] = k
                j+=1
            i+=1
        Dk.set_data(Dk_newData)
        Dlist.append(Dk)
        Pk.set_data(Pk_newData)
        Plist.append(Pk)
        k+=1
    answer = translateFloydWarshal(Dlist[len(Dlist) -1].get_data(), Plist[len(Plist)-1].get_data())
    return answer

def inQ(Q, v):
#    print ("v: {}".format(v.get_data()))
    inq = False
    for q in Q:
 #       print ("q:{}".format(q.get_data()))
        if q.get_data() == v.get_data():
            inq = True
            return inq
    return inq

def translatePrim(graph):
    minSpanTree = []
    for v in graph[1:]:
        edge = (v.get_parent().get_data(), v.get_data())
        minSpanTree.append(edge)
    return minSpanTree

def mstPrim(graph):
    Q = []
    for u in graph[0]:
         Q.append(u)
    for u in Q:
        u.set_distance(float('inf'))
        u.set_parent(None)
    root = Q[0]
    root.set_distance(0)
    while len(Q)>0:
        u = extractMin(Q)
        neighbors = u.get_neighbors()
        for v in neighbors:
            inq = inQ(Q, v[0])
            if (v[1] < v[0].get_distance()) & (inq == True): 
                v[0].set_parent(u)
                v[0].set_distance(v[1])
    minSpanTree = translatePrim(graph[0])
    return minSpanTree


def getInput():
    d = input("Please place a copy of the test file into the HW3-P2 subfolder and enter its name, using quotations, or enter 'graph.txt'.")
    return d

def convertFile(filename):
    result = []
    fileStream = open(filename, 'r')
    fileList = []
    for line in fileStream:
        fileList.append(line)
    for line in fileList:
        list = []
        i = line.find(":")
        j = line.find(",")
        list.append(int(line[i+2:j]))
        while len(list) < len(fileList):
            k = j+1
            while line[k] != ",":
                k +=1
            list.append(int(line[j+2:k]))
            j=k
        result.append(list)
    vertices = []
    counter = 1
    while counter <= len(result):
        new_vertex = vertex(counter)
        new_vertex.set_matrixPos(counter)
        vertices.append(new_vertex)
        counter += 1
    index = 0
    while index < len(result):
        v = vertices[index]
        neighborsMatrixForm = result[index]
        neighbors = []
        n = 0
        while n < len(neighborsMatrixForm): 
            if neighborsMatrixForm[n] != 0:
                u = (vertices[n], neighborsMatrixForm[n])
                neighbors.append(u)
            n += 1
        v.set_neighbors(neighbors)
        index += 1
    graph.append(vertices)
    return graph

graph = generateGraph()
createFile(graph)

d = getInput()
inputGraph = convertFile(d)

singleSourceShortestPath = dijkstra(inputGraph)
print ("The edges of the single source shortest path, with {} as the single source are:".format(singleSourceShortestPath[0].get_data()))
for v in singleSourceShortestPath[1:]:
    print ("({}, {})".format(v.get_parent().get_data(), v.get_data()))
(W, P) = createAdjacencyMatrix(inputGraph)
allPairsShortestPath = floydWarshall(W, P)
minTree = mstPrim(inputGraph)
print ("The edges of the minimum spanning tree, with {} as the root are:".format(inputGraph[0][0].get_data()))
for v in minTree:
    print (v)

    #confirming GitHub connection