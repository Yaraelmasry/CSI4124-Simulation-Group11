import simpy
import random
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import environment_setup


# Initialize variables to track server status
server_status = []
server_busy = False



def customer(env, name, store, arriving_time, service_time):

    global server_busy, server_status 


    # Simulate arriving time to the store
    yield env.timeout(arriving_time)

    #Request one of its available servers
    print('%s arriving at %d' % (name, env.now))
    with store.request() as req:
        yield req

        # Charge the battery
        print('%s getting service at %s' % (name, env.now))
        server_busy = True ##
        server_status.append(1) ##

        yield env.timeout(service_time)
        print('%s leaving the store at %s' % (name, env.now))
        server_busy = False ##
        server_status.append(0) ##

env = simpy.Environment()
##store = simpy.Resource(env, capacity=2)


#sample of 20 customers
for i in range(20):
    env.process(customer(env, 'Customer %d' % i, store , i*2, 5))

env.run()

# Plotting server utilization over time
plt.figure(figsize=(8, 5))
plt.step(range(len(server_status)), server_status, where='post', color='blue')
plt.xlabel('Time')
plt.ylabel('Server Status (Busy: 1, Idle: 0)')
plt.title('Server Utilization over Time')
plt.ylim(-0.5, 1.5)
plt.grid(True)
plt.show()