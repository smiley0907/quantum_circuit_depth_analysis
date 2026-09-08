# 09: Evaluate parallelized circuit for different qubit sizes

parallelized_results = []

for n in qubit_sizes:

    qc = create_parallelized_circuit(n)

    depth = qc.depth()
    gate_count = qc.size()

    single_qubit_gates = qc.count_ops().get("h", 0)
    two_qubit_gates = qc.count_ops().get("cx", 0)

    parallelized_results.append([
        n,
        depth,
        gate_count,
        single_qubit_gates,
        two_qubit_gates
    ])

parallelized_df = pd.DataFrame(
    parallelized_results,
    columns=[
        "Qubits",
        "Parallelized Circuit Depth",
        "Gate Count",
        "Single-Qubit Gates",
        "Two-Qubit Gates"
    ]
)

parallelized_df
