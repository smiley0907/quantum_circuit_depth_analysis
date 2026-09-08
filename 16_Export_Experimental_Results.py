# 16: Export experimental results

comparison_df.to_csv(
    "02_quantum_circuit_depth_results.csv",
    index=False
)

print("Experimental results saved to:")
print("02_quantum_circuit_depth_results.csv")
