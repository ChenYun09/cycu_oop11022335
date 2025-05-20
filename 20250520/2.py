import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('20250520/midterm_scores.csv')

# Subjects and colors
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# Define bins: 0-9, 10-19, ..., 90-100
bins = np.arange(0, 110, 10)
bin_labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]

# Calculate histogram data for each subject
hist_data = {subject: np.histogram(df[subject], bins=bins)[0] for subject in subjects}

# Prepare data for grouped bar chart
x = np.arange(len(bin_labels))  # the label locations
width = 0.1  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(figsize=(12, 8))

# Plot each subject's histogram as a group of bars
for subject, color in zip(subjects, colors):
    offset = width * multiplier
    rects = ax.bar(x + offset, hist_data[subject], width, label=subject, color=color)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Score Range')
ax.set_ylabel('Number of Students')
ax.set_title('Score Distribution by Subject')
ax.set_xticks(x + width * (len(subjects) - 1) / 2, bin_labels)
ax.legend(loc='upper right', ncols=2)
ax.set_ylim(0, max(max(hist_data[subject]) for subject in subjects) + 5)

plt.tight_layout()
plt.savefig('20250520/subject_score_distribution.png')
plt.show()