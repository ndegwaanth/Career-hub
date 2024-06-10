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
    },
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
    },
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
        "name": "MURANG'A TECHNICAL TRAINING INSTITUTE",
        "type": "college"
    },
    {
        "id": 191,
        "code": "MUT",
        "name": "MURANG'A UNIVERSITY OF TECHNOLOGY",
        "type": "university"
    },
    {
        "id": 192,
        "code": "MURANG'A UNIVERSITY TI",
        "name": "MURANG'A UNIVERSITY OF TECHNOLOGY TVET INSTITUTE",
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
        "code": "OL'LESSOS TTI",
        "name": "OL'LESSOS TECHNICAL TRAINING INSTITUTE",
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
        "code": "SANG'ALO TTI",
        "name": "SANG'ALO TECHNICAL TRAINING INSTITUTE",
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
        "name": "ST JOSEPH'S TECHNICAL INSTITUTE FOR THE DEAF NYANG'OMA",
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
]

base_directory = "institutions"

# Create the base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Create a folder for each institution
for institution in data:
    folder_name = f"{institution['code']}_{institution['name']}"
    folder_path = os.path.join(base_directory, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Save institution data to a JSON file in the folder
    json_file_path = os.path.join(folder_path, "data.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(institution, json_file, indent=4)

print("Folders and JSON files created successfully.")
