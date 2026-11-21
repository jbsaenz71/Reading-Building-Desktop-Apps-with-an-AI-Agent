def manning_flow(n, A, R, S):
    """Flow (cfs) from Manning's n, area A (ft^2), hydraulic radius R (ft), and slope S (ft/ft)."""
    return 1.49 / n * A * R ** (2 / 3) * S ** 0.5
A = 20
n = 0.03
R = 2
S = 0.01
print(manning_flow(n, A, R, S))  # Example usage

A = 40
n = 0.05
R = 3
S = 0.02
print(manning_flow(n, A, R, S))  # Example usage

