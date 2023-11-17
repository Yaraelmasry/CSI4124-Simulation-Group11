import simpy
import random
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import cost_model
import environment_setup
"""
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


"""

def customer(env, name, store,arriving_time, service_time):
    # Simulate arriving time to the store
    yield env.timeout(arriving_time)

    # Request one of its charging spots
    print('%s arriving at %d' % (name, env.now))
    with store.request() as req:
        yield req

        # Charge the battery
        print('%s getting service at %s' % (name, env.now))
        yield env.timeout(service_time)
        print('%s leaving the store at %s' % (name, env.now))


env = simpy.Environment()
store = simpy.Resource(env, capacity=2)


for i in range(4):
    env.process(customer(env, 'Customer %d' % i, store, i*2, 5))


env.run()
