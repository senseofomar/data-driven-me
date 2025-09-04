import matplotlib.pyplot as plt


# Sample data
sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sample_diet = ["No sugar", "Sugar", "Sugar", "No sugar", "No sugar", "No sugar", "Sugar"]

# Convert categorical diet to numeric (Sugar=1, No sugar=0)
diet_numeric = [0 if d == "No sugar" else 1 for d in sample_diet]

# Count categories for pie chart
sugar_count = sample_diet.count("Sugar")
no_sugar_count = sample_diet.count("No sugar")

# Example sugar grams for histogram
sugar_grams = [0, 30, 45, 0, 0, 10, 50]

# Create 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# --- 1. Bar Chart ---
axs[0, 0].bar(sample_days, diet_numeric, color="yellow")
axs[0, 0].set_title("Bar Chart: Sugar Intake (1=Yes, 0=No)")
axs[0, 0].set_ylabel("Sugar")
axs[0, 0].set_ylim(-0.1, 1.1)
axs[0, 0].set_yticks([0, 1], ["No", "Yes"])

# --- 2. Histogram ---
axs[0, 1].hist(sugar_grams, bins=5, color="skyblue", edgecolor="black")
axs[0, 1].set_title("Histogram: Sugar Grams")
axs[0, 1].set_xlabel("Sugar grams")
axs[0, 1].set_ylabel("Frequency")

# --- 3. Pie Chart ---
axs[1, 0].pie([sugar_count, no_sugar_count],
              labels=["Sugar", "No sugar"],
              autopct="%1.1f%%",
              colors=["red", "green"])
axs[1, 0].set_title("Pie Chart: Sugar Days")

# --- 4. Line Plot ---
axs[1, 1].plot(sample_days, diet_numeric, marker="o", linestyle="-", color="purple")
axs[1, 1].set_title("Line Plot: Daily Sugar Tracking")
axs[1, 1].set_ylabel("Sugar Intake")
axs[1, 1].set_yticks([0, 1], ["No", "Yes"])
axs[1, 1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()


#Line Plot - Trends over time

sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# Convert categories to numbers: Sugar=1, No sugar=0
diet_numeric = [0, 1, 1, 0, 0, 0, 1]

plt.figure(figsize=(8, 5))
plt.plot(sample_days, diet_numeric, marker='o', linestyle='-', color='purple')
plt.title("Sugar Tracking (1=Sugar, 0=No Sugar)")
plt.xlabel("Day")
plt.ylabel("Sugar Intake")
plt.yticks([0, 1], ["No sugar", "Sugar"])  # map back to labels
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

#Pie chart - Proportions

sample_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sample_diet = ["No sugar", "Sugar", "Sugar", "No sugar", "No sugar", "No sugar", "Sugar"]
sugar_count = sample_diet.count("Sugar")
no_sugar_count = sample_diet.count("No sugar")

plt.figure(figsize=(6, 6))
plt.pie([sugar_count, no_sugar_count],
        labels=["Sugar", "No sugar"],
        autopct='%1.1f%%',
        colors=["red", "green"])
plt.title("Sugar vs No Sugar Days")
plt.show()

#Histogram - distributions of numeric data

sugar_grams = [0, 30, 45, 0, 0, 10, 50]  # numeric sugar intake

plt.figure(figsize=(8, 5))
plt.hist(sugar_grams, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Sugar Intake")
plt.xlabel("Sugar grams")
plt.ylabel("Frequency")
plt.show()
