#!/bin/bash

courses=(
            "DIPLOMA IN SOCIAL WORK AND COMMUNITY DEVELOPMENT",
            "DIPLOMA IN MECHATRONIC ENGINEERING",
            "DIPLOMA IN IN SUPPLY CHAIN MANAGEMENT",
            "DIPLOMA IN BUSINESS MANAGEMENT",
            "DIPLOMA IN TOURISM MANAGEMENT",
            "DIPLOMA IN INFORMATION COMMUNICATION TECHNOLOGY",
            "CRAFT IN AUTOMOTIVE ENGINEERING",
            "CERTIFICATE IN BUSINESS MANAGEMENT",
            "CRAFT INFORMATION COMMUNICATION TECHNOLOGY",
            "CERTIFICATE IN ELECTRICAL AND ELECTRONIC ENGINEERING (POWER OPTION)",
            "CERTIFICATE IN ELECTRICAL AND ELECTRONIC TECHNOLOGY",
            "CERTIFICATE IN FOOD AND BEVERAGE PRODUCTION, SALES AND SERVICES",
            "CERTIFICATE IN INFORMATION COMMUNICATION TECHNOLOGY",
            "DIPLOMA IN ELECTRICAL ENGINEERING (POWER)",
            "CRAFT IN MECHATRONICS ENGINEERING",
            "CERTIFICATE IN SOCIAL WORK",
            "CERTIFICATE IN SUPPLY CHAIN MANAGEMENT",
            "CERTIFICATE IN TOURISM MANAGEMENT",
            "TRADE TEST GRADE III I IN MOTOR VEHICLE MECHANICS",
            "TRADE TEST GRADE III I IN ARC WELDING",
            "TRADE TEST GRADE III I IN HAIRDRESSING",
            "TRADE TEST GRADE III I IN DRESSMAKING",
            "ARTISAN CERTIFICATE IN FOOD & BEVERAGE PRODUCTION, SERVICE AND SALES",
            "TRADE TEST GRADE III I IN BEAUTY THERAPY",
            "TRADE TEST GRADE III I IN MOTOR VEHICLE ELECTRONICS"
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
