import numpy as np 

P = np.array([
    [0.88,   0.08,   0.02,   0.01,   0.005,  0.003,  0.001,  0.001],  # AAA
    [0.04,   0.85,   0.06,   0.03,   0.01,   0.005,  0.003,  0.002],  # AA
    [0.01,   0.06,   0.80,   0.08,   0.03,   0.01,   0.008,  0.002],  # A
    [0.005,  0.02,   0.07,   0.75,   0.10,   0.03,   0.02,   0.005],  # BBB
    [0.002,  0.01,   0.03,   0.10,   0.70,   0.10,   0.05,   0.008],  # BB
    [0.001,  0.005,  0.015,  0.04,   0.15,   0.60,   0.15,   0.039],  # B
    [0.0,    0.002,  0.008,  0.03,   0.10,   0.16,   0.50,   0.20 ],  # CCC
    [0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0,    1.0  ]   # D
])


#Si on est en AAA 
def state_n(P , S_0, n) : 
    S_n = S_0 @ np.linalg.matrix_power(P , n)
    return np.round(S_n , 3)

print(state_n(P , [1,0,0,0,0,0,0,0] , 1000))


import yfinance as yf
import numpy as np
from hmmlearn import hmm
import matplotlib.pyplot as plt

data = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

returns = np.log(data["Close"] / data["Close"].shift(1)).dropna().values.reshape(-1, 1)

model = hmm.GaussianHMM(n_components=3, n_iter=200)
model.fit(returns)

hidden_states = model.predict(returns)

plt.figure(figsize=(10,5))
plt.scatter(range(len(returns)), 
            returns, 
            c=hidden_states, 
            cmap="viridis", 
            s=2)
plt.title("Régimes cachés (HMM) sur Apple")
plt.show()
