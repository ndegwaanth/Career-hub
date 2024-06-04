#!/bin/bash

courses=(
            "Bachelor of Science in Horticulture",
            "Bachelor of Science in Agriculture",
            "Bachelor of Science in Seed Science & Technology",
            "Bachelor of Science in Soil & Land Use Management",
            "Bachelor of Science in Food Science & Nutrition",
            "Bachelor of Science in Apparel & Fashion Design",
            "Bachelor of Science in Animal Science",
            "Bachelor of Science in Agricultural Biotechnology",
            "Bachelor of Science in Food Operation Management",
            "Bachelor of Science in Agriculture Extension Education",
            "Bachelor of Science in Agricultural Economics",
            "Bachelor of Tourism Management (BTM)",
            "Bachelor of Hotel and Hospitality Management (BHM)",
            "Bachelor of Travel and Tour Operations Management (BTTM)",
            "Bachelor of Business Management (BBM)",
            "Bachelor of Science in Project Planning and Management (PPM)",
            "Bachelor of Science in Entrepreneurship",
            "Bachelor of Arts in Economics",
            "Bachelor of Education (Science)",
            "Bachelor of Education (Arts)",
            "Bachelor of Education (Technology Education)",
            "Bachelor of Education (Early Childhood and Primary Education)",
            "Bachelor of Education (Special Needs Education)",
            "Bachelor of Education (Home science & Technology)",
            "Bachelor of Education (Agricultural Education)",
            "Bachelor of Education (Physical Education and Recreation)",
            "Bachelor of Engineering in Agricultural and Biosystems Engineering",
            "Bachelor of Engineering in Civil and Structural Engineering",
            "Bachelor of Engineering in Mechanical and Production Engineering",
            "Bachelor of Environmental Studies (Arts) in Environmental Social Science",
            "Bachelor of Environmental Studies (Arts) in Environmental Conservation and Management.",
            "Bachelor of Environmental Studies (Science) in Biology",
            "Bachelor of Environmental Studies (Science) in Health",
            "Bachelor of Environmental Studies (Science) in Hydrology",
            "Bachelor of Environmental Studies (Science) in Geology",
            "Bachelor of Environmental Studies (Science) in Meteorology",
            "Bachelor of Environmental Studies (Arts) inIn Forestry",
            "Bachelor in Wood Science and Industrial Processes",
            "Bachelor in Agroforestry and Rural Development",
            "Bachelor In Sustainable Energy and Climate Change Systems",
            "Bachelor In Water Resource Management",
            "Bachelor Natural Resource Management",
            "Bachelor In Fisheries and Aquatic Sciences",
            "Bachelor in Wildlife Management Planning and Management",
            "Bachelor of Science (B.Sc.)",
            "Bachelor of Science in Analytical Chemistry with Computing"
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

        
