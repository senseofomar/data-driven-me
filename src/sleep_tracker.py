import matplotlib.pyplot as plt

def plot_sleep(days, hours):
    plt.figure(figsize=(10, 5))
    plt.bar(days, hours, color='navy')
    plt.title("Sleep Tracker")
    plt.xlabel("Day")
    plt.ylabel("Hours Slept")
    plt.ylim(0, 10)
    plt.grid(axis='y', linestyle='-.', alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sample_hours = [6, 4, 2, 5, 7, 3, 4]
    plot_sleep(sample_days, sample_hours)