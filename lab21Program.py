import numpy as np
from PIL import Image

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
diff = run1Hitcount/run1Hitcount.max() - run2Hitcount/run2Hitcount.max()
print(diff.max())
image = Image.fromarray(diff*225)

image.show("Difference")