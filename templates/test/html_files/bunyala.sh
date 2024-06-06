#!/bin/bash

courses=(
            "Artisan Certificate in Carpentry and Joinery",
            "Artisan Certificate in Garment Making",
            "Certificate in Accountancy(Accountancy)",
            "Certificate in Building Construction",
            "Certificate in Building Construction Technology",
            "Certificate in Business Administration(Business Administration)",
            "Certificate in Carpentry and Joinery",
            "Certificate in Computerized Secretarial Studies",
            "Certificate in Electrical and Electronic Engineering(Power Option)",
            "Certificate in Food and Beverage Production, Sales and Service",
            "Certificate in Hair Dressing and Beauty Therapy",
            "Certificate in Human Resource Management(HRM)",
            "Certificate in Information Communication Technology(ICT)",
            "Certificate in Plumbing",
            "Certificate in Sales and Marketing(Sales and Marketing)",
            "Certificate in Social Work and Community Development",
            "Craft Certificate in Fashion and Garment Making Technology",
            "Craft Certificate in Food and Beverage Production, Sales and Service",
            "Craft Certificate in General Agriculture",
            "Craft Certificate in Information Communication Technology(ICT)",
            "Craft Certificate in Motor Vehicle Mechanics",
            "Diploma in Accountancy(Accountancy)",
            "Diploma in Agricultural Engineering",
            "Diploma in Automotive Engineering",
            "Diploma in Automotive Engineering(Automotive Engineering)",
            "Diploma in Building Construction Technology",
            "Diploma in Business Administration(Business Administration)",
            "Diploma in Business Management",
            "Diploma in Clothing Technology",
            "Diploma in Cooperative Management(Cooperative Management)",
            "Diploma in Electrical and Electronic Engineering(Power Option)",
            "Diploma in Food and Beverage Production, Sales and Service Management",
            "Diploma in General Agriculture",
            "Diploma in Human Resource Management(Human Resource Management)",
            "Diploma in Information Communication Technology(ICT)",
            "Diploma in Information Technology(Information Technology)",
            "Diploma in Sales and Marketing(Sales and Marketing)",
            "Diploma in Social Work & Community Development",
            "Motor Vehicle Mechanics(MVM)"
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
