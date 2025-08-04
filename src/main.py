
from mood_tracker import plot_mood
from sleep_tracker import plot_sleep
from expense_tracker import plot_expenses
from screentime_tracker import plot_screentime
from productivity_tracker import plot_productivity

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
mood = [6, 4, 2, 5, 7, 3, 4]  # Scale: 1 = 😔, 7 = 😄
hours = [6.5, 7, 5.5, 8, 6, 9, 7.5]
expenses = [200, 450, 150, 300, 100, 500, 250]
screen_hours = [4.5, 6, 5, 7.5, 3.5, 8, 6.5]
productivity = [8, 6, 7, 5, 9, 4, 8]

if __name__ == '__main__':
    plot_mood(days, mood)
    plot_sleep(days, hours)
    plot_expenses(days, expenses)
    plot_screentime(days, screen_hours)
    plot_productivity(days, productivity)
