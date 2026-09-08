# 15: Plot depth reduction percentage

plt.figure(figsize=(8, 5))

plt.plot(
    comparison_df["Qubits"],
    comparison_df["Depth Reduction (%)"],
    marker="o"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Depth Reduction (%)")
plt.title("Depth Reduction versus Number of Qubits")
plt.xticks(qubit_sizes)
plt.grid(True)

plt.savefig(
    "05_depth_reduction_percentage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
