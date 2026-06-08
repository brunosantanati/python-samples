import pandas as pd

# Create a mini-dataset of job candidates
raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Experience_Years': [2, 7, 5, 1],
    'Passed_Interview': [True, True, False, False]
}

df = pd.DataFrame(raw_data)

# Filter for candidates with more than 3 years of experience
experienced = df[df['Experience_Years'] > 3]

print("Experienced Candidates:\n", experienced)
print("\nAverage Experience:", df['Experience_Years'].mean())