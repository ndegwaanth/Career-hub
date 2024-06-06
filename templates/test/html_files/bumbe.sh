#!/bin/bash

courses=(
            "Radio and TV Repair",
            "Diploma in Building and Civil Engineering (Building and Civil Engineering)",
            "Diploma in Building and Civil Engineering (Building and Civil Engineering)",
            "Diploma in Water and Sanitation Engineering (Water and Sanitation)",
            "Diploma in Water and Sanitation Engineering (Water and Sanitation)",
            "Diploma in Business Management (Business Management)",
            "Diploma in Business Management (Business Management)",
            "Diploma in Supply Chain Management (Supply Chain Management)",
            "Diploma in Supply Chain Management (Supply Chain Management)",
            "Diploma in Housekeeping Management (Housekeeping Management)",
            "Diploma in Housekeeping Management (Housekeeping Management)",
            "Certificate in Plumbing (Plumbing)",
            "Certificate in Plumbing (Plumbing)",
            "Craft Certificate in Carpentry and Furniture Technology (Carpentry)",
            "Craft Certificate in Carpentry and Furniture Technology (Carpentry)",
            "Building Technology (Building and Construction)",
            "Building Technology (Building and Construction)",
            "Certificate in Social Work and Community Development (Social Work)",
            "Certificate in Social Work and Community Development (Social Work)",
            "Certificate in Food and Beverage Management (Food and Beverage Management)",
            "Certificate in Food and Beverage Management (Food and Beverage Management)",
            "Certificate in Hairdressing and Beauty Therapy (Hairdressing & Beauty Therapy)",
            "Certificate in Hairdressing and Beauty Therapy (Hairdressing & Beauty Therapy)",
            "Diploma in Nutrition and Diet Therapy (Nutrition)",
            "Diploma in Nutrition and Diet Therapy (Nutrition)",
            "Certificate in Electrical Engineering Technology (Electrical Engineering)",
            "Certificate in Electrical Engineering Technology (Electrical Engineering)",
            "Craft Certificate in Motor Vehicle Mechanics (Motor Vehicle Mechanics)",
            "Craft Certificate in Motor Vehicle Mechanics (Motor Vehicle Mechanics)",
            "Certificate in Fashion Design (Fashion Design)",
            "Certificate in Fashion Design (Fashion Design)",
            "Certificate in Secretarial Studies (Secretarial Studies)",
            "Certificate in Secretarial Studies (Secretarial Studies)",
            "CPA Part I (CPA)",
            "CPA Part I (CPA)",
            "CPA Part II (CPA)",
            "CPA Part II (CPA)",
            "Advanced Diploma in Total Quality Management (Quality Management)",
            "Advanced Diploma in Total Quality Management (Quality Management)",
            "Diploma in Business Administration (Business Administration)",
            "Diploma in Business Administration (Business Administration)",
            "Accounting Technician Certificate (ATC)",
            "Accounting Technician Certificate (ATC)",
            "Diploma in Telecommunication Engineering (Telecommunication Engineering)",
            "Diploma in Telecommunication Engineering (Telecommunication Engineering)",
            "Diploma in Information Communication Technology (ICT)",
            "Diploma in Information Communication Technology (ICT)",
            "Diploma in Sales and Marketing (Sales and Marketing)",
            "Diploma in Sales and Marketing (Sales and Marketing)",
            "Diploma in Fashion Design (Fashion Design)",
            "Diploma in Fashion Design (Fashion Design)",
            "Certificate in Motor Vehicle Mechanics (Motor Vehicle Mechanics)",
            "Certificate in Motor Vehicle Mechanics (Motor Vehicle Mechanics)",
            "Certificate in Masonry, Carpentry and Joinery",
            "Certificate in Masonry, Carpentry and Joinery",
            "Diploma in Instrumentation and Control Engineering (Instrumentation and Control)",
            "Diploma in Instrumentation and Control Engineering (Instrumentation and Control)",
            "Diploma in Food and Beverage Management (Food and Beverage Management)",
            "Diploma in Food and Beverage Management (Food and Beverage Management)",
            "Diploma in Library and Information Science (Library and Information Science)",
            "Diploma in Library and Information Science (Library and Information Science)",
            "Diploma in Purchasing and Supplies Management (Purchasing and Supplies)",
            "Diploma in Purchasing and Supplies Management (Purchasing and Supplies)",
            "Certified Public Accountant (CPA)",
            "Certified Public Accountant (CPA)",
            "Diploma in Human Resource Management (Human Resource Management)",
            "Diploma in Human Resource Management (Human Resource Management)",
            "Diploma in Electrical Engineering (Electrical Engineering)",
            "Diploma in Electrical Engineering (Electrical Engineering)",
            "Diploma in Automotive Engineering (Automotive Engineering)",
            "Diploma in Automotive Engineering (Automotive Engineering)",
            "Diploma in Social Work and Community Development (Social Work and Community Development)",
            "Diploma in Social Work and Community Development (Social Work and Community Development)",
            "Certificate in Fisheries Technology (Fisheries Technology)",
            "Certificate in Fisheries Technology (Fisheries Technology)",
            "Certificate in Early Childhood Development and Education (ECDE)",
            "Certificate in Early Childhood Development and Education (ECDE)",
            "Computer Packages",
            "Computer Packages"
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
