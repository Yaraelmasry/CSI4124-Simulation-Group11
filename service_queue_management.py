import simpy
import environment_setup  # Import the environment_setup module

def serve_customer(env, customer, server):
    """Process to serve a customer."""
    with server.request() as request:
        yield request
        customer.start_service_time = env.now  # Set start service time here
        customer.wait_time = env.now - customer.arrival_time
        print(f"{env.now}: Customer {customer.name} starts service.")
        yield env.timeout(customer.service_time)
        customer.service_end_time = env.now
        print(f"{env.now}: Customer {customer.name} completes service.")

def setup_and_run(env, customers, num_servers):
    # Create server resources
    server = simpy.Resource(env, capacity=num_servers)

    # Schedule customer arrivals and processing
    for customer in customers:
        env.process(serve_customer(env, customer, server))

    # Run the simulation
    env.run()

    # Calculate and print basic performance metrics
    calculate_performance_metrics(customers)

def calculate_performance_metrics(customers):
    total_served = len(customers)
    total_wait_time = sum(customer.wait_time for customer in customers if customer.wait_time is not None)
    average_wait_time = total_wait_time / total_served if total_served > 0 else 0

    print(f"\nTotal number of customers served: {total_served}")
    print(f"Average wait time per customer: {average_wait_time:.2f}")

if __name__ == "__main__":
    # Create the simulation environment
    env = simpy.Environment()

    # Assuming that generate_customers function is available from environment_setup
    customers = environment_setup.generate_customers(env, num_customers=10)
    num_servers = 2  # You can adjust the number of servers

    # Setup and run the service process simulation
    setup_and_run(env, customers, num_servers)
