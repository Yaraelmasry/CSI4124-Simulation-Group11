import simpy
import random

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

if __name__ == "__main__":
    # Start the simulation
    simulate_queuing_system()
