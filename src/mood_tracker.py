import matplotlib.pyplot as plt

def plot_mood(days, mood):
    plt.figure(figsize=(10, 5))
    plt.bar(days, mood, color='green')
    plt.title("Mood Tracker")
    plt.xlabel("Day")
    plt.ylabel("Mood Level", rotation=0, labelpad=40)
    plt.ylim(0, 7)
    plt.grid(axis = 'y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sample_mood = [6, 4, 2, 5, 7, 3, 4]
    plot_mood(sample_days, sample_mood)