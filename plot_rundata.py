from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("rundata.csv")
# removed unnamed cols
flt = ~df.columns.str.contains("^Unnamed")
df = df.loc[:, flt]

x = list(range(20, 160, 10))

for col in df.columns:
    plt.plot(x, df[col], label=col, marker='o')

plt.xlabel("Mesh Size (nxn)")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time vs Mesh Size (for diff. solvers)")
plt.legend()
plt.grid()
plt.show()
