import subprocess as sub
from time import time
import os

os.chdir("..")

threads = [2**i for i in range(5)]
TRIALS = 5

# key=thread_count, value=time_taken
data = {}

for t in threads:
	print(f"ATTEMPTING {t} threads")
	print("---------------")
	avg = 0
	for i in range(TRIALS):
		print(f"TRIAL #{i}\n----------------\n")
		command = f"./examples/serial/idaHeat2D_sps {t} 100"
		start = time()
		sub.run(command, shell=True)
		end = time()
		duration = (end-start)
		avg += duration

		print(f"----------------\nTRIAL #{i}: {duration}s\n-------------------")

	print("\n")
	avg /= TRIALS
	data[t]=avg

print(data)
with open("Slu_thread.txt", 'w') as f:
	for key, value in data.items():
		f.write("{key},{value}\n")

