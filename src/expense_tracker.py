import matplotlib.pyplot as plt

def plot_expenses(days, expenses):
    plt.figure(figsize=(10, 5))
    plt.bar(days, expenses, color='darkorange')
    plt.title(" Expense Tracker")
    plt.xlabel("Day")
    plt.ylabel("Expenses (₹)", rotation=0, labelpad=40)
    plt.ylim(0, max(expenses) + 100)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sample_expenses = [200, 450, 150, 300, 100, 500, 250]
    plot_expenses(sample_days, sample_expenses)
