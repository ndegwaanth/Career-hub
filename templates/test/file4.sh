#!/bin/bash

data='[
    {
        "id": 171,
        "code": "MERTI TTI",
        "name": "MERTI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 172,
        "code": "MERU POLY",
        "name": "MERU NATIONAL POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 173,
        "code": "MUST",
        "name": "MERU UNIVERSITY OF SCIENCE AND TECHNOLOGY",
        "type": "university"
    },
    {
        "id": 174,
        "code": "MICHUKI TTI",
        "name": "MICHUKI TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 175,
        "code": "MITUNGUU TTI",
        "name": "MITUNGUU TECHNICAL TRAINING INSTITUTE",
        "type": "institute"
    },
    {
        "id": 176,
        "code": "MOCHONGOI TVC",
        "name": "MOCHONGOI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 177,
        "code": "MU",
        "name": "MOI UNIVERSITY",
        "type": "university"
    },
    {
        "id": 178,
        "code": "MOIBEN TVC",
        "name": "MOIBEN TECHNICAL VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 179,
        "code": "MOLO TVC",
        "name": "MOLO TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 180,
        "code": "MORENDAT",
        "name": "MORENDAT INSTITUTE OF OIL AND GAS",
        "type": "college"
    },
    {
        "id": 181,
        "code": "MKU",
        "name": "MOUNT KENYA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 182,
        "code": "MSAMBWENI TVC",
        "name": "MSAMBWENI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 183,
        "code": "MUKIRIA TTI",
        "name": "MUKIRIA TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 184,
        "code": "MUKURWEINI TTI",
        "name": "MUKURWEINI TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 185,
        "code": "MULANGO TVC",
        "name": "MULANGO TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 186,
        "code": "MMU",
        "name": "MULTIMEDIA UNIVERSITY OF KENYA",
        "type": "university"
    },
    {
        "id": 187,
        "code": "MUMIAS WEST TVC",
        "name": "MUMIAS WEST TECHNICAL VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 188,
        "code": "MUNGATSI TVC",
        "name": "MUNGATSI TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 189,
        "code": "MURAGA TVC",
        "name": "MURAGA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 190,
        "code": "MURANGA TTI",
        "name": "MURANGA TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 191,
        "code": "MUT",
        "name": "MURANGA UNIVERSITY OF TECHNOLOGY",
        "type": "university"
    },
    {
        "id": 192,
        "code": "MURANGA UNIVERSITY TI",
        "name": "MURANGA UNIVERSITY OF TECHNOLOGY TVET INSTITUTE",
        "type": "college"
    },
    {
        "id": 193,
        "code": "MUSAKASA TTI",
        "name": "MUSAKASA TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 194,
        "code": "MWALA TVC",
        "name": "MWALA TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 195,
        "code": "MWEA TVC",
        "name": "MWEA TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 196,
        "code": "NACHU TVC",
        "name": "NACHU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 197,
        "code": "NAIROBI TTI",
        "name": "NAIROBI TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 198,
        "code": "NAIVASHA TVC",
        "name": "NAIVASHA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 199,
        "code": "NAROK WEST TTI",
        "name": "NAROK WEST TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 200,
        "code": "NAVAKHOLO TVC",
        "name": "NAVAKHOLO TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 201,
        "code": "NDARAGWA TVC",
        "name": "NDARAGWA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 202,
        "code": "NDIA TVC",
        "name": "NDIA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 203,
        "code": "NGONG TVC",
        "name": "NGONG TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 204,
        "code": "NJORO TTI",
        "name": "NJORO TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 205,
        "code": "NKABUNE TTI",
        "name": "NKABUNE TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 206,
        "code": "NEPOLY",
        "name": "NORTH EASTERN NATIONAL POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 207,
        "code": "NORTH HORR TVC",
        "name": "NORTH HORR TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 208,
        "code": "NUU TVC",
        "name": "NUU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 209,
        "code": "NYAKACH TVC",
        "name": "NYAKACH TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 210,
        "code": "NYANDARUA POLY",
        "name": "NYANDARUA NATIONAL POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 211,
        "code": "NYERI POLY",
        "name": "NYERI NATIONAL POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 212,
        "code": "OKAME TVC",
        "name": "OKAME TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 213,
        "code": "OLLESSOS TTI",
        "name": "OLLESSOS TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 214,
        "code": "OMUGA TVC",
        "name": "OMUGA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 215,
        "code": "OROGARE TVC",
        "name": "OROGARE TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 216,
        "code": "PAC",
        "name": "PAN AFRICA CHRISTIAN UNIVERSITY",
        "type": "university"
    },
    {
        "id": 217,
        "code": "PCKINYANJUI TTI",
        "name": "PC KINYANJUI TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 218,
        "code": "PIU",
        "name": "PIONEER INTERNATIONAL UNIVERSITY",
        "type": "university"
    },
    {
        "id": 219,
        "code": "PUEA",
        "name": "PRESBYTERIAN UNIVERSITY OF EAST AFRICA",
        "type": "university"
    },
    {
        "id": 220,
        "code": "PU",
        "name": "PWANI UNIVERSITY",
        "type": "university"
    },
    {
        "id": 221,
        "code": "RACHUONYO TVC",
        "name": "RACHUONYO TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 222,
        "code": "RTI",
        "name": "RAILWAY TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 223,
        "code": "RIAT",
        "name": "RAMOGI INSTITUTE OF ADVANCE TECHNOLOGY",
        "type": "college"
    },
    {
        "id": 224,
        "code": "RANGWE TVC",
        "name": "RANGWE TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 225,
        "code": "RCMRD",
        "name": "REGIONAL CENTRE FOR MAPPING OF RESOURCES FOR DEVELOPMENT",
        "type": "college"
    },
    {
        "id": 226,
        "code": "RIAMO TVC",
        "name": "RIAMO TECHNICAL VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 227,
        "code": "RU",
        "name": "RIARA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 228,
        "code": "RIATIRIMBA TVC",
        "name": "RIATIRIMBA TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 229,
        "code": "RVIST",
        "name": "RIFT VALLEY INSTITUTE OF SCIENCE AND TECHNOLOGY",
        "type": "college"
    },
    {
        "id": 230,
        "code": "RIFT VALLEY TTI",
        "name": "RIFT VALLEY TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 231,
        "code": "RIRAGIA TTI",
        "name": "RIRAGIA TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 232,
        "code": "RNU",
        "name": "RONGO UNIVERSITY",
        "type": "university"
    },
    {
        "id": 233,
        "code": "RONGO UNIVERSITY TI",
        "name": "RONGO UNIVERSITY TECHNICAL & VOCATIONAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 234,
        "code": "RUIRU TVC",
        "name": "RUIRU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 235,
        "code": "RUNYENJES TVC",
        "name": "RUNYENJES TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 236,
        "code": "SABATIA TVC",
        "name": "SABATIA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 237,
        "code": "SABU",
        "name": "SABU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 238,
        "code": "SAGANA TVC",
        "name": "SAGANA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 239,
        "code": "SAIKERI TVC",
        "name": "SAIKERI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 240,
        "code": "SAIMO KIPSARAMAN TVC",
        "name": "SAIMO KIPSARAMAN TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 241,
        "code": "SAKWA TVC",
        "name": "SAKWA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 242,
        "code": "SAMBURU TTI",
        "name": "SAMBURU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 243,
        "code": "SANGALO TTI",
        "name": "SANGALO TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 244,
        "code": "SAUNI TVC",
        "name": "SAUNI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 245,
        "code": "SCIE",
        "name": "SIGALAGALA NATIONAL POLYTECHNIC",
        "type": "college"
    },
    {
        "id": 246,
        "code": "SHANZU TTI",
        "name": "SHANZU TEACHERS TRAINING COLLEGE",
        "type": "college"
    },
    {
        "id": 247,
        "code": "SIGOR TVC",
        "name": "SIGOR TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 248,
        "code": "SIT",
        "name": "SIKRI TECHNICAL TRAINING INSTITUTE FOR THE BLIND AND DEAF",
        "type": "college"
    },
    {
        "id": 249,
        "code": "SIGOR TTI",
        "name": "SIRISIA TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 250,
        "code": "SITTV",
        "name": "SIKRI TECHNICAL AND VOCATIONAL COLLEGE FOR THE BLIND AND DEAF",
        "type": "college"
    },
        {
        "id": 251,
        "code": "SEKU",
        "name": "SOUTH EASTERN KENYA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 252,
        "code": "ST.JOSEPH TI",
        "name": "ST JOSEPHS TECHNICAL INSTITUTE FOR THE DEAF NYANGOMA",
        "type": "college"
    },
    {
        "id": 253,
        "code": "SPU",
        "name": "ST PAULS UNIVERSITY",
        "type": "university"
    },
    {
        "id": 254,
        "code": "TTU",
        "name": "TAITA TAVETA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 255,
        "code": "TANA RIVER TVC",
        "name": "TANA RIVER TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 256,
        "code": "TUC",
        "name": "TANGAZA UNIVERSITY COLLEGE",
        "type": "university"
    },
    {
        "id": 257,
        "code": "TAVETA TVC",
        "name": "TAVETA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 258,
        "code": "TUK",
        "name": "TECHNICAL UNIVERSITY OF KENYA",
        "type": "university"
    },
    {
        "id": 259,
        "code": "TUM",
        "name": "TECHNICAL UNIVERSITY OF MOMBASA",
        "type": "university"
    },
    {
        "id": 260,
        "code": "TETU TVC",
        "name": "TETU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 261,
        "code": "THARAKA TVC",
        "name": "THARAKA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 262,
        "code": "THRKU",
        "name": "THARAKA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 263,
        "code": "THARAKA UNIVERSITY TI",
        "name": "THARAKA UNIVERSITY TVET INSTITUTE",
        "type": "college"
    },
    {
        "id": 264,
        "code": "CUK NAIROBI CBD TI",
        "name": "THE CUK NAIROBI CBD TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 265,
        "code": "TEAU",
        "name": "THE EAST AFRICAN UNIVERSITY",
        "type": "university"
    },
    {
        "id": 266,
        "code": "UOEM TI",
        "name": "THE UNIVERSITY OF EMBU TVET INSTITUTE",
        "type": "college"
    },
    {
        "id": 267,
        "code": "THIKA TTI",
        "name": "THIKA TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 268,
        "code": "TIGANIA EAST TVC",
        "name": "TIGANIA EAST TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 269,
        "code": "TINDIRET TVC",
        "name": "TINDIRET TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 270,
        "code": "TOMBOYA LC",
        "name": "TOM MBOYA LABOUR COLLEGE",
        "type": "college"
    },
    {
        "id": 271,
        "code": "TMU",
        "name": "TOM MBOYA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 272,
        "code": "TOTAL TVC",
        "name": "TOTAL TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 273,
        "code": "TSEIKURU TTI",
        "name": "TSEIKURU TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 274,
        "code": "TURBO TVC",
        "name": "TURBO TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
        {
        "id": 275,
        "code": "TURKANA EAST TVC",
        "name": "TURKANA EAST TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 276,
        "code": "TURKANA NORTH TVC",
        "name": "TURKANA NORTH TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 277,
        "code": "TRUC",
        "name": "TURKANA UNIVERSITY COLLEGE",
        "type": "university"
    },
    {
        "id": 278,
        "code": "UGENYA TVC",
        "name": "UGENYA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 279,
        "code": "UGUNJA TVC",
        "name": "UGUNJA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 280,
        "code": "BARA",
        "name": "UNIVERSITY OF EASTERN AFRICA, BARATON",
        "type": "university"
    },
    {
        "id": 281,
        "code": "UOE",
        "name": "UNIVERSITY OF ELDORET",
        "type": "university"
    },
    {
        "id": 282,
        "code": "UOEM",
        "name": "UNIVERSITY OF EMBU",
        "type": "university"
    },
    {
        "id": 283,
        "code": "UOK",
        "name": "UNIVERSITY OF KABIANGA",
        "type": "university"
    },
    {
        "id": 284,
        "code": "UON",
        "name": "UNIVERSITY OF NAIROBI",
        "type": "university"
    },
    {
        "id": 285,
        "code": "URIRI TVC",
        "name": "URIRI TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 286,
        "code": "UZIMA",
        "name": "UZIMA UNIVERSITY",
        "type": "university"
    },
    {
        "id": 287,
        "code": "WAJIR EAST TVC",
        "name": "WAJIR EAST TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 288,
        "code": "WANGA TVC",
        "name": "WANGA TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 289,
        "code": "WEBUYE WEST TVC",
        "name": "WEBUYE WEST TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 290,
        "code": "WERU TVC",
        "name": "WERU TECHNICAL AND VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 291,
        "code": "WOTE TTI",
        "name": "WOTE TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 292,
        "code": "WUMINGU TVC",
        "name": "WUMINGU TECHNICAL & VOCATIONAL COLLEGE",
        "type": "college"
    },
    {
        "id": 293,
        "code": "ZETECH",
        "name": "ZETECH UNIVERSITY",
        "type": "university"
    },
    {
        "id": 294,
        "code": "ZIWA TTI",
        "name": "ZIWA TECHNICAL TRAINING INSTITUTE",
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
