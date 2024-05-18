def calculate_net_gain_loss(parent1_net_income, parent2_net_income, childcare_costs, expenses):
    total_income = parent1_net_income + parent2_net_income
    net_gain_loss = total_income - childcare_costs - expenses
    return net_gain_loss
