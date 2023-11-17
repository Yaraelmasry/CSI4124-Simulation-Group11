import numpy as np

#Set random seed for reproducibility
np.random.seed(0)


import random

# Constants for inter-arrival and service time distributions
mean_interarrival = 30  # Mean inter-arrival time in seconds
std_interarrival = 6    # Standard deviation of inter-arrival time in seconds
mean_service = 20       # Mean service time in seconds
std_service = 4        # Standard deviation of service time in seconds

# Initialize variables
clock = 0
customer_number = 1
waiting_times = []
system_times = []

# Simulate the queue for the first 15 customers
while customer_number <= 15:
    # Generate inter-arrival time and service time
    interarrival_time = max(0, np.random.normal(mean_interarrival, std_interarrival))
    service_time = max(0, np.random.normal(mean_service, std_service))

    # Customer enters the system
    if clock < interarrival_time:
        clock = interarrival_time
    else:
        interarrival_time = 0

    # Calculate waiting time for the customer
    waiting_time = max(0, clock - interarrival_time)
    waiting_times.append(waiting_time)

    # Calculate total system time for the customer
    total_system_time = waiting_time + service_time
    system_times.append(total_system_time)

    # Update the clock and customer number
    clock += service_time
    customer_number += 1

# Display the results
for i in range(15):
    print(f"Customer {i+1}:")
    print(f"Waiting time for customer {i+1}: {waiting_times[i]:.2f} sec")
    print(f"Total system time for customer {i+1}: {system_times[i]:.2f} sec")
    print()

