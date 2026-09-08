# 10: Compare original and parallelized circuit depth

comparison_df = original_df[
    ["Qubits", "Original Circuit Depth"]
].copy()

comparison_df["Parallelized Circuit Depth"] = (
    parallelized_df["Parallelized Circuit Depth"]
)

comparison_df["Depth Reduction"] = (
    comparison_df["Original Circuit Depth"]
    - comparison_df["Parallelized Circuit Depth"]
)

comparison_df["Depth Reduction (%)"] = (
    comparison_df["Depth Reduction"]
    / comparison_df["Original Circuit Depth"]
) * 100

comparison_df
