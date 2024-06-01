import os
import json

data = [
    {
        "id": 51,
        "code": "GAITU TTI",
        "name": "GAITU TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 52,
        "code": "GFTI",
        "name": "GATUNDU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "College"
    },
    {
        "id": 53,
        "code": "GEN MATHENGE TTI",
        "name": "GENERAL MATHENGE TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 54,
        "code": "GTTI",
        "name": "GEREGERA TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 55,
        "code": "GTTI",
        "name": "GIKIIRO TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 56,
        "code": "GTTI",
        "name": "GITITU TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 57,
        "code": "GTTI",
        "name": "GITHABAI TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 58,
        "code": "GTTI",
        "name": "GITONGA TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 59,
        "code": "GTTI",
        "name": "GITUGI TECHNICAL TRAINING INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 60,
        "code": "GG",
        "name": "GUSII INSTITUTE OF TECHNOLOGY",
        "type": "Institute"
    },
    {
        "id": 61,
        "code": "HHKII",
        "name": "HASSAN HUSSEIN K HALGHO TECHNICAL AND VOCATIONAL INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 62,
        "code": "HIBS",
        "name": "HENRY INSTITUTE OF BUSINESS STUDIES",
        "type": "Institute"
    },
    {
        "id": 63,
        "code": "HU",
        "name": "HUMANITARIAN ACADEMY FOR DEVELOPMENT UNIVERSITY",
        "type": "University"
    },
    {
        "id": 64,
        "code": "IBIST",
        "name": "INSTITUTE OF BUSINESS INNOVATION AND TECHNICAL SKILLS",
        "type": "Institute"
    },
    {
        "id": 65,
        "code": "INERELA+",
        "name": "INTERNATIONAL NETWORK OF RELIGIOUS LEADERS LIVING WITH HIV AND AIDS, KENYA CHAPTER",
        "type": "Institute"
    },
    {
        "id": 66,
        "code": "IOB",
        "name": "INSTITUTE OF BUSINESS AND TECHNOLOGY",
        "type": "Institute"
    },
    {
        "id": 67,
        "code": "ICS",
        "name": "INSTITUTE OF CERTIFIED SECRETARIES",
        "type": "Institute"
    },
    {
        "id": 68,
        "code": "IBM",
        "name": "INSTITUTE OF BUSINESS MANAGEMENT",
        "type": "Institute"
    },
    {
        "id": 69,
        "code": "IU",
        "name": "INTERNATIONAL UNIVERSITY OF PROFESSIONAL STUDIES",
        "type": "University"
    },
    {
        "id": 70,
        "code": "JC",
        "name": "JARAMOGI OGINGA ODINGA UNIVERSITY OF SCIENCE AND TECHNOLOGY",
        "type": "University"
    },
    {
        "id": 71,
        "code": "JKUAT",
        "name": "JOMO KENYATTA UNIVERSITY OF AGRICULTURE AND TECHNOLOGY",
        "type": "University"
    },
    {
        "id": 72,
        "code": "KAG EAST UNIVERSITY",
        "name": "KAG EAST UNIVERSITY",
        "type": "University"
    },
    {
        "id": 73,
        "code": "KAGUMO TTC",
        "name": "KAGUMO TEACHERS TRAINING COLLEGE",
        "type": "College"
    },
    {
        "id": 74,
        "code": "KCA",
        "name": "KCA UNIVERSITY",
        "type": "University"
    },
    {
        "id": 75,
        "code": "KEFRI",
        "name": "KENYA FORESTRY RESEARCH INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 76,
        "code": "KSL",
        "name": "KENYA SCHOOL OF LAW",
        "type": "Institute"
    },
    {
        "id": 77,
        "code": "KENYATTA UNIVERSITY",
        "name": "KENYATTA UNIVERSITY",
        "type": "University"
    },
    {
        "id": 78,
        "code": "KCA",
        "name": "KENYA ACCOUNTANTS AND SECRETARIES NATIONAL EXAMINATIONS BOARD",
        "type": "Institute"
    },
    {
        "id": 79,
        "code": "KIM",
        "name": "KENYA INSTITUTE OF MANAGEMENT",
        "type": "Institute"
    },
    {
        "id": 80,
        "code": "KMTC",
        "name": "KENYA MEDICAL TRAINING COLLEGE",
        "type": "Institute"
    },
    {
        "id": 81,
        "code": "KNEC",
        "name": "KENYA NATIONAL EXAMINATIONS COUNCIL",
        "type": "Institute"
    },
    {
        "id": 82,
        "code": "KENYA WATER INSTITUTE",
        "name": "KENYA WATER INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 83,
        "code": "KIAMBU INSTITUTE OF SCIENCE AND TECHNOLOGY",
        "name": "KIAMBU INSTITUTE OF SCIENCE AND TECHNOLOGY",
        "type": "Institute"
    },
    {
        "id": 84,
        "code": "KIBABII UNIVERSITY",
        "name": "KIBABII UNIVERSITY",
        "type": "University"
    },
    {
        "id": 85,
        "code": "KENYA SCHOOL OF GOVERNMENT",
        "name": "KENYA SCHOOL OF GOVERNMENT",
        "type": "Institute"
    },
    {
        "id": 86,
        "code": "KENYA TECHNICAL TEACHERS COLLEGE",
        "name": "KENYA TECHNICAL TEACHERS COLLEGE",
        "type": "College"
    },
    {
        "id": 87,
        "code": "KIRIRI WOMENS UNIVERSITY OF SCIENCE AND TECHNOLOGY",
        "name": "KIRIRI WOMENS UNIVERSITY OF SCIENCE AND TECHNOLOGY",
        "type": "University"
    },
    {
        "id": 88,
        "code": "KENYA MEDICAL RESEARCH INSTITUTE",
        "name": "KENYA MEDICAL RESEARCH INSTITUTE",
        "type": "Institute"
    },
    {
        "id": 89,
        "code": "KABIANGA",
        "name": "KABIANGA UNIVERSITY",
        "type": "University"
    },
    {
        "id": 90,
        "code": "KEMU",
        "name": "KENYA METHODIST UNIVERSITY",
        "type": "University"
    },
    {
        "id": 91,
        "code": "KENYA UTALII COLLEGE",
        "name": "KENYA UTALII COLLEGE",
        "type": "Institute"
    },
    {
        "id": 92,
        "code": "KISUMU NATIONAL POLYTECHNIC",
        "name": "KISUMU NATIONAL POLYTECHNIC",
        "type": "Polytechnic"
    },
    {
        "id": 93,
        "code": "KITI",
        "name": "KENYA INDUSTRIAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 94,
        "code": "KIHBT",
        "name": "KENYA INSTITUTE OF HIGHWAYS AND BUILDING TECHNOLOGY",
        "type": "institute"
    },
    {
        "id": 95,
        "code": "KIMC",
        "name": "KENYA INSTITUTE OF MASS COMMUNICATION",
        "type": "institute"
    },
    {
        "id": 96,
        "code": "KISM",
        "name": "KENYA INSTITUTE OF SURVEYING AND MAPPING",
        "type": "institute"
    },
    {
        "id": 97,
        "code": "KEMU",
        "name": "KENYA METHODIST UNIVERSITY",
        "type": "university"
    },
    {
        "id": 98,
        "code": "KSA",
        "name": "KENYA SCHOOL OF AGRICULTURE",
        "type": "school"
    },
    {
        "id": 99,
        "code": "KESRA",
        "name": "KENYA SCHOOL OF REVENUE ADMINISTRATION",
        "type": "school"
    },
    {
        "id": 100,
        "code": "KTTC",
        "name": "KENYA TECHNICAL TRAINERS COLLEGE",
        "type": "college"
    }
]

base_directory = "institutions"

# Create the base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Create a folder for each institution
for institution in data:
    folder_name = f"{institution['id']}_{institution['code']}"
    folder_path = os.path.join(base_directory, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Save institution data to a JSON file in the folder
    json_file_path = os.path.join(folder_path, "data.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(institution, json_file, indent=4)

print("Folders and JSON files created successfully.")
