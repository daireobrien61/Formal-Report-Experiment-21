import numpy as np
import matplotlib.pyplot as plt

def importFiles(fileName) -> np.array:
    # Loads the output files from Selene into a numpy array for proccessing.
    with open(fileName, "r") as file:
        data = file.read()
    rows = data.split("\n")
    arr = np.array([[float(i) for i in r.split(" ")] for r in rows])
    return arr


def calcAverages(arrIn):
    # Computes the average value down a column for a given range of rows.
    retArr = []
    band = 10
    start = round(len(diffPowers[0])/2 - band/2)
    
    for i in range(len(arrIn[0])):
        col = [row[i] for row in arrIn[start : start + band]]
        retArr.append(np.average(col))
    return retArr


# Creates arrays based on each of the data files for processing.
run1Power = importFiles(r"data\RayTracerLambertainSourceRun1 - Power.txt")
run2Power = importFiles(r"data\RayTracerLambertainSourceRun2 - Power.txt")

run1Hitcount = importFiles(r"data\RayTracerLambertainSourceRun1 - Hitcounts.txt")
run2Hitcount = importFiles(r"data\RayTracerLambertainSourceRun2 - Hitcounts.txt")

# Computes the differences between the two graphs
diffPowers = run1Power - run2Power
diffHitcounts = run1Hitcount - run2Hitcount

#Computes the average values accross the band for all of the relevent datatypes.
powAverages = calcAverages(diffPowers)
hitcountAverages = calcAverages(diffHitcounts)

r1PowerAverage = calcAverages(run1Power)
r2PowerAverage = calcAverages(run2Power)

r1HitcountAverage = calcAverages(run1Hitcount)
r2HitcountAverage = calcAverages(run2Hitcount)


# Creates, plots then shows all 4 graphs.
fig, axes = plt.subplots(2,2, figsize=(12,7), layout="constrained", dpi=300)
axes = axes.ravel()

[axes[i].set_xlabel("Column number") for i in range(len(axes))]

axes[0].plot(range(0, 101), powAverages)
axes[0].set_title("Power differences - Figure 6.1")
axes[0].set_ylabel("Power difference")

axes[1].plot(range(0, 101), r1PowerAverage, label = "Full power")
axes[1].plot(range(0, 101), r2PowerAverage, label = "Half power")
axes[1].set_title("Power distribution - Figure 6.2")
axes[1].set_ylabel("Power difference")
axes[1].legend()

axes[2].plot(range(0, 101), hitcountAverages)
axes[2].set_title("Hit count differences - Figure 6.3")
axes[2].set_ylabel("Difference in hit counts")

axes[3].plot(range(0, 101), r1HitcountAverage, label = "Full power")
axes[3].plot(range(0, 101), r2HitcountAverage, label = "Half power")
axes[3].set_title("Hit count distribution - Figure 6.4")
axes[3].set_ylabel("Number of hits")
axes[3].legend()


plt.show()
fig.savefig("images\PowerHitcountDistributions")