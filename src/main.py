
from mood_tracker import plot_mood
from sleep_tracker import plot_sleep

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
mood = [6, 4, 2, 5, 7, 3, 4]  # Scale: 1 = 😔, 7 = 😄
hours = [6.5, 7, 5.5, 8, 6, 9, 7.5]

if __name__ == '__main__':
    plot_mood(days, mood)
    plot_sleep(days, hours)