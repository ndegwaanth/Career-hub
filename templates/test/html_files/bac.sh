#!/bin/bash

courses=(
            "Certificate in Agriculture & Community Development",
            "Certificate in Animal Health and Production",
            "Certificate in Artificial Insemination",
            "Certificate in Fashion Design (Level 5)",
            "Certificate in Horticulture",
            "Certificate in various Agricultural value chains",
            "Diploma in Agribusiness Management and Marketing",
            "Diploma in Agricultural Extension & Community Development",
            "Diploma in Agricultural Irrigation & Drainage Engineering",
            "Diploma in Agriculture and Biotechnology",
            "Diploma in Agriculture and Human Ecology Extension",
            "Diploma in Animal Health and Production Management",
            "Diploma in Animal Production and Health Management",
            "Diploma in Education (Home Science & Biology)",
            "Diploma in Farm Business Management",
            "Diploma in Fashion Design Technology",
            "Diploma in Food and Beverage Production",
            "Diploma in Horticulture",
            "Diploma in Information Communication Technology",
            "Diploma in Secondary Teacher Education",
            "Diploma in Technical Instructor Education",
            "Diploma in Technical Trainer Education",
            "Upgrading Certificate in Animal Health"
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
