# 17: Generate final experimental summary

print("Quantum Circuit Depth Analysis")
print("=" * 45)

print("\nExperimental Configuration:")
print("Qubit sizes:", qubit_sizes)

print("\nResults:")
print(comparison_df.to_string(index=False))

print("\nAverage Depth Reduction:")
print(f"{average_reduction:.2f}%")

max_index = comparison_df["Depth Reduction (%)"].idxmax()

print("\nMaximum Depth Reduction:")
print(
    f"{comparison_df.loc[max_index, 'Depth Reduction (%)']:.2f}% "
    f"at {int(comparison_df.loc[max_index, 'Qubits'])} qubits"
)
