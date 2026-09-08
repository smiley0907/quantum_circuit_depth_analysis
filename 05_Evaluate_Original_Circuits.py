# 05: Evaluate original circuit for different qubit sizes

qubit_sizes = [4, 8, 12, 16]

original_results = []

for n in qubit_sizes:

    qc = create_original_circuit(n)

    depth, gate_count = calculate_metrics(qc)

    single_qubit_gates = qc.count_ops().get("h", 0)
    two_qubit_gates = qc.count_ops().get("cx", 0)

    original_results.append([
        n,
        depth,
        gate_count,
        single_qubit_gates,
        two_qubit_gates
    ])

original_df = pd.DataFrame(
    original_results,
    columns=[
        "Qubits",
        "Original Circuit Depth",
        "Gate Count",
        "Single-Qubit Gates",
        "Two-Qubit Gates"
    ]
)

original_df
