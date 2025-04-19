# Applicant Compatibility Scorer

## Input
My solution takes the input from input.json by using the function "json.load(input.json)". Input.json is in the same format that was given in the instructions.
## Output
To get the output into output.json I first copied the format from the instructions under Output for each of the scored applicants and filled an empty array with the output. With that array filled with the scored applicants, I then use the function "json.dump(output)" to add the array into output.json.