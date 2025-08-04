import matplotlib.pyplot as plt

def plot_productivity(days, productivity):
    plt.figure(figsize=(10, 5))
    plt.bar(days, productivity, color= 'purple')
    plt.grid(axis= 'y', linestyle='--', alpha=0.3)
    plt.xlabel('Days')
    plt.ylabel('Productivity', rotation=0, labelpad=40)
    plt.ylim(0,24)
    plt.title('Productivity Tracker')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sample_productivity = [8, 6, 7, 5, 9, 4, 8]
    plot_productivity(sample_days, sample_productivity)