# 11: Display original and parallelized circuits

n = 8

original_circuit = create_original_circuit(n)
parallelized_circuit = create_parallelized_circuit(n)

print("ORIGINAL CIRCUIT")
print(original_circuit)

print("\nORIGINAL CIRCUIT DEPTH:")
print(original_circuit.depth())

print("\nPARALLELIZED CIRCUIT")
print(parallelized_circuit)

print("\nPARALLELIZED CIRCUIT DEPTH:")
print(parallelized_circuit.depth())
