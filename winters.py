class Winters:
    def __init__(self):
        pass
    def train(self, data, m, alpha, beta, gamma):
        if m < 2: raise ValueError('number of seasons must be minimum 2')
        if not isinstance(data, list) or any(not isinstance(value, float) for value in data):
            raise ValueError('data must be a list of floats or integers')
        if not (0<=alpha<=1 and 0<=beta<=1 and 0<=gamma<=1):
            raise ValueError('alpha, beta & gamma must be between 0 and 1')

        self.data = data
        self.nb_seasons = m
        self.alpha, self.beta, self.gamma = alpha, beta, gamma
        L, S, T, F = [[0 for _ in range(len(data))] for _ in range(4)]

        i = 0
        S[i] = data[0] / sum(data[:m])
        L[i] = sum(data[:m])
        T[i] = (sum(data[m:2 * m]) - sum(data[:m])) / 4
        F[i] = data[0]

        for i in range(1, len(data)):
            S[i] = data[i] / sum(data[i//m * m:(i//m + 1) * m])
            L[i] = alpha * (data[i] / S[i]) + (1 - alpha) * (L[i - 1] + T[i - 1])
            T[i] = beta * (L[i] - L[i - 1]) + (1 - beta) * T[i - 1]
            F[i] = (L[i - 1] + T[i - 1]) * S[i]
        self.components = {'level': L, 'trend': T, 'seasonality': S}
        self.forecasted = F

    def forcast(self, n: int):
        if self.forecasted is None:
            raise RuntimeError('Model is not trained yet. use Winters.train() method before forecasting')
        if not isinstance(n, int) or n < 1:
            raise ValueError('n must be a positive integer')

        L, T, S = [nums.extend([0 for _ in range(n)]) for nums in self.components.values()]
        F = self.forecasted
        m = self.nb_seasons
        for i in range(len(data), len(data) + n):
            F.append((L[i - 1] + T[i - 1]) * S[i - m])
            L[i] = alpha * (F[i] / S[i - m]) + (1 - alpha) * (L[i - 1] + T[i - 1])
            T[i] = beta * (L[i] - L[i - 1]) + (1 - beta) * T[i - 1]
            S[i] = gamma * (F[i]/L[i]) + (1 + gamma) * S[i - m]
        result = F[len(data):]
        self.forecasted = F[:len(data)]
        return result
        

    def score(self):
        if self.forecasted is None:
            raise RuntimeError('Model is not trained yet. use Winters.train() method before evaluating it')
        mad = sum([abs(self.data[i] - self.forecasted[i]) for i in range(len(self.data))])
        msd = sum([(self.data[i] - self.forecasted[i])**2 for i in range(len(self.data))])
        mape = 100 * sum([abs(self.data[i] - self.forecasted[i])/self.data[i] for i in range(len(self.data))])
        return {'MAD': mad, 'MSD': msd, 'MAPE': mape}
