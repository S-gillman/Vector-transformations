from tkinter import HORIZONTAL
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class vector:
    import matplotlib.pyplot as plt
    
    def __init__(self,x: float,y: float,z: float):
        self.x: float = x
        self.y: float = y
        self.z: float = z
    
    def dotproduct(self, v2: vector):
        a = self.x*v2.x
        b = self.y*v2.y
        c = self.z*v2.z
        return a+b+c
    def crossproduct(self, v2: vector):
        a = (self.y * v2.z) - (self.z * v2.y)
        b = (self.z * v2.x) - (self.x * v2.z)
        c = (self.x * v2.y) - (self.y * v2.x)
        return vector(a,b,c)
    def plotvector(self,axis,label,startx = 0, starty = 0, startz = 0):
        axis.quiver(startx,starty,startz,self.x,self.y,self.z,color='b',arrow_length_ratio=0.1,label=label)
    def scale(self,scale: float):
        self.x=float(scale)*self.x
        self.y=float(scale)*self.y
        self.z=float(scale)*self.z
        return self
    def addvector(self,vlist:list[vector]):
        x=self.x
        y=self.y
        z=self.z
        for v in vlist:
            x+=v.x
            y+=v.y
            z+=v.z
        return vector(x,y,z)


def main():
    print("vector 1")
    v1=vector(float(input("x: ")),float(input("y: ")),float(input("z: ")))
    print("vector 2")
    v2=vector(float(input("x: ")),float(input("y: ")),float(input("z: ")))
    print("vector 3")
    v3=vector(float(input("x: ")),float(input("y: ")),float(input("z: ")))
    vectors_list = [v1,v2,v3]
    vol = abs(v1.crossproduct(v2).dotproduct(v3))

    #plot figure
    fig= plt.figure(figsize=(8,8))
    ax1 = ppiped(fig, vectors_list,vol)
    plt.tight_layout()
    plt.show()

def ppiped(fig, vlist, volume):
    #create plot
    ax = fig.add_subplot(111, projection='3d')
    
    #plot vectors
    for i,v in enumerate(vlist):
        v.plotvector(ax,f"Vector {i+1}")

    #plot ppiped shape
    v1 = vlist[0]
    v2 = vlist[1]
    v3 = vlist[2]
    #verticies
    p0 = np.array([0, 0, 0])
    p1 = np.array([v1.x, v1.y, v1.z])
    p2 = np.array([v2.x, v2.y, v2.z])
    p3 = np.array([v3.x, v3.y, v3.z])
    p12 = p1 + p2
    p13 = p1 + p3
    p23 = p2 + p3
    p123 = p1 + p2 + p3
    
    faces = [
        [p0, p1, p12, p2],      # Bottom
        [p3, p13, p123, p23],   # Top
        [p0, p1, p13, p3],      # Side A
        [p0, p2, p23, p3],      # Side B
        [p1, p12, p123, p13],   # Side C
        [p2, p12, p123, p23]    # Side D
    ]

    #axis limits
    verticies = np.array([p0, p1, p2, p3, p12, p13, p23, p123])
    mins = verticies.min(axis=0) - 1
    maxs = verticies.max(axis=0) + 1
    
    #params for plot
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_xlim([mins[0], maxs[0]])
    ax.set_ylim([mins[1], maxs[1]])
    ax.set_zlim([mins[2], maxs[2]])
    ax.grid(True, linestyle='--')

    polygon = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='blue', alpha=0.3)
    ax.add_collection3d(polygon)

    #disp volume
    vcen = v1.addvector([v2,v3]).scale(0.5)
    ax.text(vcen.x, vcen.y, vcen.z, f" Vol: {volume:.2f}", color='black', fontsize=10, fontweight='bold',horizontalalignment='center',verticalalignment='center')

    return ax
if __name__=="__main__":
    main()