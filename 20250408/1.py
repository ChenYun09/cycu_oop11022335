import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# 定義參數
mu = 1.5
sigma = 0.4

# 計算對數常態分布的參數
s = sigma  # shape parameter
scale = np.exp(mu)  # scale parameter

# 定義 x 軸範圍
x = np.linspace(0.01, 10, 1000)

# 計算累積分布函數 (CDF)
cdf = lognorm.cdf(x, s, scale=scale)

# 繪製圖表
plt.figure(figsize=(8, 6))
plt.plot(x, cdf, label=f'Lognormal CDF (μ={mu}, σ={sigma})', color='blue')
plt.title('Lognormal Cumulative Distribution Function', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('CDF', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 儲存為 JPG 檔案
plt.savefig('lognormal_cdf.jpg', format='jpg', dpi=300)
plt.show()