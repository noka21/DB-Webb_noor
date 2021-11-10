"""
here
"""

def calculate_energy_return(time_in_micro, effect):
    """
    Calculates the energy consumption i kWh
    """
    energy = effect * time_in_micro / 1000
    return energy


def calculate_cost(energy, price_per_kwh=78.04):
    """
    Calculates the cost for a given energy consumption
    Returns the cost in kr
    """
    cost = energy * price_per_kwh/100
    return cost

noor_time = 2.5 / 60
ali_time = 3.5 / 60
hassan_and_alaa_time = 0.5 / 60



noor_energy = calculate_energy_return(noor_time, 800)
ali_energy=calculate_energy_return(ali_time, 800)
hassan_and_alaa_energy = calculate_energy_return(hassan_and_alaa_time, 600)

noor_cost=calculate_cost(noor_energy)
ali_cost=calculate_cost(ali_energy)
hassan_and_alaa_cost=calculate_cost(hassan_and_alaa_time)
print(f"Noor uses {noor_energy:.4f} kwh and that costs {noor_cost:.4f}")
