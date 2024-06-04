#!/bin/bash

courses=(
            "Certified Public Accountant (CPA)",
            "Certificate in Business Management (Business Management)",
            "Certificate in Information Communication Technology (ICT)",
            "Certificate in Web Design (Web Design)",
            "Certificate in Human Resource Management (HRM)",
            "Certificate in Graphic Design (Graphic Design)",
            "Computer Packages and Applications",
            "Diploma in Business Management (Business Management)",
            "Diploma in Human Resource Management (Human Resource Management)",
            "Diploma in Information Communication Technology (ICT)",
            "Accounting Technicians Diploma (ATD)"
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
