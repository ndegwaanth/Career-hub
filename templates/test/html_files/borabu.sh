#!/bin/bash

courses=(
            "Artisan Certificate in Fashion Design and Garment Making(Fashion Design and Garment Making)",
            "Artisan Certificate in Hairdressing and Beauty Therapy(Hairdressing and Beauty Therapy)",
            "Certificate in Cooperative Management(Cooperative Management)",
            "Certificate in Electrical and Electronics Technology()",
            "Certificate in Fashion Design and Garment Making()",
            "Certificate in Hairdressing And Beauty Therapy(Hairdressing And Beauty Therapy)",
            "Certificate in Human Resource Management(HRM)",
            "Certificate in Information Technology(Information Technology)",
            "Certificate in Supply Chain Management ()",
            "Computer Packages and Applications()",
            "Diploma in Cooperative Management(Cooperative Management)",
            "Diploma in Electrical and Electronics Engineering (Telecommunication Option)",
            "Diploma in Electrical and Electronics Engineering(Power Option)()",
            "Diploma in Fashion Design and Clothing Technology(Fashion Design and Clothing Technology)",
            "Diploma in Human Resource Management(Human Resource Management)",
            "Diploma in Information Communication Technology(ICT)",
            "Diploma in Supply Chain Management(Supply Chain Management)"
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
