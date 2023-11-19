import simpy
import environment_setup  # Import the environment_setup module

def serve_customer(env, customer, server):
    """Process to serve a customer."""
    with server.request() as request:
        yield request
        customer.start_service_time = env.now
        customer.wait_time = env.now - customer.arrival_time

        yield env.timeout(customer.service_time)
        customer.service_end_time = env.now

        # Calculate satisfaction and cost after service
        customer.calculate_satisfaction()  # Ensure this method is defined in Customer class


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
    simulation_duration = env.now
    return simulation_duration

def calculate_performance_metrics(customers):
    total_served = len(customers)
    total_wait_time = sum(customer.wait_time for customer in customers if customer.wait_time is not None)
    average_wait_time = total_wait_time / total_served if total_served > 0 else 0

    print(f"\nTotal number of customers served: {total_served}")
    print(f"Average wait time per customer: {average_wait_time:.2f}")

