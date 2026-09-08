# 03: Calculate circuit depth and gate count

def calculate_metrics(qc):
    depth = qc.depth()
    gate_count = qc.size()

    return depth, gate_count
