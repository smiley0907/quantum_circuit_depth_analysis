# 14: Display depth reduction results

print("Depth Reduction Analysis")
print("=" * 35)

for _, row in comparison_df.iterrows():

    print(
        f"{int(row['Qubits'])} Qubits -> "
        f"Depth Reduction: {int(row['Depth Reduction'])} layers, "
        f"Reduction: {row['Depth Reduction (%)']:.2f}%"
    )
