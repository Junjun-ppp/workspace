import numpy as np
import matplotlib.pyplot as plt

# ランダムウォークのサンプル数を設定
sample_size = 1000

# ランダムウォークを生成
random_walk = np.cumsum(np.random.normal(0, 1, sample_size))

# プロットの設定
plt.figure(figsize=(10, 5))
plt.plot(random_walk, color='r', label='Random Walk')
plt.title('(Non-Stationary Data Examples (Random Walk)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)

# プロットをファイルに保存
plt.savefig('random_walk_plot.png')

# プロットを表示
plt.show()
