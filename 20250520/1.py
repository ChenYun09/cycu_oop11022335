import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV data
df = pd.read_csv('20250520/midterm_scores.csv')

# Subjects to check
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']

# Calculate total score
df['TotalScore'] = df[subjects].sum(axis=1)

# Define passing score
passing_score = 60

# Count the number of failed subjects for each student
df['FailedSubjects'] = (df[subjects] < passing_score).sum(axis=1)

# Find students with four or more subjects failed
threshold = 4
failed_students = df[df['FailedSubjects'] >= threshold][['Name', 'StudentID']]

# Export failed students to a CSV file
failed_students.to_csv('20250520/failed_students.csv', index=False)

print("Students with four or more subjects failed have been saved to '20250520/failed_students.csv'.")

# Define colors for each subject
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# Create a bar chart for each subject
x = np.arange(len(df['StudentID']))  # X-axis positions for students
bar_width = 0.1  # Width of each bar

plt.figure(figsize=(12, 8))

# Plot each subject as a separate bar group
for i, (subject, color) in enumerate(zip(subjects, colors)):
    plt.bar(x + i * bar_width, df[subject], width=bar_width, label=subject, color=color)

# Add labels, legend, and title
plt.xlabel('Student ID')
plt.ylabel('Scores')
plt.title('Scores for All Subjects')
plt.xticks(x + bar_width * (len(subjects) - 1) / 2, df['StudentID'], rotation=45)  # Center the ticks
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot to a file
plt.tight_layout()
plt.savefig('20250520/subject_scores_bar_chart.png')

print("The bar chart for all subjects has been saved to '20250520/subject_scores_bar_chart.png'.")

# Define score bins (e.g., 0-10, 10-20, ..., 90-100)
bins = np.arange(0, 110, 10)

# Create a histogram for each subject
plt.figure(figsize=(12, 8))
for subject, color in zip(subjects, colors):
    plt.hist(df[subject], bins=bins, alpha=0.7, label=subject, color=color, edgecolor='black')

# Add labels, legend, and title
plt.xlabel('Score Ranges')
plt.ylabel('Number of Students')
plt.title('Distribution of Scores by Subject')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot to a file
plt.tight_layout()
plt.savefig('20250520/score_distribution_histogram.png')

print("The histogram for score distribution has been saved to '20250520/score_distribution_histogram.png'.")
