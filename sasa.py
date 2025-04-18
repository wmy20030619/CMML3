import numpy as np
import matplotlib.pyplot as plt

# 读取野生型和突变体的 SASA 数据
time_wt, sasa_wt = np.loadtxt("C:/Users/31937/Downloads/sasa_original.xvg", comments=["@","#"], unpack=True)
time_mut, sasa_mut = np.loadtxt("C:/Users/31937/Downloads/sasa_G99D.xvg", comments=["@","#"], unpack=True)

# 计算 ΔSASA = SASA_mutant - SASA_wt
delta_SASA = sasa_mut - sasa_wt

# 保存数据
np.savetxt("delta_SASA.xvg", np.column_stack((time_wt, delta_SASA)), header="Time (ps)\tdelta_SASA (nm2)")

# 绘制 ΔSASA 随时间变化
plt.plot(time_wt, delta_SASA, label="delta_SASA (Mut - WT)", color="blue")
plt.xlabel("Time (ps)")
plt.ylabel("delta_SASA (nm2)")
plt.title("SASA Change due to Mutation")
plt.legend()
plt.show()