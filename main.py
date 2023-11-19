import sys
import matplotlib.pyplot as plt
import environment_setup
import service_queue_management
import simpy
import numpy as np

def get_simulation_parameters():
    """Function to get user inputs for simulation parameters."""
    num_customers = int(input("Enter the number of customers to queue: "))
    num_servers = int(input("Enter the number of servers: "))
    return num_customers, num_servers

def run_simulation(env_setup, service_mgmt, num_customers, num_servers):
    """Function to setup and run the simulation."""
    env = simpy.Environment()
    customers = env_setup.generate_customers(env, num_customers)
    simulation_duration = service_mgmt.setup_and_run(env, customers, num_servers)
    return customers, simulation_duration

def plot_average_wait_time(customers):
    """Plot the average wait time per customer and show average."""
    wait_times = [customer.wait_time for customer in customers if customer.wait_time is not None]
    avg_wait_time = np.mean(wait_times)
    plt.hist(wait_times, bins=10, color='blue', edgecolor='black')
    plt.axvline(avg_wait_time, color='red', linestyle='dashed', linewidth=1)
    plt.title(f'Histogram of Customer Wait Times\nAverage Wait Time: {avg_wait_time:.2f} seconds')
    plt.xlabel('Wait Time')
    plt.ylabel('Number of Customers')

def plot_customer_satisfaction(customers):
    """Plot the customer satisfaction scores and show average."""
    satisfaction_scores = [customer.satisfaction for customer in customers if customer.satisfaction is not None]
    avg_satisfaction = np.mean(satisfaction_scores)
    plt.hist(satisfaction_scores, bins=10, color='green', edgecolor='black')
    plt.axvline(avg_satisfaction, color='red', linestyle='dashed', linewidth=1)
    plt.title(f'Histogram of Customer Satisfaction Scores\nAverage Score: {avg_satisfaction:.2f}')
    plt.xlabel('Satisfaction Score')
    plt.ylabel('Number of Customers')

def plot_customers_serviced_per_hour(customers, simulation_duration):
    """Plot the number of customers serviced per hour and show average."""
    service_end_times = [customer.service_end_time for customer in customers if customer.service_end_time is not None]
    hours = np.ceil(simulation_duration / 60.0)
    customers_per_hour = [0] * int(hours)
    for end_time in service_end_times:
        hour = int(np.floor(end_time / 60.0))
        customers_per_hour[hour] += 1
    avg_customers_per_hour = np.mean(customers_per_hour)
    plt.bar(range(int(hours)), customers_per_hour, color='purple')
    plt.title(f'Number of Customers Serviced per Hour\nAverage: {avg_customers_per_hour:.2f} customers/hour')
    plt.xlabel('Hour')
    plt.ylabel('Number of Customers Serviced')

def plot_results(customers, simulation_duration):
    """Function to plot the results of the simulation in subplots."""
    plt.figure(figsize=(15, 5))

    # Plot Average Wait Time
    plt.subplot(1, 3, 1)  # 1 row, 3 columns, 1st subplot
    plot_average_wait_time(customers)

    # Plot Customer Satisfaction
    plt.subplot(1, 3, 2)  # 1 row, 3 columns, 2nd subplot
    plot_customer_satisfaction(customers)

    # Plot Customers Serviced Per Hour
    plt.subplot(1, 3, 3)  # 1 row, 3 columns, 3rd subplot
    plot_customers_serviced_per_hour(customers, simulation_duration)

    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the Starbucks simulation continuously."""
    while True:
        user_input = input("Type 'run' to start simulation or 'exit' to quit: ").lower()
        if user_input == 'exit':
            print("Exiting the simulation.")
            sys.exit()
        elif user_input == 'run':
            num_customers, num_servers = get_simulation_parameters()
            customers, simulation_duration = run_simulation(environment_setup, service_queue_management, num_customers, num_servers)
            plot_results(customers, simulation_duration)
        else:
            print("Invalid input. Please type 'run' or 'exit'.")

if __name__ == "__main__":
    main()
