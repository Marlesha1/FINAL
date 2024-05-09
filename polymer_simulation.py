import numpy as np
from polymer import Polymer

def main():
    try:
        N = int(input("Enter the target degree of polymerization (N): "))
        num_molecules = int(input("Enter the number of polymer molecules to simulate: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    center_of_mass_values = []
    radius_of_gyration_values = []
    end_to_end_distance_values = []
    polydispersity_index_values = []

    for _ in range(num_molecules):
        polymer = Polymer(np.random.normal(N, 0.1 * N))  # Generate N from a normal distribution
        polymer.generate_chain()

        center_of_mass = polymer.center_of_mass()
        center_of_mass_values.append(center_of_mass)

        radius_of_gyration = polymer.radius_of_gyration()
        radius_of_gyration_values.append(radius_of_gyration)

        end_to_end_distance = polymer.end_to_end_distance()
        end_to_end_distance_values.append(end_to_end_distance)

        polydispersity_index = polymer.polydispersity_index()
        polydispersity_index_values.append(polydispersity_index)

    avg_center_of_mass = np.mean(center_of_mass_values, axis=0)
    avg_radius_of_gyration = np.mean(radius_of_gyration_values)
    avg_end_to_end_distance = np.mean(end_to_end_distance_values)
    avg_polydispersity_index = np.mean(polydispersity_index_values)
    std_dev_polydispersity_index = np.std(polydispersity_index_values)

    print("\nSimulation Results:")
    print("Average Center of Mass:", avg_center_of_mass)
    print("Average Radius of Gyration:", avg_radius_of_gyration)
    print("Average End-to-End Distance:", avg_end_to_end_distance)
    print("Average Polydispersity Index:", avg_polydispersity_index)
    print("Standard Deviation of Polydispersity Index:", std_dev_polydispersity_index)

if __name__ == "__main__":
    main()
