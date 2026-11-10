import pandas as pd

#Create fictional student dataset
data = {
    'Student ID': ['ST001','ST002','ST003','ST004','ST005'],
    'Department': ['Computer Science', 'Cybersecurity', 'Computer Science', 'Computer Science', 'Cybersecurity'],
    'Level': [100, 200, 200, 100, 300],
    'Attendance': [92, 85, 95, 70, 88],
    'Average Examination Score': [78, 71, 84, 58, 76]
}

df = pd.DataFrame(data)

#Display the dataset
print(df)

#Calculate the average score
print("\nAverage Score:", df['Average Examination Score'].mean())
print("\nAverage Attendance:", df['Attendance'].mean())
