#!/bin/bash

courses=(
    "Bachelor of Science (Physical Therapy)"
    "Bachelor of Science (Medical Psychology)"
    "Bachelor of Science (Medical Laboratory Science)"
    "Bachelor of Education (Science)"
    "Bachelor of Education (Business Studies)"
    "Bachelor of Education (Arts)"
    "Bachelor of Education (Arts)"
    "Bachelor of Education (Science)"
    "Bachelor of Science (Counselling Psychology)"
    "Bachelor of Science (Communication and Public Relations)"
    "Bachelor of Arts (Community Development)"
    "Bachelor of Science (Computer Science)"
    "Bachelor of Science (Applied Statistics with Computing)"
    "Bachelor of Science (Microbiology)"
    "Bachelor of Business Management"
    "Bachelor of Arts (Economics)"
    "Bachelor of Hotel and Hospitality Management"
    "Diploma in Hotel and Restaurant Management"
    "Diploma in Tourism Management"
    "Diploma in Business Management"
    "Diploma in Social Work"
    "Diploma in Community Development"
    "Post Graduate Diploma in Education"
)

# Function to create a valid filename
create_filename() {
    local course="$1"
    # Convert to lowercase, replace spaces with underscores, remove special characters
    local filename=$(echo "$course" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd '[:alnum:]_')
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
