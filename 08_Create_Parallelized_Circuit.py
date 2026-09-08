# 08: Create parallelized quantum circuit

def create_parallelized_circuit(n):
    qc = QuantumCircuit(n)

    for q in range(n):
        qc.h(q)

    for start in [0, 1]:

        for q in range(start, n - 1, 2):
            qc.cx(q, q + 1)

    return qc
