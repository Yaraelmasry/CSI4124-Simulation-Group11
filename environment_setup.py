import simpy
import random
import numpy as np

class Customer:
    def __init__(self, env, name, arrival_time, service_time):
        self.env = env
        self.name = name
        self.arrival_time = arrival_time  # Time at which the customer arrives
        self.service_time = service_time  # Time it takes to serve the customer
        self.start_service_time = None  # Time at which the customer starts receiving service
        self.wait_time = None  # Time the customer spends waiting in the queue
        self.service_end_time = None  # Time at which the service for the customer is completed
        self.satisfaction = None  # Level of customer satisfaction (can be calculated later)
        self.service_cost = None #cost of providing customer
        self.dissatisfaction_cost = None #cost duue to customer dissatisfaction

    def calculate_satisfaction(self):
        max_satisfaction = 10
        normal_decay_rate = 0.01  # Decay rate for wait times up to threshold_wait_time seconds
        increased_decay_rate = 0.1  # Steeper decay rate for wait times beyond threshold_wait_time seconds
        threshold_wait_time = 120  # Threshold in seconds

        if self.wait_time <= threshold_wait_time:
            # Apply normal decay rate for wait time up to threshold_wait_time seconds
            self.satisfaction = max_satisfaction * np.exp(-normal_decay_rate * self.wait_time)
        else:
            # Calculate satisfaction at threshold_wait_time seconds
            satisfaction_at_threshold = max_satisfaction * np.exp(-normal_decay_rate * threshold_wait_time)
            # Apply increased decay rate beyond threshold_wait_time seconds
            additional_wait_time = self.wait_time - threshold_wait_time
            self.satisfaction = satisfaction_at_threshold * np.exp(-increased_decay_rate * additional_wait_time)

        self.satisfaction = min(self.satisfaction, max_satisfaction)

def customer_arrival(env, customer):
    # Simulate customer arrival
    yield env.timeout(customer.arrival_time)
    customer.start_service_time = env.now
    print(f"{env.now}: Customer {customer.name} arrives.")

def initial_analysis(customers):
    # Perform initial analysis on generated customers
    for customer in customers:
        print(f"Customer {customer.name} - Arrival Time: {customer.arrival_time}")

def simulate_queuing_system():
    # Initialize simulation environment
    env = simpy.Environment()

    # Generate a list of customers with random arrival and service times
    customers = generate_customers(env, num_customers=5)

    # Schedule customer arrivals and processing
    for customer in customers:
        env.process(customer_arrival(env, customer))
    
    # Run the simulation
    env.run()

    # Perform initial analysis on the generated customers
    initial_analysis(customers)

def generate_customers(env, num_customers):
    # Generate a list of customers with random arrival and service times
    customers = []
    for i in range(num_customers):
        # Example: Exponential distribution for arrival times
        arrival_time = random.expovariate(1.0 / 5)  
        
        # Example: Uniform distribution for service times
        service_time = random.uniform(5, 15)  
        
        customers.append(Customer(env, f"{i + 1}", arrival_time, service_time))
    return customers



