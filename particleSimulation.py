"""
This simulates particles moving in a box and nucleating to form a crystal.

"""

class Particle():

    def init(self, particleNumber, velocity, mass, size):
        self.velocity = velocity
        self.particleNumber = particleNumber
        self.mass = mass
        self.size = size
        self.nucleated = False
    
    def setVelocity(self, velocity):
        self.velocity = velocity

    def setNucleated(self):
        self.nucleated = True
        self.velocity = (0,0,0)


class Simulation():
    def init(self, numberOfParticles, sizeOfParticles, sizeOfBox, timeStep, steps):
        """
        numberOfParticles - int - total number of particles in box
        sizeOfParticles - int - radius of each particle
        sizeOfBox - tuple(int, int, int) - (x,y,z) dimensions of box
        timeStep - int - seconds
        steps - int - total number of steps in the simulation
        """
        # for generating the configuration
        self.numberOfParticles = numberOfParticles
        self.sizeOfParticles = sizeOfParticles
        self.sizeOfBox = sizeOfBox
        self.generateConfigureation() 
        self.generateParticleInstances()# this returns both data structures coordDict and particleDict

    def generateConfigureation(self):
        """
        generate the starting configuration
        """
        self.initialCoods = set() # make a random configuration
        while len(coods) < self.numberOfParticles:
            self.initialCoods.add((random.randint(0,sizeOfBox[0]),random.randint(0,sizeOfBox[1]),random.randint(0,sizeOfBox[2]))



