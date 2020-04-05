#
# Brandon
#

import pandas as pd
from topology import Topology


# Resolve Topology and route to proper Topology function
def resTopology(cData):
    top = Topology(cData)
    currTop = cData.values[0][1]

    switcher = {
        "linear": top.linear,
        "datacenter": top.dataCenter,
        "full": top.full,
        "star": top.star,
        "random": top.random
    }
    # Get the function from switcher dictionary
    func = switcher.get(currTop, lambda: "Invalid topology")
    func(cData)


# Read Config file
def readFile(file):
    config = pd.read_csv(file, encoding="utf8")
    resTopology(config)


if __name__ == "__main__":

    file = "config.csv"
    readFile(file)
