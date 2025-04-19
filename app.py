import json

def average_team_attributes(team):
    # Get the attribute names from the first team member
    attribute_keys = list(team[0]['attributes'].keys())

    # Initialize a dictionary to hold the running total for each attribute
    average_attribute = {k: 0 for k in attribute_keys}

    # Sum all attribute values for each team member
    for member in team:
        for k in attribute_keys:
            average_attribute[k] += member['attributes'][k]

    # Divide each total by the number of team members to get the average
    for k in average_attribute:
        average_attribute[k] /= len(team)

    return average_attribute

def applicant_score(applicant_attributes, average_team_attributes):
    base_score = 0
    # For each attribute, check if the applicants attribute is higher than the teams average
    for attr in applicant_attributes:
        if applicant_attributes[attr] > average_team_attributes[attr]:
            # Add 0.25 to the applicants score if the applicants attribute is higher
            base_score += 0.25

    return base_score

# Output structure
with open('input.json') as f:
        data = json.load(f)

applicants = data['applicants']
team = data['team']
scored_applicants = []

for applicant in applicants:

    score = applicant_score(applicant['attributes'], average_team_attributes(team))

    scored_applicants.append({
        "name": applicant['name'],
        "score": score
    })

output = {"scoredApplicants": scored_applicants}

# Write to output.json
with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)