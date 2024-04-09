import numpy as np
import matplotlib.pyplot as plt

# ----- Differential Equation
def diffeq(x,y,dt):
    dx = (np.sin(y)*.9)*dt
    dy = (-1*np.cos(x)*.8)*dt
    return (dx,dy)

# ----- Parameters

dt = 0.1     # differential step size
trlen = 10    # length of the vector trace
trnum = 5     # number of traces along given starting value
trtime = 100  # how long to run the vector field
xmin = -5      # lower x boundary
xmax = 5      # upper x boundary
ymin = -5      # lower y boundary
ymax = 5      # upper y boundary
trden = 1     # denisty of traces beginning in a 1x1 area

# -----
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.axis([xmin,xmax,ymin,ymax])
plt.show()


xpts = int((xmax-xmin)/trden)+1
ypts = int((ymax-ymin)/trden)+1
pointfield = np.zeros((xpts,ypts,2))
for x in np.arange(len(pointfield[:,0,0])):
    for y in np.arange(len(pointfield[0,:,0])):
        pointfield[x,y,:]=[xmin + x*trden, ymin + y*trden]

vecfield = np.array([pointfield])

for i in np.arange(trtime):
    if i%(2*trlen) == 0 and i != 0:
        vecfield = np.append(vecfield,[pointfield],axis=0)
        if len(vecfield) > trnum:
            vecfield=np.delete(vecfield,0,0)
    for n in np.arange(len(vecfield)):
        for x in np.arange(xpts):
            for y in np.arange(ypts):
                oldplot = np.copy(vecfield[n,x,y,:])
                diff = diffeq(vecfield[n,x,y,0],vecfield[n,x,y,1],dt)
                newx = vecfield[n,x,y,0]+diff[0]
                newy = vecfield[n,x,y,1]+diff[1]
                vecfield[n,x,y,:]=[newx,newy]
                ax.plot((oldplot[0],newx),(oldplot[1],newy), color = 'black')
    plt.pause(0.01)
    if i > trlen:
        for j in range(xpts*ypts*len(vecfield)):
            ax.lines.pop(0)
