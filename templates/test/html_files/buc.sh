#!/bin/bash

courses=(
            "Accounting Technicians Diploma(ATD)",
            "Bachelor of Arts (German)",
            "Bachelor of Arts (French)",
            "Bachelor of Arts (Music)",
            "Bachelor of Arts (Penology, Correction and Administration)",
            "Bachelor of Arts (Psychology)",
            "Bachelor of Arts in Political Science and Public Administration",
            "Bachelor of Education (Science)",
            "Bachelor of Science",
            "Bachelor of Science (Agricultural Economics and Resource Management)",
            "Bachelor of Science (Agricultural Extension & Education)",
            "Bachelor of Science (Applied Statistics with Computing)",
            "Bachelor of Science (Computer Science)",
            "Bachelor of Science (Counselling Psychology)",
            "Bachelor of Science (Entrepreneurship Studies)",
            "Bachelor of Science (Environmental Health)",
            "Bachelor of Science (Microbiology)",
            "Bachelor of Science (Strategic Management)",
            "Bachelor of Science (with Education)",
            "Certificate in Public Relations",
            "Diploma in Business Management(Business Management)",
            "Diploma in Human Resource Management(Human Resource Management)",
            "Diploma in Public Administration",
            "Diploma in Public Relations",
            "Doctor of Philosophy in Agricultural Economics",
            "Doctor of Philosophy in Analytical Chemistry",
            "Doctor of Philosophy in Biostatistics",
            "Doctor of Philosophy in Biostatistics or Epidemiology",
            "Doctor of Philosophy in Business Management",
            "Master of Business Administration",
            "Master of Business Management (MBM)",
            "Master of Science (Project Planning & Management)",
            "Master of Science Epidemiology & Biostatistics",
            "Master of Science in Agricultural Economics and Resource Management",
            "Master of Science in Analytical Chemistry",
            "Master of Science in Pure Mathematics",
            "Master of Science in Public Health"
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
