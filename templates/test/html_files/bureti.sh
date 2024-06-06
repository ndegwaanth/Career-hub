#!/bin/bash

courses=(
            "Accounting Technician Diploma(ATD)",
            "Artisan Certificate in Carpentry and Joinery(Carpentry and Joinery)",
            "Artisan Certificate in Electrical Installation(Electrical Installation)",
            "Artisan Certificate in Masonry(Masonry)",
            "Artisan Certificate in Plumbing(Plumbing)",
            "Artisan Certificate in Storekeeping(Storekeeping)",
            "Artisan in Welding and Fabrication(Welding and Fabrication)",
            "Certificate in Automotive Engineering(Automotive Engineering)",
            "Certificate in Business Management(Business Management)",
            "Certificate in Civil Engineering(Civil Engineering)",
            "Certificate in General Agriculture(General Agriculture)",
            "Certificate in Information Technology(Information Technology)",
            "Certificate in Quantity Surveying(Quantity Surveying)",
            "Certificate in Supply Chain Management(Supply Chain Management)",
            "Certificate in Welding and Fabrication(Welding and Fabrication)",
            "Cisco Certified Network Associate(CCNA)",
            "Craft Certificate in Building Construction(Building Construction)",
            "Craft Certificate in Plumbing(Plumbing)",
            "Craft certificate in Electrical and Electronics Engineering(Electrical and Electronic Engineering)",
            "Diploma in Agriculture(Agriculture)",
            "Diploma in Business Management(Business Management)",
            "Diploma in Civil Engineering(Civil Engineering)",
            "Diploma in Electrical and Electronics Engineering(Electrical and Electronics )",
            "Diploma in Electrical Engineering(Electrical Engineering)",
            "Diploma in General Agriculture(General Agriculture)",
            "Diploma in Hairdressing and Beauty Therapy(Hairdressing & Beauty Therapy)",
            "Diploma in Information Technology(Information Technology)",
            "Diploma in Library & Information Studies(Library & Information Studies)",
            "Diploma in Quantity Surveying(Quantity Surveying)",
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
