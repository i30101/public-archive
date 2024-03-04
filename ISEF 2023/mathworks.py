import numpy as np
import matplotlib.pyplot as plt

# Define the functions for the model
def U_t(t, r):
    return 0.42 * 234.2 * np.exp(r * t)

def E_t(t, pa, r):
    return (pa * U_t(t, r)) / (1 + 1518.82 * np.exp(-0.186511 * t))

def S_t(t, pa, r):
    return E_t(t + 1, pa, r) - E_t(t, pa, r)

# Define the input parameter ranges for sensitivity analysis
t_range = np.arange(2015, 2034, 1)
pa_range = np.arange(500000, 2000000, 100000)
r_range = np.arange(0.006, 0.0101, 0.0002)

# Calculate the default output
t_default = 2022
pa_default = 1000000
r_default = 0.007708
output_default = S_t(t_default, pa_default, r_default)

# Sensitivity to t, pa, and r
output_tpr = np.zeros((len(t_range), len(pa_range), len(r_range)))
for i, t_value in enumerate(t_range):
    for j, pa_value in enumerate(pa_range):
        for k, r_value in enumerate(r_range):
            output = S_t(t_value, pa_value, r_value)
            output_tpr[i, j, k] = output

# Calculate summary statistics
mean_output = np.mean(output_tpr)
median_output = np.median(output_tpr)
min_output = np.min(output_tpr)
max_output = np.max(output_tpr)

# Print summary statistics
print(f"Mean output: {mean_output:.2f}")
print(f"Median output: {median_output:.2f}")
print(f"Minimum output: {min_output:.2f}")
print(f"Maximum output: {max_output:.2f}")

# Find input parameter values that lead to highest and lowest output values
i_max, j_max, k_max = np.unravel_index(np.argmax(output_tpr), output_tpr.shape)
t_max = t_range[i_max]
pa_max = pa_range[j_max]
r_max = r_range[k_max]
output_max = output_tpr[i_max, j_max, k_max]
print(f"Maximum output of {output_max:.2f} occurs at t={t_max}, pa={pa_max}, r={r_max}")

i_min, j_min, k_min = np.unravel_index(np.argmin(output_tpr), output_tpr.shape)
t_min = t_range[i_min]
pa_min = pa_range[j_min]
r_min = r_range[k_min]
output_min = output_tpr[i_min, j_min, k_min]
print(f"Minimum output of {output_min:.2f} occurs at t={t_min}, pa={pa_min}, r={r_min}")

# Plot the sensitivity analysis results
fig, ax = plt.subplots(3, 1, figsize=(10, 15), gridspec_kw={'hspace': 0.7})
for i, t_value in enumerate(t_range):
    ax[0].plot(r_range, np.squeeze(output_tpr[i, pa_range == pa_default, :]), label=f"t={t_value}")
ax[0].set_xlabel('Growth Rate', fontsize=12)
ax[0].set_ylabel('Number of e-bikes sold', fontsize=12)
ax[0].set_title('Sensitivity to t')
ax[0].legend(fontsize=8)

for j, pa_value in enumerate(pa_range):
    ax[1].plot(r_range, np.squeeze(output_tpr[t_range == t_default, j, :]), label=f"pa={pa_value/1000}k")
ax[1].set_xlabel('Growth Rate', fontsize=12)
ax[1].set_ylabel('Number of e-bikes sold', fontsize=12)
ax[1].set_title('Sensitivity to pa')
ax[1].legend(fontsize=8)

for k, r_value in enumerate(r_range):
    ax[2].plot(t_range, np.squeeze(output_tpr[:, pa_range == pa_default, k]), label=f"r={r_value:.5f}")
ax[2].set_xlabel('Year', fontsize=12)
ax[2].set_ylabel('Number of e-bikes sold', fontsize=12)
ax[2].set_title('Sensitivity to r')
ax[2].legend(fontsize=8)



ax[0].legend(fontsize=6, loc='upper right', bbox_to_anchor=(1.1, 1.4))
ax[1].legend(fontsize=6, loc='upper right', bbox_to_anchor=(1.1, 1.2))
ax[2].legend(fontsize=6, loc='upper right', bbox_to_anchor=(1.1, 1.4))




plt.show()
