#!/bin/bash

# Define the list of courses
courses=(
    "Certificate in Monitoring and Evaluation(monitoring and Evaluation)"
    "Certificate in Project Management(Project Management)"
    "Certificate in Supply Chain Management(Supply Chain Management)"
    "Diploma in Community Health(Community Health)"
    "Diploma in Nursing(Nursing)"
    "Short Course in Fundraising and Resource Mobilization(Fundraising and Resource Mobilization)"
    "Higher Diploma in Comprehensive Reproductive Health(Comprehensive Reproductive Health)"
    "Short Course in Strategic Management and Leadership(Strategic Management and Leadership)"
    "Higher Diploma in Community Health(Community Health)"
    "Trauma Counselling(Counselling)"
    "Bachelor of Science in Community Health Practice(Community Health Practice)"
    "Short Course in Health Systems Strengthening (Health Systems Strengthening )"
    "Bachelor of Science in Nursing(Nursing)"
    "Bachelor of Science in Health Systems Management(Health Systems Management)"
    "Short Course in Hospital Administration and Management (Hospital Administration and Management )"
    "Bsc in Rehabilitation Medicine"
    "Diploma in Leadership Enhancement and Accountability for Frontline Health Professional"
)

# Function to create a valid filename
create_filename() {
    local course="$1"
    # Convert to lowercase, replace spaces with underscores, remove special characters
    local filename=$(echo "$course" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd '[:alnum:]_()' | sed 's/)/_/g' | sed 's/(/_/g' | sed 's/__$//g')
    echo "$filename.html"
}

# Iterate over the courses and create an HTML file for each
for course in "${courses[@]}"; do
    filename=$(create_filename "$course")
    
    # Write the HTML structure to the file
    cat <<EOL > "$filename"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$course</title>
</head>
<body>
    <h1>$course</h1>
</body>
</html>
EOL

    echo "Created file: $filename"
done
