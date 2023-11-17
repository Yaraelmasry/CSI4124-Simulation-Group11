#Possion Arrival Process

import simpy
import random
import matplotlib.pyplot as plt

def generator(env, rate,arrivals):
    num_arrival = 0
    while True:
        yield env.timeout(random.expovariate(rate))
        num_arrival += 1
        #print(num_arrival, env.now)
        arrivals.append(env.now)

env = simpy.Environment()
arrival_times = []
env.process(generator(env, 1,arrival_times))
print('Customer','Arrival time')
env.run(until=20) #sample of 20

plt.figure(figsize=(8, 5))
plt.plot(arrival_times, marker='o', linestyle='-', color='blue')
plt.xlabel('Customers')
plt.ylabel('Arrival Time')
plt.title('Poisson Arrival Process')
plt.grid(True)
plt.show()