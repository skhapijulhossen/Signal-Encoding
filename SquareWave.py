import numpy as np
import matplotlib.pyplot as plt

def Sn():
    ""
    global n  
    plt.figure(figsize=(6,4))
    plt.title("Square wave using some of Sinusoids")
    plt.plot([0,1],[0,0], color="grey",linewidth=3)
    plt.ylabel("Volts")
    plt.xlabel(" t ")

    t = np.linspace(0,1,100)
    y = np.zeros(100)
    for n in range(1,n,2):
        sin = np.sin(2*np.pi*n*t)/n
        y += sin
    y = (y*4)/np.pi
    plt.plot(t,y , color="orange")
    plt.grid(True, color="lightgrey")
    plt.savefig("squareWave.png")
    plt.show()


if __name__ == "__main__":
    n = int(input("Enter Number of Harmonics should be <=11: "))
    if n <= 11:
        Sn()
    else:
        print("Entered Number of Harmonics is Greater than 11!")