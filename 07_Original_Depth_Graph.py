# 07: Plot original circuit depth

plt.figure(figsize=(8, 5))

plt.plot(
    original_df["Qubits"],
    original_df["Original Circuit Depth"],
    marker="o"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Original Circuit Depth")
plt.title("Original Circuit Depth versus Number of Qubits")
plt.xticks(qubit_sizes)
plt.grid(True)

plt.savefig(
    "03_original_circuit_depth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
