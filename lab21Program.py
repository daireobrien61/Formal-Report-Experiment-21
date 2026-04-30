import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def importFiles(fileName) -> np.array:
    with open(fileName, "r") as file:
        data = file.read()
    rows = data.split("\n")
    arr = np.array([[float(i) for i in r.split(" ")] for r in rows])
    return arr

run2Power = importFiles(r"C:\Users\daire\Documents\Aether sims\RayTracerLambertainSourceRun2 - Power.txt")
run1Power = importFiles(r"C:\Users\daire\Documents\Aether sims\RayTracerLambertainSourceRun1 - Power.txt")

run2Hitcount = importFiles(r"C:\Users\daire\Documents\Aether sims\RayTracerLambertainSourceRun2 - Hitcounts.txt")
run1Hitcount = importFiles(r"C:\Users\daire\Documents\Aether sims\RayTracerLambertainSourceRun1 - Hitcounts.txt")

diffPowers = run1Power - run2Power
diffHitcounts = run1Hitcount - run2Hitcount
plt.plot(range(0,101), diffPowers[34])
plt.show()