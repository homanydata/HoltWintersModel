data = [53, 22, 37, 45, 58, 25, 40, 50, 62, 27, 44, 56]
m = 4
alpha = 0.2
beta = 0.3
gamma = 0.5
steps = 4
L, S, T, F = [[0 for _ in range(len(data) + steps)] for _ in range(4)]

i = 0
S[i] = round(data[0] / sum(data[:m]), 2)
L[i] = 156
T[i] = (sum(data[m:2 * m]) - sum(data[:m])) / 4
F[i] = data[0]

# existing data
for i in range(1, len(data)):
    S[i] = round(data[i] / sum(data[i//m * m:(i//m + 1) * m]), 2)
    L[i] = round(alpha * (data[i] / S[i]) + (1 - alpha) * (L[i - 1] + T[i - 1]), 2)
    T[i] = round(beta * (L[i] - L[i - 1]) + (1 - beta) * T[i - 1], 2)
    F[i] = round((L[i - 1] + T[i - 1]) * S[i], 2)
# future
for i in range(len(data), len(data) + steps):
    F[i] = round((L[i - 1] + T[i - 1]) * S[i - m], 2)
    L[i] = round(alpha * (F[i] / S[i - m]) + (1 - alpha) * (L[i - 1] + T[i - 1]), 2)
    T[i] = round(beta * (L[i] - L[i - 1]) + (1 - beta) * T[i - 1], 2)
    S[i] = round(gamma * (F[i]/L[i]) + (1 + gamma) * S[i - m], 2)


# mean = lambda x: round(sum(x)/len(x), 2)
# n = 3
# MA = [mean(data[i-n//2:i+(n-n//2)]) if len(data) - n//2 > i >= n//2 else 0 for i in range(len(data))]
mad = sum([abs(data[i] - F[i]) for i in range(len(data))])
msd = sum([(data[i] - F[i])**2 for i in range(len(data))])
mape = 100 * sum([abs(data[i] - F[i])/data[i] for i in range(len(data))])
print(f'level: {L}\nseasonality: {S}\ntrend: {T}\nforecast: {F}\ndata:{data}\nMA: {MA}\nMAD: {mad}\nMSD:{msd}\nMAPE:{mape}')
