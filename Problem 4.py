import tkinter as tk
from tkinter import ttk


class DualCycleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Air Standard Dual Cycle Analysis")

        # Variables
        self.units = tk.StringVar()
        self.units.set("English")  # Default units

        self.r = tk.DoubleVar()
        self.P3_P2 = tk.DoubleVar()
        self.rc = tk.DoubleVar()
        self.T1 = tk.DoubleVar()
        self.P1 = tk.DoubleVar()

        # Labels
        ttk.Label(root, text="Compression Ratio (r):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(root, text="P3/P2 Ratio:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(root, text="Cutoff Ratio (rc):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(root, text="Initial Temperature (T1):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(root, text="Initial Pressure (P1):").grid(row=4, column=0, padx=5, pady=5, sticky="w")

        # Entries
        ttk.Entry(root, textvariable=self.r).grid(row=0, column=1, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.P3_P2).grid(row=1, column=1, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.rc).grid(row=2, column=1, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.T1).grid(row=3, column=1, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.P1).grid(row=4, column=1, padx=5, pady=5)

        # Radio Buttons for units
        ttk.Radiobutton(root, text="English", variable=self.units, value="English").grid(row=5, column=0, padx=5,
                                                                                         pady=5, sticky="w")
        ttk.Radiobutton(root, text="Metric", variable=self.units, value="Metric").grid(row=5, column=1, padx=5, pady=5,
                                                                                       sticky="w")

        # Button to calculate
        ttk.Button(root, text="Calculate", command=self.calculate).grid(row=6, columnspan=2, padx=5, pady=10)

        # Output Label
        self.output_label = ttk.Label(root, text="")
        self.output_label.grid(row=7, columnspan=2, padx=5, pady=5)

    def calculate(self):
        # Retrieve input values
        r = self.r.get()
        P3_P2 = self.P3_P2.get()
        rc = self.rc.get()
        T1 = self.T1.get()
        P1 = self.P1.get()
        units = self.units.get()

        # Perform calculations
        if units == "English":
            # Convert pressures from psi to MPa
            P1 /= 145.0377377
            # Convert temperatures from °F to K
            T1 = (T1 - 32) * 5 / 9 + 273.15

        # Calculate temperatures at state 2 and 3
        T2 = T1 * (r - 1)
        T3 = T2 * P3_P2 ** ((1 - 1 / rc) / 0.4)  # Assuming specific heat ratio (gamma) = 1.4

        # Calculate pressures at state 2 and 3
        P2 = P1 * (r ** 1.4)
        P3 = P2 * P3_P2

        # Calculate specific volumes at state 2 and 3
        V2 = 1
        V3 = V2 * (r ** (1 / 0.4))

        # Calculate pressures and volumes at state 4
        P4 = P3
        V4 = V3 * rc

        # Calculate temperatures at state 4
        T4 = T3 * (rc ** 0.4)

        # Calculate temperatures at state 5
        V1 = 1
        V5 = V1
        T5 = T1 * (V1 / V5) ** 0.4

        # Calculate work for each process (Assuming ideal gas)
        # Work for processes 1-2 (isentropic compression)
        W12 = -1 * 0.4 * (P2 * V2 - P1 * V1) / (1 - 1.4)

        # Work for processes 2-3 (constant volume heat addition)
        W23 = 0.4 * P3 * (V3 - V2)

        # Work for processes 3-4 (constant pressure heat addition)
        W34 = 0.4 * P3 * (V4 - V3)

        # Work for processes 4-5 (isentropic expansion)
        W45 = -1 * 0.4 * (P4 * V5 - P3 * V4) / (1 - 1.4)

        # Work for processes 5-1 (constant volume heat rejection)
        W51 = 0

        # Calculate net work
        W_net = W12 + W23 + W34 + W45 + W51

        # Calculate thermal efficiency
        Q_in = W23 + W34
        thermal_efficiency = (W_net / (Q_in + W51)) * 100

        # Display results
        result_text = f"Temperatures (K): T2={T2:.2f}, T3={T3:.2f}, T4={T4:.2f}, T5={T5:.2f}\n"
        result_text += f"Pressures (MPa): P2={P2:.2f}, P3={P3:.2f}, P4={P4:.2f}\n"
        result_text += f"Specific Volumes (m^3/kg): V2={V2:.4f}, V3={V3:.4f}, V4={V4:.4f}\n"
        result_text += f"Work (kJ/kg): W12={W12:.2f}, W23={W23:.2f}, W34={W34:.2f}, W45={W45:.2f}, W51={W51:.2f}\n"
        result_text += f"Net Work (kJ/kg): {W_net:.2f}\n"
        result_text += f"Thermal Efficiency (%): {thermal_efficiency:.2f}%"

        self.output_label.config(text=result_text)


def main():
    root = tk.Tk()
    app = DualCycleGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
