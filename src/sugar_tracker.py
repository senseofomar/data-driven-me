import matplotlib.pyplot as plt


def plot_sugar(days, diet):
    plt.figure(figsize=(10, 5))
    plt.bar(days, diet, color ='yellow')
    plt.title("Diet Tracker")
    plt.xlabel("Day")
    plt.ylabel("Diet")
    plt.ylim("No sugar", "Sugar")
    plt.grid(axis ='y', linestyle = "-", alpha = 0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sample_days =['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sample_diet=["No sugar", "Sugar", "Sugar", "No sugar", "No sugar", "No sugar", "Sugar"]
    plot_sugar(sample_days, sample_diet)