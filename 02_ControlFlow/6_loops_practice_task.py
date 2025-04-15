def calculate_total(spending_list):
    return sum(spending_list)

def budget_feedback(total, budget):
    if total <= budget:
        return "Great! You're within your budget."
    else:
        return f"Oops! You exceeded your budget by {total - budget} units."

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
spending = []

for day in days:
    amount = float(input(f"Enter grocery spending for {day}: "))
    spending.append(amount)

total_spent = calculate_total(spending)
print(f"\nTotal Spending: {total_spent}")
print(budget_feedback(total_spent, budget=200))
