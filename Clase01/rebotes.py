height = 100
n_rebotes = 10
for i in range(n_rebotes + 1):
	print("rebote " + str(i) + ": " + str(round(height,4)))
	height = 3*height/5