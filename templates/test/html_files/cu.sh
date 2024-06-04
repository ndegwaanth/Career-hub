#!/bin/bash

# Define the list of courses
courses=(
    "Bachelor of Commerce (BCOM)"
    "Bachelor of Procurement & Logistic Management"
    "Bachelor of Agribusiness Management"
    "Bachelor of Science (Agricultural Economics)"
    "Bachelor of Entrepreneurship & Enterprise Management"
    "Bachelor of Co-operative Management"
    "Bachelor of Science (Economics & Statistics)"
    "Bachelor of Science in Ecotourism"
    "Bachelor of Science in Natural Resources management"
    "Bachelor of Science in Food Science and Technology"
    "Bachelor of Science in Animal Products Technology"
    "Bachelor of Science in Agricultural Education and Extension"
    "Bachelor of Agribusiness Management"
    "Bachelor of Science in Animal Science"
    "Bachelor of Science in Agriculture"
    "Bachelor of Science in Horticulture"
    "Bachelor of Science in Ecotourism & Hospitality Management"
    "Bachelor of Hotel Management"
    "Bachelor of Tourism Management"
    "Bachelor of Science in Wildlife Enterprise & Management"
    "Bachelor of Science in Environmental Science"
    "Bachelor of Science in Natural Resources"
    "Bachelor of Arts"
    "Bachelor of Arts in Linguistics, Literature and Sociology"
    "Bachelor of Arts in Philosopy"
    "Bachelor of science in Information Science"
    "Bachelor of Arts in Journalism and Mass Communication"
    "Bachelor of Arts in Economics and Sociology"
    "Bachelor of Arts in Criminology and Security Studies"
    "Bachelor of Science in Community Development"
    "Bachelor of Arts (Sociology)"
    "Bachelor of Arts in Geography and Kiswahili"
    "Bachelor of Arts in History, Economics and Sociology"
    "Bachelor of Arts in Religious Studies"
    "Bachelor of Arts in Mathematics and Economics"
    "Bachelor of Arts in Government and International Relations"
    "Bachelor of Arts in Geography, Economics and Sociology"
    "Bachelor of Arts in Communication Studies"
    "Bachelor of Science"
    "Bachelor of Science (Computer Science)"
    "Bachelor of Science Applied Computer Science."
    "Bachelor of Science in BioChemistry"
    "Bachelor of Science in Biomedical Science and Technology"
    "Bachelor of Science in Mathematics"
    "Bachelor of Science in Physics"
    "Bachelor of Science in Chemistry"
    "Bachelor of Science in Biology"
    "Bachelor of Science in Fisheries and Aquaculture"
    "Bachelor of Science in Microbiology and Biotechnology"
    "Bachelor of Science in Enviromental Chemistry"
    "Bachelor of Science in Actural mathematics"
    "Bachelor of Science in Industrial Chemistry"
    "Bachelor of Science in Electrical and Electronics Engineering"
    "Bachelor of Science in Applied Statistics"
    "Bachelor of Science in Human Nutrition and Dietetics"
    "Bachelor of Science in Health Records and Information Management"
    "Bachelor of Science in Financial Management"
    "Bachelor of Science in Nursing (Basic)"
    "Bachelor of Science in Nursing (Upgrading)"
    "Bachelor of Education (Arts)"
    "Bachelor of Education (Primary Option) – school- based"
    "Bachelor of Education (Science Education)"
    "Bachelor of Education (Early Childhood Development)"
    "Diploma in Business Management"
    "Diploma in Procurement and Logistics Management"
    "Diploma in Human Resource Management"
    "Diploma in Insurance and Risk Management"
    "Diploma in Accounting"
    "Diploma in Journalism and Mass Communication"
    "Diploma in Community Development"
    "Diploma in Peace Studies and Conflict Resolution"
    "Diploma in Criminology and Security Studies"
    "Diploma in Education (Primary) school-based"
    "Diploma in Education (Secondary)"
    "Diploma in Disaster Management"
    "Diploma in Counselling Psychology"
    "Diploma in Project Planning and Management"
    "Diploma in Leadership and Public Administration"
    "Diploma in Social Work"
    "Diploma in Early Childhood Education"
    "Diploma in Animal Health and Production"
    "Diploma in Farm Resources and Management"
    "Diploma in Meat Science & Technology"
    "Diploma in Tourism & Hotel Management"
    "Diploma in Wildlife Management"
    "Diploma in Agriculture and Rural Development"
    "Diploma in Agricultural Education and Extension"
    "Diploma in Horticulture"
    "Diploma in Computer Science"
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
