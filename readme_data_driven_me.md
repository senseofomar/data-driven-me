# 📊 data-driven-me

**Track and visualize your life through personal data.** This project helps you reflect on your habits by plotting how you feel, sleep, spend, scroll, and work—week by week.

---

## 💼 Who is this for?

- Students learning Python & data visualization
- Productivity enthusiasts and habit trackers
- Anyone who wants to make sense of their everyday patterns

---

## 🔄 What does it track?

### 1. 🧠 Mood Tracker

Visualizes how your mood changes throughout the week. Instantly spot emotional highs and lows.

### 2. 🛌 Sleep Tracker

Monitors your sleep duration to highlight patterns that affect your health and focus.

### 3. 💸 Expense Tracker

Helps you track daily spending so you can budget and allocate finances better.

### 4. 📱 Screen Time Tracker

Tells you how much time you spent on social media, streaming, or working on your computer.

### 5. ✅ Productivity Tracker

Measures how productive your days were, helping you assess your overall focus and accountability.

---

## 💡 Features

- Simple, clear bar charts for each life metric
- One week = One plot per tracker
- Modular design: each tracker has its own Python file

---

## 📝 How to Use

### Option 1: Run with Sample Data (default)

Each tracker module (e.g., `mood_tracker.py`) includes a `plot_*()` function with sample data. Run the file directly or call the function in `main.py`.

### Option 2: Add Your Own Data

To add your real data:

1. Replace the sample lists (`days`, `mood`, etc.) in `main.py`
2. Or prepare a CSV/JSON file (coming soon!)

---

## 🛠️ Tech Stack

- Python 3
- `matplotlib` for plotting
- (Coming soon) `pandas` for CSV parsing
- (Coming soon) `numpy` for analysis

---

## 📂 File Structure

```
data-driven-me/
├── src/
│   ├── main.py
│   ├── mood_tracker.py
│   ├── sleep_tracker.py
│   ├── expense_tracker.py
│   ├── screentime_tracker.py
│   └── productivity_tracker.py
├── data/               ← (empty for now, will hold CSV/JSON files later)
└── requirements.txt
```

---

## ✨ Future Plans

- Add CSV/JSON support
- Combine all plots into a single dashboard
- Save plots automatically as image files

---

## 🚀 Getting Started

1. Clone the repo:

```bash
git clone https://github.com/your-username/data-driven-me.git
cd data-driven-me
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python src/main.py
```

---

## ❤️ Contributing

Got ideas? Feel free to fork and submit a pull request.

---

## 🎉 License

This project is open source under the MIT License.

---

Track what matters. Reflect on patterns. Make better choices.

🚀 Let's visualize your life!

