import pandas as pd
import subprocess as sub
from time import time

data = {
        "klu": [],
        "bnd": [],
        "kry": []
}
min_mesh = 20
max_mesh = 150
mesh = min_mesh

try:
    while mesh <= max_mesh:
        for key in data.keys():
            s = time()
            sub.call(f"./sundials/examples/serial/idaHeat2D_{key} {mesh}", shell=True)
            e = time()
            data[key].append(e-s)

        mesh += 10

    df = pd.DataFrame(data)
    df.to_csv("rundata.csv")

except:
    print(data)
