# 04: Test original quantum circuit with 4 qubits

test_circuit = create_original_circuit(4)

print("Original Quantum Circuit:")
print(test_circuit)

depth, gate_count = calculate_metrics(test_circuit)

print("\nOriginal Circuit Depth:", depth)
print("Gate Count:", gate_count)
