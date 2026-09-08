# 12: Plot original versus parallelized circuit depth

plt.figure(figsize=(8, 5))

plt.plot(
    comparison_df["Qubits"],
    comparison_df["Original Circuit Depth"],
    marker="o",
    label="Original Circuit Depth"
)

plt.plot(
    comparison_df["Qubits"],
    comparison_df["Parallelized Circuit Depth"],
    marker="o",
    label="Parallelized Circuit Depth"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Circuit Depth")
plt.title("Original versus Parallelized Circuit Depth")
plt.xticks(qubit_sizes)
plt.grid(True)
plt.legend()

plt.savefig(
    "04_original_vs_parallelized_depth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
