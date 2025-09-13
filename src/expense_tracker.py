import matplotlib.pyplot as plt

def plot_expenses(income, expenses, savings):
    plt.figure(figsize = (10, 5))
    plt.pie([income, expenses, savings],
            labels = ["Income", "Expenses", "Savings"],
            autopct ="%1.1f%%",
            colors = ["Blue","Red", "Green"])
    plt.title("Finances")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    sample_income = 84000
    sample_expenses = 50000
    sample_savings = 34000
    plot_expenses(sample_income, sample_expenses, sample_savings)
