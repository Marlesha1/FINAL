import numpy as np

class Polymer:
    def __init__(self, N):
        self.N = N
        self.positions = np.zeros((N, 3))

    def generate_chain(self):
        for i in range(1, self.N):
            theta = np.random.uniform(0, np.pi)
            phi = np.random.uniform(0, 2 * np.pi)
            dx = np.sin(theta) * np.cos(phi)
            dy = np.sin(theta) * np.sin(phi)
            dz = np.cos(theta)
            self.positions[i] = self.positions[i - 1] + np.array([dx, dy, dz])

    def center_of_mass(self):
        return np.mean(self.positions, axis=0)

    def radius_of_gyration(self):
        com = self.center_of_mass()
        return np.sqrt(np.mean(np.sum((self.positions - com)**2, axis=1)))

    def end_to_end_distance(self):
        return np.linalg.norm(self.positions[-1] - self.positions[0])

    def polydispersity_index(self):
        N_values = np.random.normal(self.N, 0.1 * self.N, 1000)
        radii = []
        for N_value in N_values:
            polymer = Polymer(int(N_value))
            polymer.generate_chain()
            radii.append(polymer.radius_of_gyration())
        return np.std(radii) / np.mean(radii)
