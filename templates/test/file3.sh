#!/bin/bash

# Define the JSON data
data='[
    {
        "id": 101,
        "code": "KEWI",
        "name": "KENYA WATER INSTITUTE",
        "type": "institute"
    },
    {
        "id": 102,
        "code": "KWSTI",
        "name": "KENYA WILDLIFE SERVICE TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 103,
        "code": "KU",
        "name": "KENYATTA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 104,
        "code": "MNUC",
        "name": "KENYATTA UNIVERSITY - MAMA NGINA UNIVERSITY COLLEGE",
        "type": "college"
    },
    {
        "id": 105,
        "code": "KERICHO TOWNSHIP TVC",
        "name": "KERICHO TOWNSHIP TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 106,
        "code": "KERIO VALLEY TVC",
        "name": "KERIO VALLEY TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 107,
        "code": "KEROKA TTI",
        "name": "KEROKA TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 108,
        "code": "KIST",
        "name": "KIAMBU INSTITUTE OF SCIENCE AND TECHNOLOGY",
        "type": "institute"
    },
    {
        "id": 109,
        "code": "KIBABII TTC",
        "name": "KIBABII DIPLOMA TEACHERS TRAINING COLLEGE",
        "type": "college"
    },
    {
        "id": 110,
        "code": "KBBU",
        "name": "KIBABII UNIVERSITY",
        "type": "university"
    },
    {
        "id": 111,
        "code": "KIBWEZI TVC",
        "name": "KIBWEZI TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 112,
        "code": "KIENI TVC",
        "name": "KIENI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 113,
        "code": "KIGUMO TTI",
        "name": "KIGUMO TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 114,
        "code": "KIIRUA TTI",
        "name": "KIIRUA TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 115,
        "code": "KIMASIAN TVC",
        "name": "KIMASIAN TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 116,
        "code": "KIMININI TVC",
        "name": "KIMININI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 117,
        "code": "KINANGO TVC",
        "name": "KINANGO TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 118,
        "code": "KINANGOP TVC",
        "name": "KINANGOP TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 119,
        "code": "KIPIPIRI TVC",
        "name": "KIPIPIRI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 120,
        "code": "KIPKABUS TVC",
        "name": "KIPKABUS TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 121,
        "code": "KIPSINENDE TVC",
        "name": "KIPSINENDE TECHNICAL VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 122,
        "code": "KIPSOEN TVC",
        "name": "KIPSOEN TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 123,
        "code": "KIPTARAGON TVC",
        "name": "KIPTARAGON TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 124,
        "code": "KYU",
        "name": "KIRINYAGA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 125,
        "code": "KWUST",
        "name": "KIRIRI WOMENS UNIVERSITY OF SCIENCE AND TECHNOLOGY",
        "type": "university"
    },
    {
        "id": 126,
        "code": "KSI POLY",
        "name": "KISII NATIONAL POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 127,
        "code": "KSU",
        "name": "KISII UNIVERSITY",
        "type": "university"
    },
    {
        "id": 128,
        "code": "KISII UNIVERSITY TI",
        "name": "KISII UNIVERSITY TVET INSTITUTE",
        "type": "college"
    },
    {
        "id": 129,
        "code": "KISTVC",
        "name": "KISIWA TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 130,
        "code": "KICDT",
        "name": "KISUMU INSTITUTE OF COMMUNITY DEVELOPMENT TRAINING",
        "type": "college"
    },
    {
        "id": 131,
        "code": "KSM POLY",
        "name": "KISUMU POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 132,
        "code": "KITALE NP",
        "name": "KITALE NATIONAL POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 133,
        "code": "KITELAKAPEL TTI",
        "name": "KITELAKAPEL TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 134,
        "code": "KITUTU MASABA TVC",
        "name": "KITUTU MASABA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 135,
        "code": "KSUC",
        "name": "KOITALEEL SAMOEI UNIVERSITY COLLEGE",
        "type": "university"
    },
    {
        "id": 136,
        "code": "KONGONI TVC",
        "name": "KONGONI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 137,
        "code": "KONOIN TTI",
        "name": "KONOIN TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 138,
        "code": "KOSHIN TTI",
        "name": "KOSHIN TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 139,
        "code": "LAIKIPIA EAST TVC",
        "name": "LAIKIPIA EAST TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 140,
        "code": "LAIKIPIA NORTH TVC",
        "name": "LAIKIPIA NORTH TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 141,
        "code": "LU",
        "name": "LAIKIPIA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 142,
        "code": "LAIKIPIA UNIVERSITY TI",
        "name": "LAIKIPIA UNIVERSITY TVET INSTITUTE",
        "type": "college"
    },
    {
        "id": 143,
        "code": "LAISAMIS TVC",
        "name": "LAISAMIS TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 144,
        "code": "LARI TVC",
        "name": "LARI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 145,
        "code": "LIKONI TVC",
        "name": "LIKONI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 146,
        "code": "LIMURU TVC",
        "name": "LIMURU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 147,
        "code": "LODWAR TVC",
        "name": "LODWAR TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 148,
        "code": "LUGARI TTC",
        "name": "LUGARI DIPLOMA TEACHERS TRAINING COLLEGE",
        "type": "college"
    },
    {
        "id": 149,
        "code": "LUKENYA",
        "name": "LUKENYA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 150,
        "code": "LUNGA LUNGA TVC",
        "name": "LUNGA LUNGA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 151,
        "code": "MMTVC",
        "name": "MAASAI MARA TECHNICAL VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 152,
        "code": "MMARAU",
        "name": "MAASAI MARA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 153,
        "code": "MABERA TVC",
        "name": "MABERA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 154,
        "code": "MTIB",
        "name": "MACHAKOS TECHNICAL INSTITUTE FOR THE BLIND",
        "type": "institute"
    },
    {
        "id": 155,
        "code": "MCKU",
        "name": "MACHAKOS UNIVERSITY",
        "type": "university"
    },
    {
        "id": 156,
        "code": "MAMA NGINA UNIVERSITY COLLEGE",
        "name": "MAMA NGINA UNIVERSITY COLLEGE",
        "type": "college"
    },
    {
        "id": 157,
        "code": "MUA",
        "name": "MANAGEMENT UNIVERSITY OF AFRICA",
        "type": "university"
    },
    {
        "id": 158,
        "code": "MANDERA TTI",
        "name": "MANDERA TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 159,
        "code": "MANYATTA TVC",
        "name": "MANYATTA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 160,
        "code": "MARIST",
        "name": "MARIST INTERNATIONAL UNIVERSITY COLLEGE",
        "type": "college"
    },
    {
        "id": 161,
        "code": "MASAI TTI",
        "name": "MASAI TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 162,
        "code": "MSU",
        "name": "MASENO UNIVERSITY",
        "type": "university"
    },
    {
        "id": 163,
        "code": "MMUST",
        "name": "MASINDE MULIRO UNIVERSITY OF SCIENCE & TECHNOLOGY",
        "type": "university"
    },
    {
        "id": 164,
        "code": "MASINGA TVC",
        "name": "MASINGA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 165,
        "code": "MATHENGE TTI",
        "name": "MATHENGE TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 166,
        "code": "MATHIOYA TVC",
        "name": "MATHIOYA TECHNICAL VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 167,
        "code": "MATHIRA TVC",
        "name": "MATHIRA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 168,
        "code": "MATILI TTI",
        "name": "MATILI TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 169,
        "code": "MAWEGO TTI",
        "name": "MAWEGO TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 170,
        "code": "MBEERE NORTH TVC",
        "name": "MBEERE NORTH TVC TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    }
]'

# Create a base directory
# Create directories
echo "$data" | jq -c '.[]' | while read -r entry; do
    code=$(echo "$entry" | jq -r '.code')
    name=$(echo "$entry" | jq -r '.name')
    mkdir -p "./$code - $name"
done

echo "Directories created successfully."
