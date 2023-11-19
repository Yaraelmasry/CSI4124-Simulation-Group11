import simpy
import random
import matplotlib as plt
import environment_setup #importing environment setup module

class Customer(environment_setup.Customer):
    def __init__(self, env, name, arrival_time, service_time):
        super().__init__(env, name, arrival_time, service_time)
        self.service_cost = None #cost of providing customer
        self.dissatisfaction_cost = None #cost duue to customer dissatisfaction 


    def calculate_cost(self):
        if self.satisfaction is None:
             #calculate satisfaction level// to be implemented in #3
            self.satisfaction = self.calculate_satisfaction()


        #define cost factors
        cost_per_unit_serv_time = 10 # cost per unit service time
        dissatisfaction_penalty = 20 # Penalty for dissatisfaction to be adjusted later 


        #calculating service cost based on service time
        self.service_cost = cost_per_unit_serv_time * self.service_time

        #calculating dissatisfaction based on satisfaction level
        self.dissatisfaction_cost = dissatisfaction_penalty * (10 - self.satisfaction)
        #assuming satisfaction scale is from 1-10



        #Total cost for customer
        total_cost = self.service_cost + self.dissatisfaction_cost
        return total_cost
    
class Simulation_parameters: #configuring parameter values
    arrival_rate = 1.0/5
    min_service_time = 5
    max_service_time = 15
    cost_per_unit_serv_time = 10
    dissatisfaction_penalty =20 

#user interface for parameter input 
def get_user_input():
    print("Enter simulation parameters:")
    arrival_rate = float(input("Arrival rate for generating customers: "))
    min_service_time = float(input("Minimum service time for customers: "))
    max_service_time = float(input("Maximum service time for customers: "))
    cost_per_unit_service_time = float(input("Cost per unit of service time: "))
    dissatisfaction_penalty = float(input("Penalty for customer dissatisfaction: "))

    return SimulationParameters(arrival_rate, min_service_time, max_service_time, cost_per_unit_service_time, dissatisfaction_penalty)


#reporting visualization for a graphical representation 

if __name__ == "__main__":

    simulation_params = get_user_input()

    env = simpy.Environment()

    customers = environment_setup.generate_customers(env, num_customers=10)
    num_servers = 2

    setup_and_run(env, customers, num_servers)

    # Visualization using matplotlib
    wait_times = [customer.wait_time for customer in customers if customer.wait_time is not None]

    plt.figure(figsize=(8, 6))
    plt.hist(wait_times, bins=10, alpha=0.7, color='skyblue')
    plt.title('Wait Time for Customers')
    plt.xlabel('Wait Time')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()





