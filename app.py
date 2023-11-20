import scipy.stats as stats

# # 計算Z值為3.04的情況的P值（顯著性差異的例子）
# z_value_1 = 3.04
# p_value_1 = 1 - stats.norm.cdf(z_value_1)
#
# # 計算Z值為0.87的情況的P值（非顯著性差異的例子）
# z_value_2 = 0.87
# p_value_2 = 1 - stats.norm.cdf(z_value_2)
#
# print(f"P value for Z=3.04: {p_value_1}")
# print(f"P value for Z=0.87: {p_value_2}")
import scipy.stats as stats

# 政黨A的調查結果
n_A = 1000
支持_A = 520
p_A = 支持_A / n_A
SE_A = (p_A * (1 - p_A) / n_A) ** 0.5

# 政黨B的調查結果
n_B = 1000
支持_B = 500
p_B = 支持_B / n_B
SE_B = (p_B * (1 - p_B) / n_B) ** 0.5

# 計算兩個比率的差異及其標準誤
D = p_A - p_B
SE_D = (SE_A**2 + SE_B**2) ** 0.5

# 進行z檢定
z_value = D / SE_D
p_value = 1 - stats.norm.cdf(z_value)

print(f"政黨A支持率: {p_A}, 標準誤: {SE_A}")
print(f"政黨B支持率: {p_B}, 標準誤: {SE_B}")
print(f"支持率差異: {D}, 差異的標準誤: {SE_D}")
print(f"z值: {z_value}, p值: {p_value}")
