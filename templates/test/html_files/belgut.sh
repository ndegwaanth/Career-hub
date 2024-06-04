#!/bin/bash

courses=(
            "Certificate in Information Communication Technology (ICT)",
            "Certificate in Building Technology (Building Technology)",
            "Certificate in Fashion Design",
            "Artisan Certificate in Electrical Installation",
            "Artisan Certificate in Food and Beverage",
            "Artisan Certificate in Fashion Design",
            "Certificate in Plumbing Technology",
            "Artisan Certificate in Plumbing Technology",
            "Certificate in Food and Beverage Production",
            "Artisan Certificate in Building Technology",
            "Craft Certificate in Electrical and Electronics Engineering (Power Option)",
            "Diploma in Information Communication Technology (ICT)",
            "Diploma in Fashion Design",
            "Diploma in Food and Beverage",
            "Diploma in Electrical and Electronics Engineering (Power Option)"
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
