#!/bin/bash

courses=(
            "Certificate in Basic TV/VCR Repair(TV/VCR Repair)",
            "Certificate in Business Management(Business Management)",
            "Certificate in Community Development",
            "Certificate in Computer Applications",
            "Certificate in Computer Repair and Maintenance",
            "Certificate in Electrical and Electronics Engineering",
            "Certificate in Electrical Installation(Electrical Installation)",
            "Certificate in Entrepreneurship(Entrepreneurship)",
            "Certificate in Guidance and Counselling(Guidance and Counselling)",
            "Certificate in Human Resource Management(Human Resource Management)",
            "Certificate in Information Technology(Information Technology)",
            "Certificate in Public Relations(Public Relations)",
            "Certificate in Sales and Marketing(Sales and Marketing)",
            "Certificate in Telecommunication Engineering",
            "Computer Packages",
            "Craft certificate in Electrical and Electronics Engineering",
            "Diploma in Business Administration",
            "Diploma in Business Management(Business Management)",
            "Diploma in Community Development(Community Development)",
            "Diploma in Electrical and Electronics Engineering",
            "Diploma in Guidance & Counselling",
            "Diploma in Information Technology(Information Technology)",
            "Diploma in Public Relations(Public Relations)",
            "Diploma in Telecommunication Engineering"
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
