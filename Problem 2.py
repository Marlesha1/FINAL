import numpy as np
import polymerClasses

def calculate_metrics(N, num_molecules):#function that calculates certain metrics or properties related to a system consisting of molecules.
    polymer_chain = polymerClasses.FreelyJointedChain()

    end_to_end_distances = []
    radius_of_gyrations = []
    for _ in range(num_molecules):
        polymer_chain.generate_polymer(N)
        end_to_end_distances.append(polymer_chain.calculate_end_to_end_distance() * 1e3)  # Convert to μm
        radius_of_gyrations.append(polymer_chain.calculate_radius_of_gyration() * 1e3)  # Convert to μm

    avg_center_of_mass = polymer_chain.calculate_avg_center_of_mass()
    avg_end_to_end_distance = np.mean(end_to_end_distances)
    std_dev_end_to_end_distance = np.std(end_to_end_distances)
    avg_radius_of_gyration = np.mean(radius_of_gyrations)
    std_dev_radius_of_gyration = np.std(radius_of_gyrations)
    poly_dispersity_index = std_dev_radius_of_gyration / avg_radius_of_gyration

    return avg_center_of_mass, avg_end_to_end_distance, std_dev_end_to_end_distance, avg_radius_of_gyration, std_dev_radius_of_gyration, poly_dispersity_index

def main():
    N = input("Degree of polymerization (1000)?: ")
    N = int(N) if N else 1000

    num_molecules = input("How many molecules (50)?: ")
    num_molecules = int(num_molecules) if num_molecules else 50

    avg_center_of_mass, avg_end_to_end_distance, std_dev_end_to_end_distance, avg_radius_of_gyration, std_dev_radius_of_gyration, poly_dispersity_index = calculate_metrics(N, num_molecules)

    print(f"Metrics for {num_molecules} molecules of degree of polymerization = {N}")
    print(f"Avg. Center of Mass (nm) = {avg_center_of_mass[0]:.3f}, {avg_center_of_mass[1]:.3f}, {avg_center_of_mass[2]:.3f}")
    print("End-to-end distance (μm):")
    print(f"\tAverage = {avg_end_to_end_distance:.3f}")
    print(f"\tStd. Dev. = {std_dev_end_to_end_distance:.3f}")
    print("Radius of gyration (μm):")
    print(f"\tAverage = {avg_radius_of_gyration:.3f}")
    print(f"\tStd. Dev. = {std_dev_radius_of_gyration:.3f}")
    print(f"PDI = {poly_dispersity_index:.2f}")

if __name__ == "__main__":
    main()
