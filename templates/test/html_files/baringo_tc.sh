#!/bin/bash

courses=(
            "Accounting Technicians Certificate (ATC)",
            "Certificate in General Agriculture (General Agriculture)",
            "Certificate in Business Management (Business Management)",
            "Certificate in Information Communication Technology (ICT)",
            "Certificate in Human Resource Management (HRM)",
            "Certificate in Building Technology (Building Technology)",
            "Certificate in Mechanical Engineering (Mechanical Engineering)",
            "Certificate in Electrical and Electronics Engineering (Electrical and Electronic Engineering)",
            "Certificate in Cooperative Management (Cooperative Management)",
            "Certificate in Information Science (Information Science)",
            "Certificate in Social Work and Community Development (Social Work and Community Development)",
            "Certificate in Automotive Engineering (Automotive Engineering)",
            "Certificate in Supply Chain Management",
            "Certificate in Petroleum Geoscience",
            "Artisan Certificate in Garment Making",
            "Certificate in Fashion Design and Garment Making",
            "Certificate in Plumbing Technology",
            "Artisan Certificate in Plumbing Technology",
            "Certificate in Entrepreneurship Management",
            "Certificate in Computerized Secretarial Studies",
            "Artisan Certificate in Welding and Fabrication",
            "Artisan Certificate in Masonry",
            "Artisan Certificate in Motor Vehicle Mechanics",
            "Artisan Certificate in Electrical Wireman",
            "Diploma in Civil Engineering (Civil Engineering)",
            "Diploma in Accountancy (Accountancy)",
            "Diploma in Banking and Finance (Banking and Finance)",
            "Diploma in Information Communication Technology (ICT)",
            "Diploma in Nutrition and Dietetics (Nutrition and Dietetics)",
            "Diploma in Food and Beverage Services (Food and Beverage Services)",
            "Diploma in Supply Chain Management (Supply Chain Management)",
            "Diploma in Cooperative Management (Cooperative Management)",
            "Diploma in General Agriculture (General Agriculture)",
            "Diploma in Building Technology (Building Technology)",
            "Diploma in Automotive Engineering (Automotive Engineering)",
            "Diploma in Computer Studies",
            "Diploma in Social Work and Community Development",
            "Diploma in Petroleum Geoscience",
            "Diploma in Electrical and Electronic Technology Engineering"
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
