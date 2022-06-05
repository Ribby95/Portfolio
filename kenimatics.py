# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 14:57:28 2022
A project to model the path of an intersteller vehicle 

@author: Robert Stuckey
"""
"Import computation packages"
import matplotlib.pyplot as plt
import math 
import numpy as np
#import sympy

#plt.figure(figsize=(8,8), dpi=80)

"creates initial time, final time and timestep"
tnot=0 #initial time
tlast=12000 #final time
step=10 #timestep 
constant=step*np.abs(tlast-tnot)  
interval=np.linspace(tnot,tlast,constant) #interval we are modeling over
g= 9.80665  #gravitational constant for accelaration/artificial gravity

"initial values for acceleration veloity and position vectors"
 #this  is a temporary value
vnot=np.array([10000,0])
xnot=np.array([0,6371000])  #initial position vector
anot=g*-xnot/np.linalg.norm(xnot)

"main loop for producing position values"
X=[]#list of x coordinates
Y=[]#list of y coordinates
AX=anot[0]#x component of accellaration
AY=anot[1]#y component of accelleration
v=vnot #initial values for velocity position and acceleration
x=xnot
a=anot #hello i am redundant but I might be usefull later

for t in interval:
    X=np.append(X,x[0])#adds the new x coordinate to the list of 
    Y=np.append(Y,x[1])#adds new y coordinate to the list
    AX=np.append(AX,a[0])#adds new x component to acceleration list
    AY=np.append(AY,a[1])#adds new y coordinate to  acceleration list
    x=x+(1/step)*v #uses newton to update position vector
    v=v+(1/step)*a#updates velocity vector
    a=g*np.array(-x)/np.linalg.norm(x) #assigns new acceleration vector
    


G=0 #for colors we set green to zero
fig, ax = plt.subplots() 
"""
for i in range(0,constant,5):#changes color of graph over time
    R=0+i/constant#starts with no red
    B=1-R #transitions slowly to red
    color = (R,G,B)
    ax.plot(X[i:i+5+1], Y[i:i+5+1], c=color)#plots incrementally
"""

ax.plot(X,Y)#comment this if 53 through 57 are inactive

origin=np.array([0,0,0])#assigns the origin for quiver
#ax.quiver(X,Y,AX,AY) #uses acceleration for quiver