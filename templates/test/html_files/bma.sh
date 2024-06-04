#!/bin/bash

courses=(
            "Certificate in Mechanical Engineering (Mechanical Engineering)",
            "Certificate in Maritime Transport and Logistics (Maritime Transport and Logistics)",
            "Certificate in Nautical Sciences (Nautical Sciences)",
            "Certificate in Marine Engineering",
            "Artisan Certificate in Seafarers",
            "Diploma in Maritime Transport and Logistics (Maritime Transport and Logistics)",
            "Diploma in Nautical Sciences (Nautical Sciences)",
            "Diploma in International Freight Management",
            "Diploma in Marine Engineering"
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
