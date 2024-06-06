#!/bin/bash

courses=(
            "Artisan Certificate in Carpentry and Joinery(Carpentry and Joinery)",
            "Artisan Certificate in Masonry(Masonry)",
            "Artisan Certificate in Plumbing(Plumbing)",
            "Artisan in Electrical and Electronics Engineering(Electrical and Electronics Engineering)",
            "Certificate in Building Construction(Building Construction)",
            "Certificate in Business Information Technology(BIT)",
            "Certificate in Business Management(Business Management)",
            "Certificate in Carpentry and Joinery(Carpentry and Joinery)",
            "Certificate in Computer Hardware(Computer Hardware)",
            "Certificate in Information Communication Technology(ICT)",
            "Certificate in Networking(Computer Networking)",
            "Certificate in Plumbing(Plumbing)",
            "Certificate in Sales and Marketing(Sales and Marketing)",
            "Certificate in Social Work and Community Development(Social Work)",
            "Certificate in Supply Chain Management(Supply Chain Management)",
            "Certificate in Web Design and Development(Web Design)",
            "Computer Packages()",
            "Diploma in Accountancy(Accounting)",
            "Diploma in Building Technology(Building Technology)",
            "Diploma in Business Information Technology(BIT)",
            "Diploma in Business Management(Business Management)",
            "Diploma in Civil Engineering(Civil Engineering)",
            "Diploma in Cooperative Management(Cooperative Management)",
            "Diploma in Computer Studies(Computer Studies)",
            "Diploma in Human Resource Management(Human Resource Management)",
            "Diploma in Information Communication Technology(ICT)",
            "Diploma in Land Survey(Land Survey)",
            "Diploma in Quantity Surveying(Quantity Surveying)",
            "Diploma in Social Work and Community Development(Social Work and Community Development)",
            "Diploma in Supply Chain Management(Supply Chain Management)",
            "Electrical Installation(Physics)",
            "Craft Certificate in Road Construction(Road Construction)"
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
