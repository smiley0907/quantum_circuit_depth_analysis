# 06: Display original circuit results

print("Original Quantum Circuit Analysis")
print("=" * 45)

for _, row in original_df.iterrows():

    print(
        f"{int(row['Qubits'])} Qubits -> "
        f"Depth: {int(row['Original Circuit Depth'])}, "
        f"Gate Count: {int(row['Gate Count'])}"
    )
