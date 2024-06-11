import json
import pandas as pd

# Load the data from the provided file
file_path = '/mnt/data/symptom_translated.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract disease names and symptoms from the data
disease_symptoms = []
for entry in data:
    instruction = entry['instruction']
    output = entry['output']
    
    # Extract disease name from the instruction
    if "의 증상은 무엇입니까?" in instruction:
        disease_name = instruction.split("의 증상은 무엇입니까?")[0].strip()
    else:
        # If the format is not as expected, skip this entry
        continue
    
    # Extract symptoms from the output
    if "다음은 " in output:
        symptoms = output.split("다음은 ")[1].strip().split(", ")
    else:
        # If the format is not as expected, skip this entry
        continue
    
    # Create a dictionary for the disease and its symptoms
    disease_symptoms.append({
        'Disease': disease_name,
        'Symptoms': symptoms
    })

# Create a DataFrame from the extracted data
df = pd.DataFrame(disease_symptoms)

# Save the DataFrame to a CSV file
output_file_path = '/mnt/data/disease_symptoms.csv'
df.to_csv(output_file_path, index=False)