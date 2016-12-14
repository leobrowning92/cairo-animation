import os
import cairo as cairo
import numpy as np
from render import Animate

class Particle(object):
    def __init__(self,x,y,velocity):

        self.position = np.array([x,y])
        self.velocity = velocity
        assert len(self.velocity)==2


    def move(self):
        self.position= np.add(self.velocity, self.position)
    def accelerate(self,a):
        self.velocity=np.add(self.velocity,a)






if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # These are the required arguments for the Animation
    BACK = [1, 1, 1, 1]
    FRONT = [149/255, 131/255, 189/255, 0.05]
    SIZE = 1000
    UNIT=1.0/SIZE
    number=1000 # number of particles in the system
    particles=[None]*number
    for i in range(number):
         particles[i] = Particle(0.5/number+i/number, 0.5, [0,0])


    def step(self):
        # render.clear_canvas()
        for particle in particles:
            pos=particle.position
            particle.move()
            render.circle(pos[0],pos[1],2*render.pix)
            particle.accelerate([0,np.random.uniform(-UNIT/10,UNIT/10)])
        return True


    # These are the bits that need to be run when calling the Animation
    render = Animate(SIZE, BACK, FRONT,100,step,save=False)
    render.start()
