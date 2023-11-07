import numpy as np
import matplotlib.pyplot as plt

# ホワイトノイズのサンプル数を設定
sample_size = 1000

# ホワイトノイズを生成
white_noise = np.random.normal(0, 1, sample_size)

# 平均を計算
mean = np.mean(white_noise)

# プロットの設定
plt.figure(figsize=(10, 5))
plt.plot(white_noise, color='b', label='White Noise')
plt.axhline(y=mean, color='r', linestyle='-', label='Mean')
plt.title('Stationary Data Examples (White Noise)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
plt.savefig('white_noise_with_mean_plot.png')

# プロットを表示
plt.show()
