import datetime

time = datetime.datetime.now()

for i in range(1000):
	print(i)

time2 = datetime.datetime.now()

print(time)
print(time2)

long = time2 - time
print(long)
