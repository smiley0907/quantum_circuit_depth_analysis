# 02: Create original quantum circuit

def create_original_circuit(n):
    qc = QuantumCircuit(n)

    for q in range(n):
        qc.h(q)

    for q in range(n - 1):
        qc.cx(q, q + 1)

    return qc
