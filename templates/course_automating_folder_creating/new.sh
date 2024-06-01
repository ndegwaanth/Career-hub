#!/bin/bash

# JSON-like data from user
data='[
    {"id": 15, "code": "BORABU TVC", "name": "BORABU TECHNICAL AND VOCATIONAL COLLEGE", "type": "College", "link": "file15.html"},
    {"id": 16, "code": "BAC", "name": "BUKURA AGRICULTURAL COLLEGE", "type": "College", "link": "file16.html"},
    {"id": 17, "code": "BUMBE TTI", "name": "BUMBE TECHNICAL TRAINING INSTITUTE", "type": "College", "link": "file17.html"},
    {"id": 18, "code": "BUNGOMA NORTH TVC", "name": "BUNGOMA NORTH TECHNICAL AND VOCATIONAL COLLEGE", "type": "College", "link": "file18.html"},
    {"id": 19, "code": "BUNYALA TVC", "name": "BUNYALA TECHNICAL AND VOCATIONAL COLLEGE", "type": "College", "link": "file19.html"},
    {"id": 20, "code": "BURETI TTI", "name": "BURETI TECHNICAL TRAINING INSTITUTE", "type": "College", "link": "file20.html"},
    {"id": 21, "code": "BUSHIANGALA TTI", "name": "BUSHIANGALA TECHNICAL TRAINING INSTITUTE", "type": "College", "link": "file21.html"},
    {"id": 22, "code": "BUTERE TVC", "name": "BUTERE TECHNICAL AND VOCATIONAL COLLEGE", "type": "College", "link": "file22.html"},
    {"id": 23, "code": "CUEA", "name": "CATHOLIC UNIVERSITY OF EASTERN AFRICA", "type": "University", "link": "file23.html"},
    {"id": 24, "code": "CTTR", "name": "CENTRE FOR TOURISM TRAINING AND RESEARCH", "type": "College", "link": "file24.html"},
    {"id": 25, "code": "CHAMASIRI TVC", "name": "CHAMASIRI TECHNICAL AND VOCATIONAL COLLEGE", "type": "College", "link": "file25.html"},
    {"id": 26, "code": "CHANZEYWE TVC", "name": "CHANZEYWE TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 27, "code": "CHEPALUNGU TTI", "name": "CHEPALUNGU TECHNICAL TRAINING INSTITUTE", "type": "College"},
    {"id": 28, "code": "CHEPSIREI TVC", "name": "CHEPSIREI TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 29, "code": "CHERANGANY TVC", "name": "CHERANGANY TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 30, "code": "CHUKA TVC", "name": "CHUKA TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 31, "code": "CU", "name": "CHUKA UNIVERSITY", "type": "University"},
    {"id": 32, "code": "COPUK", "name": "CO-OPERATIVE UNIVERSITY OF KENYA", "type": "University"},
    {"id": 33, "code": "CIT", "name": "COAST INSTITUTE OF TECHNOLOGY", "type": "Institute"},
    {"id": 34, "code": "DAVID M WAMBULI TVC", "name": "DAVID M WAMBULI TECHNICAL VOCATIONAL COLLEGE", "type": "College"},
    {"id": 35, "code": "DAYSTAR", "name": "DAYSTAR UNIVERSITY", "type": "University"},
    {"id": 36, "code": "DKUT", "name": "DEDAN KIMATHI UNIVERSITY OF TECHNOLOGY", "type": "University"},
    {"id": 37, "code": "DR. DANIEL WAKO MURENDE TVC", "name": "DR. DANIEL WAKO MURENDE TECHNICAL & VOCATIONAL COLLEGE", "type": "College"},
    {"id": 38, "code": "EASA", "name": "EAST AFRICAN SCHOOL OF AVIATION", "type": "School"},
    {"id": 39, "code": "EBUKANGA TVC", "name": "EBUKANGA TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 40, "code": "EU", "name": "EGERTON UNIVERSITY", "type": "University"},
    {"id": 41, "code": "EKERUBO GIETAI TTI", "name": "EKERUBO GIETAI TECHNICAL TRAINING INSTITUTE", "type": "Institute"},
    {"id": 42, "code": "ELDAMA RAVINE TVC", "name": "ELDAMA RAVINE TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 43, "code": "ELDO POLY", "name": "ELDORET POLYTECHNIC", "type": "Polytechnic"},
    {"id": 44, "code": "ELWAK TVC", "name": "ELWAK TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 45, "code": "EMGWEN TVC", "name": "EMGWEN TECHNICAL & VOCATIONAL COLLEGE", "type": "College"},
    {"id": 46, "code": "EMBU COLLEGE", "name": "EMBU COLLEGE", "type": "College"},
    {"id": 47, "code": "EU", "name": "EMBU UNIVERSITY", "type": "University"},
    {"id": 48, "code": "ENZUI TTI", "name": "ENZUI TECHNICAL TRAINING INSTITUTE", "type": "Institute"},
    {"id": 49, "code": "ESAGERI TVC", "name": "ESAGERI TECHNICAL AND VOCATIONAL COLLEGE", "type": "College"},
    {"id": 50, "code": "GRETSA", "name": "GRETSA UNIVERSITY", "type": "University"}
]'

# Create directories
echo "$data" | jq -c '.[]' | while read -r entry; do
    code=$(echo "$entry" | jq -r '.code')
    name=$(echo "$entry" | jq -r '.name')
    mkdir -p "./$code - $name"
done

echo "Directories created successfully."
