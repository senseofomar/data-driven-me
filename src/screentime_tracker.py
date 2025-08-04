import matplotlib.pyplot as plt

def plot_screentime(days, hours):
    plt.figure(figsize=(10, 5))
    plt.bar(days, hours, color='skyblue')
    plt.title("Screen Time Tracker")
    plt.xlabel("Day")
    plt.ylabel("Hours on Screen", rotation=0, labelpad=40)
    plt.ylim(0, max(hours) + 1)
    plt.grid(axis="y", linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sample_screen_hours = [4.5, 6, 5, 7.5, 3.5, 8, 6.5]
    plot_screentime(sample_days, sample_screen_hours)
