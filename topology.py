'''
Config file Details:

    nodes: (size of the virtual network graph)
    
    topology: datacenter, linear, full, star, or random (i.e., randomly connected graph) (case insensitive)

    α: the bias of the random coin (ignored if the topology is not random)

    min: virtual node weight — this models the min virtual CPU capacity allocated to a virtual node (VM)

    max: virtual node weight — this models the max virtual CPU capacity allocated to a
    virtual node (VM)

    min: virtual link weight —this models the min bandwidth reserved by a virtual link

    max: virtual link weight —this models the max bandwidth reserved by a virtual link

Output file Details (example):

    Source-Node-ID Destination Node-ID Link0-weight
    Source-Node-ID Destination Node-ID Link1-weight
    ...
    Node0-weight Node1-weight ... NodeN-weight

If the virtual network that we want is 0 − −1 − −2 − −3, a valid config file could be:

nodes: 4
topology: linear
alpha: xxx (irrelevant)
node-min: 20
node-max: 40
link-min: 10
link-max: 30

While a valid output file could be:
0 1 29
1 2 29
2 3 20
12 20 10 24

'''

import random as rd


class Topology:

    def __init__(self, data):
        self.data = data

    # Linear topology
    #  0 --- 1 --- 2 --- 3
    def linear(self, data):
        print("\nLinear Topology.......\n")
        nodes = int(data['nodes'])
        linkMin = int(data['link-min'])
        linkMax = int(data['link-max'])
        nodeMin = int(data['node-min'])
        nodeMax = int(data['node-max'])

        self.writeToFile("\nLinear Topology:\n")

        for i in range(nodes):
            if ((i+1) is not nodes):
                self.writeToFile(
                    f'{i} -- {i + 1} ---- Link: {rd.randint(linkMin, linkMax)}\n')

        self.writeToFile(
            f'{rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)}\n')

    # Datacenter (Tree) topology
    # 0    1       2   3
    #  \ / | \      \ /
    #   4  5  6      7
    # --------------------------

    def dataCenter(self, data):
        print("\nDatacenter Topology....")
        nodes = int(data['nodes'])
        linkMin = int(data['link-min'])
        linkMax = int(data['link-max'])
        nodeMin = int(data['node-min'])
        nodeMax = int(data['node-max'])

        self.writeToFile("\nFat Tree Topology:\n")

        for i in range(nodes):
            if ((i+1) is not nodes):
                self.writeToFile(
                    f'{i} -- {i + 1} ---- Link: {rd.randint(linkMin, linkMax)}\n')

        self.writeToFile(
            f'{rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)}\n')

    # Full topology
    # 0-----1
    # |\   /|
    # 2--3--4
    def full(self, data):
        print("\nFull Topology....")
        nodes = int(data['nodes'])
        linkMin = int(data['link-min'])
        linkMax = int(data['link-max'])
        nodeMin = int(data['node-min'])
        nodeMax = int(data['node-max'])

        self.writeToFile("\nFull Topology:\n")

        for i in range(nodes):
            if ((i+1) is not nodes):
                self.writeToFile(
                    f'{i} -- {i + 1} ---- Link: {rd.randint(linkMin, linkMax)}\n')

        self.writeToFile(
            f'{rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)}\n')

    # Star topology
    # 1     2
    #    0
    # 3     4
    def star(self, data):
        print("\nStar Topology.....")
        nodes = int(data['nodes'])
        linkMin = int(data['link-min'])
        linkMax = int(data['link-max'])
        nodeMin = int(data['node-min'])
        nodeMax = int(data['node-max'])

        self.writeToFile("\nStar Topology:\n")

        for i in range(nodes):
            if ((i+1) is not nodes):
                self.writeToFile(
                    f'{0} -- {i + 1} ----- Link: {rd.randint(linkMin, linkMax)}\n')

        self.writeToFile(
            f'{rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)} - {rd.randint(nodeMin, nodeMax)}\n')

    # Random topology
    def random(self, data):
        print("\nRandom Topology.....")

        self.writeToFile("\nRandom Topology:\n")

    # Function to write to file
    def writeToFile(self, data):
        outputFile = open("output.txt", "a+")
        outputFile.write(data)
        outputFile.close()
