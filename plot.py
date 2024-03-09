import numpy as np
import matplotlib.pyplot as plt
import random as rand

# Extension (meters)
initial_extension = np.array([8, 15, 22, 29, 36, 43, 50, 58, 65, 72, 79])
initial_extension = initial_extension * 1.e-5

# Final extention (meters)
final_extension = np.array([76, 69, 62, 55, 47, 40, 33, 26, 19, 12, 8])
final_extension = final_extension * 1.e-5

# Load (N)
applied_mass_initial = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
load_initial = applied_mass_initial * 9.81

applied_mass_final = np.array([0.95, 0.85, 0.75, 0.65, 0.55, 0.45, 0.35, 0.25, 0.15, 0.05, 0.0])
load_final = applied_mass_final * 9.81

# Combine initial and final extensions
combined_extension = np.concatenate((initial_extension, final_extension))

# Combine initial and final loads
combined_load = np.concatenate((load_initial, load_final))

# Sort the combined data in ascending order
sort_indices = np.argsort(combined_load)
combined_load = combined_load[sort_indices]
combined_extension = combined_extension[sort_indices]

# Perform linear regression
slope, intercept = np.polyfit(combined_load, combined_extension, 1)

# Create a function for the line of best fit
line_of_best_fit = np.poly1d([slope, intercept])

# Generate random, small error values
y_error = 0.00002

# Plot the combined data with error bars
plt.errorbar(combined_load, combined_extension, yerr=y_error, fmt='o', capsize=3)

# Plot the line of best fit
plt.plot(combined_load, line_of_best_fit(combined_load), 'r')

plt.ylabel('Extension (m)')
plt.xlabel('Load (N)')
plt.title('Extension vs. Load')
plt.grid(True)
plt.show()