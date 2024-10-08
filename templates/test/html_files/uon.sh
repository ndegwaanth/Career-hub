#!/bin/bash

courses=(
            "Diploma In Leather Technology",
            "Diploma In Estate Agency And Property Management",
            "Post Graduate Diploma In Housing Administration",
            "Diploma In Business Management (fes)",
            "Diploma In Sales & Marketing(fes)",
            "Diploma In Adult Education And Community Development",
            "Diploma In Youth Development Work",
            "Diploma In Early Childhood Education",
            "Diploma In Purchasing & Supplies Management",
            "Diploma In Business Management",
            "Diploma In Sales & Marketing",
            "Diploma In Human Resource Management",
            "Diploma In Public Relations",
            "Diploma In Guidance And Counseling",
            "Higher Diploma In Medical Diagnostic Ultrasound",
            "Diploma In Audiology And Public Health Otology",
            "Diploma Programmes in Humanities and Social Sciences",
            "Ordinary Diploma",
            "Diploma In Women, Leadership And Governance In Africa",
            "Diploma In Chinese Language And Culture",
            "Diploma In International Studies/strategic Studies",
            "Diploma In International Studies",
            "Diploma In Theatre And Film Studies",
            "Diploma In Criminology And Social Order",
            "Diploma In Social Work And Social Development",
            "Diploma Programmes in Kisumu Campus",
            "Diploma In Purchasing And Supplies Management",
            "Diploma In Human Resource Management",
            "Diploma In Guidance And Counseling",
            "Ordinary Diploma",
            "Diploma In Sales And Marketing",
            "Diploma In Guidance And Counseling",
            "Diploma In Project Planning And Management",
            "Diploma In Human Resource Management",
            "Diploma In Public Relations",
            "Diploma In Purchasing And Supplies Management",
            "Diploma In Business Management",
            "Diploma In Project Planning And Management",
            "Diploma In Adult Education And Community Development",
            "Diploma In Youth Development Work",
            "Diploma In Business Management",
            "Diploma In Sales And Marketing",
            "Diploma In Human Resource Management",
            "Diploma In Purchasing And Supplies Management",
            "Diploma In Public Relations",
            "Diploma In Guidance And Counseling",
            "Ordinary Diploma",
            "Bachelor of Science in ( Food Science & Technology)",
            "Bachelor of Science in ( Agriculture,education And Extension)",
            "Bachelor of Science in (agribusiness Management)",
            "Bachelor of Science in (food Science, Nutrition & Dietetics)",
            "Climate Change & Development",
            "Bachelor of Science in Agribusiness Management",
            "Bachelor of Science in agricultural Economics",
            "Bachelor of Science in agricultural Education And Extension",
            "Bachelor of Science in Agriculture(animal Science Major)",
            "Bachelor of Science in Fisheries And Aquaculture Management",
            "Bachelor of Science in Wildlife Management And Conservation",
            "Bachelor of Science in Food Science And Technology",
            "Bachelor of Science in Food Nutrition And Dietetics",
            "Bachelor of Science in (agriculture)",
            "Bachelor of Science in ( Range Management)",
            "Bachelor of Science in Management Of Agroecosystems & Environment",
            "Bachelor of Science in Horticulture",
            "Bachelor Of Veterinary Medicine",
            "Bachelor of Science in Wildlife Management And Conservation",
            "Bachelor of Science in (bio-medical Technology)",
            "Bachelor of Science in Wildlife Management",
            "Bachelor Programmes in Biological and Physical Sciences",
            "Bachelor of Science in Environmental Chemistry",
            "Bachelor of Science in Analytical Chemistry",
            "Bachelor of Science in Industrial Chemistry",
            "Bachelor of Science in Chemistry",
            "Bachelor of Science in Petroleum Geoscience",
            "Bachelor of Science in Actuarial Science",
            "Bachelor of Science in Mathematics",
            "Bachelor of Science in Statistics",
            "Bachelor of Science in Mathematics And Computing",
            "Bachelor of Science in (meteorology)",
            "Bachelor of Science in Atmospheric Science",
            "Bachelor of Science in (microprocessor Technology & Instrumentation)",
            "Bachelor of Science in Astronomy And Astrophysics",
            "Bachelor of Science in Physics",
            "Bachelor of Education Science (physics)",
            "Bachelor of Science in (biology)",
            "Bachelor of Science in Microbiology And Biotechnology",
            "Bachelor of Science in Environmental Conservation And Natural Resource Management",
            "Bachelor of Science in Computer Science",
            "Bachelor of Science in Industrial Chemistry",
            "Bachelor of Science",
            "Bachelor of Science (distance Learning)",
            "Bachelor of Science in Geology (distance Learning)",
            "Bachelor of Education (science)",
            "Bachelor of Science in Analytical Chemistry",
            "Bachelor of Science in Chemistry",
            "Bas/barch",
            "B.a. Design",
            "Bachelor of Science in (civil Engineering)",
            "Bachelor of Science in (environmental And Biosystems Engineering)",
            "Bachelor of Science in ( Electrical And Electronic Engineering)",
            "Bachelor of Science in (surveying)",
            "Bachelor of Science in ( Electrical Engineering)",
            "Bachelor of Science in (geospatial Engineering)",
            "Bachelor of Science in (mechanical Engineering)",
            "Bachelor Of Real Estate",
            "Bachelor Of Construction Management",
            "Bachelor Of Quantity Surveying",
            "B.a (urban & Regional Planning)",
            "Bachelor Of Commerce By Distance",
            "Bachelor Of Arts(distance)",
            "Bachelor Of Education (arts, Bachelor of Education Distance)",
            "Bachelor Of Education Arts In History And Geography",
            "Bachelor Of Education Arts In History And Cre",
            "Bachelor Of Education Arts In Geography And Mathematics",
            "Bachelor Of Education Arts In Double Mathematics",
            "Bachelor Of Education Arts In Mathematics And Business Studies",
            "Bachelor Of Education Arts In Geography And Environmental Studies And Business Studies",
            "Bachelor Of Education Arts In English And Literature",
            "Bachelor Of Education Science In Physics And Geography And Environmental Studies",
            "Bachelor Of Education Science In Double Mathematics",
            "Bachelor of Science in Physics",
            "Bachelor of Science in Analytical Chemistry",
            "Bachelor of Science in Industrial Chemistry",
            "Bachelor of Science in Geology",
            "Bachelor of Science in Meteorology",
            "Bachelor of Science in Pure Mathematics",
            "Bachelor of Science in Applied Mathematics",
            "Bachelor of Science in Zoology",
            "Bachelor of Science in Botany",
            "Bachelor of Science in Geography And Environmental Studies",
            "Bachelor Of Arts In History",
            "Bachelor Of Arts In Tourism",
            "Bachelor Of Arts In English Language",
            "Bachelor Of Arts In Literature",
            "Bachelor Of Arts In Kiswahili",
            "Bachelor Of Arts In Communication",
            "Bachelor Of Arts In Arabic Studies",
            "Bachelor Of Arts Sociology And Social Work",
            "Bachelor Of Arts Christian Religious Studies",
            "Bachelor Of Arts In Philosophy",
            "Bachelor Of Arts In Psychology",
            "Bachelor Of Arts In Guidance And Counseling",
            "Bachelor Of Arts In Geography And Environmental Studies",
            "Bachelor Of Commerce In Accounting",
            "Bachelor Of Commerce In Finance",
            "Bachelor Of Commerce In Marketing",
            "Bachelor Of Commerce In Human Resource Management",
            "Bachelor Of Commerce In Insurance And Management",
            "Bachelor Of Commerce In Procurement And Purchasing And Supplies",
            "Bachelor Of Commerce In Operations Management",
            "Bachelor Of Commerce In Business Information Systems",
            "Bachelor Of Arts In Political Science And Public Administration",
            "Bachelor of Education Science By Distance Learning",
            "Bachelor Of Education (arts, Bachelor of Education)",
            "Bachelor of Education (arts) in Mathematics And Economics)",
            "Bachelor of Education (arts) Linguistics And Literature",
            "Bachelor of Education (arts) Mathematics And Geography",
            "Bachelor of Education (arts) Kiswahili And Religious Studies",
            "Bachelor of Education (arts) History And Religious Studies",
            "Bachelor of Education (arts) History And Economics",
            "Bachelor of Education (arts) Geography And History",
            "Bachelor of Education (arts) Business And Mathematics",
            "Bachelor of Education (arts) Business And Economics",
            "Bachelor of Education (arts) Kiswahili And Literature",
            "Bachelor of Education (arts) History And Kiswahili",
            "Bachelor of Education (arts) Geography And Religious Studies",
            "Bachelor of Education (arts) Geography And Economics",
            "Bachelor of Education (arts) Business And Geography",
            "Bachelor of Science Agricultural Education And Extention (Bachelor of Science in Ae&e)",
            "Bachelor Of Sciences (Bachelor of Science)",
            "Bachelor of Education (science) (Bachelor of Education.sc)",
            "Bachelor Of Education In Early Childhood Education",
            "Bachelor Of Education (arts)"
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
