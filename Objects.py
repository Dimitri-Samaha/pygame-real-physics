import numpy as np


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

objects = []

class MecaPt:
    def __init__(self, coords, mass, velocity=0, color=RED, radius=1737.4*1000) -> None:
        if coords != [0, 0]:
            self.coords = np.array(coords)
        else:
            self.coords = np.zeros(2)
        self.mass = mass
        self.velocity = np.array(velocity)
        self.color = color
        self.radius = radius

    def get_vec(self, sys) -> list:
        x = self.coords[0]-sys.coords[0]
        y = self.coords[1]-sys.coords[1]
        dist = ((x**2)+(y**2))**0.5
        return dist, (x, y)

    def __repr__(self) -> str:
        return str(type(self).__mro__)
    
    def get_forces(self) -> list:
        forces = []
        for objec in objects:
            if type(objec) != MecaPt and list(objec.coords) != list(self.coords):
                if objec.is_acting(self):
                    forces.append(objec)
        return forces

    def get_acceleration(self):
        forces = self.get_forces()
        somme = np.zeros(2)
        for objec in forces:
            f = objec.force(self)
            somme += f[0]*f[1]
        self.acceleration = somme/self.mass
        return self.acceleration

    def get_velocity(self):
        acceleration = self.get_acceleration()
        if type(acceleration) == np.ndarray:
            self.velocity = self.velocity+acceleration/120
        return self.velocity
    
    def update(self):
        velocity = self.get_velocity()
        if type(velocity) == np.ndarray:
            self.coords = self.coords+velocity/120


class Planet(MecaPt):
    def __init__(self, coords, mass, velocity=0, color=RED, radius= 6371*1000) -> None:
        self.mass, self.velocity, self.color = mass, velocity, color
        self.radius = radius
        if coords != [0, 0]:
            self.coords = np.array(coords)
        else:
            self.coords = np.zeros(2)
        self.cstG = 6.67428*10**(-11)
        
    def __repr__(self) -> str:
        return str(type(self).__mro__)

    def force(self, sys : MecaPt) -> tuple:
        dist, coords = self.get_vec(sys)
        vector = np.array([coords[0]/dist, coords[1]/dist])
        f = self.cstG*self.mass*sys.mass / (dist**2)
        print(f)
        return (f, vector)
    
    def is_acting(self, sys : MecaPt):
        return True

