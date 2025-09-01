import numpy as np
x = np.array([1,2,3,4,5],np.float64)
y = np.zeros_like(x)
m = 1e-9
s = 0.0
# for i,xi in enumerate(x):
#     if xi > m:
#         s_new = s*np.exp(m-xi) + np.exp(xi-xi)
#         if i > 0:
#             y[:i] = y[:i] * s * np.exp(m-xi) / s_new#更新前列
#         y[i] = 1/s_new
#         m,s = xi,s_new
#     else:
#         e = np.exp(xi-m)
#         s_new = s + e
#         if i > 0:
#             y[:i] = y[:i]*s / s_new #更新前列
#         y[i] = e/s_new
#         s = s_new
#     print(f"i is {i}, xi is {xi},y is {y}")
# print(f"y is {y}")

# ref = np.exp(x - x.max()); ref /= ref.sum()
# print("max abs diff =", np.max(np.abs(y - ref)))
for i,xi in enumerate(x):
    

