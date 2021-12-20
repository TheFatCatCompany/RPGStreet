import discord
import asyncio
from discord.ext import commands, tasks
import math
import random
import sys
import time
import datetime
import pytz
import fileinput
import json
import requests
import io
import pickle
import os
import numpy
import key
intents = discord.Intents().default()
intents.members = True
client = commands.Bot(command_prefix = '*', intents = intents)
ishibashiResetTime = None
import time
Car_HP = {
"2000 Honda Integra" : 120,
"2000 Honda Integra Type R" : 187,
"1999 Honda Civic Type R EK9" : 183,
"2003 Honda Civic Type R EP3" : 215,
"2003 Honda NSX R" : 296,
"2001 Honda S2000" : 240,
"2021 Honda Civic Type R FK8" : 306,
"1991 Honda Civic EG6 SiR": 168,
"1999 Honda Civic LX": 106,
"2006 Honda Civic Si": 197,
"2018 Honda Civic Sport": 180,
"2018 Honda Civic Si Coupe": 205,
"2006 Honda Accord 3.0 EX": 244,
"2010 Honda Accord EX-L V6": 271,
"2015 Honda Accord Sport": 189,
"2015 Honda Accord EX-L V6": 278,
"2018 Honda Accord Sport": 192,
"2021 Honda CR-V": 190,
"1999 Honda CR-V": 146,
"2005 Honda Pilot": 255,
"2010 Honda Crosstour": 271,
"2005 Honda Element": 160,
"2001 Honda Odyssey Absolute": 200,
"2021 Honda N-ONE RS": 64,
"2021 Honda StepWGN Spada": 148,
"1999 Honda StepWGN": 125,
"2016 Honda CR-Z": 130,
"2021 Honda HR-V": 141, 
"2005 Honda Stream": 130,
"2014 Honda Stream": 150,
"2021 Honda Clarity": 212,
"2000 Honda Insight": 80,
"2021 Honda Insight": 151,
"2000 Honda ACTY": 45,
"2021 Honda ACTY": 45,
"2021 Honda Fit": 130,
"2001 Honda Life Dunk": 64,
"1992 Honda Vigor": 176,
"1989 Honda Accord": 120,
"2003 Acura RSX Type S" : 200,
"2017 Acura NSX" : 500,
"2005 Acura TL Type S": 286,
"2007 Acura TL": 258,
"2018 Acura TLX 3.5": 290,
"2018 Acura MDX": 290,
"2018 Acura ILX": 201,
"2021 Acura TLX Type S": 355,
"1995 Acura Legend": 230,
"2014 Acura TSX Sport Wagon": 201,
"1990 Ford Mustang Foxbody" : 220,
"2010 Ford Mustang GT500" : 500,
"2015 Ford Mustang GT" : 435,
"1975 Ford Pinto": 150,
"1999 Ford Crown Victoria": 200,
"2017 Ford Focus Hatch": 123,
"2017 Ford Focus RS": 350,
"2017 Ford Fusion Titanium": 231,
"2017 Ford Fusion Sport": 325,
"2018 Ford F-150 Super Cab": 325,
"2018 Ford F-150 Raptor": 450,
"2016 Shelby Mustang GT350R" : 526,
"1992 Volkswagen Golf GTi MK2" : 137,
"2017 Volkswagen Golf GTi MK7" : 230,
"2015 Volkswagen Scirocco R" : 280,
"2018 Volkswagen Passat R-Line": 174,
"1969 Volkswagen Beetle": 53,
"1999 BMW M3" : 240,
"2003 BMW M3" : 333,
"2008 BMW M3" : 414,
"2017 BMW M3" : 425,
"2005 BMW M5" : 507,
"2018 BMW M5" : 600,
"2017 BMW M4" : 425,
"2017 BMW M6" : 560,
"2018 BMW i8" : 231,
"1959 BMW 507": 150,
"2018 BMW 530i": 248,
"2018 BMW X3": 248,
"2018 BMW 750i": 445,
"1974 BMW 2002 Turbo": 169,
"2011 BMW 1M": 335,
"2018 BMW 330i": 248,
"2020 BMW M235i xDrive Gran Coupe": 301,
"2007 Saturn Ion": 145,
"2001 Saturn SL2": 124,
"1998 Saturn SW2": 114,
"2017 Ferrari 488GTB" : 661,
"2017 Ferrari F12" : 731,
"2003 Ferrari 575M Maranello" : 515,
"1999 Ferrari 360" : 400,
"1995 Ferrari F355" : 375,
"1965 Ferrari 250 GTO" : 296,
"1968 Ferrari Dino" : 177,
"1970 Ferrari 365 GTB/4 Daytona" : 352,
"2008 Ferrari F430" : 503,
"2008 Ferrari California" : 454,
"2016 Ferrari LaFerrari" : 949,
"2010 Ferrari 458 Italia": 570,
"1993 Toyota MR2 GT-S" : 218,
"1986 Toyota Corolla Sprinter Trueno" : 112,
"1993 Toyota Supra Twin Turbo" : 320,
"1998 Toyota Chaser Tourer V" : 295,
"1997 Toyota Soarer" : 295,
"1998 Toyota Altezza RS200" : 207,
"1996 Toyota Cresta 2.5 Twin Turbo": 295,
"1984 Toyota Landcruiser 60 3F" : 155,
"2003 Toyota Tundra" : 245,
"2018 Toyota Land Cruiser Prado" : 170,
"2018 Toyota 4Runner TRD Pro" : 270,
"2018 Toyota Tundra TRD Pro" : 381,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 150,
"2017 Toyota Century": 376,
"2019 Toyota Corolla Hatch XSE": 168,
"2019 Toyota Corolla Hatch SE": 168,
"2019 Toyota Corolla Touring Sport": 168,
"2021 Toyota GR Supra": 335,
"2008 Toyota Sequoia V8": 245, 
"2005 Toyota Camry LE V6": 210,
"1999 Toyota Corolla LE": 120,
"2002 Toyota Sienna 5D Symphony": 210,
"2010 Toyota Camry LE": 169, 
"2016 Toyota Avalon Limited": 268,
"2018 Toyota Camry XSE": 206,
"2018 Toyota Corolla XLE": 132,
"1969 Toyota 2000GT": 150,
"2001 Toyota Camry LE V6": 194,
"2006 Toyota Sienna Limited": 215,
"2017 Toyota Sienna SE": 296,
"2018 Toyota Sienta": 120,
"2018 Toyota Alphard": 268,
"2018 Toyota Crown Majesta": 245,
"2018 Toyota Tundra SR5 5.7L V8": 381,
"2018 Toyota Hiace": 134,
"1993 Toyota Hiace": 130, 
"1997 Toyota Celica GT-Four": 245,
"1998 Toyota GT-one TS020": 600,
"1993 Toyota Mark II Tourer V JZX90": 295,
"2018 Toyota GT86": 205,
"1997 Toyota Tercel": 95,
"1997 Toyota Celica GT": 135,
"2016 Toyota Land Cruiser": 381,
"2019 Toyota Tacoma SR5": 278,
"2019 Toyota Tacoma TRD Pro": 278,
"1993 Toyota Sera": 108,
"2020 Toyota Avalon Touring": 301,
"2020 Toyota Avalon Limited": 301,
"2020 Toyota Avalon Limited Hybrid": 215,
"2020 Toyota Avalon TRD": 301,
"2020 Toyota Camry LE": 203,
"2020 Toyota Camry SE Hybrid": 208,
"2011 Toyota Prius": 134,
"2020 Toyota Prius XLE AWD": 121,
"2021 Toyota GR Yaris": 268,
"2022 Toyota GR86 Base": 228,
"2022 Toyota GR86 Premium": 228,
"2018 Toyota Camry SE": 203,
"2009 Lexus LFA" : 552,
"2007 Lexus ISF" : 417,
"1998 Lexus GS300" : 218,
"2018 Lexus LC500" : 471,
"2018 Lexus LS500 AWD" : 415,
"2019 Lexus ES300h": 215,
"2018 Lexus GS F": 467,
"2003 Lexus LS430": 290,
"2019 Lexus RX350": 308,
"1999 Lexus RX300 4WD": 220,
"2019 Lexus LX570": 383,
"2022 Lexus IS500 F Sport Performance": 472,
"2022 Lexus IS350 F Sport": 311,
"1990 Nissan Skyline GTR R32" : 276,
"1994 Nissan Skyline GTR R33 Spec-V" : 276,
"1999 Nissan Skyline GTR R34": 325,
"2002 Nissan Skyline GTR V-Spec II Nur" : 330,
"1996 Nissan 180SX" : 205,
"1993 Nissan Silvia K's Type S S14" : 217,
"2018 Nissan GTR Track Edition R35" : 565,
"2007 Nissan Fairlady Z" : 309,
"2018 Nissan Fairlady Z NISMO" : 350,
"2018 Nissan Fairlady Z" : 332,
"1989 Nissan 300ZX Turbo Z" : 276,
"2018 Nissan GT-R50 by Italdesign": 720,
"2018 Nissan GT-R NISMO": 600,
"2018 Nissan Maxima Platinum": 300,
"2018 Nissan Sentra SR Turbo": 188,
"2017 Nissan Leaf": 148,
"1973 Nissan Skyline H/T 2000GT-R": 160,
"1987 Nissan Skyline GTSR R31": 210,
"1989 Nissan Skyline GTS-4 R32": 212,
"1998 Nissan Skyline 25GT-X Turbo R34": 276,
"1965 Nissan Silvia 1600 Coupe": 89,
"1990 Nissan Silvia S13": 135,
"1999 Nissan Silvia Spec-R S15": 250,
"1995 Nissan GT-R Skyline R33 LM": 300,
"1998 Nissan R390 GT1": 550,
"1992 Nissan Cefiro 2.0 Turbo": 205,
"1990 Nissan Laurel Turbo Medalist": 205,
"2017 Nissan Armada Platinum": 390,
"1994 Nissan Hardbody": 95,
"2018 Nissan Titan Platinum Reserve": 390,
"2003 Nissan Skyline GT-R R34 Z-Tune": 500,
"2015 Nissan Juke": 215,
"2021 Nissan Altima 2.0 SR": 236,
"2021 Nissan Altima 2.5 Platinum": 182,
"2022 Nissan GT-R T-Spec": 565,
"2015 Lamborghini Veneno": 750,
"2003 Lamborghini Gallardo" : 493,
"2007 Lamborghini Gallardo SL" : 523,
"2008 Lamborghini Gallardo LP560-4" : 552,
"2010 Lamborgini Gallardo LP570-4 SL ": 562,
"2013 Lamborghini Gallardo LP570-4 SC" : 562,
"2014 Lamborghini Huracan LP610-4" : 602,
"2017 Lamborghini Huracan Performante" : 630,
"2001 Lamborghini Murcielago" :572,
"2006 Lamborghini Murcielago LP640" : 631,
"2009 Lamborghini Murcielago LP670-4 SV" :660,
"2015 Lamborghini Aventador SV" : 740,
"2016 Lamborghini Aventador S" : 740,
"1971 Lamborghini Miura P400SV" : 385,
"1996 Lamborghini Diablo SV" : 510,
"1985 Lamborghini Countach LP5000s QV" : 449,
"2020 Lamborghini Sian": 819, 
"2021 Lamborghini Urus": 641,
"2021 Lamborghini Huracan Evo": 630,  
"1995 Lamborghini Diablo SE30 Jota": 600, 
"2000 Lamborghini Diablo GTR": 582, 
"2017 Bentley Continental GT" : 626,
"2015 Bentley Bentayga" : 600,
"2015 Koenigsegg Regera" : 1500,
"2010 Koenigsegg Agera" : 898,
"2007 Koenigsegg CCX" : 795,
"2005 Bugatti Veyron 16.4" : 1000,
"2016 Bugatti Chiron" : 1500,
"2017 Porsche 911 GT2 RS" : 690,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" :542,
"2016 Porsche 911 Turbo" : 542,
"2016 Porsche 718 Boxster" : 295,
"2017 Porsche 718 Cayman GTS" : 360,
"1975 Porsche 911 Turbo" : 270,
"1995 Porsche 911 GT2" : 430,
"1987 Porsche 959" : 445,
"1999 Porsche 911 GT3" : 355,
"1980 Porsche 924 Turbo": 177,
"2015 Lotus Evora 400" : 400,
"2011 Lotus Exige S" : 345,
"1996 Lotus Esprit V8" : 350,
"2006 Lotus Elise S" : 134,
"2022 Lotus Emira V6"
"2018 Mazda Miata MX-5 Club" : 155,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 178,
"1989 Mazda MX-5 Miata" : 113,
"1989 Mazda RX-7 Savanna Turbo" : 200,
"1992 Mazda RX-7" : 236,
"1998 Mazda RX-7 RZ" : 276,
"2009 Mazda RX-8" : 228,
"2019 Mazda6 Signature": 227,
"2019 Mazda3 Hatch": 186,
"2019 Mazda CX-5": 227,
"2019 Mazda CX-3": 148,
"2014 Mazda2": 100,
"2015 Mazda5": 157,
"2001 Mazda RX-7 Spirit R Type A" : 280,
"2006 Mazdaspeed 6 GT": 274,
"2013 Mazdaspeed 3": 263,
"2018 Morgan Three-Wheeler" : 80,
"1998 Subaru Impreza 22B STi": 300,
"1995 Subaru Impreza WRX STi Version II": 271,
"2002 Subaru Impreza WRX STi": 261,
"2003 Subaru Impreza WRX STi": 261,
"2005 Subaru Impreza WRX STi": 300,
"2010 Subaru Impreza WRX STi R205": 315,
"2019 Subaru WRX STi": 310,
"1993 Subaru SVX": 230,
"2000 Subaru Forester STI": 265,
"2019 Subaru WRX": 268,
"2022 Subaru WRX": 271,
"2018 Subaru BRZ": 205,
"2022 Subaru BRZ Premium": 228,
"2022 Subaru BRZ Limited": 228,
"1988 Isuzu Impulse": 140,
"1979 Isuzu 117 Coupe": 120,
"1994 Mitsubishi Lancer Evo II": 256,
"2010 Mitsubishi Lancer Evo X GSR": 295,
"1999 Mitsubishi Lancer Evo VI GSR":276,
"2004 Mitsubishi Lancer Evo VIII MR FQ400":405,
"2003 Mitsubishi Lancer Evo VIII GSR": 300,
"1994 Mitsubishi 3000 GT VR-4": 324,
"1994 Mitsubishi FTO GPX": 200,
"1992 Mitsubishi Galant VR-4": 205,
"1974 VAZ Lada 1200": 62,
"1975 UAZ-469": 75,
"1965 GAZ Volga 21": 75,
"1995 Hyundai Sonata 2.0i": 103,
"2013 Hyundai Genesis Coupe 3.8" : 348,
"2013 Hyundai Elantra GT": 148,
"2017 Hyundai Sonata Limited": 185,
"2005 Hyundai Tiburon GT V6": 170,
"2018 Kia Stinger GT": 365,
"2017 Kia Optima SX 2.0T": 245,
"2006 Audi R8": 414,
"2008 Audi R8 V10": 518,
"2010 Audi R8 GT": 552,
"2012 Audi R8 Plus": 542,
"2015 Audi R8 Coupe 5.2 FSI quattro": 610, 
"1994 Audi RS2 Avant": 315,
"2018 Audi RS5": 444,
"2018 Audi RS3": 400,
"2018 Audi RS7": 605,
"2018 Audi RS6 Avant": 596,
"2018 Audi TTRS": 400,
"2018 Mercedes-AMG E63 S 4Matic":603,
"2018 Mercedes-Maybach S560": 463,
"2018 Mercedes-AMG S65 Sedan": 621,
"1990 Mercedes-Benz 190E Evolution II": 235,
"2016 Mercedes-AMG GT S": 503,
"2013 Mercedes-Benz SLS AMG GT": 583,
"2012 Mercedes-Benz C63 AMG Black Series": 510,
"2000 Mercedes-Benz C32 AMG": 350,
"2020 Mercedes-AMG A35 4Matic": 302,
"2020 Chevy Corvette C8 Stingray Z51": 495,
"2019 Chevy Corvette C7 ZR1": 755,
"2018 Chevy Corvette C7 ZO6": 650,
"2018 Chevy Corvette C7 Stingray": 460,
"1953 Chevy Corvette": 150,
"1960 Chevy Corvette C1": 315,
"1963 Chevy Corvette C2 Stingray 427": 360,
"1967 Chevy Corvette C3 327": 300,
"1970 Chevy Corvette C3 454": 460,
"1984 Chevy Corvette C4": 205,
"1988 Chevy Corvette C4 ZR1": 375,
"2001 Chevy Corvette C5": 350,
"2002 Chevy Corvette C5 Z06": 405,
"2007 Chevy Corvette C6": 430,
"2007 Chevy Corvette C6 Z06": 505,
"2007 Chevy Corvette C6 ZR1": 638,
"2018 Chevy Camaro 1LE": 455,
"2018 Chevy Camaro ZL1": 650,
"1969 Chevy Camaro SS 396": 325,
"2017 Chevy Malibu 1.5 Turbo": 163,
"2016 Chevy Malibu 2LT": 247,
"2017 Chevy Cruze Hatch Premier": 153,
"2016 Chevy Impala LT": 305,
"2018 Alfa Romeo 4C": 237,
"2018 Alfa Romeo Giulia Quadrifoglio": 503,
"2018 Alfa Romeo Stelvio Quadrifoglio": 503,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 237,
"2013 Alfa Romeo MiTo 1.4 8v": 104,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 256,
"2006 Alfa Romeo 8c Competizione": 444,
"1992 Alfa Romeo 155 Q4": 187,
"1985 Alfa Romeo Spider Veloce": 126,
"2017 Suzuki Swift Sport": 138,
"2016 Suzuki Alto Works": 63,
"2016 Suzuki Hustler G 4WD": 51,
"2003 Suzuki Liana 1.6 Sedan": 104,
"1995 Suzuki Samurai 1.3i": 69,
"2002 Suzuki Grand Vitara": 142,
"2018 Pagani Huayra BC": 730,
"2013 Pagani Huayra": 720,
"2010 Pagani Zonda Cinque": 678,
"2005 Pagani Zonda F": 594,
"1999 Pagani Zonda C12S": 547,
"1970 AMC AMX": 340,
"1972 AMC Javelin": 220,
"1969 AMC Ambassador": 280,
"1970 AMC Rebel The Machine": 340,
"1975 AMC Pacer X": 152,
"2018 Dodge Challenger SRT Hellcat Widebody":707,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 485,
"2018 Dodge Challenger SRT Demon": 850,
"2008 Dodge Challenger SE": 250,
"2008 Dodge Challenger SRT8": 425,
"2018 Dodge Charger Hellcat": 707,
"2018 Dodge Charger GT Plus": 300,
"2011 Dodge Charger SRT8": 470,
"2005 Dodge Charger SRT8": 425,
"2017 Dodge Viper ACR": 645,
"2017 Dodge Viper GTS": 645,
"2012 Dodge Dart R/T": 184,
"2010 Dodge Avenger Express": 173,
"2008 Dodge Journey SXT": 235,
"2007 Dodge Nitro 4.0 R/T": 256,
"2007 Dodge Viper SRT-10": 600,
"2007 Dodge Viper SRT10 ACR": 600,
"2000 Dodge Intrepid R/T": 242,
"2003 Dodge Neon SRT-4": 230,
"1970 Dodge Dart Hemi Super Stock": 425,
"1970 Dodge Dart Swinger 340": 275,
"1970 Dodge Challenger R/T 426 Hemi": 425,
"1969 Dodge Charger Daytona Hemi": 425,
"1969 Dodge Charger R/T Hemi": 425,
"2018 Mclaren Senna": 800,
"2018 McLaren 720S": 710,
"2015 McLaren 570S": 562,
"2013 McLaren MP4-12C": 616,
"1992 McLaren F1": 618,
"1997 McLaren F1 GT": 618,
"1995 McLaren F1 LM": 680,
"2013 McLaren P1": 904,
"1974 MG Midget": 71,
"1928 MG M-Type Midget": 20,
"2007 Aston Martin DBS": 510,
"2016 Aston Martin DB11": 600,
"2016 Aston Martin V12 Vantage S": 565,
"2018 Aston Martin DBS Superleggera": 715,
"2013 Aston Martin V8 Vantage": 436,
"2011 Aston Martin One-77": 750,
"2004 Aston Martin Vanquish S": 520,
"2008 Aston Martin DB9": 470,
"2019 Aston Martin Valkyrie": 1130,
"2018 Range Rover Supercharged": 518,
"2018 Range Rover Velar R-Dynamic": 332,
"2018 Range Rover Sport SVR": 575,
"2016 Land Rover Defender 70th Edition": 399,
"1957 Land Rover Series 1": 55,
"2003 Infiniti G35": 280,
"2017 Infiniti Q60 Red Sport": 400,
"2015 Infiniti Q50 Eau Rouge": 560,
"2019 Infiniti Q50": 300,
"2019 Tesla Model S Ludicrous Performance": 762,
"2019 Tesla Model S Standard Range": 340,
"2019 Tesla Model 3 Performance": 450,
"2019 Tesla Model 3 Standard Range": 204,
"2019 Tesla Model X Ludicrous Performance": 613,
"2019 Tesla Model X Standard Range": 340,
"2019 Mini Cooper S": 189,
"2019 Mini John Cooper Works": 228,
"1969 Morris Mini Cooper S": 76,
"2020 Cadillac CT4-V": 325,
"2019 Cadillac CTS-V": 640,
"2019 Cadillac CTS 3.6L V6": 335,
"2019 Cadillac ATS-V Coupe": 464,
"2016 Cadillac ELR": 233,
"2020 Cadillac CT6 Platinum": 500,
"2020 Cadillac Escalade": 420,
"2020 Cadillac XT5": 310,
"2014 Cadillac CTS-V Sport Wagon": 556,
"2004 Cadillac Seville": 275,
"2011 Cadillac DTS": 292,
"1975 Cadillac Fleetwood Brougham": 190,
"1976 Cadillac Eldorado": 190,
"1959 Cadillac Eldorado Brougham": 345,
"Renault R35 Tank": 82,
"2019 Renault Clio Iconic TCe 100": 132,
"2019 Renault Clio RS Line TCe 130": 174,
"2019 Renault Clio E-TECH Launch Edition": 188,
"2018 Renault Clio RS Trophy": 220,
"2003 Renault Clio V6": 251,
"1993 Renault Clio Williams": 145,
"1993 Renault Clio": 95,
"1993 Renault Twingo": 55,
"2010 Renault Twingo RS 133 Cup": 133,
"2010 Renault Twingo RS": 133,
"2020 Renault Twingo": 65,
"2020 Renault Megane RS 300 Trophy": 296,
"2020 Renault Megane RS Trophy R": 300,
"2020 Renault Megane RS Line TCe 140": 187,
"2005 Renault Megane Sport 225 Cup": 225,
"LIGHNING MCQUEEN":9999999999999999999999999999999999999999,
"2018 Fortnite Shopping Cart GT-S": 69696969699696969696969,
"2019 Fortnite ATK GT-4R": 3045789034753478587578237587234857234895723485723489577897589347589023478589347582347582347890,
"1009 Thanos Car": 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555.5


}

Upgrade_path_hp = {
"Stock": 1,
"Race Stage 1": 1.1,
"Race Stage 2": 1.2,
"Race Stage 3": 1.3,
"Race Stage 4": 1.5,
"Race Stage 5": 2.0,
"Drag Stage 1": 1.2,
"Drag Stage 2": 1.3,
"Drag Stage 3": 1.4,
"Drag Stage 4": 2.0,
"Drag Stage 5": 2.5,
"Offroad Stage 1": 1.1,
"Offroad Stage 2": 1.2,
"Offroad Stage 3": 1.2,
"Offroad Stage 4": 1.2,
"Offroad Stage 5": 1.3,
}

Upgrade_path_handling = {
"Stock": 0,
"Race Stage 1": .05,
"Race Stage 2": 0.1,
"Race Stage 3": 0.15,
"Race Stage 4": 0.2,
"Race Stage 5": 0.35,
"Drag Stage 1": 0.025,
"Drag Stage 2": 0.05,
"Drag Stage 3": 0.075,
"Drag Stage 4": 0.1,
"Drag Stage 5": 0.175,
"Offroad Stage 1": 0,
"Offroad Stage 2": 0.025,
"Offroad Stage 3": 0.05,
"Offroad Stage 4": 0.1,
"Offroad Stage 5": 0.15,
}

Upgrade_path_price = {
"Stock":0,
"Race Stage 1": 0.3,
"Race Stage 2": 0.5,
"Race Stage 3" :0.7,
"Race Stage 4": 1,
"Race Stage 5": 1.8,
"Drag Stage 1": 0.2,
"Drag Stage 2": 0.4,
"Drag Stage 3": 0.8,
"Drag Stage 4": 1.2,
"Drag Stage 5": 2,
"Offroad Stage 1": 0.1,
"Offroad Stage 2": 0.3,
"Offroad Stage 3": 0.7,
"Offroad Stage 4": 1,
"Offroad Stage 5": 1.9
}

Upgrade_path_cool = {
"Stock": 0,
"Race Stage 1": 0.5,
"Race Stage 2": 0.75,
"Race Stage 3": 1,
"Race Stage 4": 1.5,
"Race Stage 5": 2,
"Drag Stage 1": 0.25,
"Drag Stage 2": 0.5,
"Drag Stage 3": 1,
"Drag Stage 4": 1.5,
"Drag Stage 5": 2,
"Offroad Stage 1": 0.5,
"Offroad Stage 2": 0.75,
"Offroad Stage 3": 1,
"Offroad Stage 4": 1.5,
"Offroad Stage 5": 2,
}

Upgrade_path_offroad = {
"Stock": 0,
"Race Stage 1": -0.5,
"Race Stage 2": -1,
"Race Stage 3": -2,
"Race Stage 4": -2.5,
"Race Stage 5": -3,
"Drag Stage 1": 0,
"Drag Stage 2": -0.5,
"Drag Stage 3": -1.5,
"Drag Stage 4": -1.5,
"Drag Stage 5": -2,
"Offroad Stage 1": 0.5,
"Offroad Stage 2": 1,
"Offroad Stage 3": 1.5,
"Offroad Stage 4": 2,
"Offroad Stage 5": 3,
}

Upgrade_path_comfort = {
"Stock": 0,
"Race Stage 1": -0.5,
"Race Stage 2": -1,
"Race Stage 3": -2,
"Race Stage 4": -2.5,
"Race Stage 5": -3,
"Drag Stage 1": 0,
"Drag Stage 2": -0.5,
"Drag Stage 3": -1.5,
"Drag Stage 4": -1.5,
"Drag Stage 5": -2,
"Offroad Stage 1": -0.5,
"Offroad Stage 2": -0.5,
"Offroad Stage 3": -0.5,
"Offroad Stage 4": -0.5,
"Offroad Stage 5": -0.5,
}

Upgrade_path_seats = {
"Stock": 0,
"Race Stage 1": 0,
"Race Stage 2": 0,
"Race Stage 3": -2,
"Race Stage 4": -2,
"Race Stage 5": -2,
"Drag Stage 1": 0,
"Drag Stage 2": -2,
"Drag Stage 3": -2,
"Drag Stage 4": -2,
"Drag Stage 5": -2,
"Offroad Stage 1": 0,
"Offroad Stage 2": 0,
"Offroad Stage 3": 0,
"Offroad Stage 4": -2,
"Offroad Stage 5": -2,
}

Upgrade_path_skill = {
"Race Stage 1": 3,
"Race Stage 2" : 5,
"Race Stage 3" : 7,
"Race Stage 4": 9,
"Race Stage 5": 10,
"Drag Stage 1" : 3,
"Drag Stage 2" : 6,
"Drag Stage 3" : 8,
"Drag Stage 4" : 9,
"Drag Stage 5": 10,
"Offroad Stage 1": 4,
"Offroad Stage 2": 5,
"Offroad Stage 3": 7,
"Offroad Stage 4": 9,
"Offroad Stage 5": 10,
}





Car_Handling = {
"2000 Honda Integra" : 0.95,
"2000 Honda Integra Type R" : 1,
"1999 Honda Civic Type R EK9" : 1.1,
"2003 Honda Civic Type R EP3" : 1.1,
"2003 Honda NSX R" : 1.1,
"2001 Honda S2000" : 1,
"2021 Honda Civic Type R FK8" : 1.3,
"1991 Honda Civic EG6 SiR": 1.1,
"1999 Honda Civic LX": 0.85,
"2006 Honda Civic Si": 0.9,
"2018 Honda Civic Sport": 0.9,
"2018 Honda Civic Si Coupe": 1,
"2006 Honda Accord 3.0 EX": 0.8,
"2010 Honda Accord EX-L V6": 0.8,
"2015 Honda Accord Sport": 0.8,
"2015 Honda Accord EX-L V6": 0.8,
"2018 Honda Accord Sport": 0.85,
"2021 Honda CR-V": 0.75,
"1999 Honda CR-V": 0.7,
"2005 Honda Pilot": 0.65,
"2010 Honda Crosstour": 0.65,
"2005 Honda Element": 0.7,
"2001 Honda Odyssey Absolute": 0.8,
"2021 Honda N-ONE RS": 1.0,
"2021 Honda StepWGN Spada": 0.75,
"1999 Honda StepWGN": 0.70,
"2016 Honda CR-Z": 0.9,
"2021 Honda HR-V": 0.8, 
"2005 Honda Stream": 0.75,
"2014 Honda Stream": 0.75,
"2021 Honda Clarity": 0.7,
"2000 Honda Insight": 0.85,
"2021 Honda Insight": 0.8,
"2000 Honda ACTY": 0.8,
"2021 Honda ACTY": 0.8,
"2021 Honda Fit": 0.85,
"2001 Honda Life Dunk": 0.9,
"1992 Honda Vigor": 0.75,
"1989 Honda Accord": 0.8,
"2003 Acura RSX Type S" : 1.0,
"2017 Acura NSX" : 1.2,
"2005 Acura TL Type S": 0.85,
"2007 Acura TL": 0.8,
"2018 Acura TLX 3.5": 0.85,
"2018 Acura MDX": 0.7,
"2018 Acura ILX": 0.85,
"2021 Acura TLX Type S": 0.9,
"1995 Acura Legend": 0.75,
"2014 Acura TSX Sport Wagon": 0.8,
"1990 Ford Mustang Foxbody" : 0.8,
"2010 Ford Mustang GT500" : 0.85,
"2015 Ford Mustang GT" : 0.8,
"1975 Ford Pinto": 0.5,
"1999 Ford Crown Victoria": 0.7,
"2017 Ford Focus Hatch": 0.85,
"2017 Ford Focus RS": 1,
"2017 Ford Fusion Titanium": 0.8,
"2017 Ford Fusion Sport": 0.8,
"2018 Ford F-150 Super Cab": 0.6,
"2018 Ford F-150 Raptor": 0.7,
"2016 Shelby Mustang GT350R" : 1,
"1992 Volkswagen Golf GTi MK2" : 0.9,
"2017 Volkswagen Golf GTi MK7" : 1,
"2015 Volkswagen Scirocco R" : 1,
"2018 Volkswagen Passat R-Line": .85,
"1969 Volkswagen Beetle": .7,
"1999 BMW M3" : 0.9,
"2003 BMW M3" : 0.95,
"2008 BMW M3" : 1,
"2017 BMW M3" : 0.9,
"2005 BMW M5" : 0.8,
"2018 BMW M5" : 0.85,
"2017 BMW M4" : 0.95,
"2017 BMW M6" : 0.85,
"2018 BMW i8" : 1,
"1959 BMW 507": 0.65,
"2018 BMW 530i": 0.8,
"2018 BMW X3": 0.75,
"2018 BMW 750i": 0.75,
"1974 BMW 2002 Turbo": 0.8,
"2011 BMW 1M": 1,
"2018 BMW 330i": 0.8,
"2020 BMW M235i xDrive Gran Coupe": 1,
"2007 Saturn Ion": 0.75,
"2001 Saturn SL2": 0.7,
"1998 Saturn SW2": 0.7,
"2017 Ferrari 488GTB" : 1.1,
"2017 Ferrari F12" : 0.9,
"2003 Ferrari 575M Maranello" : 0.85,
"1999 Ferrari 360" : 1,
"1995 Ferrari F355" : 0.9,
"1965 Ferrari 250 GTO" : 0.7,
"1968 Ferrari Dino" : 0.7,
"1970 Ferrari 365 GTB/4 Daytona" : 0.7,
"2008 Ferrari F430" : 0.95,
"2008 Ferrari California" : 0.95,
"2016 Ferrari LaFerrari" : 1.15,
"2010 Ferrari 458 Italia": 1,
"1993 Toyota MR2 GT-S" : 0.9,
"1986 Toyota Corolla Sprinter Trueno" : 1.2,
"1993 Toyota Supra Twin Turbo" : 1,
"1998 Toyota Chaser Tourer V" : 0.9,
"1997 Toyota Soarer" : 0.85,
"1998 Toyota Altezza RS200" : 0.9,
"1996 Toyota Cresta 2.5 Twin Turbo": 0.85,
"1984 Toyota Landcruiser 60 3F" : 0.5,
"2003 Toyota Tundra" : 0.55,
"2018 Toyota Land Cruiser Prado" : 0.55,
"2018 Toyota 4Runner TRD Pro" : 0.6,
"2018 Toyota Tundra TRD Pro" : 0.6,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 0.5,
"2017 Toyota Century": 0.7,
"2019 Toyota Corolla Hatch XSE": 0.95,
"2019 Toyota Corolla Hatch SE": 0.85,
"2019 Toyota Corolla Touring Sport": 0.85,
"2021 Toyota GR Supra": 1.1,
"2008 Toyota Sequoia V8": 0.6,
"2005 Toyota Camry LE V6": 0.8,
"1999 Toyota Corolla LE": 0.8,
"2002 Toyota Sienna 5D Symphony": 0.7,
"2010 Toyota Camry LE": 0.8, 
"2016 Toyota Avalon Limited": 0.8,
"2018 Toyota Camry XSE": 0.8,
"2018 Toyota Corolla XLE": 0.9,
"1969 Toyota 2000GT": 0.7,
"2001 Toyota Camry LE V6": 0.8,
"2006 Toyota Sienna Limited": 0.8,
"2017 Toyota Sienna SE": 0.85,
"2018 Toyota Sienta": 0.85,
"2018 Toyota Alphard": 0.75,
"2018 Toyota Crown Majesta": 0.75,
"2018 Toyota Tundra SR5 5.7L V8": 0.65,
"2018 Toyota Hiace": 0.65,
"1993 Toyota Hiace": 0.6, 
"1997 Toyota Celica GT-Four": 0.9,
"1998 Toyota GT-one TS020": 1.3,
"1993 Toyota Mark II Tourer V JZX90": 0.9,
"2018 Toyota GT86": 0.95,
"1997 Toyota Tercel": 0.8,
"1997 Toyota Celica GT": 0.9,
"2016 Toyota Land Cruiser": 0.6,
"2019 Toyota Tacoma SR5": 0.65,
"2019 Toyota Tacoma TRD Pro": 0.7,
"1993 Toyota Sera": 1,
"2020 Toyota Avalon Touring": 0.8,
"2020 Toyota Avalon Limited": 0.75,
"2020 Toyota Avalon Limited Hybrid": 0.75,
"2020 Toyota Avalon TRD": 0.85,
"2020 Toyota Camry LE": 0.75,
"2020 Toyota Camry SE Hybrid": 0.8,
"2011 Toyota Prius": 0.7,
"2020 Toyota Prius XLE AWD": 0.75,
"2021 Toyota GR Yaris": 1.1,
"2022 Toyota GR86 Base": 1.0,
"2022 Toyota GR86 Premium": 1.05,
"2018 Toyota Camry SE": 0.8,
"2009 Lexus LFA" : 1,
"2007 Lexus ISF" : 0.85,
"1998 Lexus GS300" : 0.8,
"2018 Lexus LC500" : 0.85,
"2018 Lexus LS500 AWD" : 0.7,
"2019 Lexus ES300h": 0.8,
"2018 Lexus GS F": 0.95,
"2003 Lexus LS430": 0.65,
"2019 Lexus RX350": 0.65,
"1999 Lexus RX300 4WD": 0.65,
"2019 Lexus LX570": 0.6,
"2022 Lexus IS500 F Sport Performance": 0.9,
"2022 Lexus IS350 F Sport": 0.9,
"1990 Nissan Skyline GTR R32" : 0.95,
"1994 Nissan Skyline GTR R33 Spec-V" : 0.9,
"1999 Nissan Skyline GTR R34": 1,
"2002 Nissan Skyline GTR V-Spec II Nur" : 1.1,
"1996 Nissan 180SX" : 1,
"1993 Nissan Silvia K's Type S S14" : 0.95,
"2018 Nissan GTR Track Edition R35" : 1.1,
"2007 Nissan Fairlady Z" : 0.9,
"2018 Nissan Fairlady Z NISMO" : 1,
"2018 Nissan Fairlady Z" : 0.9,
"1989 Nissan 300ZX Turbo Z" : 0.85,
"2018 Nissan GT-R50 by Italdesign": 1.1,
"2018 Nissan GT-R NISMO": 1.2,
"2018 Nissan Maxima Platinum": 0.8,
"2018 Nissan Sentra SR Turbo": 0.85,
"2017 Nissan Leaf": 0.75,
"1973 Nissan Skyline H/T 2000GT-R": 0.65,
"1987 Nissan Skyline GTSR R31": 0.9,
"1989 Nissan Skyline GTS-4 R32": 0.8,
"1998 Nissan Skyline 25GT-X Turbo R34": 0.85,
"1965 Nissan Silvia 1600 Coupe": 0.6,
"1990 Nissan Silvia S13": 0.9,
"1999 Nissan Silvia Spec-R S15": 1,
"1995 Nissan GT-R Skyline R33 LM": 1.25,
"1998 Nissan R390 GT1": 1.3,
"1992 Nissan Cefiro 2.0 Turbo": 0.8,
"1990 Nissan Laurel Turbo Medalist": 0.75,
"2017 Nissan Armada Platinum": 0.55,
"1994 Nissan Hardbody": 0.6,
"2018 Nissan Titan Platinum Reserve": 0.55,
"2003 Nissan Skyline GT-R R34 Z-Tune": 1.05,
"2015 Nissan Juke": 0.75,
"2021 Nissan Altima 2.0 SR": 0.8,
"2021 Nissan Altima 2.5 Platinum": 0.8,
"2022 Nissan GT-R T-Spec": 1.1,
"2015 Lamborghini Veneno": 1,
"2003 Lamborghini Gallardo" : 0.9,
"2007 Lamborghini Gallardo SL" : 1.05,
"2008 Lamborghini Gallardo LP560-4" : 1.0,
"2010 Lamborgini Gallardo LP570-4 SL ": 1.1,
"2013 Lamborghini Gallardo LP570-4 SC" : 1.1,
"2014 Lamborghini Huracan LP610-4" : 1.1,
"2017 Lamborghini Huracan Performante" : 1.2,
"2001 Lamborghini Murcielago" :0.85,
"2006 Lamborghini Murcielago LP640" : 0.9,
"2009 Lamborghini Murcielago LP670-4 SV" :1,
"2015 Lamborghini Aventador SV" : 1.1,
"2016 Lamborghini Aventador S" : 1,
"1971 Lamborghini Miura P400SV" : 0.7,
"1996 Lamborghini Diablo SV" : 0.8,
"1985 Lamborghini Countach LP5000s QV" : 0.75,
"2020 Lamborghini Sian": 1.1, 
"2021 Lamborghini Urus": 0.9,
"2021 Lamborghini Huracan Evo": 1.1,  
"1995 Lamborghini Diablo SE30 Jota": 0.8, 
"2000 Lamborghini Diablo GTR": 1.0, 
"2017 Bentley Continental GT" : 0.8,
"2015 Bentley Bentayga" : 0.75,
"2015 Koenigsegg Regera" : 0.9,
"2010 Koenigsegg Agera" : 0.9,
"2007 Koenigsegg CCX" : 0.9,
"2005 Bugatti Veyron 16.4" : 0.85,
"2016 Bugatti Chiron" : 0.9,
"2017 Porsche 911 GT2 RS" : 1.2,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" :0.9,
"2016 Porsche 911 Turbo" : 1,
"2016 Porsche 718 Boxster" : 1.05,
"2017 Porsche 718 Cayman GTS" : 1.1,
"1975 Porsche 911 Turbo" : 0.8,
"1995 Porsche 911 GT2" : 0.9,
"1987 Porsche 959" : 0.85,
"1999 Porsche 911 GT3" : 0.9,
"1980 Porsche 924 Turbo": 0.8,
"2015 Lotus Evora 400" : 1,
"2011 Lotus Exige S" : 1.1,
"1996 Lotus Esprit V8" : 0.8,
"2006 Lotus Elise S" : 1.2,
"2018 Mazda Miata MX-5 Club": 1.1,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 1.2,
"1989 Mazda MX-5 Miata" : 1.1,
"1989 Mazda RX-7 Savanna Turbo" : 0.9,
"1992 Mazda RX-7" : 1,
"1998 Mazda RX-7 RZ" : 1.1,
"2009 Mazda RX-8" : 0.95,
"2019 Mazda6 Signature": 0.85,
"2019 Mazda3 Hatch": 0.9,
"2019 Mazda CX-5": 0.8,
"2019 Mazda CX-3": 0.8,
"2014 Mazda2": 0.85,
"2015 Mazda5": 0.8,
"2006 Mazdaspeed 6 GT": 0.9,
"2013 Mazdaspeed 3": 0.95,
"2001 Mazda RX-7 Spirit R Type A" : 1.1,
"2018 Morgan Three-Wheeler" : 0.65,
"1998 Subaru Impreza 22B STi": 0.95,
"1995 Subaru Impreza WRX STi Version II": 0.9,
"2002 Subaru Impreza WRX STi": 0.9,
"2003 Subaru Impreza WRX STi": 0.95,
"2005 Subaru Impreza WRX STi": 0.95,
"2010 Subaru Impreza WRX STi R205": 1.05,
"2019 Subaru WRX STi": 1,
"1993 Subaru SVX": 0.85,
"2000 Subaru Forester STI": 0.85,
"2019 Subaru WRX": 0.95,
"2022 Subaru WRX": 0.95,
"2018 Subaru BRZ": 0.9,
"2022 Subaru BRZ Premium": 0.95,
"2022 Subaru BRZ Limited": 1.0,
"1988 Isuzu Impulse": 0.8,
"1979 Isuzu 117 Coupe": 0.7,
"1994 Mitsubishi Lancer Evo II": 0.9,
"2010 Mitsubishi Lancer Evo X GSR": 0.95,
"1999 Mitsubishi Lancer Evo VI GSR": 1,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 1.05,
"2003 Mitsubishi Lancer Evo VIII GSR": 1,
"1994 Mitsubishi 3000 GT VR-4": 0.9,
"1994 Mitsubishi FTO GPX": 0.85,
"1992 Mitsubishi Galant VR-4": 0.85,
"1974 VAZ Lada 1200":0.5,
"1975 UAZ-469":0.5,
"1965 GAZ Volga 21":0.4,
"1995 Hyundai Sonata 2.0i": 0.7,
"2013 Hyundai Genesis Coupe 3.8" : 0.85,
"2013 Hyundai Elantra GT": 0.8,
"2017 Hyundai Sonata Limited": 0.8,
"2018 Kia Stinger GT": 0.85,
"2017 Kia Optima SX 2.0T": 0.8,
"2005 Hyundai Tiburon GT V6": 0.8,
"2006 Audi R8":0.95,
"2008 Audi R8 V10":0.95,
"2010 Audi R8 GT": 1.1,
"2012 Audi R8 Plus": 1,
"2015 Audi R8 Coupe 5.2 FSI quattro": 1, 
"1994 Audi RS2 Avant": 0.9,
"2018 Audi RS5": 0.9,
"2018 Audi RS3": 0.9,
"2018 Audi RS7": 0.85,
"2018 Audi RS6 Avant": 0.9,
"2018 Audi TTRS": 1,
"2018 Mercedes-AMG E63 S 4Matic": 0.85,
"2018 Mercedes-Maybach S560": 0.6,
"2018 Mercedes-AMG S65 Sedan": 0.7,
"1990 Mercedes-Benz 190E Evolution II": 0.85,
"2016 Mercedes-AMG GT S": 1,
"2013 Mercedes-Benz SLS AMG GT": 0.9,
"2012 Mercedes-Benz C63 AMG Black Series": 0.9,
"2000 Mercedes-Benz C32 AMG": 0.85,
"2020 Mercedes-AMG A35 4Matic": 1,
"2020 Chevy Corvette C8 Stingray Z51": 1.1,
"2019 Chevy Corvette C7 ZR1": 1.1,
"2018 Chevy Corvette C7 ZO6": 1.05,
"2018 Chevy Corvette C7 Stingray": 1,
"1953 Chevy Corvette": 0.6,
"1960 Chevy Corvette C1": 0.6,
"1963 Chevy Corvette C2 Stingray 427": 0.7,
"1967 Chevy Corvette C3 327": 0.7,
"1970 Chevy Corvette C3 454": 0.7,
"1984 Chevy Corvette C4": 0.75,
"1988 Chevy Corvette C4 ZR1": 0.8,
"2001 Chevy Corvette C5": 0.8,
"2002 Chevy Corvette C5 Z06": 0.85,
"2007 Chevy Corvette C6": 0.85,
"2007 Chevy Corvette C6 Z06": 0.9,
"2007 Chevy Corvette C6 ZR1": 1,
"2018 Chevy Camaro 1LE": 1,
"2018 Chevy Camaro ZL1": 1.1,
"1969 Chevy Camaro SS 396": 0.6,
"2017 Chevy Malibu 1.5 Turbo": 0.8,
"2016 Chevy Malibu 2LT": 0.8,
"2017 Chevy Cruze Hatch Premier": 0.8,
"2016 Chevy Impala LT": 0.75,
"2018 Alfa Romeo 4C": 1.1,
"2018 Alfa Romeo Giulia Quadrifoglio": 1,
"2018 Alfa Romeo Stelvio Quadrifoglio": 0.9,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 0.95,
"2013 Alfa Romeo MiTo 1.4 8v": 0.8,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 0.8,
"2006 Alfa Romeo 8c Competizione": 0.8,
"1992 Alfa Romeo 155 Q4": 0.8,
"1985 Alfa Romeo Spider Veloce": 0.75,
"2017 Suzuki Swift Sport": 0.85,
"2016 Suzuki Alto Works": 0.9,
"2016 Suzuki Hustler G 4WD": 0.85,
"2003 Suzuki Liana 1.6 Sedan": 0.8,
"1995 Suzuki Samurai 1.3i": 0.8,
"2002 Suzuki Grand Vitara": 0.75,
"2018 Pagani Huayra BC": 1.2,
"2013 Pagani Huayra": 1.1,
"2010 Pagani Zonda Cinque": 1.2,
"2005 Pagani Zonda F": 1,
"1999 Pagani Zonda C12S": 0.95,
"1970 AMC AMX": 0.65,
"1972 AMC Javelin": 0.6,
"1969 AMC Ambassador": 0.55,
"1970 AMC Rebel The Machine": 0.7,
"1975 AMC Pacer X": 0.75,
"2018 Dodge Challenger SRT Hellcat Widebody": 0.85,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 0.8,
"2018 Dodge Challenger SRT Demon": 0.75,
"2008 Dodge Challenger SE": 0.8,
"2008 Dodge Challenger SRT8": 0.8,
"2018 Dodge Charger Hellcat": 0.85,
"2018 Dodge Charger GT Plus": 0.8,
"2011 Dodge Charger SRT8": 0.8,
"2005 Dodge Charger SRT8": 0.75,
"2017 Dodge Viper ACR": 1.1,
"2017 Dodge Viper GTS": 0.95,
"2012 Dodge Dart R/T": 0.85,
"2010 Dodge Avenger Express": 0.8,
"2008 Dodge Journey SXT": 0.6,
"2007 Dodge Nitro 4.0 R/T": 0.65,
"2007 Dodge Viper SRT-10": 0.9,
"2007 Dodge Viper SRT10 ACR": 1,
"2000 Dodge Intrepid R/T": 0.75,
"2003 Dodge Neon SRT-4": 0.85,
"1970 Dodge Dart Hemi Super Stock": 0.7,
"1970 Dodge Dart Swinger 340": 0.7,
"1970 Dodge Challenger R/T 426 Hemi": 0.7,
"1969 Dodge Charger Daytona Hemi": 0.65,
"1969 Dodge Charger R/T Hemi": 0.6,
"2018 Mclaren Senna": 1.25,
"2018 McLaren 720S": 1,
"2015 McLaren 570S": 1,
"2013 McLaren MP4-12C": 1,
"1992 McLaren F1": 0.9,
"1997 McLaren F1 GT": 0.95,
"1995 McLaren F1 LM": 1,
"2013 McLaren P1": 1.1,
"1974 MG Midget": 0.7,
"1928 MG M-Type Midget": 0.4,
"2007 Aston Martin DBS": 0.95,
"2016 Aston Martin DB11": 0.9,
"2016 Aston Martin V12 Vantage S": 0.95,
"2018 Aston Martin DBS Superleggera": 1,
"2013 Aston Martin V8 Vantage": 0.9,
"2011 Aston Martin One-77": 0.9,
"2004 Aston Martin Vanquish S": 0.85,
"2008 Aston Martin DB9": 0.85,
"2019 Aston Martin Valkyrie": 1.3,
"2018 Range Rover Supercharged": 0.7,
"2018 Range Rover Velar R-Dynamic": 0.75,
"2018 Range Rover Sport SVR": 0.8,
"2016 Land Rover Defender 70th Edition": 0.65,
"1957 Land Rover Series 1": 0.5,
"2003 Infiniti G35": 0.9,
"2017 Infiniti Q60 Red Sport": 0.9,
"2015 Infiniti Q50 Eau Rouge": 1,
"2019 Infiniti Q50": 0.8,
"2019 Tesla Model S Ludicrous Performance": 0.8,
"2019 Tesla Model S Standard Range": 0.8,
"2019 Tesla Model 3 Performance": 0.85,
"2019 Tesla Model 3 Standard Range": 0.85,
"2019 Tesla Model X Ludicrous Performance": 0.75,
"2019 Tesla Model X Standard Range": 0.75,
"2019 Mini Cooper S": 1,
"2019 Mini John Cooper Works": 1.05,
"1969 Morris Mini Cooper S": 0.9,
"2020 Cadillac CT4-V": 0.9,
"2019 Cadillac CTS-V": 0.85,
"2019 Cadillac CTS 3.6L V6": 0.8,
"2019 Cadillac ATS-V Coupe": 0.9,
"2016 Cadillac ELR": 0.85,
"2020 Cadillac CT6 Platinum": 0.75,
"2020 Cadillac Escalade": 0.6,
"2020 Cadillac XT5": 0.7,
"2014 Cadillac CTS-V Sport Wagon": 0.8,
"2004 Cadillac Seville": 0.75,
"2011 Cadillac DTS": 0.75,
"1975 Cadillac Fleetwood Brougham": 0.45,
"1976 Cadillac Eldorado": 0.45,
"1959 Cadillac Eldorado Brougham": 0.5,
"Renault R35 Tank": 0.4,
"2019 Renault Clio Iconic TCe 100": 0.9,
"2019 Renault Clio RS Line TCe 130": 0.9,
"2019 Renault Clio E-TECH Launch Edition": 0.85,
"2018 Renault Clio RS Trophy": 1.1,
"2003 Renault Clio V6": 0.85,
"1993 Renault Clio Williams": 0.9,
"1993 Renault Clio": 0.85,
"1993 Renault Twingo": 0.9,
"2010 Renault Twingo RS 133 Cup": 1.15,
"2010 Renault Twingo RS": 1.1,
"2020 Renault Twingo": 1,
"2020 Renault Megane RS 300 Trophy": 1.1,
"2020 Renault Megane RS Trophy R": 1.3,
"2020 Renault Megane RS Line TCe 140": 0.85,
"2005 Renault Megane Sport 225 Cup": 1,
"LIGHNING MCQUEEN":9999999999999999999999999999999999999999,
"2018 Fortnite Shopping Cart GT-S": 69696969699696969696969,
"2019 Fortnite ATK GT-4R": 3045789034753478587578237587234857234895723485723489577897589347589023478589347582347582347890,
"1009 Thanos Car": 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555.5

}

Car_Price = {
"2000 Honda Integra" : 4500,
"2000 Honda Integra Type R" : 15000,
"1999 Honda Civic Type R EK9" : 15000,
"2003 Honda Civic Type R EP3" : 12000,
"2003 Honda NSX R" : 85000,
"2001 Honda S2000" : 8000,
"2021 Honda Civic Type R FK8" : 35000,
"1991 Honda Civic EG6 SiR": 13000,
"1999 Honda Civic LX": 3000,
"2006 Honda Civic Si": 7500,
"2018 Honda Civic Sport": 22000,
"2018 Honda Civic Si Coupe": 25000,
"2006 Honda Accord 3.0 EX": 8000,
"2010 Honda Accord EX-L V6": 11000,
"2015 Honda Accord Sport": 15000,
"2015 Honda Accord EX-L V6": 18000,
"2018 Honda Accord Sport": 27000,
"2021 Honda CR-V": 30000,
"1999 Honda CR-V": 4500,
"2005 Honda Pilot": 6000,
"2010 Honda Crosstour": 11000,
"2005 Honda Element": 5500,
"2001 Honda Odyssey Absolute": 6000,
"2021 Honda N-ONE RS": 18000,
"2021 Honda StepWGN Spada": 34000,
"1999 Honda StepWGN": 2000,
"2016 Honda CR-Z": 13000,
"2021 Honda HR-V": 25000, 
"2005 Honda Stream": 3000,
"2014 Honda Stream": 13000,
"2021 Honda Clarity": 33400,
"2000 Honda Insight": 5000,
"2021 Honda Insight": 28000,
"2000 Honda ACTY": 2000,
"2021 Honda ACTY": 15000,
"2021 Honda Fit": 20000,
"2001 Honda Life Dunk": 4000,
"1992 Honda Vigor": 6500,
"1989 Honda Accord": 2000,
"2003 Acura RSX Type S" : 9000,
"2017 Acura NSX" : 140000,
"2005 Acura TL Type S": 7500,
"2007 Acura TL": 6500,
"2018 Acura TLX 3.5": 38000,
"2018 Acura MDX": 45000,
"2018 Acura ILX": 30000,
"2021 Acura TLX Type S": 55000,
"1995 Acura Legend": 6000,
"2014 Acura TSX Sport Wagon": 18000,
"1990 Ford Mustang Foxbody" : 5000,
"2010 Ford Mustang GT500" : 30000,
"2015 Ford Mustang GT" : 35000,
"1975 Ford Pinto": 2000,
"1999 Ford Crown Victoria": 1000,
"2017 Ford Focus Hatch": 17000,
"2017 Ford Focus RS": 37000,
"2017 Ford Fusion Titanium": 32000,
"2017 Ford Fusion Sport": 34000,
"2018 Ford F-150 Super Cab": 33000,
"2018 Ford F-150 Raptor": 55000,
"2016 Shelby Mustang GT350R" : 50000,
"1992 Volkswagen Golf GTi MK2" : 4000,
"2017 Volkswagen Golf GTi MK7" : 30000,
"2015 Volkswagen Scirocco R" : 30000,
"2018 Volkswagen Passat R-Line": 26000,
"1969 Volkswagen Beetle": 10000,
"1999 BMW M3" : 17000,
"2003 BMW M3" : 14000,
"2008 BMW M3" : 32000,
"2017 BMW M3" : 65000,
"2005 BMW M5" : 20000,
"2018 BMW M5" : 80000,
"2017 BMW M4" : 70000,
"2017 BMW M6" : 90000,
"2018 BMW i8" : 135000,
"1959 BMW 507": 1000000,
"2018 BMW 530i": 53400,
"2018 BMW X3": 41000,
"2018 BMW 750i": 100000,
"1974 BMW 2002 Turbo": 145600,
"2011 BMW 1M": 65000,
"2018 BMW 330i": 40000,
"2020 BMW M235i xDrive Gran Coupe": 50000,
"2007 Saturn Ion": 1500,
"2001 Saturn SL2": 500,
"1998 Saturn SW2": 500,
"2017 Ferrari 488GTB" : 300000,
"2017 Ferrari F12" : 400000,
"2003 Ferrari 575M Maranello" : 70000,
"1999 Ferrari 360" : 50000,
"1995 Ferrari F355" : 45000,
"1965 Ferrari 250 GTO" : 20000000,
"1968 Ferrari Dino" : 400000,
"1970 Ferrari 365 GTB/4 Daytona" : 600000,
"2008 Ferrari F430" : 90000,
"2008 Ferrari California" : 80000,
"2016 Ferrari LaFerrari" : 1700000,
"2010 Ferrari 458 Italia": 160000,
"1993 Toyota MR2 GT-S" : 15000,
"1986 Toyota Corolla Sprinter Trueno" : 18000,
"1993 Toyota Supra Twin Turbo" : 80000,
"1998 Toyota Chaser Tourer V" : 20000,
"1997 Toyota Soarer" : 10000,
"1996 Toyota Cresta 2.5 Twin Turbo": 16000,
"1998 Toyota Altezza RS200" : 12000,
"1984 Toyota Landcruiser 60 3F" : 17000,
"2003 Toyota Tundra" : 10000,
"2018 Toyota Land Cruiser Prado" : 55000,
"2018 Toyota 4Runner TRD Pro" : 45000,
"2018 Toyota Tundra TRD Pro" : 50000,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 10000,
"2017 Toyota Century": 180000,
"2019 Toyota Corolla Hatch XSE": 24000,
"2019 Toyota Corolla Hatch SE": 21000,
"2019 Toyota Corolla Touring Sport": 26000,
"2021 Toyota GR Supra": 55000,
"2008 Toyota Sequoia V8": 15000,
"2005 Toyota Camry LE V6": 4995,
"1999 Toyota Corolla LE": 2995,
"2002 Toyota Sienna 5D Symphony": 5995,
"2010 Toyota Camry LE": 6995, 
"2016 Toyota Avalon Limited": 35000,
"2018 Toyota Camry XSE": 32000,
"2018 Toyota Corolla XLE": 27000,
"1969 Toyota 2000GT": 1000000,
"2001 Toyota Camry LE V6": 4500,
"2006 Toyota Sienna Limited": 10000,
"2017 Toyota Sienna SE": 37000,
"2018 Toyota Sienta": 25000,
"2018 Toyota Alphard": 45000,
"2018 Toyota Crown Majesta": 45000,
"2018 Toyota Tundra SR5 5.7L V8": 46000,
"2018 Toyota Hiace": 25000,
"1993 Toyota Hiace": 6995, 
"1997 Toyota Celica GT-Four": 65000,
"1998 Toyota GT-one TS020": 1000000,
"1993 Toyota Mark II Tourer V JZX90": 15000,
"2018 Toyota GT86": 28000,
"1997 Toyota Tercel": 750,
"1997 Toyota Celica GT": 3000,
"2016 Toyota Land Cruiser": 75000,
"2019 Toyota Tacoma SR5": 32000,
"2019 Toyota Tacoma TRD Pro": 45000,
"1993 Toyota Sera": 15000,
"2020 Toyota Avalon Touring": 45000,
"2020 Toyota Avalon Limited": 44000,
"2020 Toyota Avalon Limited Hybrid": 46000,
"2020 Toyota Avalon TRD": 44000,
"2020 Toyota Camry LE": 25000,
"2020 Toyota Camry SE Hybrid": 30000,
"2011 Toyota Prius": 7000,
"2020 Toyota Prius XLE AWD": 30000,
"2021 Toyota GR Yaris": 35000,
"2022 Toyota GR86 Base": 27000,
"2022 Toyota GR86 Premium": 30000,
"2018 Toyota Camry SE": 25000,
"2009 Lexus LFA" : 400000,
"2007 Lexus ISF" : 32000,
"1998 Lexus GS300" : 7000,
"2018 Lexus LC500" : 100000,
"2018 Lexus LS500 AWD" : 120000,
"2019 Lexus ES300h": 43000,
"2018 Lexus GS F": 86000,
"2003 Lexus LS430": 15000,
"2019 Lexus RX350": 44000,
"1999 Lexus RX300 4WD": 15000,
"2019 Lexus LX570": 86000,
"2022 Lexus IS500 F Sport Performance": 60000,
"2022 Lexus IS350 F Sport": 45000,
"1990 Nissan Skyline GTR R32" : 40000,
"1994 Nissan Skyline GTR R33 Spec-V" : 70000,
"1999 Nissan Skyline GTR R34": 150000,
"2002 Nissan Skyline GTR V-Spec II Nur" : 300000,
"1996 Nissan 180SX" : 15000,
"1993 Nissan Silvia K's Type S S14" : 15000,
"2018 Nissan GTR Track Edition R35" : 120000,
"2007 Nissan Fairlady Z" : 8000,
"2018 Nissan Fairlady Z NISMO" : 35000,
"2018 Nissan Fairlady Z" : 30000,
"1989 Nissan 300ZX Turbo Z" : 6500,
"2018 Nissan GT-R50 by Italdesign": 1000000,
"2018 Nissan GT-R NISMO": 140000,
"2018 Nissan Maxima Platinum": 40000,
"2018 Nissan Sentra SR Turbo": 25000,
"2017 Nissan Leaf": 31000,
"1973 Nissan Skyline H/T 2000GT-R": 180000,
"1987 Nissan Skyline GTSR R31": 25000,
"1989 Nissan Skyline GTS-4 R32": 10000,
"1998 Nissan Skyline 25GT-X Turbo R34": 13000,
"1965 Nissan Silvia 1600 Coupe": 50000,
"1990 Nissan Silvia S13": 13000,
"1999 Nissan Silvia Spec-R S15": 20000,
"1995 Nissan GT-R Skyline R33 LM": 1000000,
"1998 Nissan R390 GT1": 1000000,
"1992 Nissan Cefiro 2.0 Turbo": 12000,
"1990 Nissan Laurel Turbo Medalist": 13000,
"2017 Nissan Armada Platinum": 40000,
"1994 Nissan Hardbody": 4000,
"2018 Nissan Titan Platinum Reserve": 54000,
"2003 Nissan Skyline GT-R R34 Z-Tune":500000,
"2015 Nissan Juke": 15000,
"2021 Nissan Altima 2.0 SR": 30000,
"2021 Nissan Altima 2.5 Platinum": 32000,
"2022 Nissan GT-R T-Spec": 140000,
"2015 Lamborghini Veneno": 4500000,
"2003 Lamborghini Gallardo" : 85000,
"2007 Lamborghini Gallardo SL" : 145000,
"2008 Lamborghini Gallardo LP560-4" : 130000,
"2010 Lamborgini Gallardo LP570-4 SL ": 210000,
"2013 Lamborghini Gallardo LP570-4 SC" : 220000,
"2014 Lamborghini Huracan LP610-4" : 190000,
"2017 Lamborghini Huracan Performante" : 250000,
"2001 Lamborghini Murcielago" :150000,
"2006 Lamborghini Murcielago LP640" : 190000,
"2009 Lamborghini Murcielago LP670-4 SV" :350000,
"2015 Lamborghini Aventador SV" : 400000,
"2016 Lamborghini Aventador S" : 350000,
"1971 Lamborghini Miura P400SV" : 1000000,
"1996 Lamborghini Diablo SV" : 210000,
"1985 Lamborghini Countach LP5000s QV" : 250000,
"2020 Lamborghini Sian": 2640000, 
"2021 Lamborghini Urus": 240000,
"2021 Lamborghini Huracan Evo": 330000,  
"1995 Lamborghini Diablo SE30 Jota": 730000, 
"2000 Lamborghini Diablo GTR": 1100000, 
"2017 Bentley Continental GT" : 320000,
"2015 Bentley Bentayga" : 400000,
"2015 Koenigsegg Regera" : 1100000,
"2010 Koenigsegg Agera" : 900000,
"2007 Koenigsegg CCX" : 700000,
"2005 Bugatti Veyron 16.4" : 800000,
"2016 Bugatti Chiron" : 3000000,
"2017 Porsche 911 GT2 RS" : 300000,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" :80000,
"2016 Porsche 911 Turbo" : 140000,
"2016 Porsche 718 Boxster" : 45000,
"2017 Porsche 718 Cayman GTS" : 60000,
"1975 Porsche 911 Turbo" : 120000,
"1995 Porsche 911 GT2" : 900000,
"1987 Porsche 959" : 800000,
"1999 Porsche 911 GT3" : 65000,
"1980 Porsche 924 Turbo": 18000,
"2015 Lotus Evora 400" : 70000,
"2011 Lotus Exige S" : 60000,
"1996 Lotus Esprit V8" : 50000,
"2006 Lotus Elise S" : 20000,
"2018 Mazda Miata MX-5 Club" : 27000,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 14000,
"1989 Mazda MX-5 Miata" : 10000,
"1989 Mazda RX-7 Savanna Turbo" : 18000,
"1992 Mazda RX-7" : 30000,
"1998 Mazda RX-7 RZ" : 40000,
"2009 Mazda RX-8" : 15000,
"2019 Mazda6 Signature": 36000,
"2019 Mazda3 Hatch": 24000,
"2019 Mazda CX-5": 31000,
"2019 Mazda CX-3": 23000,
"2014 Mazda2": 7000,
"2015 Mazda5": 10000,
"2006 Mazdaspeed 6 GT": 10000,
"2013 Mazdaspeed 3": 17000,
"2001 Mazda RX-7 Spirit R Type A" : 85000,
"2018 Morgan Three-Wheeler" : 45000,
"1998 Subaru Impreza 22B STi": 65000,
"1995 Subaru Impreza WRX STi Version II": 10000,
"2002 Subaru Impreza WRX STi": 12000,
"2003 Subaru Impreza WRX STi": 27000,
"2005 Subaru Impreza WRX STi": 30000,
"2010 Subaru Impreza WRX STi R205": 40000,
"2019 Subaru WRX STi": 40000,
"1993 Subaru SVX": 10000,
"2000 Subaru Forester STI": 15000,
"2019 Subaru WRX": 26000,
"2022 Subaru WRX": 30000,
"2018 Subaru BRZ": 25000,
"2022 Subaru BRZ Premium": 27000,
"2022 Subaru BRZ Limited": 30000,
"1988 Isuzu Impulse": 4000,
"1979 Isuzu 117 Coupe": 15000,
"1994 Mitsubishi Lancer Evo II": 15000,
"2010 Mitsubishi Lancer Evo X GSR":30000,
"1999 Mitsubishi Lancer Evo VI GSR":16000,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 60000,
"2003 Mitsubishi Lancer Evo VIII GSR":24000,
"1994 Mitsubishi 3000 GT VR-4": 18000,
"1992 Mitsubishi Galant VR-4": 15000,
"1994 Mitsubishi FTO GPX": 12000,
"1974 VAZ Lada 1200":699,
"1975 UAZ-469":999,
"1965 GAZ Volga 21":1999,
"1995 Hyundai Sonata 2.0i": 3000,
"2013 Hyundai Genesis Coupe 3.8" : 15000,
"2013 Hyundai Elantra GT": 7000,
"2017 Hyundai Sonata Limited": 32000,
"2005 Hyundai Tiburon GT V6": 5000,
"2018 Kia Stinger GT": 40000,
"2017 Kia Optima SX 2.0T": 30000,
"2006 Audi R8":80000,
"2008 Audi R8 V10":110000,
"2010 Audi R8 GT": 155000,
"2012 Audi R8 Plus": 100000,
"1994 Audi RS2 Avant": 60000,
"2018 Audi RS5": 80000,
"2018 Audi RS3": 60000,
"2018 Audi RS7": 120000,
"2018 Audi RS6 Avant": 85000,
"2018 Audi TTRS": 68000,
"2015 Audi R8 Coupe 5.2 FSI quattro": 150000, 
"2018 Mercedes-AMG E63 S 4Matic": 115000,
"2018 Mercedes-Maybach S560": 200000,
"2018 Mercedes-AMG S65 Sedan": 240000,
"1990 Mercedes-Benz 190E Evolution II": 145000,
"2016 Mercedes-AMG GT S": 155000,
"2013 Mercedes-Benz SLS AMG GT": 200000,
"2012 Mercedes-Benz C63 AMG Black Series": 125000,
"2000 Mercedes-Benz C32 AMG": 25000,
"2020 Mercedes-AMG A35 4Matic": 49000,
"2020 Chevy Corvette C8 Stingray Z51": 75000,
"2019 Chevy Corvette C7 ZR1": 110000,
"2018 Chevy Corvette C7 ZO6": 80000,
"2018 Chevy Corvette C7 Stingray": 50000,
"1953 Chevy Corvette": 660000,
"1960 Chevy Corvette C1": 75000,
"1963 Chevy Corvette C2 Stingray 427": 110000,
"1967 Chevy Corvette C3 327": 45000,
"1970 Chevy Corvette C3 454": 55000,
"1984 Chevy Corvette C4": 8000,
"1988 Chevy Corvette C4 ZR1": 37000,
"2001 Chevy Corvette C5": 15000,
"2002 Chevy Corvette C5 Z06": 20000,
"2007 Chevy Corvette C6": 25000,
"2007 Chevy Corvette C6 Z06": 40000,
"2007 Chevy Corvette C6 ZR1": 70000,
"2018 Chevy Camaro 1LE": 44400,
"2018 Chevy Camaro ZL1": 65000,
"1969 Chevy Camaro SS 396": 40000,
"2017 Chevy Malibu 1.5 Turbo": 25000,
"2016 Chevy Malibu 2LT": 25000,
"2017 Chevy Cruze Hatch Premier": 17000,
"2016 Chevy Impala LT": 24000,
"2018 Alfa Romeo 4C": 56000,
"2018 Alfa Romeo Giulia Quadrifoglio": 75000,
"2018 Alfa Romeo Stelvio Quadrifoglio": 80000,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 16000,
"2013 Alfa Romeo MiTo 1.4 8v": 7000,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 10000,
"2006 Alfa Romeo 8c Competizione": 60000,
"1992 Alfa Romeo 155 Q4": 25000,
"1985 Alfa Romeo Spider Veloce": 6000,
"2017 Suzuki Swift Sport": 28000,
"2016 Suzuki Alto Works": 12000,
"2016 Suzuki Hustler G 4WD": 10000,
"2003 Suzuki Liana 1.6 Sedan": 3000,
"1995 Suzuki Samurai 1.3i": 1500,
"2002 Suzuki Grand Vitara": 3500,
"2018 Pagani Huayra BC": 2500000,
"2013 Pagani Huayra": 1400000,
"2010 Pagani Zonda Cinque": 1800000,
"2005 Pagani Zonda F": 1400000,
"1999 Pagani Zonda C12S": 500000,
"1970 AMC AMX": 30000,
"1972 AMC Javelin": 25000,
"1969 AMC Ambassador": 12000,
"1970 AMC Rebel The Machine": 60000,
"1975 AMC Pacer X": 15000,
"2018 Dodge Challenger SRT Hellcat Widebody": 75000,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 48000,
"2018 Dodge Challenger SRT Demon": 125000,
"2008 Dodge Challenger SE": 14000,
"2008 Dodge Challenger SRT8": 25000,
"2018 Dodge Charger Hellcat": 70000,
"2018 Dodge Charger GT Plus": 37000,
"2011 Dodge Charger SRT8": 27000,
"2005 Dodge Charger SRT8": 17000,
"2017 Dodge Viper ACR": 150000,
"2017 Dodge Viper GTS": 76000,
"2012 Dodge Dart R/T": 12000,
"2010 Dodge Avenger Express": 8000,
"2008 Dodge Journey SXT": 8000,
"2007 Dodge Nitro 4.0 R/T": 8000,
"2007 Dodge Viper SRT-10": 55000,
"2007 Dodge Viper SRT10 ACR": 80000,
"2000 Dodge Intrepid R/T": 2500,
"2003 Dodge Neon SRT-4": 8000,
"1970 Dodge Dart Hemi Super Stock": 250000,
"1970 Dodge Dart Swinger 340": 55000,
"1970 Dodge Challenger R/T 426 Hemi": 100000,
"1969 Dodge Charger Daytona Hemi": 600000,
"1969 Dodge Charger R/T Hemi": 90000,
"2018 Mclaren Senna": 850000,
"2018 McLaren 720S": 335000,
"2015 McLaren 570S": 190000,
"2013 McLaren MP4-12C": 120000,
"1992 McLaren F1": 15000000,
"1997 McLaren F1 GT": 20000000,
"1995 McLaren F1 LM": 20000000,
"2013 McLaren P1": 2000000,
"1974 MG Midget": 12000,
"1928 MG M-Type Midget": 25000,
"2007 Aston Martin DBS": 100000,
"2016 Aston Martin DB11": 200000,
"2016 Aston Martin V12 Vantage S": 185000,
"2018 Aston Martin DBS Superleggera": 305000,
"2013 Aston Martin V8 Vantage": 75000,
"2011 Aston Martin One-77": 3350000,
"2004 Aston Martin Vanquish S": 100000,
"2008 Aston Martin DB9": 35000,
"2019 Aston Martin Valkyrie": 3200000,
"2018 Range Rover Supercharged": 115000,
"2018 Range Rover Velar R-Dynamic": 80000,
"2018 Range Rover Sport SVR": 130000,
"2016 Land Rover Defender 70th Edition": 70000,
"1957 Land Rover Series 1": 30000,
"2003 Infiniti G35": 14000,
"2017 Infiniti Q60 Red Sport": 55000,
"2015 Infiniti Q50 Eau Rouge": 100000,
"2019 Infiniti Q50": 40000,
"2019 Tesla Model S Ludicrous Performance": 158000,
"2019 Tesla Model S Standard Range": 100000,
"2019 Tesla Model 3 Performance": 60000,
"2019 Tesla Model 3 Standard Range": 35000,
"2019 Tesla Model X Ludicrous Performance": 170000,
"2019 Tesla Model X Standard Range": 115000,
"2019 Mini Cooper S": 27000,
"2019 Mini John Cooper Works": 38000,
"1969 Morris Mini Cooper S": 30000,
"2020 Cadillac CT4-V": 50000,
"2019 Cadillac CTS-V": 90000,
"2019 Cadillac CTS 3.6L V6": 55000,
"2019 Cadillac ATS-V Coupe": 69000,
"2016 Cadillac ELR": 66000,
"2020 Cadillac CT6 Platinum": 92000,
"2020 Cadillac Escalade": 80000,
"2020 Cadillac XT5": 49000,
"2014 Cadillac CTS-V Sport Wagon": 40000,
"2004 Cadillac Seville": 5000,
"2011 Cadillac DTS": 7000,
"1975 Cadillac Fleetwood Brougham": 12000,
"1976 Cadillac Eldorado": 15000,
"1959 Cadillac Eldorado Brougham": 200000,
"Renault R35 Tank": 70000,
"2019 Renault Clio Iconic TCe 100": 24000,
"2019 Renault Clio RS Line TCe 130": 30000,
"2019 Renault Clio E-TECH Launch Edition": 31000,
"2018 Renault Clio RS Trophy": 30000,
"2003 Renault Clio V6": 55000,
"1993 Renault Clio Williams": 20000,
"1993 Renault Clio": 1500,
"1993 Renault Twingo": 1000,
"2010 Renault Twingo RS 133 Cup": 6000,
"2010 Renault Twingo RS": 5000,
"2020 Renault Twingo": 17000,
"2020 Renault Megane RS 300 Trophy": 50000,
"2020 Renault Megane RS Trophy R": 56000,
"2020 Renault Megane RS Line TCe 140": 30000,
"2005 Renault Megane Sport 225 Cup": 6000,
"LIGHNING MCQUEEN":9999999999999999999999999999999999999999,
"2018 Fortnite Shopping Cart GT-S": 69696969699696969696969,
"2019 Fortnite ATK GT-4R": 3045789034753478587578237587234857234895723485723489577897589347589023478589347582347582347890,
"1009 Thanos Car": 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555.5

}

Car_Cool = {
"2000 Honda Integra" : 4,
"2000 Honda Integra Type R" : 7,
"1999 Honda Civic Type R EK9" : 8.5,
"2003 Honda Civic Type R EP3" : 8,
"2003 Honda NSX R" : 9.5,
"2001 Honda S2000" : 5,
"2021 Honda Civic Type R FK8" : 6.5,
"1991 Honda Civic EG6 SiR": 7.5,
"1999 Honda Civic LX": 3,
"2006 Honda Civic Si": 4,
"2018 Honda Civic Sport": 2.5,
"2018 Honda Civic Si Coupe": 5,
"2006 Honda Accord 3.0 EX": 3,
"2010 Honda Accord EX-L V6": 3,
"2015 Honda Accord Sport": 3,
"2015 Honda Accord EX-L V6": 3,
"2018 Honda Accord Sport": 3,
"2021 Honda CR-V": 2,
"1999 Honda CR-V": 2.5,
"2005 Honda Pilot": 1,
"2010 Honda Crosstour": 0.5,
"2005 Honda Element": 1,
"2001 Honda Odyssey Absolute": 5,
"2021 Honda N-ONE RS": 5,
"2021 Honda StepWGN Spada": 4,
"1999 Honda StepWGN": 3.5,
"2016 Honda CR-Z": 4.5,
"2021 Honda HR-V": 2, 
"2005 Honda Stream": 2.5,
"2014 Honda Stream": 2.5,
"2021 Honda Clarity": 1,
"2000 Honda Insight": 5.5,
"2021 Honda Insight": 2,
"2000 Honda ACTY": 3,
"2021 Honda ACTY": 3,
"2021 Honda Fit": 2.5,
"2001 Honda Life Dunk": 4,
"1992 Honda Vigor": 2.5,
"1989 Honda Accord": 3,
"2003 Acura RSX Type S" : 6,
"2017 Acura NSX" : 7.5,
"2005 Acura TL Type S": 4,
"2007 Acura TL": 3,
"2018 Acura TLX 3.5": 3,
"2018 Acura MDX": 2,
"2018 Acura ILX": 3,
"2021 Acura TLX Type S": 6.5,
"1995 Acura Legend": 7,
"2014 Acura TSX Sport Wagon": 5,
"1990 Ford Mustang Foxbody" : 3.5,
"2010 Ford Mustang GT500" : 6.5,
"2015 Ford Mustang GT" : 5,
"1975 Ford Pinto": 1,
"1999 Ford Crown Victoria": 3.5,
"2017 Ford Focus Hatch": 2.5,
"2017 Ford Focus RS": 6,
"2017 Ford Fusion Titanium": 3,
"2017 Ford Fusion Sport": 3,
"2018 Ford F-150 Super Cab": 4,
"2018 Ford F-150 Raptor": 6.5,
"2016 Shelby Mustang GT350R" : 7,
"1992 Volkswagen Golf GTi MK2" : 4,
"2017 Volkswagen Golf GTi MK7" : 5,
"2015 Volkswagen Scirocco R" : 5.5,
"2018 Volkswagen Passat R-Line": 3,
"1969 Volkswagen Beetle": 7,
"1999 BMW M3" : 8.5,
"2003 BMW M3" : 8,
"2008 BMW M3" : 7.5,
"2017 BMW M3" : 7,
"2005 BMW M5" : 7.5,
"2018 BMW M5" : 7,
"2017 BMW M4" : 7,
"2017 BMW M6" : 7,
"2018 BMW i8" : 8,
"1959 BMW 507": 10,
"2018 BMW 530i": 3,
"2018 BMW X3": 2,
"2018 BMW 750i": 4,
"1974 BMW 2002 Turbo": 9,
"2011 BMW 1M": 7.5,
"2018 BMW 330i": 3,
"2020 BMW M235i xDrive Gran Coupe": 7,
"2007 Saturn Ion": 2,
"2001 Saturn SL2": 1,
"1998 Saturn SW2": 1,
"2017 Ferrari 488GTB" : 8,
"2017 Ferrari F12" : 8.5,
"2003 Ferrari 575M Maranello" : 7,
"1999 Ferrari 360" :7,
"1995 Ferrari F355" : 7,
"1965 Ferrari 250 GTO" : 10,
"1968 Ferrari Dino" : 9,
"1970 Ferrari 365 GTB/4 Daytona" : 9.5,
"2008 Ferrari F430" : 8,
"2008 Ferrari California" : 7,
"2016 Ferrari LaFerrari" : 10,
"2010 Ferrari 458 Italia": 8,
"1993 Toyota MR2 GT-S" : 8,
"1986 Toyota Corolla Sprinter Trueno" : 9.5,
"1993 Toyota Supra Twin Turbo" : 10,
"1998 Toyota Chaser Tourer V" : 8,
"1997 Toyota Soarer" : 7.5,
"1996 Toyota Cresta 2.5 Twin Turbo": 7.5,
"1998 Toyota Altezza RS200" : 7.5,
"1984 Toyota Landcruiser 60 3F" : 9,
"2003 Toyota Tundra" : 4.5,
"2018 Toyota Land Cruiser Prado" : 5,
"2018 Toyota 4Runner TRD Pro" : 7,
"2018 Toyota Tundra TRD Pro" : 7,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 5,
"2017 Toyota Century": 8.5,
"2019 Toyota Corolla Hatch XSE": 4,
"2019 Toyota Corolla Hatch SE": 3,
"2019 Toyota Corolla Touring Sport": 6,
"2021 Toyota GR Supra": 7.5,
"2008 Toyota Sequoia V8": 4,
"2005 Toyota Camry LE V6": 3,
"1999 Toyota Corolla LE": 3,
"2002 Toyota Sienna 5D Symphony": 3,
"2010 Toyota Camry LE": 3, 
"2016 Toyota Avalon Limited": 3.5,
"2018 Toyota Camry XSE": 4,
"2018 Toyota Corolla XLE": 3.5,
"1969 Toyota 2000GT": 10,
"2001 Toyota Camry LE V6": 3,
"2006 Toyota Sienna Limited": 3,
"2017 Toyota Sienna SE": 5,
"2018 Toyota Sienta": 5,
"2018 Toyota Alphard": 5.5,
"2018 Toyota Crown Majesta": 5,
"2018 Toyota Tundra SR5 5.7L V8": 4.5,
"2018 Toyota Hiace": 4.5,
"1993 Toyota Hiace": 4, 
"1997 Toyota Celica GT-Four": 8.5,
"1998 Toyota GT-one TS020": 10,
"1993 Toyota Mark II Tourer V JZX90": 7,
"2018 Toyota GT86": 5,
"1997 Toyota Tercel": 2,
"1997 Toyota Celica GT": 4,
"2016 Toyota Land Cruiser": 7,
"2019 Toyota Tacoma SR5": 4,
"2019 Toyota Tacoma TRD Pro": 7,
"1993 Toyota Sera": 8,
"2020 Toyota Avalon Touring": 4.5,
"2020 Toyota Avalon Limited": 4,
"2020 Toyota Avalon Limited Hybrid": 4,
"2020 Toyota Avalon TRD": 5,
"2020 Toyota Camry LE": 3,
"2020 Toyota Camry SE Hybrid": 3,
"2011 Toyota Prius": 2,
"2020 Toyota Prius XLE AWD": 2,
"2021 Toyota GR Yaris": 7,
"2022 Toyota GR86 Base": 6,
"2022 Toyota GR86 Premium": 6,
"2018 Toyota Camry SE": 3.5,
"2009 Lexus LFA" : 10,
"2007 Lexus ISF" : 6.5,
"1998 Lexus GS300" : 6,
"2018 Lexus LC500" : 8,
"2018 Lexus LS500 AWD" : 7,
"2019 Lexus ES300h": 6,
"2018 Lexus GS F": 7,
"2003 Lexus LS430": 6,
"2019 Lexus RX350": 5,
"1999 Lexus RX300 4WD": 4.5,
"2019 Lexus LX570": 5.5,
"2022 Lexus IS500 F Sport Performance": 7,
"2022 Lexus IS350 F Sport": 6,
"1990 Nissan Skyline GTR R32" : 9.5,
"1994 Nissan Skyline GTR R33 Spec-V" : 9,
"1999 Nissan Skyline GTR R34": 9.5,
"2002 Nissan Skyline GTR V-Spec II Nur" : 10,
"1996 Nissan 180SX" : 7.5,
"1993 Nissan Silvia K's Type S S14" : 8,
"2018 Nissan GTR Track Edition R35" : 7,
"2007 Nissan Fairlady Z" : 6,
"2018 Nissan Fairlady Z NISMO" : 6.5,
"2018 Nissan Fairlady Z" : 6,
"1989 Nissan 300ZX Turbo Z" : 5,
"2018 Nissan GT-R50 by Italdesign": 9.5,
"2018 Nissan GT-R NISMO": 8,
"2018 Nissan Maxima Platinum": 3,
"2018 Nissan Sentra SR Turbo": 3,
"2017 Nissan Leaf": 3.5,
"1973 Nissan Skyline H/T 2000GT-R": 10,
"1987 Nissan Skyline GTSR R31": 9,
"1989 Nissan Skyline GTS-4 R32": 5,
"1998 Nissan Skyline 25GT-X Turbo R34": 5.5,
"1965 Nissan Silvia 1600 Coupe": 9.5,
"1990 Nissan Silvia S13": 8,
"1999 Nissan Silvia Spec-R S15": 8,
"1995 Nissan GT-R Skyline R33 LM": 10,
"1998 Nissan R390 GT1": 10,
"1992 Nissan Cefiro 2.0 Turbo": 5,
"1990 Nissan Laurel Turbo Medalist": 6.5,
"2017 Nissan Armada Platinum": 4,
"1994 Nissan Hardbody": 4.5,
"2018 Nissan Titan Platinum Reserve": 4,
"2003 Nissan Skyline GT-R R34 Z-Tune": 10,
"2015 Nissan Juke": 1,
"2021 Nissan Altima 2.0 SR": 3,
"2021 Nissan Altima 2.5 Platinum": 3,
"2022 Nissan GT-R T-Spec": 8,
"2015 Lamborghini Veneno": 10,
"2003 Lamborghini Gallardo" : 7.5,
"2007 Lamborghini Gallardo SL" : 8.5,
"2008 Lamborghini Gallardo LP560-4" : 8,
"2010 Lamborgini Gallardo LP570-4 SL ": 8.5,
"2013 Lamborghini Gallardo LP570-4 SC" : 8.5,
"2014 Lamborghini Huracan LP610-4" : 8,
"2017 Lamborghini Huracan Performante" : 9,
"2001 Lamborghini Murcielago" :8,
"2006 Lamborghini Murcielago LP640" : 8.5,
"2009 Lamborghini Murcielago LP670-4 SV" :9,
"2015 Lamborghini Aventador SV" : 9,
"2016 Lamborghini Aventador S" : 8.5,
"1971 Lamborghini Miura P400SV" : 9.5,
"1996 Lamborghini Diablo SV" : 8,
"1985 Lamborghini Countach LP5000s QV" : 9.5,
"2020 Lamborghini Sian": 10, 
"2021 Lamborghini Urus": 7.5,
"2021 Lamborghini Huracan Evo": 8,  
"1995 Lamborghini Diablo SE30 Jota": 10, 
"2000 Lamborghini Diablo GTR": 10, 
"2017 Bentley Continental GT" : 7.5,
"2015 Bentley Bentayga" : 7,
"2015 Koenigsegg Regera" : 10,
"2010 Koenigsegg Agera" : 9.5,
"2007 Koenigsegg CCX" : 9,
"2005 Bugatti Veyron 16.4" : 9.5,
"2016 Bugatti Chiron" : 10,
"2017 Porsche 911 GT2 RS" : 8,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" :7,
"2016 Porsche 911 Turbo" : 7.5,
"2016 Porsche 718 Boxster" : 6,
"2017 Porsche 718 Cayman GTS" : 7,
"1975 Porsche 911 Turbo" : 9,
"1995 Porsche 911 GT2" : 9.5,
"1987 Porsche 959" : 10,
"1999 Porsche 911 GT3" : 7.5,
"1980 Porsche 924 Turbo": 6.5,
"2015 Lotus Evora 400" : 6.5,
"2011 Lotus Exige S" : 7.5,
"1996 Lotus Esprit V8" : 7.5,
"2006 Lotus Elise S" : 6,
"2018 Mazda Miata MX-5 Club" : 6.5,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 6,
"1989 Mazda MX-5 Miata" : 8,
"1989 Mazda RX-7 Savanna Turbo" : 7.5,
"1992 Mazda RX-7" : 8.5,
"1998 Mazda RX-7 RZ" : 9,
"2009 Mazda RX-8" : 7,
"2019 Mazda6 Signature": 5,
"2019 Mazda3 Hatch": 4,
"2019 Mazda CX-5": 2,
"2019 Mazda CX-3": 1.5,
"2014 Mazda2": 2,
"2015 Mazda5": 2,
"2006 Mazdaspeed 6 GT": 6,
"2013 Mazdaspeed 3": 5.5,
"2001 Mazda RX-7 Spirit R Type A" : 9.5,
"2018 Morgan Three-Wheeler" : 9,
"1998 Subaru Impreza 22B STi": 9.5,
"1995 Subaru Impreza WRX STi Version II": 8,
"2002 Subaru Impreza WRX STi": 7.5,
"2003 Subaru Impreza WRX STi": 7.5,
"2005 Subaru Impreza WRX STi": 7.5,
"2010 Subaru Impreza WRX STi R205": 8,
"2019 Subaru WRX STi": 7.5,
"1993 Subaru SVX": 6,
"2000 Subaru Forester STI": 7,
"2019 Subaru WRX": 5.5,
"2022 Subaru WRX": 5.5,
"2018 Subaru BRZ": 6,
"2022 Subaru BRZ Premium": 6,
"2022 Subaru BRZ Limited": 6,
"1988 Isuzu Impulse": 5,
"1979 Isuzu 117 Coupe": 8,
"1994 Mitsubishi Lancer Evo II": 8,
"2010 Mitsubishi Lancer Evo X GSR": 8,
"1999 Mitsubishi Lancer Evo VI GSR": 8.5,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 9,
"2003 Mitsubishi Lancer Evo VIII GSR": 8,
"1994 Mitsubishi 3000 GT VR-4": 6,
"1994 Mitsubishi FTO GPX": 5,
"1992 Mitsubishi Galant VR-4": 6,
"1974 VAZ Lada 1200":8,
"1975 UAZ-469":9,
"1965 GAZ Volga 21":8,
"1995 Hyundai Sonata 2.0i": 2,
"2013 Hyundai Genesis Coupe 3.8" : 5,
"2013 Hyundai Elantra GT": 4,
"2017 Hyundai Sonata Limited": 4,
"2005 Hyundai Tiburon GT V6": 5,
"2018 Kia Stinger GT": 7.5,
"2017 Kia Optima SX 2.0T": 4,
"2006 Audi R8":7.5,
"2008 Audi R8 V10":7.5,
"2010 Audi R8 GT": 8.5,
"2012 Audi R8 Plus": 8,
"2015 Audi R8 Coupe 5.2 FSI quattro": 8,
"1994 Audi RS2 Avant": 8.5,
"2018 Audi RS5": 7,
"2018 Audi RS3": 7,
"2018 Audi RS7": 7,
"2018 Audi RS6 Avant": 7,
"2018 Audi TTRS": 7.5, 
"2018 Mercedes-AMG E63 S 4Matic": 7,
"2018 Mercedes-Maybach S560": 8,
"2018 Mercedes-AMG S65 Sedan": 8,
"1990 Mercedes-Benz 190E Evolution II": 8,
"2016 Mercedes-AMG GT S": 8,
"2013 Mercedes-Benz SLS AMG GT": 8.5,
"2012 Mercedes-Benz C63 AMG Black Series": 7.5,
"2000 Mercedes-Benz C32 AMG": 7,
"2020 Mercedes-AMG A35 4Matic": 7,
"2020 Chevy Corvette C8 Stingray Z51": 7.5,
"2019 Chevy Corvette C7 ZR1": 8,
"2018 Chevy Corvette C7 ZO6": 7.5,
"2018 Chevy Corvette C7 Stingray": 7,
"1953 Chevy Corvette": 10,
"1960 Chevy Corvette C1": 8.5,
"1963 Chevy Corvette C2 Stingray 427": 9.5,
"1967 Chevy Corvette C3 327": 7.5,
"1970 Chevy Corvette C3 454": 8,
"1984 Chevy Corvette C4": 5.5,
"1988 Chevy Corvette C4 ZR1": 8,
"2001 Chevy Corvette C5": 6,
"2002 Chevy Corvette C5 Z06": 7,
"2007 Chevy Corvette C6": 6.5,
"2007 Chevy Corvette C6 Z06": 7,
"2007 Chevy Corvette C6 ZR1": 8.5,
"2018 Chevy Camaro 1LE": 7,
"2018 Chevy Camaro ZL1": 7.5,
"1969 Chevy Camaro SS 396": 7.5,
"2017 Chevy Malibu 1.5 Turbo": 3.5,
"2016 Chevy Malibu 2LT": 4,
"2017 Chevy Cruze Hatch Premier": 3.5,
"2016 Chevy Impala LT": 4.5,
"2018 Alfa Romeo 4C": 8,
"2018 Alfa Romeo Giulia Quadrifoglio": 8,
"2018 Alfa Romeo Stelvio Quadrifoglio": 7,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 6,
"2013 Alfa Romeo MiTo 1.4 8v": 5,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 6.5,
"2006 Alfa Romeo 8c Competizione": 8.5,
"1992 Alfa Romeo 155 Q4": 7.5,
"1985 Alfa Romeo Spider Veloce": 6.5,
"2017 Suzuki Swift Sport": 5,
"2016 Suzuki Alto Works": 5.5,
"2016 Suzuki Hustler G 4WD": 5,
"2003 Suzuki Liana 1.6 Sedan": 3,
"1995 Suzuki Samurai 1.3i": 7.5,
"2002 Suzuki Grand Vitara": 3,
"2018 Pagani Huayra BC": 10,
"2013 Pagani Huayra": 9,
"2010 Pagani Zonda Cinque": 10,
"2005 Pagani Zonda F": 9,
"1999 Pagani Zonda C12S": 9,
"1970 AMC AMX": 7.5,
"1972 AMC Javelin": 7,
"1969 AMC Ambassador": 5,
"1970 AMC Rebel The Machine": 9.5,
"1975 AMC Pacer X": 4,
"2018 Dodge Challenger SRT Hellcat Widebody": 7,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 6.5,
"2018 Dodge Challenger SRT Demon": 8,
"2008 Dodge Challenger SE": 5,
"2008 Dodge Challenger SRT8": 6,
"2018 Dodge Charger Hellcat": 7,
"2018 Dodge Charger GT Plus": 4,
"2011 Dodge Charger SRT8": 5,
"2005 Dodge Charger SRT8": 5,
"2017 Dodge Viper ACR": 8.5,
"2017 Dodge Viper GTS": 8,
"2012 Dodge Dart R/T": 4,
"2010 Dodge Avenger Express": 3,
"2008 Dodge Journey SXT": 2.5,
"2007 Dodge Nitro 4.0 R/T": 1,
"2007 Dodge Viper SRT-10": 8,
"2007 Dodge Viper SRT10 ACR": 8.5,
"2000 Dodge Intrepid R/T": 1,
"2003 Dodge Neon SRT-4": 2,
"1970 Dodge Dart Hemi Super Stock": 10,
"1970 Dodge Dart Swinger 340": 8.5,
"1970 Dodge Challenger R/T 426 Hemi": 9,
"1969 Dodge Charger Daytona Hemi": 10,
"1969 Dodge Charger R/T Hemi": 8.5,
"2018 Mclaren Senna": 10,
"2018 McLaren 720S": 9,
"2015 McLaren 570S": 8,
"2013 McLaren MP4-12C": 7.5,
"1992 McLaren F1": 10,
"1997 McLaren F1 GT": 10,
"1995 McLaren F1 LM": 10,
"2013 McLaren P1": 9.5,
"1974 MG Midget": 8,
"1928 MG M-Type Midget": 8.5,
"2007 Aston Martin DBS": 7.5,
"2016 Aston Martin DB11": 8,
"2016 Aston Martin V12 Vantage S": 7.5,
"2018 Aston Martin DBS Superleggera": 8,
"2013 Aston Martin V8 Vantage": 7,
"2011 Aston Martin One-77": 9.5,
"2004 Aston Martin Vanquish S": 7,
"2008 Aston Martin DB9": 7,
"2019 Aston Martin Valkyrie": 10,
"2018 Range Rover Supercharged": 6,
"2018 Range Rover Velar R-Dynamic": 5.5,
"2018 Range Rover Sport SVR": 6.5,
"2016 Land Rover Defender 70th Edition": 9,
"1957 Land Rover Series 1": 9,
"2003 Infiniti G35": 6.5,
"2017 Infiniti Q60 Red Sport": 7,
"2015 Infiniti Q50 Eau Rouge": 7.5,
"2019 Infiniti Q50": 4,
"2019 Tesla Model S Ludicrous Performance": 8,
"2019 Tesla Model S Standard Range": 4,
"2019 Tesla Model 3 Performance": 7,
"2019 Tesla Model 3 Standard Range": 3,
"2019 Tesla Model X Ludicrous Performance": 7.5,
"2019 Tesla Model X Standard Range": 2,
"2019 Mini Cooper S": 6,
"2019 Mini John Cooper Works": 7,
"1969 Morris Mini Cooper S": 7.5,
"2020 Cadillac CT4-V": 7,
"2019 Cadillac CTS-V": 8,
"2019 Cadillac CTS 3.6L V6": 5,
"2019 Cadillac ATS-V Coupe": 7.5,
"2016 Cadillac ELR": 6.5,
"2020 Cadillac CT6 Platinum": 5.5,
"2020 Cadillac Escalade": 5,
"2020 Cadillac XT5": 2,
"2014 Cadillac CTS-V Sport Wagon": 8,
"2004 Cadillac Seville": 2,
"2011 Cadillac DTS": 1,
"1975 Cadillac Fleetwood Brougham": 6.5,
"1976 Cadillac Eldorado": 7,
"1959 Cadillac Eldorado Brougham": 10,
"Renault R35 Tank": 10,
"2019 Renault Clio Iconic TCe 100": 3,
"2019 Renault Clio RS Line TCe 130": 4,
"2019 Renault Clio E-TECH Launch Edition": 4,
"2018 Renault Clio RS Trophy": 7,
"2003 Renault Clio V6": 8,
"1993 Renault Clio Williams": 8,
"1993 Renault Clio": 2,
"1993 Renault Twingo": 1,
"2010 Renault Twingo RS 133 Cup": 7,
"2010 Renault Twingo RS": 6.5,
"2020 Renault Twingo": 3,
"2020 Renault Megane RS 300 Trophy": 7,
"2020 Renault Megane RS Trophy R": 7.5,
"2020 Renault Megane RS Line TCe 140": 5,
"2005 Renault Megane Sport 225 Cup": 6.5,
"LIGHNING MCQUEEN":9999999999999999999999999999999999999999,
"2018 Fortnite Shopping Cart GT-S": 69696969699696969696969,
"2019 Fortnite ATK GT-4R": 3045789034753478587578237587234857234895723485723489577897589347589023478589347582347582347890,
"1009 Thanos Car": 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555.5
}

Car_Description = {
"2000 Honda Integra" : "A JDM passenger car with lots of tuning potential.",
"2000 Honda Integra Type R" : "The hotter variant of the Honda Integra. Has more horsepower and stiffer suspension.",
"1999 Honda Civic Type R EK9" : "The 1st generation Civic Type R. The coolest Civic ever.",
"2003 Honda Civic Type R EP3" : "The 2nd generation Civic Type R. The last true Civic Type R.",
"2003 Honda NSX R" : "The hottest version of the legendary Honda NSX.",
"2001 Honda S2000" : "A bargain sports car that was made by Honda. Unlike most small sports cars, the S2000 was quite quick.",
"2021 Honda Civic Type R FK8" : "The new Civic Type R. Built from the ground up with speed in mind, the FK8 grips the road like an F1 car. However, much to the disdain of VTEC purists, this Type R lacks the severe torque curve that made a Type R a Type R. The new 2021 model features slightly revamped styling and chassis upgrades.",
"1991 Honda Civic EG6 SiR": "A JDM exclusive VTEC rocket. Shingo's car from Initial D.",
"1999 Honda Civic LX": "Oh, I have this car. It's reliable, efficient, and pretty comfortable. I'm not going to call it fast, (ever) but it is fun to drive.",
"2006 Honda Civic Si": "Oh man. The Civic Si. This is the infamous 8th gen Civic Si, endlessly ruined by ricers. The thing is, it's actually not such a bad car. It's a fun to drive (if not fast) sports car. However, there's nobody that's saying that you can't make it fast, with the right mods.",
"2018 Honda Civic Sport": "The Sport is ugly. Uglier than the already extraordinarily ugly Civic. However, it has been rated very highly on multiple reputable car magazines for being fun to drive and practical.",
"2018 Honda Civic Si Coupe": "The 2018 Civic Si Coupe is possibly the only FK8 gen Civic that doesn't look bad. It actually looks good- albeit at a bit of a stretch. Looks aside, the 2018 Civic Si is the best that the Si has ever been; it's fun to drive, and is actually decently quick for the price.",
"2006 Honda Accord 3.0 EX": "Take a look at that kid to your left in a riced out Honda Civic challenging you to a race. You think that you can't win because you're in an Accord? Well, think again. This Accord has 244 horsepower. Didn't expect that, did you.",
"2010 Honda Accord EX-L V6": "This is a sleeper car. It looks absolutely identical to every other Accord apart from the subtle V6 badging on the back. It has 271 horses.",
"2015 Honda Accord Sport": "This is literally the only sport package that I have seen that only adds 2 horsepower. Nevermind, I've seen a bunch of those.",
"2015 Honda Accord EX-L V6": "This is the real Accord Sport. It's actually quite quick, expecially when you remember that it's an Accord.",
"2018 Honda Accord Sport": "The new Accord is completely redesigned inside and outside, with a new engine, a more responsive chassis, and a completely new interior. Seems they ran out of money when they got to the back seats, though. Sucks. Would've been the perfect Accord.",
"2021 Honda CR-V": "In a broad sense, the 2021 Honda CR-V is the quintessential small SUV. It's spacious without being overly bulky, comfortable without feeling soft or bouncy, and endlessly usable thanks to lots of cargo space. It's also easy to drive and offers available all-wheel drive. Yet the key to the CR-V's appeal is that it typically manages to do these things just a little bit better than the competition.",
"1999 Honda CR-V": "Built on the Civic platform, the CR-V successfully integrates familiar Honda components into a fresh new design. Honda's famous four-wheel double-wishbone suspension makes an appearance on the CR-V (the first-ever application of four-wheel double-wishbone technology on a sport-ute), as does the familiar four-speed automatic transmission, which now comes with an overdrive on/off switch. The 2.0-liter DOHC inline four-cylinder engine makes 146 horsepower and 133 foot-pounds of torque, up 20 horsepower from 1998, thanks to intake and exhaust tuning along with an increased compression ratio.",
"2005 Honda Pilot": "The 2005 Honda Pilot receives a new 255-hp engine, along with numerous functional changes. A tire-pressure monitoring system has been added, and EX models with leather get vehicle stability control. Slightly increased fuel capacity helps extend driving range, and a revised power steering pump provides improved on-center steering feel. Inside the cabin, the instrument panel has been tweaked with ambient lighting and a six-disc CD changer for all EX trims. A driver footrest has been added, and leather-upholstered EX models can now be had with a sunroof. The LX now has standard keyless entry, and all models get an integrated remote key and fob.",
"2010 Honda Crosstour": "The 2010 Honda Accord Crosstour is indeed a cross between multiple genres. Like many crossover SUVs, it's based on a sedan; unlike true crossovers, though, the Accord Crosstour doesn't offer the versatility of a wagon or SUV. Think of it as a V6-powered Accord hatchback with marginally increased ground clearance and available all-wheel drive, and you'll get the idea. Consumers never really got on board with this unusual concept, causing the Crosstour to be discontinued.",
"2005 Honda Element": "Intended to accommodate the lifestyles of the young and active, the 2005 Honda Element is a spunky small SUV with a thoughtfully designed interior wrapped up in a unique shell. Intended to acommodate young Gen-Y types who wanted an affordable vehicle with flexible cargo-hauling ability, the Element s chock-full of features that make it easy to take the mountain bikes to the trailhead, the surfboard to the waves or the 27-inch TV to the dorm or apartment. Riding on a wheelbase of just 101.4 inches and measuring only 166.5 inches in overall length, the Element is compact, yet the space inside makes it hard to believe that the Element is actually 8 inches shorter in length than a Civic coupe.",
"2001 Honda Odyssey Absolute": "The Honda Odyssey is a minivan manufactured by Honda since 1994, originally conceived and engineered in Japan, in the wake of the country's economic crisis which in turn imposed severe constraints on the vehicle's size and overall concept, dictating the minivan's manufacture in an existing facility with minimal modification. The result was a smaller minivan, in the compact MPV class, that was well received in the Japanese domestic market but less well received in North America. Subsequent generations diverged to reflect market variations, and Honda built a plant in Lincoln, Alabama, incorporating the ability to manufacture larger models. Since model year 1999, Honda has marketed a larger (large MPV-class) Odyssey in North America and a smaller Odyssey in Japan and other markets. This is the sporty Absolute variant of the third generation Odysset, with AWD and a 200 hp K24A engine.",
"2021 Honda N-ONE RS": "Earlier this fall, Honda introduced the second generation of its N-One kei car. The new N-One went on sale in Japan this past weekend, and while it looks a whole lot like its predecessor, and most of the changes have been reserved for the interior, the sportiest RS version does have one particular characteristic that is sure to earn it a great many fans: It comes only with a six-speed manual.",
"2021 Honda StepWGN Spada": "The Honda Stepwgn (stylised as STEPWGN, pronounced 'step wagon') is a mid-sized MPV produced by Honda since 1996. It is designed with a higher cabin, in contrast to the Odyssey and also the Stream respectively. Additionally, it can accommodate eight people, instead of seven in the Odyssey and Stream. For its first two generations the car had one door on the driver's side and two doors on the passenger's side. This is a fifth generation Spada model.",
"1999 Honda StepWGN": "The Honda Stepwgn (stylised as STEPWGN, pronounced 'step wagon') is a mid-sized MPV produced by Honda since 1996. It is designed with a higher cabin, in contrast to the Odyssey and also the Stream respectively. Additionally, it can accommodate eight people, instead of seven in the Odyssey and Stream. For its first two generations the car had one door on the driver's side and two doors on the passenger's side. This is a first generation model, with a 4 speed auto.",
"2016 Honda CR-Z": "Let's face it: You don't shop for a hybrid looking for high performance. Great fuel economy and exhilarating performance just don't go together unless you're dropping close to a million dollars on a Porsche 918 Spyder. But Honda at least makes an attempt with its 2016 CR-Z. This small, sporty hybrid coupe is lightweight, steers quickly and parks easily. A sleek exterior and adventurous dashboard design make it one of the more attractive designs among its more futuristic or merely pragmatic competitors.",
"2021 Honda HR-V": "The Honda HR-V has been on the extra-small SUV scene since 2016 and has made a name for itself as a value-packed vehicle with a clever folding back seat (Honda calls it the 'Magic Seat') and a comfortable ride.", 
"2005 Honda Stream": "This MPV was based on the seventh generation of the Honda Civic, using a McPherson front suspension and a multilink rear suspension. The Stream had a 2720 mm (107 in) long wheelbase, which was 110 mm (4 in) more than for the Civic sedan. This modification allowed engineers to install a third row of seats, thus making the Stream a 7 seater in a 2-3-2 configuration.",
"2014 Honda Stream": "This MPV was based on the seventh generation of the Honda Civic, using a McPherson front suspension and a multilink rear suspension. The Stream had a 2720 mm (107 in) long wheelbase, which was 110 mm (4 in) more than for the Civic sedan. This modification allowed engineers to install a third row of seats, thus making the Stream a 7 seater in a 2-3-2 configuration.",
"2021 Honda Clarity": "The 2021 Honda Clarity is an eco-minded sedan sold in two variations: as a hydrogen fuel cell or a plug-in hybrid electric vehicle (PHEV). The former is only available in California because it's the only state with any substantial hydrogen infrastructure. Since the fuel cell is used to power an electric motor, the Clarity drives and feels like a battery-powered EV, and you can fill the hydrogen fuel tank in just a few minutes. The Clarity Plug-In Hybrid, meanwhile, uses a small battery pack paired with a gasoline engine. As a result, the Clarity Plug-In Hybrid offers 47 miles of pure electric range, but its backup gasoline engine allows it to travel as far as any regular sedan.",
"2000 Honda Insight": "Honda started the new millennium by bringing the buying public the first production gasoline-electric hybrid. With its ultralow drag styling, aluminum body structure and innovative Integrated Motor Assist (IMA), the Insight can travel as far as 70 miles on a gallon of gas (with a 10.6-gallon fuel tank, you can drive from Los Angeles to Salt Lake City and still have a gallon of gas in reserve).",
"2021 Honda Insight": "If you'd like the fuel efficiency of something like the Toyota Prius but with more traditional styling, the 2021 Honda Insight could be an ideal alternative. Sized between Honda's Civic sedan and the larger Accord, the Insight has a standard hybrid powertrain that gets an EPA-estimated 52 mpg in combined city/highway driving. That's right up there with the most efficient hybrids on the market. The Insight is roomy and enjoyable to drive, too, so you're not really giving up anything to go the hybrid route.",
"2000 Honda ACTY": "The Honda Acty is a series of cabover microvans and kei trucks produced by the Japanese automaker Honda from 1977 to 2021, designed for the Japanese domestic market (JDM). 'Acty' is short for 'Activity'. This is a third generation model 5-door van.",
"2021 Honda ACTY": "The Honda Acty is a series of cabover microvans and kei trucks produced by the Japanese automaker Honda from 1977 to 2021, designed for the Japanese domestic market (JDM). 'Acty' is short for 'Activity'. This is a new fourth generaton truck.",
"2021 Honda Fit": "Compared to other models in Honda's lineup, the 2021 Fit doesn't garner a whole lot of attention. It's not cool like the Civic Type R or hugely popular like the CR-V. But this little car is affordable and surprisingly versatile. In sports analogy terms, you could say it's underrated. While the Fit uses a modestly powered four-cylinder engine, acceleration feels sprightly around town and it hits highway speeds sooner than most compact hatchbacks and small crossovers. It's also quite fuel-efficient, and we found it easy to match EPA estimates in real-world driving — something that can't be said about many Fit competitors. The Fit's nimble handling is another draw.",
"2001 Honda Life Dunk": "The Honda Life is an automobile nameplate that was used on various kei car/city cars produced by Honda: passenger cars, microvans, and kei trucks. The first series of the nameplate was built between 1971 and 1974, with the nameplate revived in 1997 and used until 2014. The Japanese-market Life has rarely been marketed outside Japan. In December 2000, a turbocharged variant named Honda Life Dunk was introduced as 2001 year model. The Honda Life Dunk and the Honda That's were listed by Forbes magazine as among the weirdest car names.",
"1992 Honda Vigor": "The Honda Vigor is a premium sedan that was derived from the Honda Integra. It was sold in Japan through the Honda Verno dealer network from 1981 to 1995, and sold in North America from June 1991 (model year 1992) to 1994 as the Acura Vigor. Early Vigors were more upmarket versions of the Accord, and served as Honda's flagship until the arrival of the Honda Legend.",
"1989 Honda Accord": "The '89 Accord was THE choice in its class back when it was new in the showrooms and was in great demand. As a result, the didn't come cheap.",
"2003 Acura RSX Type S" : "An Integra made for the North America. The Type S was the fastest version.",
"2017 Acura NSX" : "The new Acura NSX is an AWD rocket. Unfortunately, it lacks the sense of purity that made the original so great. However, it makes up for it with sheer speed.",
"2005 Acura TL Type S": "Basically a VTEC powered sedan. I kinda like it. But the tranny a bit bad.",
"2007 Acura TL": "Woah! I can get this for only $6500? Yep, that's what happens to overpriced vehicles.",
"2018 Acura TLX 3.5": "The Acura TLX is one of Acura's attempts at making a sports sedan. It's not exactly blisteringly quick, but it is fun to drive.",
"2018 Acura MDX": "An SUV made by Acura.",
"2018 Acura ILX": "Acura's entry level sedan.",
"2021 Acura TLX Type S": "The Acura TLX is a Mid-size luxury car sold by Acura. Acura introduced a high performance Type-S variant for the second generation TLX, marking the return of the Type S brand after over a decade-long hiatus. It features an all-new DOHC 3.0-liter V6 with a single twin-scroll turbocharger and direct injection, producing 355 hp and 354 lb-ft of torque. Both the A-Spec and the Type-S will use Super Handling All-Wheel Drive (SH-AWD) which can send 70% of torque to the rear axle and of that power as much as 100% to either rear wheel.",
"1995 Acura Legend": "The Acura Legend is a mid-size luxury/executive car manufactured by Honda from Japan. It was sold in the U.S., Canada, under Honda's luxury brand, Acura, from 1985 to 1995, as both a sedan, which was classified as a full-size car,and a coupe, which was classified as a mid-size car (similar to how the Honda Accord is set up today). It was the first flagship sedan sold under the Acura nameplate, until being renamed in 1996 as the Acura 3.5RL. The 3.5RL was the North American version of the KA9 series Honda Legend.",
"2014 Acura TSX Sport Wagon": "By all measures, the Acura TSX Sport Wagon should have been an enthusiast’s dream come true. Acura took the TSX — which was fun to drive, fuel-efficient and dead reliable — and made it into a wagon for even more practicality. But it wasn't. The TSX Sport Wagon was only available with a lethargic 5-speed auto, and an underpowered 4-cylinder engine. However, the TSX's handling characteristics were untouched, making this still fun to drive.",
"1990 Ford Mustang Foxbody" :  "A square muscle car widely used in many racing disciplines, from drag to drift.",
"2010 Ford Mustang GT500" : "A superpowered Mustang that was geared to take out the Corvette. Unfortunately, they forgot to superpower the chassis.",
"2015 Ford Mustang GT" : "The new generation Mustang. It is better than the previous gen in every way... except for the styling.", 
"1975 Ford Pinto": "Boom, kaboom, a barbecue that seats four.",
"1999 Ford Crown Victoria": "The car of choice for coppers for good reason. Rugged, cheap, decently quick, and it's body on frame, baby. Time to ram some kids in Civics.",
"2017 Ford Focus Hatch": "A compact hatch made by Ford. Not all that great... but I mean... it's cheap.",
"2017 Ford Focus RS": "A $37,000 sports car with the interior of a $16,000 economy car. It makes up for it for being as fast as something worth twice the price, though.", 
"2017 Ford Fusion Titanium": "A *almost* top of the line Ford Fusion.",
"2017 Ford Fusion Sport": "A top of the line Ford Fusion, this has the same ecoboost twin turbo V6 as the F-150.",
"2018 Ford F-150 Super Cab": "A completely solid truck... in perhaps every single way.",
"2018 Ford F-150 Raptor": "This is the F-150 on steroids. It has 450 horsepower, big, meaty tires, a FREAKIN skidplate, and raised suspension.",
"2016 Shelby Mustang GT350R" : "The hot version of the new Mustang. Unlike the previous Shelby, this time they didn't forget about the chassis.",
"1992 Volkswagen Golf GTi MK2" : "The 2nd gen Golf GTi. A Euro icon.",
"2017 Volkswagen Golf GTi MK7" : "The newest generation Golf GTi It's not slow.",
"2015 Volkswagen Scirocco R" : "A Scirocco, basically a cooler Golf. This one is the R, the fast one.",
"2018 Volkswagen Passat R-Line": "The Volkswagen Passat is a large four door family car manufactured by Volkswagen. The R-Line is supposed to look fast or something, but it isn't.",
"1969 Volkswagen Beetle": "The Volkswagen Beetle—officially the Volkswagen Type 1, informally in German the Käfer (meaning 'beetle'), in parts of the English-speaking world the Bug,  and known by many other nicknames in other languages—is a two-door, rear-engine economy car, intended for five occupants that was manufactured and marketed by Volkswagen. The need for a people's car (Volkswagen in German), its concept and its functional objectives were formulated by the leader of Nazi Germany, Adolf Hitler, who wanted a cheap, simple car to be mass-produced for his country's new road network. Lead engineer Ferdinand Porsche and his team took until 1938 to finalise the design. The influence on Porsche's design of other contemporary cars, such as the Tatra V570, and the work of Josef Ganz remains a subject of dispute. The result was the first Volkswagen, the Type 1 (the Beetle). It was one of the first rear-engined cars since the Brass Era, and with 21,529,464 produced, the Beetle is the longest-running and most-manufactured car of a single platform ever made.",
"1999 BMW M3" : "The BMW E36 M3 is a retro classic... whether you like it or not. Used in every motorsport thinkable, really. It's awesome.",
"2003 BMW M3" : "The E46 M3 is the succesor to the E36, and looks mostly the same apart from being a bit more rounded on the edges. But I assure you that the E46 is a different animal compared to the E36. While the E36 was nimble and light, the E46 is heavy and wide. While less agile, the E46 feels planted, not to mention the fact that it has far more power than the E36.",
"2008 BMW M3" : "The E92 M3 is the succesor to the E46, and gets new styling as well as a brand new engine: a 414 horsepower V8. With its wide stance and simple, powerful V8 going through the rear wheels, no wonder this car is so popular with tuners.",
"2017 BMW M3" : "The F80 M3 is ludicrously fast and handles well, but it can't help but feel a bit synthetic. Many people miss the thrill of the older, more analog M3s.",
"2005 BMW M5" : "The most iconic M5 ever made in my opinion, and definitely the last great one ever made. The E60 M5 has a naturally aspirated V10 that feels great when you step on the pedal.",
"2018 BMW M5" : "The new M3 is the fastest ever made. However, it feels very synthetic.",
"2017 BMW M4" : "The M4 is the successor to the 2008 M3, basically.",
"2017 BMW M6" : "The Maserati Gran Turismo of the BMW bunch. Goes quick in a straight line, but turns like a boat. I suppose it's because it kind of is one.",
"2018 BMW i8" : "The BMW i8 is a hybrid coupe made by BMW. ",
"1959 BMW 507": "The BMW 507 was a V8 powered roadster made by BMW. It was styled by the same person that styled the original Fairlady Z, Albrecht Von Goertz.",
"2018 BMW 530i": "The BMW 530i is a midsize sedan made by BMW. Generally an all around good car, excelling in nothing, but good in everything nevertheless.",
"2018 BMW X3": "The BMW X3 is a compact SUV made by BMW.",
"2018 BMW 750i": "The BMW 7 series is a fullsize luxury sedan made by BMW. Within the spectrum of large luxury sedans, it's more on the sporty side, and is actually suprisingly fast.",
"1974 BMW 2002 Turbo": "The BMW 2002 Turbo was a sports coupe made by BMW. It was very fast in its day.",
"2011 BMW 1M": "The BMW 1M was a small sports coupe created by BMW, and was actually very fast. It looked good in orange.",
"2018 BMW 330i": "The BMW 330i is a compact sedan made by BMW. It's generally an all around good car, but with nothing to push it to absolute excellence. But if you wanted absolute excellence, you would buy an M3, right?",
"2020 BMW M235i xDrive Gran Coupe": "The M235i Gran Coupe is the performance variant of the 228i Gran Coupe, and it... isn't a coupe, but instead a small sedan. Contrary to what people believed this car to be, it really isn't a WRX beater, but instead a cushy straight line rocket- which really isn't a problem at all, in my opinion.",
"2007 Saturn Ion": "The Saturn Ion was a compact sedan made by Saturn. It's... actually suprisingly reliable for a Saturn.",
"2001 Saturn SL2": "The Saturn SL2 was a compact sedan made by Saturn. It is plastic trash.",
"1998 Saturn SW2": "The Saturn SW2 was a compact wagon made by Saturn. Like the SL2, it is also plastic trash.",
"2017 Ferrari 488GTB" : "The newest V8 Ferrari. Beautifully styled and well crafted, it's what an Italian sports car should be.",
"2017 Ferrari F12" : "A V12 Ferrari. Jeremy Clarkson says that it's sometimes too powerful. JEREMY CLARKSON SAID THAT.",
"2003 Ferrari 575M Maranello" : "This is a grand tourer in every respect. It's actually quite comfy, no lie.",
"1999 Ferrari 360" : "A V8 Ferrari, and a good one, at that.",
"1995 Ferrari F355" : "This is the last Ferrari with popup headlights. It looked kind of dated, even back then. I'm not gonna say it's slow, though.",
"1965 Ferrari 250 GTO" : "The most expensive car ever made, the Ferrari 250 GTO's body was hand-hammered out of a single sheet of 6000 series aluminum; meaning that no 250 was identical to the other.",
"1968 Ferrari Dino" : "The Ferrari Dino was named after Dino Ferrari, the founder Enzo Ferrari's son. It had an all-aluminum V6 also used in the Fiat Dino.",
"1970 Ferrari 365 GTB/4 Daytona" : "Nicknamed the 'Daytona' by the public to commemorate the 1 2 3 finish by Ferrari in the February 1967 24 Hours of Daytona, the 365 GTB/4 was the successor to the Ferrari 275 GTB/4, and is a front-engined, rear wheel drive, V12 GT car.",
"2008 Ferrari F430" : "The Ferrari F430 is a mid engined V8 car by Ferrari. It is the successor to the Ferrari 360, with a redesigned body with greater downforce, while retaining the same drag coefficient.",
"2008 Ferrari California" : "The Ferrari California was targeted at a different audience than the rest of Ferrari's cars; those who cared more about luxury and glamour than actual performance. But, as Ferrari is... well, Ferrari, the California is still quite quick.",
"2016 Ferrari LaFerrari" : "The Ferrari LaFerrari was a mid engined hypercar manufactured by Ferrari. Externally, the lines of LaFerrari contain active diffusers, guide vanes on the underbody, and an active rear spoiler. These elements all provide downforce while reducing drag. LaFerrari is hand-built from varying degrees of lightweight carbon-fiber among its brethren grand prix cars. Even the seats are molded into the tub, and the steering wheel and pedals adjust to accommodate a driver’s height. So yes, LaFerrari comes to you; if you are lucky enough to be one of the 499 on the invitation-to-own list.",
"2010 Ferrari 458 Italia": "Replacing the Ferrari F430, the Ferrari 458 Italia was a mid engined supercar manufactured by Ferrari. In Ferrari's first official announcement of the car, the 458 was described as the successor to the F430 but arising from an entirely new design, incorporating technologies developed from the company's experience in Formula One. It was succeeded by the Ferrari 488 GTB.",
"1993 Toyota MR2 GT-S" : "The Toyota MR2 GT-S was the turbocharged variant of Toyota's well balanced mid-engined sports car. Unfortunately, Toyota decided to just not make it anymore." ,
"1986 Toyota Corolla Sprinter Trueno" : "Toyota's resident meme, the AE86 Corolla was nicknamed the 'Hachi-Roku' or 'Eight-Six' in English. It was widely used in many motosports such as drift, rally, and touring car championships, and was revered for it's well balanced nature and it's easily tunable 4A-GEU inline-four engine. However, all of this racing heritage is comparatively irrelevant to the AE86's meme status, resulting from its appearance in the hugely popular anime/manga series, Initial D.",
"1993 Toyota Supra Twin Turbo" : "The Toyota Supra Twin Turbo was the twin turbo variant of the Toyota Supra MKIV. These cars were generally over-engineered, and were able to be tuned to the 400-500 hp range without upgrading any internal parts while still providing exceptional reliability. Its 2JZ-GTE engine is still widely used in engine swaps because of these things.",
"1998 Toyota Chaser Tourer V" : "The Toyota Chaser Tourer V was a JDM only super sedan with a turbocharged inline 6; the 1JZ-GTE. It was considered a true all rounder, and was over-engineered to a ridiculous amount, just like the Supra, and it is still a very fast car." ,
"1997 Toyota Soarer" : "The Toyota Soarer was known as the Lexus SC300 in North America. However, this Toyota Soarer is JDM exclusive. It has a twin turbo inline 6, the 1JZ-GTE. This engine was exceptionally over-engineered, and had the ability to be tuned to slightly insane horsepower numbers while still maintaining reliblity. And the Soarer, being branded as a Lexus in North America, is a quite comfortable and luxurious car. All of these qualities make the Soarer quite amazing.",
"1998 Toyota Altezza RS200" : "The Toyota Altezza was known as the Lexus IS in North America. The RS200 never came to North America. The RS200 came with more horsepower, better brakes, and stiffer suspension compared to the tamer AS200.",
"1996 Toyota Cresta 2.5 Twin Turbo": "The Toyota Cresta Twin Turbo is a Supra with 4 doors and a 1JZ-GTE. IT'S AWESOME.",
"1984 Toyota Landcruiser 60 3F" : "Toyota utility vehicles are famously known to be literally almost indestructible. That is the same with the Landcruiser. The car synonymous with impossible conditions and the word 'rescue', the Toyota Landcruiser is both the UN's and ISIS's car of choice a for good reason.",
"2003 Toyota Tundra" : "The 2003 Toyota Tundra SR5 is an honest truck from Toyota with a Japanese made 4.7 L V8.",
"2018 Toyota Land Cruiser Prado" : "The Land Cruiser Prado is a smaller, Asian market exclusive version of the Land Cruiser.",
"2018 Toyota 4Runner TRD Pro" : "The 4Runner TRD Pro is the ultimate version of the ultimate body-on-frame offroad SUV available to the normal consumer. It houses a decently powerful V6, and while it may not include an advanced infotainment system, it has crawl control, so... there.",
"2018 Toyota Tundra TRD Pro" : "The Toyota Tundra TRD Pro is the ultimate version of the ultimate Toyota truck. It houses a powerful 5.7 L V8, making in excess of 350 HP. It also has many suspension upgrades, and like the 4Runner of the same moniker, it also has crawl control.",
"1992 Toyota Hilux Surf SSR-G Wide Body" : "The tip-top trim of the Toyota Hilux Surf. It was offroad tuned by Toyota themselves from the factory.",
"2017 Toyota Century": "The ultimate in Japanese luxury, this is the car of the Japanese Emperor. With a silky smooth and reliable 5.0 L V8 making 376 HP, this car is not a slouch. With modern retro styling remeniscent of the luxury greats of the 1960s, this is truly the ultimate in Toyota luxury.",
"2019 Toyota Corolla Hatch XSE": "The Corolla gets a hatchback in 2019, and it aims to be more than just a boring appliance. I say that it succeeded. The XSE, With its wide track, low profile tires, and distinctive handsome styling, is a car that I would actually drive for fun.",
"2019 Toyota Corolla Hatch SE": "The Corolla gets a hatchback in 2019, and it aims to be more than just a boring appliance. I say that it succeeded. Unlike the XSE, which aims to be sporty, the SE is meant to be the more mature Corolla. The no hassle, reliable commuter car that the Corolla always is. The only difference is the driving dynamics. It's actually fun to drive.",
"2019 Toyota Corolla Touring Sport": "Based on the new, fun to drive, handsome Corolla hatch, this is the station wagon we want. OF COURSE, only the Japanese get it, as always.",
"2021 Toyota GR Supra": "The Supra finally gets a successor. However... it's not really a Toyota? It uses the B58B30 straight-6 found in the M240i and the new Z4. At least it's a straight six...",
"2008 Toyota Sequoia V8": "I know a kid named Sasha who has this car. Actually, it's this one. https://4aae76bac0e998c0806f-425f2f9f94637db78b7b534fb5acbdb3.ssl.cf1.rackcdn.com/5TDBY67A48S007027/e274cdba0cdc3807cdb0deb953a114c4.jpg",
"2005 Toyota Camry LE V6": "This is a masterpiece of a consumer car with a 1MZ-FE Toyota V6 engine, famed for its smoothness and reliability. It may not exactly be fast, but it is refined.",
"1999 Toyota Corolla LE": "This is a very common vehicle. It is very nice. However, many people do not see that.",
"2002 Toyota Sienna 5D Symphony": "The Sienna Symphony is a special edition of the Sienna XLE with upgraded audio equipment.",
"2010 Toyota Camry LE": "This is the worst Camry. Not gonna exactly say that it's BAD, though.", 
"2016 Toyota Avalon Limited": "A Lexus ES with more space inside. The stereotypical car of the average senior American.",
"2018 Toyota Camry XSE": "This new Camry wants to be sporty- hence the change in naming convention from XLE to XSE. It's a Camry. Nobody wants it to be sporty. Give up Toyota.",
"2018 Toyota Corolla XLE": "There are now 2 top configurations of the Corolla sedan. This is the more refined one.",
"1969 Toyota 2000GT": "This is the world's first Japanese supercar. It's classic styling was very contemporary for the time, but it was still iconically Japanese.",
"2001 Toyota Camry LE V6": "This is the preferred car of homeless people for a reason. Comfortable, reliable, efficient, cheap to maintain, easy to maintain, and you won't get any weird stares when you are sleeping in it.",
"2006 Toyota Sienna Limited": "The wood on this car... This is basically a Lexus minivan. The wood on Toyota's luxury cars never cease being smooth. The veneer never fades.",
"2017 Toyota Sienna SE": "The JDM styling of this minivan is a testament to tuner culture in Japan, and it looks really sexy.",
"2018 Toyota Sienta": "This is a JDM mini-minivan that can seat 6 people in complete comfort somehow while taking up the same space as a compact sedan. All contained within an iconically Japanese box. Amazing.",
"2018 Toyota Alphard": "THE JDM minivan. Well... one of the 3 main ones- (The StepWGN, the Elgrand, and... this one). The Alphard is an amazingly luxurious vehicle for its size, and is best described as a luxury yacht for the road.",
"2018 Toyota Crown Majesta": "This car is comfortable, luxurious, and refined, with an interior at home in a Lexus. This car is also quite fast, rugged, and is used as the standard Japanese fleet police car.",
"2018 Toyota Tundra SR5 5.7L V8": "This truck is the Toyota truck made for the US, as a competitor to the Ford F-150 and the Chevy Silverado. However, it is still very much a Toyota, with car-like ride and handling, and unfailing reliability.",
"2018 Toyota Hiace": "This car is iconic to say the least. Copied in almost every corner of the world except the US, the Hiace is the original light utility van meant for city streets. In Japan, it also set off a type of tuner culture focused on modding these things.",
"1993 Toyota Hiace": "The 1993 Toyota Hiace was the precursor of the Alphard. You can see bits of Alphard everywhere in this car.", 
"1997 Toyota Celica GT-Four": "Tuned for a rally championship, the Celica GT-Four was a limited edition model of the ST205 Celica, and with its AWD system, it was the closest thing that Toyota had to the GT-R.",
"1998 Toyota GT-one TS020": "This is a roadgoing LMP1 car by Toyota, with a 600 HP V8. Only one was ever made. Buy it before it disappears again.",
"1993 Toyota Mark II Tourer V JZX90": "The sport model of a four door, fullsize JDM luxury car made by Toyota, often repurposed as a drift missile by tuners.",
"2018 Toyota GT86": "Overpriced new, and slow, this car is somewhat uninspiring if you are planning to drag it or race others stock. But it offers great handling DYNAMICS, which means that with an engine swap or a turbo, this thing can be a monster. This car is owned by many Vape gods, including the sister car, the SUBARU Bee-are-zed.",
"1997 Toyota Tercel": "The Tercel is a subcompact sedan/coupe made by Toyota. There is literaly nothing else to say about this car. Yeah, it's a good car, and dirt cheap, too. But that's kinda it.",
"1997 Toyota Celica GT": "The Celica GT is a basic 3 door coupe made by Toyota. There is a faster, JDM exclusive version known as the GT-Four that people actually care about.",
"2016 Toyota Land Cruiser": "The Land Cruiser. Currently a large SUV, it is used by villans and heroes, murderers and rescuers, ISIS and the UN... the name Land Cruiser is synonymous with unbreakability and unfailing reliability. It works in mountains and canyons, snow, sand, storm, and mud. It is the ultimate utility package.",
"2019 Toyota Tacoma SR5": "The Toyota Tacoma is a small pickup truck manufactured by Toyota. This one is the SR5 V6, (with a V6 instead of a 4-banger, obviously) with some power to spare.",
"2019 Toyota Tacoma TRD Pro": "The Toyota Tacoma is a small pickup truck manufactured by Toyota. This one is the TRD Pro, the tip top trim of the Tacoma, utilizing the SR5 V6's adequately powerful V6, and adding on many powerful offroad upgrades like fatter tires, new shocks, a skidplate, and even a snorkel.",
"1993 Toyota Sera": "Oh man. The Toyota Sera. The Toyota Sera was a small sports car manufactured by Toyota in the 90s. It was the car that inspired the Mclaren F1. Although it was not that fast, its innovative design spurred forward the new generation of exotic vehicles.",
"2020 Toyota Avalon Touring": "The Toyota Avalon is a large luxury sedan manufactured by Toyota. The Touring is currently the range-topping model, with features such as adaptive sports suspension and amplified exhaust system. With 301 HP under the hood thanks to the new 2GR-FKS engine, this thing is no slouch. The Touring also has an exclusive Sport+ mode, better known as the 'is this really an Avalon' mode. This is my (the developer's) car.",
"2020 Toyota Avalon Limited": "The Toyota Avalon is a large luxury sedan manufactured by Toyota. The Limited, like the Touring, is also technically a range topping model. But unlike the Touring, which focuses on the sportier side, (sportiness in an Avalon? What?) the Limited focuses on the luxury side, coming with heated and cooled real leather seats for both the front and back, real wood trim, and cushy suspension. However, with 301 hp under the hood thanks to the new 2GR-FKS engine, this car is no slouch.",
"2020 Toyota Avalon Limited Hybrid": "The Toyota Avalon is a large luxury sedan manufactured by Toyota. The Limited, like the Touring, is also technically a range topping model. But unlike the Touring, which focuses on the sportier side, (sportiness in an Avalon? What?) the Limited focuses on the luxury side, coming with heated and cooled real leather seats for both the front and back, real wood trim, and cushy suspension. This one comes with a 215 hp 4-cyl + electric motor package, making it smooth, but a bit slow compared to the rest of its brethren.",
"2020 Toyota Avalon TRD": "Do you want your Avalon to be a sports car? (no) If yes, Toyota has your back! With sports tuned suspension, big brakes, a cat-back exhaust, some lightened materials, black alloy wheels, and annoying red seatbelts, TRD has turned your humdrum Avalon into a fire-breathing machine. It's still FWD though. And there weren't any power increases. Just 301 hp. Stop looking at me like that.",
"2020 Toyota Camry LE": "It's a Camry. What? Yes.",
"2020 Toyota Camry SE Hybrid": "A Camry hybrid.",
"2011 Toyota Prius": "The Toyota Prius is a compact hatchback manufactured by Toyota, and is exclusively hybrid powered. The Prius was developed as a test bed for Toyota's Hybrid Synergy Drive, and as such was the first car that it was used on. This is a 3rd generation Prius, and one of my personal cars. (The developer's)",
"2020 Toyota Prius XLE AWD": "The Toyota Prius is a compact hatchback manufactured by Toyota, and is exclusively hybrid powered. The Prius was developed as a test bed for Toyota's Hybrid Synergy Drive, and as such was the first car that it was used on. This is a 4th generation Prius after the facelift, and comes with AWD, making it useful in snowy climates.",
"2021 Toyota GR Yaris": "Every so often Toyota, purveyor of sensible, family-friendly SUVs, minivans, and sedans, builds a car that absolutely blows you away: The 2000GT that debuted in 1965 and was intended to take on the Jaguar E-Type; the rally-inspired Celica GT-Four of the early '90s; the flawed but fabulous Lexus LFA with its screaming naturally aspirated V-10. The 2020 Toyota GR Yaris is without a doubt a member of this select group. In fact, it might be the best of the lot. You see, this little hot hatch, specifically designed and engineered to allow the Yaris to compete in the World Rally Championship, is perhaps the most focused driver's car you can buy right now this side of a Porsche 911 GT3 RS.",
"2022 Toyota GR86 Base": "The second-generation Toyota GR 86 is due for the 2022 model year, and although it's completely new, it follows the same rear-wheel-drive formula as the first-gen car. Developed again in conjunction with the Subaru BRZ, the 2022 GR 86 will be powered by a horizontally opposed four-cylinder engine and a standard six-speed manual transmission. This time around, Toyota has addressed our principal complaint with the last generation and has given the GR 86 more horsepower for 2022. The new model is powered by a 2.4-liter horizontally opposed four-cylinder engine that makes 228 horsepower, which is 23 hp more than the outgoing model's 2.0-liter mill. The base model comes with the 1st gen's old Michelin Primacies, making it a hoot to slide.",
"2022 Toyota GR86 Premium": "The second-generation Toyota GR 86 is due for the 2022 model year, and although it's completely new, it follows the same rear-wheel-drive formula as the first-gen car. Developed again in conjunction with the Subaru BRZ, the 2022 GR 86 will be powered by a horizontally opposed four-cylinder engine and a standard six-speed manual transmission. This time around, Toyota has addressed our principal complaint with the last generation and has given the GR 86 more horsepower for 2022. The new model is powered by a 2.4-liter horizontally opposed four-cylinder engine that makes 228 horsepower, which is 23 hp more than the outgoing model's 2.0-liter mill. The upgraded Premium model comes with grippier Michelin Pilot Sport 4 tires and 18 inch alloy wheels, along with leather upholstrey, aluminum pedal covers, and a rear spoiler.",
"2018 Toyota Camry SE": "It's a Camry. What? Yes.",
"2009 Lexus LFA" : "Completely redesigned three times before production because of 'imperfections' before being sold at a LOSS, the Lexus LFA is Japanese over-engineering to a 'T'. With an exhaust note precision tuned by Yamaha, an interior that looks like it came from a spaceship, and angular, iconically Japanese styling, you probably won't notice that Lexus forgot to add cupholders. Even a Chevy Spark has cupholders. I guess not even Lexus can have its perfection.",
"2007 Lexus ISF" : "The Lexus ISF was the first Lexus F Sport offering that people took seriously. It was actually surprisingly fast. However, some critisize the Lexus ISF for 'betraying the Lexus brand' because of its poor interior quality compared to other Lexuses. I agree, but I have to say, the ISF is still a blast to drive.",
"1998 Lexus GS300" : "A high quality family car with a 2JZ. You know what that means...  *wink*",
"2018 Lexus LC500" : "A superluxury supercoupe by Lexus. ...Which means it's reliable. It also handles pretty well, and its V8 sounds amazing. Does this mean that Lexus has finally reached perfection? No. Coupes aren't that practcal, unfortunately.",
"2018 Lexus LS500 AWD" : "The new Lexus LS features 'hand pleated fabric' and glass designs on its doors because Lexus feels that leather and aluminum is now too 'boring' and 'standard' I think you know what you're getting now." ,
"2019 Lexus ES300h": "The hybrid model of the all new, completely re-designed Lexus ES. The spindle grille has aged well here.",
"2018 Lexus GS F": "A sports sedan. It is fast. A good sports sedan. It has that V8 growl. A very good sports sedan. It has JDM taillights. An amazing sports sedan. It's reliable and practical. A perfect sports sedan. No... wait... it costs over 80 grand.",
"2003 Lexus LS430": "A luxury sedan for a bargain price, with a silky smooth V8 that only accepts the best fuel.",
"2019 Lexus RX350": "A luxury urban SUV. It really is quite nice.",
"1999 Lexus RX300 4WD": "A luxury urban SUV, before those were a thing. You'll be lucky to find any of these in mint condition.",
"2019 Lexus LX570": "Based on the Land Cruiser, the Lexus LX is basically the same car, but with more leather and wood. Also, it's cheaper than the Land Cruiser when it's used for some reason.",
"2022 Lexus IS500 F Sport Performance": "We often pine for bygone vehicles, wishing automakers would continue building the great ones forever. Some say you can never go back, but apparently Lexus isn't among them. With the 2022 IS500 F Sport Performance, the brand has reached into its catalog of hits and pulled out the more-than-decade-old, still-amazing 5.0-liter V-8 that debuted in the IS F (and continues on in the LC500) and created a V-8 sports sedan that rekindles a love we thought we'd lost.",
"2022 Lexus IS350 F Sport": "The 2021 Lexus IS 350 F Sport is a V6-powered small luxury sedan that has a distinct Japanese flair that helps it stand out in a crowd. The F Sport package does enough to give the IS 350 some purpose without looking gaudy or overwrought. The interior, too, features a design that you won't find on anything coming out of Germany. The design is backed by a generally fun-to-drive nature. Yes, it's slower than most rivals, but the IS 350 is pretty enjoyable on a winding road where raw horsepower is less of a factor.",
"1990 Nissan Skyline GTR R32" : "An AWD Japanese supercar, and the first Nissan Skyline GTR to be drooled upon by the American public. It was the first time the Skyline GTR was nicknamed 'Godzilla'.",
"1994 Nissan Skyline GTR R33 Spec-V" : "The successor to the R32. The engine did not get any changes, but it featured stiffer suspension, larger brakes, more refinement, and a styling update. It was also heavier.",
"1999 Nissan Skyline GTR R34": "This is the point where the Skyline GTR became a ridiculous western phenomenon. It held the world record at the Nurburgring. It was the coolest car in Gran Turismo. So, when it featured in Fast and Furious, the R34 Nissan GTR became the most drooled upon car ever made overnight. Not even the desire of the Ferrari F40 to come to American shores overshadowed the desire to own the R34. Actually, it was the other way round.",
"2002 Nissan Skyline GTR V-Spec II Nur" : "A special edition of the most drooled upon car in American history... Oh man. The world literally came to an end when the Japanese told the Americans that they couldn't have this car, either. It was revenge to the greatest degree.",
"1996 Nissan 180SX" : "The Nissan 180SX is a drift icon, known for it's balanced chasis.",
"1993 Nissan Silvia K's Type S S14" : "The Silvia. Yes. The Silvia was a car seemingly built with tuners and drifting in mind. It's a car, that today, is synonymous with the word 'drift'. Apart from obviously being popular with drifters, the Silvia was also very popular with Japanese street racers, or 'hashiriya' because of its tunability and well balanced handling.",
"2018 Nissan GTR Track Edition R35" : "The R35 GTR was Nissan's answer to the cries of hundreds of thousands of car enthusiasts that wanted a new Skyline GTR. By 2007, the Nissan Skyline GTR R34 was out of production for 5 years, with no plan of returning. Then it came. The R35 finally came to the U.S. The public was overjoyed. The new GTR was a budget supercar slayer, and people remembered why the GTR in the past was called 'Godzilla'. Oh, and you could also tune it. The new VR38DETT twin turbo V6 engine was highly tunable, although not to the level of the RB26DETT found in the R34. Everybody wanted one. Track junkies, racecar drivers, tuners, famous actors, high profile rappers, singers, just plain rich people, middle aged men, teenagers, cringy youtubers... you name it. It's now 2018, and the R35 is aging, and is on its 3rd and probably last redesign before the R36, and the hyperactive supercar slayer has now evolved into a quiet, comfortable GT car. However, it's still by no means 'slow'. It's still the fastest ticket from 0 to 10 miles per hour and back again.", 
"2007 Nissan Fairlady Z" : "Originally a concept car in the early 2000s, the Nissan Fairlady Z was the 'revival' of the car of the same name that ended production in 1978. It entered production with basically no changes to the concept car, and is a great choice for a budget sports car.",
"2018 Nissan Fairlady Z NISMO" : "The NISMO tuned variant of the 2018 Nissan Fairlady Z. It is lighter, and has stiffer suspension and more horsepower.",
"2018 Nissan Fairlady Z" : "The successor to the Z33 Fairlady Z came out in 2009. It had refreshed styling, a brand new interior, and more horsepower. It is fast, fun to drive, and relatively cool, but the engline idle noise is unbearably loud.",
"1989 Nissan 300ZX Turbo Z" : "Also known as the the Z32, the 300ZX in its base form wasn't very fast. Sure, it looked fast, but it wasn't fast, kind of like a Harley. The only seriously fast version of the 300ZX was the twin turbo version. That's this.", 
"2018 Nissan GT-R50 by Italdesign": "Overstyled and understyled at the same time... that is the way of the Italians. This Italian designed special edition GTR marks the 50th anniversary of the GTR namesake, and it goes for a cool $1000000",
"2018 Nissan GT-R NISMO": "This is the hottest R35 GTR that you can buy, with all of that OEM tuned goodness, including an excessively large but functional rear wing.",
"2018 Nissan Maxima Platinum": "The Nissan Maxima is a midsize sedan. The Platinum trim is the highest.",
"2018 Nissan Sentra SR Turbo": "The Nissan Sentra is a compact sedan. The SR Turbo is the sportiest model.",
"2017 Nissan Leaf": "The new gen Nissan Leaf is new for 2017, and it features styling at home on a normal car. Its range is also extended a very large amount.",
"1973 Nissan Skyline H/T 2000GT-R": "The Nissan Skyline 2000GT-R is the first GT-R. It's a real piece of history. Don't scratch it.",
"1987 Nissan Skyline GTSR R31": "The GT-R badge was finally revived as of the introduction of this car. There were only 600 of these made.",
"1989 Nissan Skyline GTS-4 R32": "The sedan version of the R32 Skyline.",
"1998 Nissan Skyline 25GT-X Turbo R34": "The highest end version of the R34 Skyline, with an RB25 engine.",
"1965 Nissan Silvia 1600 Coupe": "The first Silvia. It only has 89 horsepower, but nevertheless, it is still a piece of history that I think should belong in a museum.",
"1990 Nissan Silvia S13": "The S13 Silvia is the first of the really famous Silvias, used for street racing, and this radical new sport called 'drifting'.",
"1999 Nissan Silvia Spec-R S15": "The S15 Silvia is the most venerated Silvia; if not that, the most famous.",
"1995 Nissan GT-R Skyline R33 LM": "The GT-R R33 LM is a unicorn car. A one of a kind. It is the rarest Skyline ever made, with an OEM widebody and alloys.",
"1998 Nissan R390 GT1": "This is a roadgoing LMP1 car, much like the Toyota GT-one. It is powered by a 550 HP twin turbo V8.",
"1992 Nissan Cefiro 2.0 Turbo": "The Cefiro is a four door midsize sedan made by Nissan. In the US, the Cefiro was known as the Maxima. There was unfortunately no Maxima Turbo that made it to the US.",
"1990 Nissan Laurel Turbo Medalist": "The Laurel is a four door sedan made by Nissan. This particular Laurel is a Medalist, the highest trim, and has an RB20DET.",
"2017 Nissan Armada Platinum": "The Armada is a large 5 door luxury SUV made by Nissan. It features a 390 HP NA V8. This particular Armada is in the Platinum trim, which adds many luxury extras.",
"1994 Nissan Hardbody": "The Hardbody is a small truck made by Nissan. It is famous for being extremely reliable, and also for being excessively modified in the 90s in African American neighborhoods by gang leaders. They are awesome.",
"2018 Nissan Titan Platinum Reserve": "The Nissan Titan is a full-size pickup truck manufactured by Nissan. This is the second generation, coded the A61. It was originally meant to be a lightly reskinned, rebadged version of the Dodge Ram, but the plans fell through as a result of the 2008 financial crisis. The Platinum Reserve is the premium option, which comes with a decidedly opulent interior, as well as a price to match.",
"2003 Nissan Skyline GT-R R34 Z-Tune": "The Nismo Z-tune was a factory modified version of the Nissan Skyline R34 GT-R. Nismo designed a prototype Z-tune in 2002 when Nissan put an end to R34 Skyline production.  Nismo purchased 18 used R34 GT-R V·Specs, each with less than 18,000 miles on the clock, and they were completely stripped and resprayed to a ‘Z-tune Silver,’ a special color exclusively for the Z-tune. Only one car was left in its original color, 'Midnight Purple III'. For the 18 production Z-tunes, the Z1 engine was revised to allow it to reach 8000 rpm. The turbochargers were supplied by IHI in Japan. The new 'Z2' engine was advertised as making as much as 500 hp. The bodywork in the new Z-tunes were designed with new vents on the bonnet and bumpers, as well as wider arches, the same functional components as Nismo's GT500 racing cars. Nismo also added a more aggressive suspension setup from Sachs, and specially designed Brembo brakes to accompany the wider wheels supported by the new arches. The entire car was essentially handmade, with the car being completely stripped and re-built from the chassis up. Engineers reinforced and stiffened the chassis seam welding in key areas such as the door seams and door frames and added carbon fibre to the strut towers and transmission tunnel and the engine bay, completely redesigning the suspension, drivetrain, engine, gearbox and other components so as to work at maximum efficiency and reliability as is expected of a road-going vehicle. Although Nismo planned on building 20 cars, they ceased production on only 19 (including 2 prototypes). The Z-tune is often regarded as the most expensive (prices for some have been known to exceed US$290,000) street legal GT-Rs ever built. This specific Z-Tune is a prime example of a 'Z2' Z-tune, painted in the Z-tune exclusive 'Z-tune Silver'. The Z-Tune that was painted in 'Midnight Purple III' is currently nowhere to be found.",
"2015 Nissan Juke": "Much like a teenager sporting piercings and multicolored, spiked hair, the 2015 Nissan Juke seemingly shouts 'Look at me!' Though its styling may be controversial, there's no denying that this compact crossover looks like nothing else in the small car segment... I guess.",
"2021 Nissan Altima 2.0 SR": "The 2021 Nissan Altima is a four-door midsize family sedan that was completely overhauled just a couple years ago. As one of the newer choices in the segment, the Altima offers an impressive amount of cutting-edge safety features — several of which are packaged in Nissan's ProPilot Assist system. If you're looking for a little more oomph under the hood, this model, with the turbocharged 2.0-liter four-cylinder with 236 hp and 267 lb-ft on tap is your bestr bet.",
"2021 Nissan Altima 2.5 Platinum": "The 2021 Nissan Altima is a four-door midsize family sedan that was completely overhauled just a couple years ago. As one of the newer choices in the segment, the Altima offers an impressive amount of cutting-edge safety features — several of which are packaged in Nissan's ProPilot Assist system. The Altima Platinum offers the nicest interior, with nice leather upholstery, memory settings for the driver's seat, and ambient interior lighting. The Platinum trim also comes with standard AWD.",
"2022 Nissan GT-R T-Spec": "The GT-R T-Spec is the final special edition of the R35 GT-R. There are some performance upgrades from the Premium, like gold Rays wheels and carbon ceramic brakes. The real draws of the T-spec, though are its two exclusive paint colors, which pay homage to iconic past GT-Rs. The first is Millennium Jade, which last appeared on the R34 GT-R V-Spec II Nür, a coveted special edition from the early 2000s named after the Nürburgring racetrack. Of the 718 V-spec II Nür units built, just 156 of them were Millennium Jade, and the new T-spec is the first time this color is available stateside. The second color, Midnight Purple, harks back to the Midnight Purple III on the R34 V-spec, of which only 132 units were built. The color also recalls the Midnight Opal that came on a special edition GT-R in 2014 that was limited to 100 units worldwide, of which 50 came to the U.S.",
"2015 Lamborghini Veneno": "Based on the Lamborghini Aventador, the Veneno was developed to celebrate Lamborghini’s 50th anniversary. It contains the Aventador's 6.5L V12, which in this form, makes 720 HP. It retains the same chassis. When introduced, it had a price of $4,500,000, which makes it the one of the most expensive production cars in the world.",
"2003 Lamborghini Gallardo" : "2003 marked the first year of production of the best selling Lamborghini ever made, the Gallardo. Affectionately called the 'Baby Lambo', the Gallardo was a small, mid-engined V10 powered supercar. While the Gallardo did lose 2 cylinders compared to its big brother, the Murcielago, it never lost the ability to make you feel special." ,
"2007 Lamborghini Gallardo SL" : "Superlegerra means 'super light' in English. So, obviously, the Gallardo Superlegerra would just be a Gallardo with a little less weight, right? No. apart from getting a major weight diet, the Superlegerra got a large carbon fibre rear wing, stiffer suspension, new wheels, and 30 extra horsepower, not to mention all the cool extra badges.",
"2008 Lamborghini Gallardo LP560-4" : "The Gallardo had a very major mid cycle refresh in 2008, getting brand new angular looking styling, a refreshed interior, 60 extra horsepower, and all wheel drive. These changes made the new Gallardo as formidable as a track machine as the previous Superlegerra was.",
"2010 Lamborgini Gallardo LP570-4 SL ": "The Superlegerra of the mid cycle refresh was a car with the exact same changes as the previous Superlegerra, except with the new one at the base. It had a big rear wing, stiffer suspension, new wheels, but only 10 extra horsepower compared to the previous Superlegerra's 30 extra horsepower.",
"2013 Lamborghini Gallardo LP570-4 SC" : "The Squadra Corse was functionally the 'final edition' of the Gallardo, and it came after the 2013 refresh of the Lamborghini Gallardo, which added more triangles. It has the exact same engine as the Superlegerra, and also weighs the exact same amouunt, which means it's basically a newer Superlegerra.",
"2014 Lamborghini Huracan LP610-4" : "The Lamborghini Huracan is the successor to the Gallardo. It too is a small, mid-engined V10 sports car nicknamed the 'Baby Lambo'. However, over are the days of the 'Baby' being slower than the big bro. The little one now has over 600 horsepower, and can completely obliterate the Aventador on a track. But that's not really why anybody buys a Lamborghini, is it? The problem is, the Huracan just doesn't feel that special. And what's a Lamborghini without the ability to make you feel special? " ,
"2017 Lamborghini Huracan Performante" : "The Performante to the Huracan is what the Superlegerra was to the Gallardo, except much more. Although the Performante only gains 20 horsepower, it is much lighter and has far more downforce than the base Huracan, allowing you to take ay corner flat out. But, this car being a Lamborghini, none of this is very important. What is important is the car's ability to make you feel special. And the Performante does. This, to me makes the Performante package completely worth it.",
"2001 Lamborghini Murcielago" :"The Murcielago was the successor to the Diablo, and it is a wide, low, V12 supercar. This, to many, is the definition of a Lamborghini.",
"2006 Lamborghini Murcielago LP640" : "The mid-cycle refresh of the Murcielago featured a design refresh with more triangles, a new interior, and 60 more horsepower.",
"2009 Lamborghini Murcielago LP670-4 SV" :"The Super Veloce, or SV badge has been used on almost every one of Lamborghini's flagship cars with the exception of the Countach to mark the fastest one since the Miura. The LP670-4 SV has 30 more horsepower than the base, a HUGE rear wing, black accents, an option to have a huge SV decal on the side, and all wheel drive.",
"2015 Lamborghini Aventador SV" : "The ultimate version of the pre mid-refresh version of the Aventador, the successor to the Murcielago. It came with more horsepower, badges, and a cool wing.",
"2016 Lamborghini Aventador S" : "The Aventador S is the mid cycle refresh of the Aventador, and just like the mid cycle refresh of the Gallardo, it comes with even more triangles and more horsepower.",
"1971 Lamborghini Miura P400SV" : "This was the most powerful version of the Miura, Lamborghini's first supercar. The Miura had cool popup headlights. They did pop up... technically.",
"1996 Lamborghini Diablo SV" : "The Diablo was Lamborghini's flagship supercar throughout General Motors' reign over Lamborghini, and was the successor to the Countach. It is the widest car ever made, beating out even the super wide Ferrari 512TR. The SV was the most powerful version of the Diablo.",
"1985 Lamborghini Countach LP5000s QV" : "The Countach was the car on every 80's kid's poster, and for good reason. It was a flat, wide wedge, the first of its kind. It was the successor to the Miura." ,
"2020 Lamborghini Sian": "The first open-top hybrid Lamborghini super sports car to feature a supercapacitor, the Sián Roadster roars with electrified intensity, resonating with the inimitable V12 sound from the most powerful Lamborghini engine to date. Limited to only 19 examples, the Sián Roadster advances hybrid technology with the world’s first use of a supercapacitor in a materials-science application unique to the industry.", 
"2021 Lamborghini Urus": "What's the issue with something like an Aventador or Huracan? Only one person can come along for a joyride, obviously. But there is a solution: Lamborghini's Urus, which is the brand's new-ish SUV. Just don't let a lifted ride height, all-wheel drive and seating for five confuse things: The 2021 Urus is a Lamborghini first and foremost.",
"2021 Lamborghini Huracan Evo": "The Huracan Evo is the latest iteration of the 'entry-level' Italian supercar. For the Evo, Lamborghini started with the dynamic improvements it developed for the Huracan Performante and slightly updated the styling. This includes new front and rear bumper designs and a relocated exhaust and rear spoiler. The goal is a more aggressive design with improved aerodynamic efficiency.",  
"1995 Lamborghini Diablo SE30 Jota": "At 600hp, the Diablo SE30 JOTA remains the most powerful Diablo variant ever produced. The JOTA upgrade kit was created by Lamborghini for VIP clients who wished to go GT racing in the FIA BPR GT Series, competing against the Mclaren F1 GTR, Ferrari F40 GTE, and Porsche 911 GT2. The JOTA was designed for the already raw, race inspired Diablo SE30 to produce more power. Developed by Lamborghini Engineering, the former Lamborghini F1 division, less than 30 kits were produced for the world.", 
"2000 Lamborghini Diablo GTR": "After campaigning the Diablo SV-R for four years in the Diablo Supertrophy, Lamborghini launched a completely new car for the 2000 season. Just as the SV-R was a race-ready SV, the Diablo GTR, introduced at the 1999 Bologna Motor Show, converted the Diablo GT to a track oriented car with power improvements, a stripped interior, and weight reduction. he GTR interior was stripped down to save weight; the air conditioning, stereo, and sound and heatproofing were removed, and a single racing seat with 6-point seatbelt harness, MOMO fire suppression system and steering wheel, complete integrated roll cage, fixed Plexiglass windows with sliding sections, and fresh air intake were fitted. The GT had already featured a radically styled body, but the GTR took this a little further with features such as a very large rear spoiler bolted directly to the chassis like a true race car, 18 inch hollow magnesium Speedline centerlock wheels, pneumatic air jacks for raising the car in the pit lane (like the SV-R, it was too low for a rolling jack), and an emergency fuel shutoff switch on the left front fender. Thirty cars were initially planned to be produced but actual production amounted to 40 units, and 40 chassis were prepared to replace cars wrecked in racing accidents. In the hands of multiple Australian Drivers' Champion Paul Stokell, a Diablo GTR run by Team Lamborghini Australia won the 2003 and 2004 Australian Nations Cup Championships.", 
"2017 Bentley Continental GT" : "Bentley's only 2 door coupe, the Continental GT is a leather clad rocket with an unconventional turbocharged W12 engine.",
"2015 Bentley Bentayga" : "Just like every other luxury car brand, Bentley has made an SUV. It's one of the rare cases of the concept car looking worse than the production car. Yes, the Bentayga is ugly, but the concept was REALLY ugly. Look it up.",
"2015 Koenigsegg Regera" : "The Koenigsegg Regera is the successor to the Agera, and is a mid engined dry sumped turbo V8 hybrid hypercar with over 1000 horsepower. The motors have over 600 HP alone. Also, this car, because of the frankly ridiculous torque output, the Regera has only 1 gear.",
"2010 Koenigsegg Agera" : "The Koenigsegg Agera is the successor to the CCX, and is a mid engined drysumped twin turbo V8 hypercar with over 800 horsepower. Like every other Koenigsegg model, Ageras are custom built.",
"2007 Koenigsegg CCX" : "The Koenigsegg CCX is the successor to the CCR, and is a mid engined drysumped supercharged V8 hypercar. The CCX is unique in the aspect that it is the only Koenigsegg street legal in the United States, and is powered by alcohol. Koenigsegg seems to have made a drunkard.",
"2005 Bugatti Veyron 16.4" : "The Bugatti Veyron is a dry sumped 1000 HP mid engined quad-turbo 8L W16 all wheel drive hypercar, and was the fastest production car in the world for some time.",
"2016 Bugatti Chiron" : "The Bugatti Chiron is the successor to the Veyron, and is a 1500 HP mid engined quad turbo 8L W16 all wheel drive hypercar. The carbon fibers on the hood meet at a perfect 45 degree angle.",
"2017 Porsche 911 GT2 RS" : "The 911 GT2 RS is the current fastest Porsche in production. It is the cover car of the video game Forza Motorsport 7.",
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : "A really, really, really, really fast station wagon. Those are always pretty cool.",
"2016 Porsche 911 Turbo" : "The 911 is still rear engined. No wonder people call it a Beetle. Well, 911s are fast though.",
"2016 Porsche 718 Boxster" : "The Boxster is the entry level Porsche, and is a convertible. It's called the boxster because of its turbo flat-4 boxer engine.",
"2017 Porsche 718 Cayman GTS" : "The Cayman is the entry level Porsche for those who are actually car people. Otherwise, its the car you just don't buy. This is the only Porsche I actually respect. It is a mid-engined turbo flat-4 sports car.",
"1975 Porsche 911 Turbo" : "This is a classic car easily identifiable from other, lesser Porsches of its era by it's vented ducktail rear wing.",
"1995 Porsche 911 GT2" : "Literally worth nearly a million dollars, only 1,100 of these were produced by Porsche.",
"1987 Porsche 959" : "The 959 was the fastest car in the world before the Ferrari F40 was. It was made as a rally homologation car.",
"1999 Porsche 911 GT3" : "It's a generic looking Porsche that I don't really know much about.",
"1980 Porsche 924 Turbo": "The 924 Turbo is a 2 door fastback style sports car that was made by Porsche. The turbo version was made to bridge the gap between the entry level 924 and the more expensive 911. Although earlier models had reliability issues, by 1980, Porsche had sorted it out.",
"2015 Lotus Evora 400" : "You know that obnoxious announcer for those car shows? He has one of these. It's a mid engined sports car by Lotus that had the same engine as a Toyota Corolla.",
"2011 Lotus Exige S" : "The Lotus Exige is basically a serious, non-midlife-crisis version of the Elise.",
"1996 Lotus Esprit V8" : "The Esprit V8 is the only real 'supercar' that Lotus has ever made. It still had balanced handling, so was still a Lotus.",
"2006 Lotus Elise S" : "Basically the midlife crisis vehicle. Might not be quick in a straight line, but completely destroys larger cars in the cornes.",
"2018 Mazda Miata MX-5 Club" : "The new Mazda MX-5 was able to conduct weight reduction through the use of something Mazda called the '1-gram policy'. Engineers were tasked to shave off 1 gram off of every single part of the MX-5. It worked. Many say that this MX-5 has finally captured the soul that made the first MX-5 so special.",
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : "Mazdaspeed is Mazda's in-house tuning suite. They transformed the fun loving MX-5 into a track machine.",
"1989 Mazda MX-5 Miata" : "The original MX-5 is now considered by almost all car enthusiasts as a timeless classic. It isn't fast in a straight line, in fact, that's the point; the small amount of power makes for a thrilling driving experience in the corners. There are now MX-5 only racing divisions that exist in almost every country that this car was exported to.",
"1989 Mazda RX-7 Savanna Turbo" : "The RX-7 Savanna was the first RX-7 that was actually taken seriously by the American public. It wasn't much of a sports car, and more of a grand tourer. Kind of like a smaller, rotary engined Toyota Soarer.",
"1992 Mazda RX-7" : "The 3rd generation RX-7 was more similar to the 1st than the 2nd, as it was a pure-blooded sports car rather than a grand tourer. Nicknamed by many magazines as 'The Racecar For The Road', (even Playboy reviewed it) the 3rd generation RX-7 outperformed almost everything else on the road at the time. However, the RX-7 was infamous for it's terrible reliability and sky-high repair costs.",
"1998 Mazda RX-7 RZ" : "Special edition of the third gen RX-7. The 3rd generation RX-7 was more similar to the 1st than the 2nd, as it was a pure-blooded sports car rather than a grand tourer. Nicknamed by many magazines as 'The Racecar For The Road', (even Playboy reviewed it) the 3rd generation RX-7 outperformed almost everything else on the road at the time. However, the RX-7 was infamous for it's terrible reliability and sky-high repair costs.",
"2009 Mazda RX-8" : "The successor to the RX-7, the RX-8 is a rotary 4-door sports car. It is very similar to the 2nd gen RX-7, in it being a GT car. I know that that obnoxious announcer for those car shows has one of these.",
"2019 Mazda6 Signature": "The Mazda6 is a sedan manufactured by Mazda. Mazda tries to invoke emotion within this car, and I feel like it kind of did work. With its handsome styling, its upscale interior, and most importantly its fun driving dynamics, the Mazda6 actually feels like a unique experience.",
"2019 Mazda3 Hatch": "The Mazda3 is a compact sedan/hatchback manufactured by Mazda. 2019 sees a much awaited redesign of the Mazda 3, with futuristic styling that is quintessentially Mazda, and a more active chassis and engine. Unfortunately, it seems that you can barely see out of the back window of the hatch. What we have here is the hatch, which is slightly more expensive than the sedan.",
"2019 Mazda CX-5": "The Mazda CX-5 is a compact crossover manufactured by Mazda, and is the top rated crossover on pretty much every car magazine ever, because of its comparatively upscale interior and it's 'fun' driving dynamics.",
"2019 Mazda CX-3": "The Mazda CX-3 is a subcompact crossover manufactured by Mazda. You see these things every once in a while.",
"2014 Mazda2": "The Mazda2 is a subcompact hatchback manufactured by Mazda that was discontinued in the USDM market in 2015. It is based on the Toyota Yaris.",
"2015 Mazda5": "The Mazda5 is a MPV manufactured by Mazda. The car is quite similar to the JDM exclusive Honda Freed/Spike and the Toyota Sienta, which are both amazingly practical boxes.",
"2006 Mazdaspeed 6 GT": "The Mazdaspeed 6 is a sports sedan manufactured by Mazda. It is a great sleeper, as it doesn't have a huge wing like its primary competition, the Evo and the STi. It's also a bit slower though. Overall, it is a very good choice for a understated sports car for the understated professional that doesn't want to look like too much of an idiot in front of his wife and kids.",
"2013 Mazdaspeed 3": "The Mazdaspeed 3 is a hot hatchback manufactured by Mazda. It is a great daily driver, as it is both very practical, relatively comfortable, gets good gas mileage, and it is also quite fun to drive on a track.",
"2001 Mazda RX-7 Spirit R Type A" : "Special edition of the third gen RX-7. The Spirit R is the final edition of the FD RX-7, and it is currently extremely expensive. The 3rd generation RX-7 was more similar to the 1st than the 2nd, as it was a pure-blooded sports car rather than a grand tourer. Nicknamed by many magazines as 'The Racecar For The Road', (even Playboy reviewed it) the 3rd generation RX-7 outperformed almost everything else on the road at the time. However, the RX-7 was infamous for it's terrible reliability and sky-high repair costs.",
"2018 Morgan Three-Wheeler" : "It's made of wood, has like 60 horsepower and only 3 wheels.",
"1998 Subaru Impreza 22B STi": "The coolest Subaru ever made. It's an Imprezza that is a coupe. Apparently, a lot of others think so too, as the 22B to this day still keeps its astronomical price.",
"1995 Subaru Impreza WRX STi Version II": "It's not exactly ICONIC, but it's still an Imprezza STi. You can get one of these for a bargain price.",
"2002 Subaru Impreza WRX STi": "This WRX STi was known as the bugeye STi. Once you see it, you will know why. This one... is iconic.",
"2003 Subaru Impreza WRX STi": "This STi is an extremely iconic car, because of its numerous appearances in rally.",
"2005 Subaru Impreza WRX STi": "It's an STi sedan with a turbo flat 4 boxer and all wheel drive. Just like all the others before it.",
"2010 Subaru Impreza WRX STi R205": "The R205 edition of the hatch STi has retuned suspension and dampers, a new ball bearing turbo, and an exhaust system that creates less backpressure for a final 316 horsepower from the 2 litre flat 4 boxer engine. It is of course JDM exclusive, and only 400 of these exist.",
"2019 Subaru WRX STi": "The 2019 Subaru WRX STi is, according to Subaru, their fastest STi yet. It also has a redesigned interior that looks nicer than the German 'luxury' cars, so there.",
"1993 Subaru SVX": "The SVX is a 2 door coupe that was manufactured by Subaru. This example features the optional turbo V6, widely regarded as one of the best sounding V6s ever made.",
"2000 Subaru Forester STI": "The Forester was a wagon made by Subaru. The STI version, with the US spec WRX STi's flat four under the hood, STi Sport springs, revised struts at each corner, and beefier anti-roll bars to handle the upgraded engine, the Forester STI is an amalgamation between utility and sport that shouldn't exist, but one that I'm glad exists anyway.",
"2019 Subaru WRX": "The 2019 Subaru WRX might be one of the quickest and most powerful sport compacts available for less than $30,000, but it's also one of the least civil. A loud cabin, a stiff-legged ride, and a laggy turbocharged engine are some of the Subaru's surlier traits—a legacy of its rally-car roots. Its infotainment system is antiquated, and its interior is drab. Still, if you're willing to sacrifice comfort and convenience, you will be enthused with the model's standard all-wheel-drive system, quick and well-weighted steering, and strong brakes. There are less powerful alternatives that strike a better balance between engaging dynamics and everyday refinement, but few are more fun on a twisty mountain road—whether that road is paved or not.",
"2022 Subaru WRX": "Rally-inspired sport compact cars are on the verge of extinction, but the new 2022 Subaru WRX aims to reignite interest for this enthusiast-focused breed. With the adoption of a new architecture aimed at better driving dynamics as well as the addition of more powerful 271-hp turbocharged flat-four engine, the new WRX promises to be an improvement over the outgoing version.",
"2018 Subaru BRZ": "Beloved by young driving enthusiasts looking for affordable thrills, the 2018 Subaru BRZ is a small, lightweight sports coupe with rear-wheel drive, a manual transmission and over 200 horsepower. It’s the only Subaru that isn’t all-wheel drive, and remains one of the least expensive ways for performance enthusiasts to have fun on a budget. It’s powered by a 2.0-liter version of Subaru’s flat, horizontally opposed 4-cylinder engine, a unique design that helps lower the coupe’s center of gravity and improve its handling. The Subaru BRZ competes with the Mazda Miata and mechanically and visually similar Toyota 86, but unlike the 2-seat Miata roadster, the BRZ is offered only as a closed coupe and it offers a small back seat.",
"2022 Subaru BRZ Premium": "The second-generation Subaru BRZ is due for the 2022 model year, and although it's completely new, it follows the same rear-wheel-drive formula as the first-gen car. Developed again in conjunction with the Toyota 86, the 2022 BRZ will be powered by a horizontally opposed four-cylinder engine and a standard six-speed manual transmission. This time around, Subaru has addressed our principal complaint with the last generation and has given the BRZ more horsepower for 2022. The new model is powered by a 2.4-liter horizontally opposed four-cylinder engine that makes 228 horsepower, which is 23 hp more than the outgoing model's 2.0-liter mill. The base Premium model comes with the 1st gen's old Michelin Primacies, making it a hoot to slide.",
"2022 Subaru BRZ Limited": "The second-generation Subaru BRZ is due for the 2022 model year, and although it's completely new, it follows the same rear-wheel-drive formula as the first-gen car. Developed again in conjunction with the Toyota 86, the 2022 BRZ will be powered by a horizontally opposed four-cylinder engine and a standard six-speed manual transmission. This time around, Subaru has addressed our principal complaint with the last generation and has given the BRZ more horsepower for 2022. The new model is powered by a 2.4-liter horizontally opposed four-cylinder engine that makes 228 horsepower, which is 23 hp more than the outgoing model's 2.0-liter mill. The upgraded Limited model comes with grippier Michelin Pilot Sport 4 tires and 18 inch alloy wheels, along with leather upholstrey, aluminum pedal covers, and a rear spoiler.",
"1988 Isuzu Impulse": "A sports car made by... Isuzu wtf",
"1979 Isuzu 117 Coupe": "The Isuzu 117 is a very underrated, very pretty car.",
"1994 Mitsubishi Lancer Evo II": "The Evo II was immensely popular with 'hashiriya', or Japanese street racers, because it was tunable, easy to drive, and adaptable.",
"2010 Mitsubishi Lancer Evo X GSR": "The X is everybody's least favorite Evo, and was the last gen made. Unfortunate.",
"1999 Mitsubishi Lancer Evo VI GSR": "The VI was the generation, in my opinion, where the Evo came into its prime. The VI is one of the most iconic Evos to date.",
"2004 Mitsubishi Lancer Evo VIII MR FQ400": "The FQ400 is really fast. REALLY FAST. SUPERCAR FAST. It was an AWD turbocharged monster sedan with over 400 horsepower. Ironically, it was the fastest Evo ever made that reminded you most of the Evo's true nature. Today’s factory tuned small cars like say, a Focus RS or a Civic Type R look like they were engineered from the ground up as true performance machines, with their performance baked into their original design. The Evo FQ400, on the other hand, looks like an average Lancer shitbox with a full battalion of branded performance parts glued on. It isn’t really a pretty car. But let me remind you. it's fast.",
"2003 Mitsubishi Lancer Evo VIII GSR": "The normal edition of the Evo VIII, with a turbo straight four. Refer to the FQ400's description for more info on this car.",
"1994 Mitsubishi 3000 GT VR-4": "The 3000GT VR-4 was a 2 door coupe made by Mitsubishi. With AWD, four wheel steering, and over 300 horsepower, it was truly ahead of it's time.",
"1994 Mitsubishi FTO GPX": "The Mitsubishi FTO was a 2 door coupe made by Mitsubishi. It had front wheel drive, and was nicknamed the FTSlow, because the only slightly fast one was the top of the line GPX. Oh. That's what we have here.",
"1992 Mitsubishi Galant VR-4": "The Galant VR-4 is a four door sports sedan manufactured by Mitsubishi. Unlike its Lancer counterpart, the Evo, it doesn't have that much fame per say in worldwide car culture, but is a cool car nevertheless. It is equipped with a 2.0L I4 turbo.",
"1974 VAZ Lada 1200":"You know bratan. I think it is time. Bring out the iron cheburek. AvtoVAZ - eto klass! Uamee, Professional Gopnik, Boris - Let's go! Davai! Strong steel box, on 4 wheel In rajon I'm making deal Fast steel box, on 4 wheel Knock the spies back on heel Run on vodka, never slow Russian motor never blow Seeking out the western spy I not quit but still they try (I not quit but still they try) Western spy have much to fear When I switch in 2nd gear Silent night, no one around My tire tracks is all they found (tire tracks is all they found) (all they found) Dump the bodies, drive away Militsiya is on its way My Lada now is in gear 5 Lets go pizdec, long way to drive Opa! Avto AvtoVAZ Lada AvtoVAZ Моя машина - это класс! On the highway still gear 5 Thanking god, I'm still alive Militsiya is cracking down Two hours pass, they here in town Now three days, still no rest Where I'm going? East or west? I have lost orientation This a house or police station? (police station) In eastern bloc it always rain Drive my Lada down the drain Coming close you feel the pain I hit you like a subway train Slavic life, now flying high Get the ladies every time Slavic life, now all is real Lada closing every deal Stomp the spies further west Heel or toe, this is your test Ushankas on, Makarovs out In the street you hear my shout. https://www.youtube.com/watch?v=4xei2-cW9eo", 
"1975 UAZ-469":"Live out your PUBG fantasies in this Russian Jeep.",
"1965 GAZ Volga 21":"Buy this for Alexei Kosygin Simulator 1965.",
"1995 Hyundai Sonata 2.0i": "This car was made before Hyundai was actually a respectable car company. Please buy it for scrap metal.",
"2013 Hyundai Genesis Coupe 3.8" : "A sports coupe made by Hyundai. Thuroughly forgettable, but surprisingly quick.",
"2013 Hyundai Elantra GT": "A regular, unassuming, but quality hatchback. A car that finally made the Hyundai brand more than just a copycat.",
"2017 Hyundai Sonata Limited": "A comfortable sedan from Hyundai. Hyundai seems to be continuing to make quality vehicles.",
"2005 Hyundai Tiburon GT V6": "A rudimentary sports car that was made by Hyundai in the early 2000s.",
"2018 Kia Stinger GT": "Kia's first serious sports car. It features muscular styling and a decent amount of speed for the price. The interior is also quite nice. The GT comes with a V6 turbo, while the base comes with a turbo four.",
"2017 Kia Optima SX 2.0T": "Basically Kia's take on the Accord Sport. They did a decent job doing it, and the styling is distinctively handsome.",
"2006 Audi R8":"The 1st generation Audi R8. Has a naturally aspirated 4.2 L V8.",
"2008 Audi R8 V10":"The mid-cycle refreshed Audi R8. Looks exactly like before, but with additional wheel options and a new engine option (the V8 was still sold). The V10 in this car was taken from the then current Lamborghini Gallardo.",
"2010 Audi R8 GT": "An Audi R8 V10 with a bunch of aero bits, some weight reduction, uncomfortable racing seats, and a power boost.",
"2012 Audi R8 Plus": "The end cycle refresh of the Audi R8. Has a power boost and redesigned lights.",
"2015 Audi R8 Coupe 5.2 FSI quattro": "The 2nd generation R8 has a completely redesigned body and interior, and the V10 from the Huracan.", 
"1994 Audi RS2 Avant": "This station wagon, back in the early 1990s, outperformed basically everything else on the road both in speed and practicality. It subsequently became a renowned classic." ,
"2018 Audi RS5": "The new Audi RS5 is a coupe filled with the latest tech, extremely agressive styling, and a 444 HP 2.9 liter twin turbocharged V6, replacing the previous generation's growling naturally aspirated V8. This in turn made the new RS5 not as fun as its predecessor, certainly not fun enough to justify its styling cues." ,
"2018 Audi RS3": "This car was described by Car and Driver as 'a tiny mouse with the heart of a lion'. With its 400 HP turbo five in a car this tiny, they aren't lying. But still, what a big price for such a small car.",
"2018 Audi RS7": "This car is very fast. Really fast. It's also very practical with its ridiculous amount of cargo capacity, and the styling is great. However, for a sports sedan for six figures, the RS7 rides like a pile of overly serious German boulders, and the steering feels as devoid of feeling as those same boulders. So, I guess you could describe the RS7 as the fastest boring German boulder in the world?" ,
"2018 Audi RS6 Avant": "Ah, an Audi RS6. By definition a car interesting enough to set the Autocar-to-Mira test track hotline ringing, but not the unknown quantity (of interesting) it once was. -A quote from Autocar magazine. I think it summarizes this car quite nicely.",
"2018 Audi TTRS": "The only TT that you can take seriously, the TTRS has a hyperactive turbo five that makes 400 HP, and that is put down onto the asphalt with Audi's signature Quattro AWD system." ,
"2018 Mercedes-AMG E63 S 4Matic": "Equipped with a 603 HP twin turbo V8 engine, the E63 AMG is a very quick car with a 0-60 mph time of a mere 3.0 seconds, and a AWD system that allows the sedan to corner like a supercar. It's main downfalls are its ridiculous price, and its extremely uncomfortable performance seats.",
"2018 Mercedes-Maybach S560":"Looks like an S-Class, doesn't it? Look at the badge on the C pillar. It is an S-Class, yes, but at the same time... it isn't. It has folding tray tables in the back, a refridgerator box, and it comes with hand-crafted champagne flutes.  Entertainment screens attached to the front seatbacks are standard and offer rear passengers their own set of infotainment controls as well as individual sets of wireless headphones. Even with all this equipment, the S560 is able to circle a skidpad at 0.91 g of grip, and accelerate to 60 mph in 4.7 seconds with its 463 HP 4.0 L twin-turbo V8. All of this might sound great. Now look at the price. Tell me it's great now. Can you?",
"2018 Mercedes-AMG S65 Sedan": "This AMG Mercedes costs $240,000. That's the point. This 12 cylinder S-Class is the most expensive S-Class to date, even more expensive than the V12 version of the ultra-luxury Maybach S650.",
"1990 Mercedes-Benz 190E Evolution II": "A cosworth tuned naturally aspirated straight-4 touring car classic with a low ride height and a huge rear wing.",
"2016 Mercedes-AMG GT S": "Mercedes-AMG's new halo car, while losing horsepower, does not lose any performance. While the car on paper is virtually identical to the SLS on paper in terms of top speed, braking force, and grip, the SLS and the GT S are two completely different cars. The GT S definitely delivers more of a serious personality when driving. The SLS is just a hooligan." ,
"2013 Mercedes-Benz SLS AMG GT": "Everything from this car's oversized 6.2 L V8 and the badges flaunting it, its all-too-numerous vents, its unneccesarily long pinnochio nose, its complete disregard for noise restrictions, and those stupid gullwing doors mark this car as the car of a true idiot. We all love this car. To some, it's the only German car worth owning.",
"2012 Mercedes-Benz C63 AMG Black Series": "You thought the SLS was stupid? Look at this. The C63 AMG Black Series looks like a race car with it's carbon fiber front canards and unneccesarily huge wing. LOOKS LIKE. You're right. The C63 AMG Black Series drives like the aero equipment creates lift instead of downforce. The race car looks? BS.('B'lack 'S'eries, get it lol) That makes the C63 AMG Black Series as much of a complete hooligan as the SLS. I absolutely love that. In my opinion, the C63 Black Series is exactly what an AMG Mercedes should be.",
"2000 Mercedes-Benz C32 AMG": "The C32 AMG is a four door sedan manufactured by Mercedes-Benz. It has a supercharged (not turbocharged) V6 for better throttle response. It is very subtle in its styling, and it is quite difficult to distinguish from the regular C320, which is something I like. I probably wouldn't buy one personally because of reliability issues and subsequent maintainance costs, but it is for no reason an awful car to drive.",
"2020 Mercedes-AMG A35 4Matic": "The A35 is the performance version of Mercedes-Benz's compact A-Class. It's a ball of perennial energy that basically never rests. There's no off switch. It's batshit crazy.",
"2020 Chevy Corvette C8 Stingray Z51": "The new Corvette C8 is the Ferrari-fighting mid engined homegrown exotic budget warrior that we've all been waiting for. With the Z51 Performance Package, (which this car has), the base version of the C8 literally eats other cars alive.",
"2019 Chevy Corvette C7 ZR1": "The hottest version of the Corvette, new for 2019, with an even more boosted engine making in excess of 700 horsepower, a huge rear wing that looks more at home on a C7R, and carbon canards ripped straight off the Camaro ZL1.",
"2018 Chevy Corvette C7 ZO6": "A hotter version of the C7 Stingray. Looks best in yellow.",
"2018 Chevy Corvette C7 Stingray": "When the C7 Stingray came out, the Europeans were amazed that Americans were able to design and make a sportscar on par with a European one. As if they hadn't already been doing that, that is...",
"1953 Chevy Corvette": "The original Corvette almost got canned from the beginning. Nobody liked it. Nobody liked this car. The reason? Well, you may know that current Corvettes all have V8s... but the Corvette started life in 1956 with a V6 making a slightly puny 150 horsepower. Luckily for the little sports car, GM got the idea that they were making a mistake, and decided to put a V8 in the car instead. It was a smash hit. Now, these V6 Corvettes sell for upwards of $600,000 on auction.",
"1960 Chevy Corvette C1": "In 1960, the Corvette got a redesign, getting rid of the fins. It is still considered 1st generation, as little changed underneath.",
"1963 Chevy Corvette C2 Stingray 427": "The C2 Corvette Stingray was America's Ferrari. It made over 300 horsepower, which was frankly amazing at the time, and featured a clean, redesigned body with pop-up headlights. Looks best in blue.",
"1967 Chevy Corvette C3 327": "Nicknamed 'Mako Shark', the 3rd generation Corvettewas slower than the 2nd gen Corvette. Chevy had something up their sleeve.",
"1970 Chevy Corvette C3 454": "The hottest version of the 'Mako Shark' Corvette was the 454, making an amazing 460 horsepower! Unfortunately, 1971 was when the US emissions regulations were implemented, and they hit hard. The power output of the C3 halved the next year. This detrimental cycle continued, as GM, Ford, and other American car companies either went bankrupt, or reduced in quality. On the bright side, 1971 marked the year that Japanese cars started their takeover of the States.",
"1984 Chevy Corvette C4": "Much slower than the previous generation Corvette, the C4 was a car much affected by emissions regulations.",
"1988 Chevy Corvette C4 ZR1": "The ZR1 was a cool American car in the age of terribly uncool American cars. By 1988, the quality of American cars had all but disintegrated. (no, literally they would disintegrate)",
"2001 Chevy Corvette C5": "The C5 was the last Corvette to have pop-up headlights, and marked the end of Corvettes prioritizing form over function. Now, the base model had 350 horsepower.",
"2002 Chevy Corvette C5 Z06": "The C5 Z06 was the hot version of the C5 Corvette, and marked the first time that the label 'Z06' had appeared on a production car. Chevy did use the label 'Z06' on some of its racecars, however. But most of those were burned to the ground, literally, when GM decided it didn't like racing anymore.",
"2007 Chevy Corvette C6": "The C6 Corvette. A car with nothing to talk about. Yes, it has more horsepower. It also has no popup headlights. *yawn*",
"2007 Chevy Corvette C6 Z06": "The Corvette C6 Z06 was the first Corvette to ever be reviewed positively on the famous show 'Top Gear'. One of the reasons might be the fact that it has 505 horsepower. The fact that it has 505 horsepower also might be a reason that GM went bankrupt in 2009." ,
"2007 Chevy Corvette C6 ZR1": "Reviewed favorably on basically every form of motoring media there was, (apart from interior quality) the Corvette ZR1 made in excess of 600 horsepower, making the thing a literal beast. But, every silver lining has a dark cloud. The ZR1 might be one of the reasons for GM's bankruptcy in 2009.",
"2018 Chevy Camaro 1LE": "The 1LE is the lesser track package that is available for the Camaro. Unlike some 'sport' packages, the 1LE package makes the Camaro legitimately fast.",
"2018 Chevy Camaro ZL1": "The ZL1 is the hottest Camaro available today, and comes complete with carbon fiber canards, each the size of your foot. The ZL1 package makes your Camaro into a literal supercar without the price that usually comes of one. But, like on almost all American performance cars, it is easy to see where they cut costs.",
"1969 Chevy Camaro SS 396": "An iconic muscle car, with headlights that turn on in the most satisfying way. Look it up.",
"2017 Chevy Malibu 1.5 Turbo": "A shitbox by Chevy. Yay.",
"2016 Chevy Malibu 2LT": "A slightly faster version of a shitbox. Yay?",
"2017 Chevy Cruze Hatch Premier": "They call it the 'premier'. I call it the 'i don't know i guess it depends on your intelligence whether you think it should be called the premier'. I like my version better. Short and concise.",
"2016 Chevy Impala LT": "A fullsize sedan that comes with wifi. Great. Now I can watch my Youtube videos in the car. Not that I didn't already have cellular data that lets me do the exact same thing.",
"2018 Alfa Romeo 4C": "A honestly quite good track car by Alfa Romeo. I have to say, Alfa's been getting back on track recently.",
"2018 Alfa Romeo Giulia Quadrifoglio": "The most fun sports sedan available today. Not gonna say it's reliable, not gonna say it's cheap, not gonna say it has good build quality, but it's just a fun car. On an Alfa Romeo, the annoyances are all part of the charm of the car. And this car definitely feels like an Alfa Romeo. The rear doors are too short, there isn't enough legroom, some of the plastic bits seem a bit 'iffy', the steering wheel is too close to your chest... the list goes on and on. But if you didn't expect that when buying an Alfa, what are you even doing?",
"2018 Alfa Romeo Stelvio Quadrifoglio": "An Alfa Romeo crossover to join all the sports crossovers on the market, namely the Lamborghini Urus and the Porsche Macan.",
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": "Even as a dealer, I suggest you don't but this car. Even for an Alfa, it's just TOO janky.",
"2013 Alfa Romeo MiTo 1.4 8v": "Not an Alfa. Named like an Alfa, but not an Alfa.",
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": "A fun little sports sedan. Also a bit weird and quirky. And a bit janky. But it's an Alfa.",
"2006 Alfa Romeo 8c Competizione": "Makes a godly V8 noise, and looks great on paper, and is really handsome. Then you remember that it's an Alfa Romeo. There has to be something wrong with it. And there is. It handles like the suspension is made of teabags glued together.",
"1992 Alfa Romeo 155 Q4": "A classic Alfa that has all wheel drive. We all know what went wrong with it.",
"1985 Alfa Romeo Spider Veloce": "What, it's an Alfa Romeo Spider. Like the Fiat Spider but better, because it's an Alfa and not a Fiat.",
"2017 Suzuki Swift Sport": "A playful little hatch, with an engine code that literally reads 'K14C DITC 1.4 BOOSTERJET'. Fun.",
"2016 Suzuki Alto Works": "A Kei car that isn't as fast as it looks, but feels as fast as it looks. A fun little car, good to add to your collection. If it was a person, it would be that one little kid running around the park making car noises.",
"2016 Suzuki Hustler G 4WD": "A cute little kei car with an equally cute name. Has character.",
"2003 Suzuki Liana 1.6 Sedan": "A shitbox that happened to be featured on Top Gear as the 'Reasonably Priced Car', and was still used at the end of the original BBC series for F1 drivers.",
"1995 Suzuki Samurai 1.3i": "sUzUKi SaMuRAi!!!!1!1!!1!!!!!!1!!! No seriously. Get this car. It's a really cool tiny little offroader that is just as cute as it is capable. One thing Suzuki does well with cars is character. All of its cars have some sort of character, some more than others. And the Samurai definitely has a lot of character.",
"2002 Suzuki Grand Vitara": "The Grand Vitara. It's basically that one old man that shows up to your party regardless of how many people you invite. You never really wanted it, but you cater for it anyways. The Grand Vitara is a boring looking SUV that somehow has a sort of... character.",
"2018 Pagani Huayra BC": "This is a special limited edition of the already special limited edition Huayra. There are only 20 of these in the world. Buy it before it's gone.",
"2013 Pagani Huayra": "With a ludicrously powerful AMG-sourced V12 making over 700 horsepower in a body lighter than the one of a Toyota Corolla, you know this car is going to be a trip when you step inside it. But the interior of this car is more at home in a 5 star hotel than a racecar. I guess it's going to be a nice, albeit short trip.",
"2010 Pagani Zonda Cinque": "The Pagani Zonda Cinque is called the Cinque because there are only 5 in existance. With its characteristic carbon aero bits and its red accents, its pretty easy to recognize.",
"2005 Pagani Zonda F": "The AMG-sourced V12 gets an upgrade in the Zonda F. It's insane.",
"1999 Pagani Zonda C12S": "The Zonda C12 debuted in 1999 at the Geneva Motor Show. It was powered by a 6.0 L Mercedes-Benz V12 engine producing 460 PS at 5200 rpm and 640 Nm at 4200 rpm mated to a 5-speed manual transmission gearbox. Like you even care about all of that stuff when you buy this car. It's the feeling, it's that for everybody. And this thing? It definitely provides.",
"1970 AMC AMX": "The AMX is a 2 seat muscle car made by AMC. The AMX name is from the 'American Motors experimental' code used on a concept vehicle and then on two prototypes shown on the company's 'Project IV' automobile show tour in 1966. Kinda sounds like the NSX, doesn't it.",
"1972 AMC Javelin": "The AMC Javelin was a 'Murican front-engine, rear-wheel-drive, two-door hardtop manufactured and marketed by AMC.",
"1969 AMC Ambassador": "The Ambassador was the top-of-the-line automobile produced by AMC from 1958 until 1974. In 1969, the Ambassador received a major restyling, with a 4-inch gain in overall length and wheelbase. The front end appearance was revised with new quad headlight clusters mounted horizontally in a new molded plastic grille.",
"1970 AMC Rebel The Machine": "The AMC Rebel was a mid-size car produced by AMC from 1967 to 1970. The most recognizable muscle car version of the AMC Rebel was named The Machine and was available for the 1970 model year. In its most 'Murican factory trim, The Machine was boldly painted red, white, and blue.",
"1975 AMC Pacer X": "The AMC Pacer was a two-door compact car produced in the United States by AMC from 1975 to 1979. A new model was introduced in 1979, the AMC Pacer X, with a serious high performance focus.",
"2018 Dodge Challenger SRT Hellcat Widebody": "The Dodge Challenger is a 2-door coupe made by Dodge. The SRT Hellcat Widebody is the highest trim available to the normal consumer. It's HEMI V8 makes a ridiculous 707 horsepower, and the widebody tries to keep it in check. The issue here is the chassis. It's from a 10-year old economy car.",
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": "The Dodge Challenger is a 2-door coupe made by Dodge. The Scat pack is for those who want a throwback retro-modern muscle car without having to handle the insane 707 hp provided by the Hellcat.",
"2018 Dodge Challenger SRT Demon": "This car was immediately sold out upon its inception. This is a drag machine- tuned by the OEM, with an insane 850 HP and fat rear tires. The front tires are the thickness of dinner plates, though... Oh yeah, and I forgot- the chassis is from a 10-year old economy car.",
"2008 Dodge Challenger SE": "The Dodge Challenger is a 2-door coupe made by Dodge. This one is the shittiest model in game. (modern dodge is shit)",
"2008 Dodge Challenger SRT8": "The Dodge Challenger is a 2-door coupe made by Dodge. This one has a Hemi V8, and is actually quite fast- in a straight line. Just... don't ask it to turn any time soon.",
"2018 Dodge Charger Hellcat": "The Dodge Charger is a 4-door sedan made by Dodge. This insane piece of work has a 707 horsepower HEMI V8. It's a sedan. Left me scratching my head too.",
"2018 Dodge Charger GT Plus": "The Dodge Charger is a 4-door sedan made by Dodge. This is highest end consumer model of the Charger. The Daytona and the Hellcat are for insane people.",
"2011 Dodge Charger SRT8": "The Dodge Charger is a 4-door sedan made by Dodge. This one has a HEMI V8. it's the car for you if you want the same thing that you could've gotten over 5 years ago in a more modern looking package.",
"2005 Dodge Charger SRT8": "The Dodge Charger is a 4-door sedan made by Dodge. This one has a HEMI V8. They end up using this exact same engine for over 10 years because FCA doesn't know how to spend money.",
"2017 Dodge Viper ACR": "Ah. The Dodge Viper. If you somehow don't know, the Dodge Viper is a V10 powered American supercar. The ACR is the highest trim, and it had a bunch of aero bits tacked on, like a hideously huge spoiler. Thing is, it actually did something.",
"2017 Dodge Viper GTS": "The Dodge Viper. After a couple years, you kinda forget this thing. And then you remember. If you somehow don't know, the Dodge Viper is a V10 powered American supercar. The GTS is the normal trim of this car, if you could call this car normal.",
"2012 Dodge Dart R/T": "A disgusting little shitbox that was the brainchild of the genius FCA. It sold, kinda. Then it didn't. Then it was gone. Good riddance. Oh, and here's a review copied from edmunds- 'I bought the car last year July and as we speak it’s at the mechanic.this is the 7th time going to the mechanic because the TRANSMISSION is bad bad bad bad. I Hate the car.' Pure gold.",
"2010 Dodge Avenger Express": "*Looks in interior* *Finds something that looks like nice metal* *Taps it to test* *Taps shitty Chinese plastic* No, seriously, this sedan is full of it. I mean, look at it! https://static.cargurus.com/images/site/2017/05/14/22/16/2010_dodge_avenger_express-pic-183196848802726899-640x480.jpeg",
"2008 Dodge Journey SXT": "The Dodge Journey is a mid-size crossover SUV manufactured and marketed by the FCA's Dodge brand since 2008. All you really need to know is that sitting in it feels like sitting in a porta potty. No, sorry. The plastic is nicer in a porta potty.",
"2007 Dodge Nitro 4.0 R/T": "The Dodge Nitro is a compact SUV that was produced by Dodge from the 2007 to the 2012 model year. It's absolutely hideous. It looks like a tissue box with huge arms. Look at it. https://www.caranddriver.com/images/08q1/267367/2008-dodge-nitro-photo-190003-s-original.jpg",
"2007 Dodge Viper SRT-10": "The Dodge Viper. After a couple years, you kinda forget this thing. And then you remember. If you somehow don't know, the Dodge Viper is a V10 powered American supercar. The 3rd gen Viper got a facelift because it looked really ugly.",
"2007 Dodge Viper SRT10 ACR": "Ah. The Dodge Viper. If you somehow don't know, the Dodge Viper is a V10 powered American supercar. The ACR is the highest trim, and it had a bunch of aero bits tacked on, like a hideously huge spoiler. Thing is, it actually did something.",
"2000 Dodge Intrepid R/T": "The Intrepid was a 4-door sedan made by Dodge. It's shi- no... uh just buy it. It's uh... $2500, so uh... it's cheap. Uh... just get it off of my lot. It's an eyesore. It looks like a stretched out cockroach.",
"2003 Dodge Neon SRT-4": "*throws up* *throws up again* *and again* Uh... ahem. The uh... Dod- *throws up* -The Dodge Neon was a 4-door compact sedan made by Dodge. The SRT-4 was- a... You know what, I give up trying to explain with a straight face. I just... never understood the appeal of the Dodge Neon. It always seemed like one of those cars that you went out and bought because- you'd just never heard of anything else. Honda Civic? What's that. Toyota Corolla? No clue. How about a Volkswagen Golf? Nuh uh. You wanted something that both looked and felt like it was made out of plastic. And that's your Dodge Neon. The SRT-4 was the nice one, but it was still basiaclly made of plastic.",
"1970 Dodge Dart Hemi Super Stock": "While the age of factory-produced drag cars is long past, the Dart HEMI Super Stock represents the peak of the short-lived factory drag race wars. In short, there was never a faster factory-built drag car ever made. There were only 50 of these built by Hurst and delivered to dealers for drag racing greats like “Dandy” Dick Landy. A giant 426 HEMI was shoehorned into the engine bay, with a little help – literally – from a few sledgehammer hits to the fender walls. The wheel arches and shock towers were modified similarly to provide clearance for the valve covers. Then, to lighten the body, a fiberglass nose, fenders, and hood were bolted on along with lightened bumpers and the removal of the mirrors, radio, heaters and, yes, the back seat. The unique L023 coded Dart’s HEMI itself was built by hand-picked technicians from Chrysler’s Marine and Industrial division. It was laughably rated at 425 horsepower; in actuality, it easily touted more than 500. While some were driven on the streets, the L023 came with a factory sticker stating, “This vehicle was not manufactured for use on Public Streets, Roads or Highways, and does not conform to Motor Vehicle Safety Standards.” Whether that was a warning or a sales pitch is still up for debate.",
"1970 Dodge Dart Swinger 340": "The Dodge Dart is an automobile originally built by Dodge from 1960 to 1976 in North America, with production extended to later years in various other markets. At the same time the 4-barrel carbureted 273 235 bhp (175 kW) was replaced on the options list by the 275 bhp (205 kW) 4-barrel carbureted 340 cu in (5.6 L) available only in the 1968–1972 Swinger and the hottest Dart, the performance-oriented GTS models. This one has the 5.6 L V8.",
"1970 Dodge Challenger R/T 426 Hemi": "The Challenger was a 2-door coupe manufactured by Dodge. It still exists today. Among Mopar enthusiasts the Challenger R/T stands near the king of the hill on the drag strip or road course. With a 426 Hemi under the hood pumping out 425 horsepower, few would dispute the R/T’s ability to pounce when asked to. The dual hood scoops are functional, forcing air into the engine bay, although the true performance enhancement was the “Shaker” hood option that protruded through the hood and attached directly to the air-cleaner. Externally, you can also tell an R/T 426 by its wider fenders, rolled to accommodate the 15-inch wheel option. On the inside, the trademark simulated walnut three-spoke steering wheel and Hurst pistol-grip shifter make an unforgettable impression. As a package, the Challenger R/T has enough appeal to make a Mopar lover out of anyone.",
"1969 Dodge Charger Daytona Hemi": "While the Charger Daytona Hemi is closely related (and from a few steps back, virtually indistinguishable) from the Plymouth Superbird, it actually predates the better-known car by about a year. The “aero” cars were created to out-do the Ford Torino Talladega, which was outcompeting the older Charger 500. The only way to go faster was either more power or a clever design. When the engineers did the math, they realized that power was not an option, so to the wind tunnel they went. The aero gear—the nosecone, flush rear window, and functional spoilers—added a lot of weight, but lowered the drag coefficient to just 0.28, making it incredibly fast. In fact, the Charger Daytona was the first NASCAR entry to do more than 200 mph, in the hands of Buddy Baker in 1970. Street cars were needed to homologate the racing variant, so Dodge built 505 street versions. As for the rear spoiler, there’s a controversy about whether its extreme height was for aerodynamics or to allow the trunk to open. Ultimately, it is functional and the trunk opens just fine, so it’s a moot point.",
"1969 Dodge Charger R/T Hemi": "The Dodge Charger was a midsize car built by Dodge. The R/T was the car that General Lee used.",
"2018 Mclaren Senna": "The Senna, codenamed 'P15', is the newest McLaren Ultimate Series model, designed to be the most-track focused road car to ever come from the manufacturer. It's largely based on the McLaren 720S, with an upgraded version of that car's carbon fiber monocoque and a slightly upgraded version of its twin turbo V8 engine. It is named after legendary Brazilian Formula One driver Ayrton Senna, honoring and giving tribute to his success with the McLaren Formula One Team between 1988 and 1993 Formula 1 seasons.",
"2018 McLaren 720S": "The McLaren 720S is a sports coupe(supercar) built by McLaren. Although similar in size and equipped with a higher capacity engine, it weighs 198 lb (90 kg) less than its predecessor due to various lightened components and a redesigned carbon fiber monocoque that extends to the roof and buttresses. Its four liter twin-turbocharged V8 is a redesign of the 3.8 liter variant of previous McLaren models.",
"2015 McLaren 570S": "The 570S is the first of McLaren's new 'Sports Series' models, a new range that is more casual and less extreme than McLaren's 'Super Series' range.",
"2013 McLaren MP4-12C": "The 12C is McLaren's first in-house-developed car since the 1993 McLaren F1 and the first McLaren car to be developed fully in-house, with a new 3.8L twin-turbocharged V8 engine. It is also the first model in McLaren's 'Super Series' model range, succeeded by the McLaren 650S in 2014.",
"1992 McLaren F1": "Conceived by Gordon Murray to bring Bruce McLaren’s dream of a McLaren road car to life, this car took over 30 years to reach fruition. And that 30 years was damn worth it. The engine compartment is lined with gold. The driver’s seat is located in the center of the car. More than twenty years after it was first introduced, it’s still the fastest naturally aspirated car in the world. It's the F1, with its insane 618 HP BMW V12.",
"1997 McLaren F1 GT": "Is the standard McLaren F1 too common for you? The F1 GT may be the answer to your problem, as just three were produced as Le Mans homologation specials. The F1 GT retains the same 6.1 L naturally aspirated V12 engine from the F1, the BMW S70/2, with identical power and torque specifications.",
"1995 McLaren F1 LM": "The McLaren F1 LM is a track oriented edition of the McLaren F1 built to honour the five McLaren F1 GTRs that competed and finished the 1995 24 Hours of Le Mans in first, third, fourth, fifth and thirteenth places overall. The LM is based on the McLaren F1 GTR and built on the standard F1 chassis, with modifications necessary for the modified GTR to be a road legal car—but without the engine intake restrictions that racing regulations impose on the GTR racing car.",
"2013 McLaren P1": "Succeeding the F1 that was introduced in 1993, the P1, whose name stands for 'Position 1, is the second model in McLaren's 'Ultimate Series' model range and the first one since McLaren Automotive's founding in 2010. Designed to 'be the best driver's car in the world', the P1 utilizes technologies from Formula One, including a hybrid powertrain. The P1 is undoubtedly an amazing vehicle. But to car people, this car is widely known as the normie-mobile, and for good reason.",
"1974 MG Midget": "The MG Midget is a small two-seater sports car produced by MG from 1961 to 1979. It revived a name that had been used on earlier models. The engine grew to 1275 cc for the MkIII Midget, using the development seen on the Mini Cooper S. Enthusiasts were disappointed that this was a detuned version of the 76 bhp Cooper S engine, giving only 65 hp.",
"1928 MG M-Type Midget": "The M-Type was one of the first genuinely affordable sports cars to be offered by an established manufacturer, as opposed to modified versions of factory-built saloon cars and tourers. By offering a car with excellent road manners and an entertaining driving experience at a low price (the new MG cost less than double the cheapest version of the Morris Minor on which it was based) despite relatively low overall performance the M-type set the template for many of the MG products that were to follow, as well as many of the other famous British sports cars of the 20th century.",
"2007 Aston Martin DBS": "The new DBS effectively replaced the top-of-the-line Vanquish, and, in its time, it was faster than any Aston before it. It is no stripped down street racer though. It is layered in luxurious leather and alcantara and high tech materials throughout.",
"2016 Aston Martin DB11": "Built on an all-new aluminum platform replacing the VH platform that was last seen in the Aston Martin Vanquish, the DB11 is the successor to the DB9. It is also the first series-production Aston Martin with a turbocharged engine. And there goes another NA engine.",
"2016 Aston Martin V12 Vantage S": "The V12 Vantage S is a more lighter and powerful paddle-shifter variant of the V12 Vantage that debuted for the 2013 model year. It is powered by Aston Martin's long-running 5.9 litre V12 engine, codenamed AM28, which has been updated with a new engine management system and variable valve timing with knock sensors for higher efficiency.",
"2018 Aston Martin DBS Superleggera": "'For over half a century, the name DBS has meant just one thing: the ultimate production Aston Martin. A DBS is a distilled concentrate of all that has made Aston Martin not just one of the most coveted brands in the automotive sphere, but in all fields of endeavour, right around the world. Now the new DBS Superleggera has arrived. Its beauty leaves no room for doubt. Its power cannot be reasoned with. Unquestionably, DBS Superleggera sits at the pinnacle of the Aston Martin production range. It is both a shining light expressing the most beautiful automotive art and, at the same time, a dark and menacing shadow of brutal, unequivocal strength. It is this fine blend of seemingly opposing traits that makes the DBS Superleggera the absolute Aston Martin. Aggressive, yet beautiful. Super lightweight, yet powerfully strong. A commanding presence, yet lavishly finished.' - Official Description    Hey, we all know that this car will depreciate just like the others. Stop. get some help.",
"2013 Aston Martin V8 Vantage": "The V8 Vantage is the cheapest way to become an Aston Martin owner, apart from the Cygnet. It is a V8 powered sports coupe.",
"2011 Aston Martin One-77": "Designed as a halo car, the One-77 is capable of reaching a 220 mph top speed. As indicated by its name, the One-77 was available in a limited production run of 77 cars until 2012",
"2004 Aston Martin Vanquish S": "The Aston Martin Vanquish is a super grand tourer introduced by British car manufacturer Aston Martin in 2001. The Aston Martin Vanquish S debuted at the 2004 Paris Auto Show, with increased power and slight styling revisions.",
"2008 Aston Martin DB9": "It’s a rare car that can walk the tightrope between a classic grand touring experience and state-of-the-art engineering, but the DB9 does just that. It exudes an air of hand-crafted Britishness from every aluminum panel, wood insert, and leather-trimmed surface--and yet under the skin lives a thoroughly modern assembly of extruded aluminum bonded with a high-tech adhesive, and a 21st century V12 under the bonnet (as they say in the island nation that spawned the car). The DB9 manages to turn these modern accoutrements into a classic GT driving experience, although the performance numbers would make any actual classic Aston blush, as 60 mph comes in a blistering 4.7 seconds. It doesn’t hurt that the lines of the car, penned by the legendary designers Ian Callum and Henrik Fisker, are stunningly gorgeous from any angle. The pretty DB9 maintains all of the grace and poise of the headiest Astons of old, with contemporary performance and unparalleled luxury—not a bad combination, all told.",
"2019 Aston Martin Valkyrie": "The Aston Martin Valkyrie comes as close as possible to a Formula One car without being restricted to the track. Its technology comes directly from our involvement with Red Bull Racing Advanced Technologies and has all the hallmarks of our crafted luxury. Precision aerodynamics mean Valkyrie corners and brakes as aggressively as Red Bull Racing’s dominant RB6 racecar, while active aspects of the suspension keep the chassis flat to the road.",
"2018 Range Rover Supercharged": "A luxury SUV that burns all of your fuel while supercharging to the service station.",
"2018 Range Rover Velar R-Dynamic": "A luxury city crossover that is probably too Dynamic for Dynamic.",
"2018 Range Rover Sport SVR": "The Range Rover Sport SVR is a quote en quote 'Super-SUV'. I don't get it. I guess it's pretty fast, but it suffers the same problem as the Range Rover Supercharged.",
"2016 Land Rover Defender 70th Edition": "You see these cars in the repair shops more than you see Mercs. And people buy 5 times more Mercs. These cars are damn cool though.",
"1957 Land Rover Series 1": "Hm. I thought most of these things rusted out. Well this is a rare one. The Series 1 is the first Land Rover Jeep for the British Army.",
"2003 Infiniti G35": "The G35 was a sports coupe manufactured by Infiniti, a subsidiary of Nissan Motor Company. The G35 was known as the Skyline in Japan, and was able to be tuned excessively. However, it was inferior to the previous Skylines.",
"2017 Infiniti Q60 Red Sport": "The Q60 is a luxury sports coupe manufactured by Infiniti, a subsidiary of Nissan Motor Company. This Q60 is the Red Sport, with a 400 HP V6.",
"2015 Infiniti Q50 Eau Rouge": "The Q50 is a luxury sports sedan manufactured by Infiniti, a subsidiary of Nissan Motor Company. This is the Eau Rouge, with the Nissan GTR's VR38DETT twin turbo V6, pushing out a ridiculous 560 HP through all four wheels. The Eau Rouge was never really put into production, but here it is.",
"2019 Infiniti Q50": "The Q50 is a luxury sports sedan manufactured by Infiniti, a subsidiary of Nissan Motor Company. This is the 3.0t Luxe AWD trim, the middle man in between the basic Pure trim and the Red Sport 400.",
"2019 Tesla Model S Ludicrous Performance": "The Tesla Model S is an all-electric five-door liftback car, produced by Tesla, Inc., and introduced on June 22, 2012. The Tesla Model S is built from the ground up as an electric vehicle, with high-strength architecture and a floor-mounted battery pack allowing for incredible impact protection, making the Tesla Model S one of the safest cars on the road. (apart from when it blows up) This is the Ludicrous Performance model, with almost 800 horsepower- so 'safe' is kind of an abstract concept. Well, regardless of how safe the car is, I personally won't buy it.",
"2019 Tesla Model S Standard Range": "The Tesla Model S is an all-electric five-door liftback car, produced by Tesla, Inc., and introduced on June 22, 2012. The Tesla Model S is built from the ground up as an electric vehicle, with high-strength architecture and a floor-mounted battery pack allowing for incredible impact protection, making the Tesla Model S one of the safest cars on the road. (apart from when it blows up) This is the base model.",
"2019 Tesla Model 3 Performance": "The Tesla Model 3 is a luxury all-electric four-door sedan (compact executive car) manufactured and sold by Tesla, Inc. It was advertised as the 'first affordable Tesla', with the base price set at $35,000. This is the not-so-affordable Performance model, with 450 horsepower.",
"2019 Tesla Model 3 Standard Range": "The Tesla Model 3 is a luxury all-electric four-door sedan (compact executive car) manufactured and sold by Tesla, Inc. It was advertised as the 'first affordable Tesla', with the base price set at $35,000. This is that $35,000 base model that Tesla was so adamant about.",
"2019 Tesla Model X Ludicrous Performance": "The Tesla Model X is a mid-size all-electric luxury SUV made by Tesla, Inc. The prototype was unveiled at Tesla's design studios in Hawthorne on February 9, 2012. It has really stupid overcomplicated motorized doors that break all the time, and cost a fortune to repair. This is the Ludicrous Performance model, with an ungodly amount of horsepower for an SUV.",
"2019 Tesla Model X Standard Range": "The Tesla Model X is a mid-size all-electric luxury SUV made by Tesla, Inc. The prototype was unveiled at Tesla's design studios in Hawthorne on February 9, 2012. It has really stupid overcomplicated motorized doors that break all the time, and cost a fortune to repair. The base model, this is.",
"2019 Mini Cooper S": "The Mini Cooper S is a hatchback manufactured by Mini. While it is touted as the quintessential British hot hatch- it is neither British or very hot. It is in fact just a BMW hatch with a 4-banger.",
"2019 Mini John Cooper Works": "The Mini John Cooper Works is a hot hatch manufactured by Mini. It is basically a BMW, so it isn't really British, but it's still pretty damn fast. And that gains my respect.",
"1969 Morris Mini Cooper S": "The Morris Mini Cooper S is a hatchback manufactured by Morris. Compared to the new Minis, this Mini is actually mini. If you're over the height of 5 foot 10, you won't fit. Oh yeah, it also isn't German.",
"2020 Cadillac CT4-V": "Cadillac's smaller compact luxury sedan, the CT4 is... well it's the ATS. Cadillac essentially reinvented every single model in 2020, replacing the CTS with the CT5, and the ATS with this car, the CT4. This is the V variant with a chunky 2.7 liter turbo-4, with 325 horsepower. Compared to the previous ATS-V with a 464 hp twin-turbo V6, it really is a sad drop. But it's still pretty powerful.",
"2019 Cadillac CTS-V": "The Cadillac CTS-V is a high-performance version of the Cadillac CTS, Cadillac's mid-size sedan. It's an insane piece of work, with a 640 hp supercharged V8 paired to an 8-speed automatic.",
"2019 Cadillac CTS 3.6L V6": "The Cadillac CTS is Cadillac's mid-size sedan. This model is a medium high range model of the CTS, with a naturally aspirated 3.6L V6.",
"2019 Cadillac ATS-V Coupe": "The Cadillac ATS-V is a high-performance version of Cadillac's compact luxury sedan, the ATS. With a 464 hp twin-turbo V6, the ATS-V is a fire breathing machine.",
"2016 Cadillac ELR": "The Cadillac ELR was a plug in hybrid coupe manufactured by Cadillac based on the Chevrolet Volt. It was discontinued in 2016 after mediocre sales numbers.",
"2020 Cadillac CT6 Platinum": "The Cadillac CT6 is a large luxury sedan manufactured by Cadillac. This trim, the Platinum, is the highest level trim available.",
"2020 Cadillac Escalade": "The Cadillac Escalde is a large luxury SUV manufactured by Cadillac. It's gaudy and expensive, but also relatively luxurious and powerful.",
"2020 Cadillac XT5": "Cadillac's most popular model, the XT5 is a crossover. Obviously.",
"2014 Cadillac CTS-V Sport Wagon": "Probably Cadillac's oddest performance venture, the Cadillac CTS-V Sport Wagon is a super powerful station wagon.",
"2004 Cadillac Seville": "The Cadillac Seville is a luxury sedan that was manufactured by Cadillac. Genuinely comfortable and VERY CHEAP, this car, dare I say it, is actually quite a good deal.",
"2011 Cadillac DTS": "The DTS is a smooth riding, if a bit boaty, sedan manufactured by Cadillac. It was discontinued in 2011 to make room for Cadillac's newer models.",
"1975 Cadillac Fleetwood Brougham": "The Cadillac Fleetwood Brougham was the top model of the big, chunky 1970s sedan that the Fleetwood was. Rides like a dream, but handles and accelerates like a yacht with a two-stroke lawnmower engine.",
"1976 Cadillac Eldorado": "The Cadillac Eldorado of the 1970s was big, huge, and ginormous at the same time. It suffered the same fate as the rest of the big Caddies after the 1973 oil crisis, getting huge power cuts and heavy gas-guzzler taxes.",
"1959 Cadillac Eldorado Brougham": "The hand-built Cadillac Eldorado Brougham of the late 1950s was more exclusive than even the Rolls-Royces of the time, costing twice the price of the Eldorado Biarritz, with a sticker price of nearly $14,000, the equivalent of $124,000 today. Even among the Broughams, the 1959 model was special- unlike the previous model years, bodywork production was farmed out to Pininfarina in Italy instead of Cadillac themselves in Detroit.",
"Renault R35 Tank": "Not the R35 you were looking for, huh. This is still cool though.",
"2019 Renault Clio Iconic TCe 100": "The Renault Clio is a B-Segment supermini car. This is the most recent generation of the Clio, in the mid-range Iconic trim with the 100kW engine.",
"2019 Renault Clio RS Line TCe 130": "The Renault Clio is a B-Segment supermini car. This is the most recent generation of the Clio, in the top-of-the-line RS Line trim with the most powerful petrol engine available for the base clio, the 130hp turbo four.",
"2019 Renault Clio E-TECH Launch Edition": "The Renault Clio is a B-Segment supermini car. This is the most recent generation of the Clio, and is the launch edition of the E-TECH powertrain for the Clio.",
"2018 Renault Clio RS Trophy": "The Renault Clio is a B-Segment supermini car. The Clio RS Trophy is the top of the line hot hatch version of the Clio, lauded for its tossability around corners and its light weight.",
"2003 Renault Clio V6": "The Renault Clio V6 has almost no resemblance to the base Clio. This specific Renault Clio V6 is the facelifted Phase 2, which are slightly more expensive.",
"1993 Renault Clio Williams": "In 1993, Renault launched a limited edition of the Renault Clio, called the Williams, to homologate for the Group A rally championship. Originally limited to 3800 vehicles, the Williams sold out so fast that Renault built 1600 more.",
"1993 Renault Clio": "The Renault Clio is a B-Segment supermini car. This is the last year of the Phase 1 Clio I.",
"1993 Renault Twingo": "The Renault Twingo is a 4-passenger city car built by Renault. This is the first generation of the Twingo. How do you like the styling?",
"2010 Renault Twingo RS 133 Cup": "The Renault Twingo is a 4-passenger city car built by Renault. This is the Twingo RS 133 Cup, the further-lightened version of the already hot Twingo RS.",
"2010 Renault Twingo RS": "The Renault Twingo is a 4-passenger city car built by Renault. This is the Twingo RS, the hot version with 133 horsepower.",
"2020 Renault Twingo": "The Renault Twingo is a 4-passenger city car built by Renault. This is the brand new Twingo, and it is reviewed quite well by reviewers.",
"2020 Renault Megane RS 300 Trophy": "The Renault Megane is a small family car built by Renault. The Megane RS Trophy is the top of the line version of the Megane RS, with a baffling 296 horsepower.",
"2020 Renault Megane RS Trophy R": "No expense has been spared in the development of this record-breaking front wheel drive car. It's got carbon fiber wheels, an Akrapovic titanium exhaust system, carbon fiber body panels, and more, all to save weight.",
"2020 Renault Megane RS Line TCe 140": "The Renault Megane is a small family car built by Renault. This is the top-of-the-line model of the base Megane.",
"2005 Renault Megane Sport 225 Cup": "The Renault Megane is a small family car built by Renault. This is the 225 Cup, the hot version.",
"LIGHNING MCQUEEN":"KACHOW!!!!!!!!!!!!1!1!!!111!!!!!!!!!!!!,                                                                                                                  kachow.",
"2018 Fortnite Shopping Cart GT-S": "ok",
"2019 Fortnite ATK GT-4R": "Kanato: *Slaps roof of ATK* This bad boy can fit 4 virgins",
"1009 Thanos Car": "'THANOS CAR THANOS CAR Thanos Car THANOS CAR eTHAN OSCAR thanos car THANOS CAR' is a car that snaps all other cars in half until they are all perfectly balanced, as all things should be."
}

Car_Exterior_Images = {
"2000 Honda Integra" : "https://upload.wikimedia.org/wikipedia/commons/9/9c/3RD-Acura-Integra.jpg",
"2000 Honda Integra Type R" : "https://cnet4.cbsistatic.com/img/TpCDELrVRhnAgCWw_nu-TRBDgNo=/936x527/2016/11/23/afe2f36f-e514-4cca-8785-1754dcc6a042/2000-honda-integra-type-r-1.jpg",
"1999 Honda Civic Type R EK9" : "https://www.mad4wheels.com/img/free-car-images/hires/5790/honda-civic-type-r-x-1999-282429.jpg",
"2003 Honda Civic Type R EP3" : "https://www.performance-car-guide.co.uk/images/L-Civic-Type-R-1-1.jpg",
"2003 Honda NSX R" : "http://www.foroshonda.com/foros/attachments/f13/5763d1327096782-honda-nsx-type-r-2002-muchisimas-fotos-img_8234.jpg",
"2001 Honda S2000" : "https://cdn1.mecum.com/auctions/fl0117/fl0117-267328/images/fl0117-267328_11@2x.jpg?1483568391000",
"2021 Honda Civic Type R FK8" : "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/img-4872-1589999977.jpg?crop=1.00xw:0.668xh;0,0&resize=1200:*",
"1991 Honda Civic EG6 SiR": "https://honda-tech.com/forums/attachments/vehicles-sale-42/414846d1461496673-%2Areal-deal%2A-rhd-eg6-sir-%245500-image1.jpg",
"1999 Honda Civic LX": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/96-98_Honda_Civic_LX_sedan.jpg/1200px-96-98_Honda_Civic_LX_sedan.jpg",
"2006 Honda Civic Si": "http://consumerguide.com/wp-content/uploads/2014/07/06802031990005.jpg",
"2018 Honda Civic Sport": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/media/672264/2018-honda-civic-in-depth-model-review-car-and-driver-photo-693715-s-original.jpg?crop=1xw:1xh;center,center&resize=900:*",
"2018 Honda Civic Si Coupe": "https://cdntdreditorials.azureedge.net/cache/e/4/0/2/7/6/e40276de926b5d23b55e8a9691734504495d960e.jpg",
"2006 Honda Accord 3.0 EX": "https://www.svtperformance.com/attachments/2205-jpg.590103/",
"2010 Honda Accord EX-L V6": "https://st.motortrend.com/uploads/sites/10/2015/11/2010-honda-accord-sedan-exl-v6-5-speed-auto-angular-front.png",
"2015 Honda Accord Sport": "https://st.motortrend.com/uploads/sites/10/2015/09/2015-Honda-Accord-Sport-front-three-quarter-03.jpg",
"2015 Honda Accord EX-L V6": "https://di-uploads-pod2.dealerinspire.com/capitalregionhondadealers/uploads/2015/04/2015-Accord-EX-L-Sedan-gray.jpg",
"2018 Honda Accord Sport": "https://di-uploads-pod5.dealerinspire.com/fletcherjonesbigislandhondahilo/uploads/2018/01/2018_Honda_Accord_Sport_2.0T_Red_EDIT-1024x768.jpg",
"2021 Honda CR-V": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2021-honda-cr-v-hybrid-touring-106-1614324428.jpg?crop=0.574xw:0.647xh;0.295xw,0.264xh&resize=640:*",
"1999 Honda CR-V": "https://www.iihs.org/api/ratings/model-year-images/1653",
"2005 Honda Pilot": "https://file.kelleybluebookimages.com/kbb/base/house/2005/2005-Honda-Pilot-FrontSide_HTPILEX051_505x375.jpg",
"2010 Honda Crosstour": "https://www.iihs.org/api/ratings/model-year-images/2320",
"2005 Honda Element": "https://www.iihs.org/api/ratings/model-year-images/1674",
"2001 Honda Odyssey Absolute": "https://www.japan-partner.com/images/4c6ba6753b/--07723da0da.jpg",
"2021 Honda N-ONE RS": "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/oe3ydk9nr5wzwusmy18r.jpg",
"2021 Honda StepWGN Spada": "https://i.ytimg.com/vi/scEVb8IvZyQ/maxresdefault.jpg",
"1999 Honda StepWGN": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Honda_Stepwgn_1999_Rear.jpg",
"2016 Honda CR-Z": "https://media.ed.edmunds-media.com/honda/cr-z/2016/oem/2016_honda_cr-z_2dr-hatchback_ex-l-wnavigation_fq_oem_1_1600.jpg",
"2021 Honda HR-V": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2021-honda-hr-v-mmp-1-1595869461.jpg?crop=0.889xw:1.00xh;0.0561xw,0&resize=640:*", 
"2005 Honda Stream": "https://d1ix0byejyn2u7.cloudfront.net/drive/images/made/drive/images/remote/https_ssl.caranddriving.com/f2/images/used/big/honstream_750_500_70.jpg",
"2014 Honda Stream": "https://upload.wikimedia.org/wikipedia/commons/b/bc/2006_Honda_Stream_01.JPG",
"2021 Honda Clarity": "https://di-uploads-pod13.dealerinspire.com/mckenneysalinashonda/uploads/2020/08/hybrid.jpg",
"2000 Honda Insight": "https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/00q1/267322/honda-insight-photo-6022-s-original.jpg?fill=2:1&resize=1200:*",
"2021 Honda Insight": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2021-honda-insight-01-source-1584989283.jpg",
"2000 Honda ACTY": "https://www.cars-directory.net/pics/honda/acty_van/2000/honda_acty_van_2700607.jpg",
"2021 Honda ACTY": "https://www.carjunction.com/car_images2/10940_/1.jpg",
"2021 Honda Fit": "https://www.autotrader.com/wp-content/uploads/2020/02/2020-Honda-Fit-.1..jpg",
"2001 Honda Life Dunk": "https://static.carfromjapan.com/spec_a204aeea-6ae1-4335-8b06-2990499ff3b4_640_0",
"1992 Honda Vigor": "https://img.favcars.com/honda/vigor/wallpapers_honda_vigor_1992_1.jpg",
"1989 Honda Accord": "https://global.honda/content/dam/site/global/heritage/cq_img/timeline/products-history/automobile/Accord/1989/04.jpg",
"2003 Acura RSX Type S" : "https://st.automobilemag.com/uploads/sites/11/2003/07/2002-Acura-RSX-Type-S-Factory-Performance-Package-front-three-quarter-01.jpg",
"2017 Acura NSX" : "https://www.autoguide.com/blog/wp-content/gallery/2017-acura-nsx-review/2017-Acura-NSX-01.jpg",
"2005 Acura TL Type S": "https://www.netcarshow.com/Acura-TL_Type-S-2007-1280-01.jpg",
"2007 Acura TL": "https://pictures.topspeed.com/IMG/jpg/200609/2007-acura-tl.jpg",
"2018 Acura TLX 3.5": "https://www.acura.ca/Content/acura.ca/98c11878-f151-4080-8bb1-58487e470b7a/TeaserGallery/05_my20_tlx_overview_TeaserGallery_desktop_05a.jpg?mode=crop&width=1536&height=785",
"2018 Acura MDX": "https://www.thetorquereport.com/wp-content/uploads/2018/01/2018-Acura-MDX-Sport-Hybrid-0003.jpg",
"2018 Acura ILX": "https://static.cargurus.com/images/site/2015/04/10/15/02/2016_acura_ilx-pic-5529454482336105455-1600x1200.jpeg",
"2021 Acura TLX Type S": "https://media.ed.edmunds-media.com/acura/tlx/2021/oem/2021_acura_tlx_sedan_type-s_fq_oem_1_815.jpg",
"1995 Acura Legend": "https://bringatrailer.com/wp-content/uploads/2020/02/1994_acura_legend_15821468858db7e804b64dbb61994-Acura-Legend-Coupe-8.jpg?fit=940%2C626",
"2014 Acura TSX Sport Wagon": "https://www.vroomgirls.com/wp-content/uploads/2011/11/AcuraTSXSportsWagon-1-620x210.jpg",
"1990 Ford Mustang Foxbody" : "https://upload.wikimedia.org/wikipedia/commons/2/2f/Ford_Mustang_convertible.jpg",
"2010 Ford Mustang GT500" : "https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/09q2/267376/2010-ford-mustang-shelby-gt500-photo-283121-s-original.jpg",
"2015 Ford Mustang GT" : "https://enthusiastnetwork.s3.amazonaws.com/uploads/sites/5/2014/01/2015-Ford-Mustang-front-three-quarters.jpg?impolicy=entryimage",
"1975 Ford Pinto": "https://i.pinimg.com/originals/06/f1/05/06f1050f7d83adabc133e3669679802f.jpg",
"1999 Ford Crown Victoria": "https://upload.wikimedia.org/wikipedia/commons/7/73/Ford_Crown_Victoria.jpg",
"2017 Ford Focus Hatch": "https://cdn.motor1.com/images/mgl/PwoRG/s1/2017-ford-focus-hatchback.jpg",
"2017 Ford Focus RS": "https://www.autoguide.com/blog/wp-content/gallery/2017-ford-focus-rs/2017FordFocusRS013.jpg",
"2017 Ford Fusion Titanium": "https://cdn.motor1.com/images/mgl/zjKK6/s1/2017-ford-fusion.jpg",
"2017 Ford Fusion Sport": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/16q3/669461/2017-ford-fusion-sport-first-drive-review-car-and-driver-photo-670393-s-original.jpg",
"2018 Ford F-150 Super Cab": "https://i.ytimg.com/vi/pZ5k2QeDyWM/maxresdefault.jpg",
"2018 Ford F-150 Raptor": "https://bca86c45816ab2b18f82-19209e2b5741cc1b16092203fe85f171.ssl.cf1.rackcdn.com/1FTFW1RG0JFD82883/d0c10378a37b5407bf00b30457e0e1dd.jpg",
"2016 Shelby Mustang GT350R" : "https://www.ford.com/cmslibs/content/dam/brand_ford/en_us/brand/performance/gt350/2018/features/3-2/GT350-bydesign-crop_large.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg",
"1992 Volkswagen Golf GTi MK2" : "http://jadefansite.com/images/imagegallery-50312-59c2807eb735f.jpg",
"2017 Volkswagen Golf GTi MK7" : "https://images.cdn.circlesix.co/image/2/1200/700/5/uploads/posts/2017/07/3721bdd02ab2e05a95c8060effe54b80.jpg",
"2015 Volkswagen Scirocco R" : "https://s1.cdn.autoevolution.com/images/gallery/VOLKSWAGEN-Scirocco-R-5140_4.jpg",
"2018 Volkswagen Passat R-Line": "https://st.motortrend.com/uploads/sites/5/2018/07/2018-Volkswagen-Passat-front-three-quarter-01.jpg",
"1969 Volkswagen Beetle": "https://0.cdn.autotraderspecialty.com/Car-100973777-8b89cfb2ef97af661d5c57a783c2107f.jpg?w=800&h=800&r=fit",
"1999 BMW M3" : "http://bestcarmag.com/sites/default/files/1999-bmw-m3-1879707-8646296.jpg",
"2003 BMW M3" : "https://s1.cdn.autoevolution.com/images/news/gallery/somebodys-selling-a-2003-bmw-m3-csl-but-you-wont-like-its-price-photo-gallery_3.jpg",
"2008 BMW M3" : "https://pictures.topspeed.com/IMG/jpg/200704/2008-bmw-m3-coupe-21.jpg",
"2017 BMW M3" : "https://media.ed.edmunds-media.com/bmw/m3/2017/ot/2017_bmw_m3_LIFE1_ot_1123163_1600.jpg",
"2005 BMW M5" : "https://www.supercars.net/blog/wp-content/uploads/2016/04/Screenshot-2016-04-25-11.21.35.png",
"2018 BMW M5" : "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/17q3/685272/2018-bmw-m5-photos-and-information-news-car-and-driver-photo-688789-s-original.jpg",
"2017 BMW M4" : "https://cdn.bmwblog.com/wp-content/uploads/2020/03/bmw-m4.jpg",
"2017 BMW M6" : "https://i.ytimg.com/vi/mr8IFVmJl1I/maxresdefault.jpg",
"2018 BMW i8" : "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/16q3/669461/2016-bmw-i8-test-review-car-and-driver-photo-670463-s-original.jpg",
"1959 BMW 507": "https://www.ultimatecarpage.com/images/car/51/BMW-507-1304.jpg",
"2018 BMW 530i": "https://media.ed.edmunds-media.com/bmw/5-series/2018/td/2018_bmw_5-series_actf34_td_306181_1600.jpg",
"2018 BMW X3": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/17q2/678296/2018-bmw-x3-official-photos-and-info-news-car-and-driver-photo-684403-s-original.jpg",
"2018 BMW 750i": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2018-bmw-750i-placement-1528316442.jpg",
"1974 BMW 2002 Turbo": "https://rmsothebys-cache.azureedge.net/a/1/b/5/e/4/a1b5e4d772a8f9dfb0c4257d4bfb8f2b12cbda56.jpg",
"2011 BMW 1M": "http://www.blogcdn.com/www.autoblog.com/media/2011/08/01-2011-bmw-1-series-m-review.jpg",
"2018 BMW 330i": "https://a1281fef8f189e24ae4c-e28e3c9fab64e591bcc5e009ce02564e.ssl.cf1.rackcdn.com/WBA8B9G52JNU99601/02e22a75a76a3d93e2e61520f1345a04.jpg",
"2020 BMW M235i xDrive Gran Coupe": "https://cdn.bmwblog.com/wp-content/uploads/2020/02/2020-BMW-M235i-xDrive-Gran-Coupe-46.jpg",
"2007 Saturn Ion": "https://i.ytimg.com/vi/9V2BXw8twps/maxresdefault.jpg",
"2001 Saturn SL2": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/1996-1999_Saturn_SL2_--_03-16-2012.JPG/1200px-1996-1999_Saturn_SL2_--_03-16-2012.JPG",
"1998 Saturn SW2": "http://zombdrive.com/images1600_/1998_saturn_s-series_wagon_sw1_fq_oem_1_500.jpg",
"2017 Ferrari 488GTB" : "https://cdn.arstechnica.net/wp-content/uploads/2017/08/Ferrari-488-GTB-listing-image.jpg",
"2017 Ferrari F12" : "https://cdn1.mecum.com/auctions/ca0819/ca0819-388427/images/1-1562590270179@2x.jpg?1565913785000",
"2003 Ferrari 575M Maranello" : "https://upload.wikimedia.org/wikipedia/commons/f/fd/Ferrari_575M_Maranello.jpg",
"1999 Ferrari 360" : "https://upload.wikimedia.org/wikipedia/commons/6/6d/Ferrari_F360_Modena_-_Flickr_-_The_Car_Spy_%2820%29.jpg",
"1995 Ferrari F355" : "https://www.autocar.co.uk/sites/autocar.co.uk/files/images/car-reviews/first-drives/legacy/f355-0971.jpg",
"1965 Ferrari 250 GTO" : "https://www.leithcars.com/blogs/1421/wp-content/uploads/2015/11/Ferrari-250-GTO-3.jpg",
"1968 Ferrari Dino" : "https://rmsothebys-cache.azureedge.net/4/8/d/3/e/b/48d3ebaed45aaa0c2929bc5293d7c84b1dfe966c.jpg",
"1970 Ferrari 365 GTB/4 Daytona" : "https://rmsothebys-cache.azureedge.net/2/3/3/9/6/4/233964c79c4917a1f545692739f06fa20395cd42.jpg",
"2008 Ferrari F430" : "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Ferrari_F430_front_20080605.jpg/1200px-Ferrari_F430_front_20080605.jpg",
"2008 Ferrari California" : "http://autotras.com/images/90/ferrari-california-characteristics.jpg",
"2016 Ferrari LaFerrari" : "https://rmsothebys-cache.azureedge.net/7/4/3/c/3/2/743c3210ce721cd7b9760476655c63d3c494690d.jpg",
"2010 Ferrari 458 Italia": "https://images.hgmsites.net/hug/ferrari_100319022_h.jpg",
"1993 Toyota MR2 GT-S" : "https://upload.wikimedia.org/wikipedia/commons/7/7e/1993ToyotaMR2Hardtop.jpg",
"1986 Toyota Corolla Sprinter Trueno" : "https://static.wikia.nocookie.net/initiald/images/e/e8/Toyota_Sprinter_Trueno_GT-APEX_AE86_Hatchback_real.jpg/revision/latest?cb=20200524004713",
"1993 Toyota Supra Twin Turbo" : "https://pictures.topspeed.com/IMG/jpg/201405/1993-toyota-supra-generat-12.jpg",
"1998 Toyota Chaser Tourer V" : "https://img.favcars.com/toyota/chaser/toyota_chaser_1998_wallpapers_2.jpg",
"1997 Toyota Soarer" : "https://cdn.dealeraccelerate.com/international/1/157/8108/1920x1440/1992-toyota-soarer",
"1998 Toyota Altezza RS200" : "http://cdn2.3dtuning.com/info/Toyota%20Altezza%20RS200%202004%20Sedan/factory/4.jpg",
"1996 Toyota Cresta 2.5 Twin Turbo": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Toyota_cresta_jzx100_2.5exceedg_1_f.jpg",
"1984 Toyota Landcruiser 60 3F" : "http://carphotos.cardomain.com/ride_images/3/2612/461/31527730001_large.jpg",
"2003 Toyota Tundra" : "https://static.cargurus.com/images/site/2008/01/05/15/11/2003_toyota_tundra_4_dr_sr5_v8_extended_cab_sb-pic-31174-1600x1200.jpeg",
"2018 Toyota Land Cruiser Prado" : "https://upload.wikimedia.org/wikipedia/commons/3/31/2018_Toyota_Land_Cruiser_Prado_%28GDJ150R%29_VX_4WD_wagon_%282018-06-05%29_01.jpg",
"2018 Toyota 4Runner TRD Pro" : "http://st.motortrend.ca/uploads/sites/5/2017/07/2017-Toyota-4Runner-TRD-Pro-front-three-quarters-02-e1504051140989.jpg",
"2018 Toyota Tundra TRD Pro" : "https://s3.amazonaws.com/toyota-cms-media/wp-content/uploads/2019/10/2020_Tundra_TRD_Pro_27_B1725D460BDA4702B3AA06E06CA361B0738D249E-1-1500x1061.jpg",
"1992 Toyota Hilux Surf SSR-G Wide Body" : "https://i.ytimg.com/vi/9wPh7ANjrq8/maxresdefault.jpg",
"2017 Toyota Century": "https://pictures.topspeed.com/IMG/jpg/201710/toyota-century-2.jpg",
"2019 Toyota Corolla Hatch XSE": "https://www.cstatic-images.com/stock/1170x1170/55/img-887489310-1524577914755.jpg",
"2019 Toyota Corolla Hatch SE": "https://5c7706b196d2c0411e73-385cc776c879991ce5855d03ec2ea83c.ssl.cf1.rackcdn.com/JTNK4RBEXK3019226/c68a03b28a9a7214153cb06792510c5c.jpg",
"2019 Toyota Corolla Touring Sport": "https://img.drivemag.net/media/default/0001/93/toyota-corolla-touring-sports-2019-5009-default-large.jpeg",
"2021 Toyota GR Supra": "https://cnet4.cbsistatic.com/img/-Hdd0LsVjPrkf6OAkLATTTW12Cc=/2019/01/13/6ae85e42-8420-4404-82be-7cc48e28586b/2020-toyota-supra-ogi-1.jpg",
"2008 Toyota Sequoia V8": "https://upload.wikimedia.org/wikipedia/commons/f/f6/2008_Toyota_Sequoia_SR5_--_NHTSA.jpg",
"2005 Toyota Camry LE V6": "http://zombdrive.com/images/2005-toyota-camry-1.jpg",
"1999 Toyota Corolla LE": "http://zombdrive.com/images1600_/2000_toyota_corolla_sedan_le_rq_oem_1_500.jpg",
"2002 Toyota Sienna 5D Symphony": "https://s1.cdn.autoevolution.com/images/gallery/TOYOTASienna-4710_1.jpg",
"2010 Toyota Camry LE": "https://st.motortrend.com/uploads/sites/10/2015/11/2010-toyota-camry-le-v6-6-speed-at-sedan-angular-front.png", 
"2016 Toyota Avalon Limited": "https://reviewgarage.files.wordpress.com/2016/08/2016_toyota_avalon_hybrid02_bf71c427765236bb3c692b91fb8565785bcb3b90.jpg?w=1400",
"2018 Toyota Camry XSE": "https://i.ytimg.com/vi/rYb-JIJQOYg/maxresdefault.jpg",
"2018 Toyota Corolla XLE": "https://95octane.com/wp-content/uploads/2017/05/2017_toyota_corolla_review_1.jpg",
"1969 Toyota 2000GT": "https://rmsothebys-cache.azureedge.net/4/6/9/f/5/4/469f545e1890cd46b57ca9befd0af6e894121aec.jpg",
"2001 Toyota Camry LE V6": "https://enthusiastnetwork.s3.amazonaws.com/uploads/sites/5/2011/08/2001-Toyota-Camry.jpg?impolicy=modalgallery",
"2006 Toyota Sienna Limited": "https://i.ytimg.com/vi/pW2NPfteb9U/maxresdefault.jpg",
"2017 Toyota Sienna SE": "https://i.gaw.to/content/photos/30/41/304182_2017_Toyota_Sienna.jpg",
"2018 Toyota Sienta": "https://newcar.carlist.my/uploads/model_year_images/9090_large.jpg",
"2018 Toyota Alphard": "https://upload.wikimedia.org/wikipedia/commons/6/66/Toyota_Alphard_350_V6_%28III%29_%E2%80%93_Frontansicht%2C_2._April_2018%2C_Hongkong.jpg",
"2018 Toyota Crown Majesta": "https://i.ytimg.com/vi/L9tZaEfSEtk/maxresdefault.jpg",
"2018 Toyota Tundra SR5 5.7L V8": "https://images-na.ssl-images-amazon.com/images/I/714k5H12aAL.jpg",
"2018 Toyota Hiace": "https://images.summitmedia-digital.com/topgear/images/2017/01/30/TOYOTAHIACE_16.jpg",
"1993 Toyota Hiace": "http://www.yotaimports.com/wp-content/uploads/2018/10/DSC_0534.jpg", 
"1997 Toyota Celica GT-Four": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/wallpapers-toyota-celica-1994-4-1518446849.jpg",
"1998 Toyota GT-one TS020": "https://i.kinja-img.com/gawker-media/image/upload/s--mpHt_k_O--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/grwj8hcczhbrc1doh9xs.jpg",
"1993 Toyota Mark II Tourer V JZX90": "https://www.thetruthaboutcars.com/wp-content/uploads/2016/10/autowp_ru_toyota_mark_ii_tourer_v_3.jpg",
"2018 Toyota GT86": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/media/682287/2017-toyota-86-engine-and-transmission-review-car-and-driver-photo-682291-s-original.jpg",
"1997 Toyota Tercel": "https://dxsdcl7y7vn9x.cloudfront.net/251218/38EB7D3D-7618-437E-B936-AB8A23D24A02_1.jpg",
"1997 Toyota Celica GT": "https://i.pinimg.com/originals/8c/04/68/8c0468aa6e2d51c9133b59a449c3fba4.jpg",
"2016 Toyota Land Cruiser": "https://upload.wikimedia.org/wikipedia/commons/f/fc/2016-2018_Toyota_Land_Cruiser_%28VDJ200R%29_VX_wagon_%282018-09-03%29_01.jpg",
"2019 Toyota Tacoma SR5": "https://file.kbb.com/kbb/images/content/editorial/slideshow/2016-toyota-tacoma-unveiled/2016-toyota-tacoma-600-(3)-600-001.jpg",
"2019 Toyota Tacoma TRD Pro": "https://274ea2957309fdba7396-692c78ed4b4b9a6d27e52e3b63613274.ssl.cf1.rackcdn.com/5TFCZ5AN0KX166992/a4e3b2c8e21494e7c0e98e69bc034414.jpg",
"1993 Toyota Sera": "https://i.ytimg.com/vi/nuvAOT1_XlI/maxresdefault.jpg",
"2020 Toyota Avalon Touring": "https://s.aolcdn.com/commerce/autodata/images/USC90TOC011A01300.jpg",
"2020 Toyota Avalon Limited": "https://www.thetruthaboutcars.com/wp-content/uploads/2020/06/DSC0550-610x405.jpg",
"2020 Toyota Avalon Limited Hybrid": "https://19ae1d166eabb2fd071b-f85f58f3e3becab2261d2dcacdb50b5b.ssl.cf1.rackcdn.com/4T1C21FB8LU012928/ae74fdd99cfe04a721f1c9857c106c57.jpg",
"2020 Toyota Avalon TRD": "https://www.torquenews.com/sites/default/files/images/2020_toyota_avalon_trd_celestial_silver_metallic_front_end.jpg",
"2020 Toyota Camry LE": "https://0dd0a947995863497b70-e28f712be312e2ecfa6cb93fc976597f.ssl.cf1.rackcdn.com/4T1C11AKXLU864367/3538fb9c78c7a624541076328531182a.jpg",
"2020 Toyota Camry SE Hybrid": "https://www.toyota.com/imgix/responsive/images/mlp/colorizer/2020/camryhybrid/8T7/1.png?bg=fff&fm=webp",
"2011 Toyota Prius": "https://images.hgmsites.net/hug/2011-toyota-prius_100331679_h.jpg",
"2020 Toyota Prius XLE AWD": "https://cnet3.cbsistatic.com/img/hNJiYSL49NeL38GDr0-LTZBaf7c=/1200x675/2018/12/12/82606e3e-eea4-402e-967d-ed6544db4073/2019-toyota-prius-ogi.jpg",
"2021 Toyota GR Yaris": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Toyota_GR_Yaris_%28XP21%29_%E2%80%93_f_03052021.jpg",
"2022 Toyota GR86 Base": "https://www.cnet.com/a/img/9dhCbciRwQxVw_ilUkW57xapjps=/940x0/2021/06/04/ee3cf0a6-2c88-4f63-a74b-252c50ba1dc5/2022-toyota-gr-86-base-model-111.jpg",
"2022 Toyota GR86 Premium": "https://cdn.motor1.com/images/mgl/8Q033/s3/2022-toyota-gr-86-exterior-review.jpg",
"2018 Toyota Camry SE": "https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/17q3/685270/2018-toyota-camry-se-25l-test-review-car-and-driver-photo-691169-s-original.jpg",
"2017 Nissan Armada Platinum": "https://www.motortrend.com/uploads/sites/5/2016/10/2017-Nissan-Armada-Platinum-front-three-quarter-in-motion-04-e1475531831892.jpg",
"1994 Nissan Hardbody": "https://bringatrailer.com/wp-content/uploads/2020/01/1994_nissan_d21_hardbody_pickup_truck_xe_4wd_1580451908565ef66e7dff9f9812.jpeg?fit=2048%2C1366",
"2018 Nissan Titan Platinum Reserve": "https://14794cb074070f2635be-909c741dfbd93d74800510af85411879.ssl.cf1.rackcdn.com/1N6AA1E51KN532873/aa9aa43a66fb3a8c6d8ad42250026b6e.jpg",
"2003 Nissan Skyline GT-R R34 Z-Tune": "https://www.diariomotor.com/imagenes/picscache/1440x655c/nissan-gt-r-nismo-z-tune-p_1440x655c.jpg",
"2015 Lamborghini Veneno": "https://i.pinimg.com/originals/fa/b1/6e/fab16e7a7d0b34a0050c36ec2be6ab3f.jpg",
"2009 Lexus LFA" : "https://upload.wikimedia.org/wikipedia/commons/c/c9/Lexus_LFA_005.JPG",
"2007 Lexus ISF" : "https://pictures.topspeed.com/IMG/jpg/200701/2008-lexus-is-f-5.jpg",
"1998 Lexus GS300" : "https://upload.wikimedia.org/wikipedia/commons/6/6a/98-00_Lexus_GS300.jpg",
"2018 Lexus LC500" : "https://media-cf.assets-cdk.com/websites/content/c332295a96e14e9aaf8d340b53363954_c586x939-5957x2557_x5957.jpg",
"2019 Lexus ES300h": "http://blog.consumerguide.com/wp-content/uploads/sites/2/2018/06/ES-front-1.jpg",
"2018 Lexus GS F": "https://shortshift.co/wp-content/uploads/2016/12/2017-Lexus-GS-F-Christmas.jpg",
"2003 Lexus LS430": "https://s1.cdn.autoevolution.com/images/gallery/LEXUSLS-3403_3.jpg",
"2019 Lexus RX350": "https://hips.hearstapps.com/hmg-prod/images/2018-lexus-rx450hl-placement-1529695429.jpg",
"1999 Lexus RX300 4WD": "https://twstatic.net/attachments/img_4412-jpg.2521529/",
"2019 Lexus LX570": "https://s.aolcdn.com/commerce/autodata/images/USC60LES131A021001.jpg",
"2018 Lexus LS500 AWD" : "https://static.cargurus.com/images/article/2017/05/05/15/00/2018_lexus_ls_500_preview_overview-pic-7162349450088168353-1600x1200.jpeg",
"2022 Lexus IS500 F Sport Performance": "http://cdn.carbuzz.com/gallery-images/1600/888000/800/888810.jpg",
"2022 Lexus IS350 F Sport": "https://cimg3.ibsrv.net/ibimg/hgm/1920x1080-1/100/791/2021-lexus-is_100791179.jpg",
"1990 Nissan Skyline GTR R32" : "https://d32c3oe4bky4k6.cloudfront.net/-/media/uscamediasite/images/story-images/2018/03/gt-r_buyer-thumb.ashx?modified=20180329135136",
"1994 Nissan Skyline GTR R33 Spec-V" : "https://www.supercars.net/blog/wp-content/uploads/2016/02/NISSAN-Skyline-GT-R-V-Spec-R33-4039_12.jpg",
"1999 Nissan Skyline GTR R34": "https://cdn.motor1.com/images/mgl/yW7zb/s1/1999-nissan-skyline-gt-r-r34.jpg",
"2002 Nissan Skyline GTR V-Spec II Nur" : "https://nsx.np.dl.playstation.net/nsx/material/5/513e7a2d3f6963b9fac31c30aafc9a8a495bb570-1168149.jpg",
"1996 Nissan 180SX" : "https://upload.wikimedia.org/wikipedia/commons/6/68/180SX_1995_front.jpg",
"1993 Nissan Silvia K's Type S S14" : "https://img.favcars.com/nissan/silvia/nissan_silvia_photos_3.jpg",
"2018 Nissan GTR Track Edition R35" : "https://images.hgmsites.net/hug/2018-nissan-gt-r_100656832_h.jpg",
"2007 Nissan Fairlady Z" : "https://ccmarketplace.azureedge.net/cc-temp/listing/103/7586/10060483-2007-nissan-350z-std.jpg",
"2018 Nissan Fairlady Z NISMO" : "https://upload.wikimedia.org/wikipedia/commons/9/9f/2018_Nissan_Fairlady_Z_Nismo.jpg",
"2018 Nissan Fairlady Z" : "https://upload.wikimedia.org/wikipedia/commons/4/4d/Nissan_370Z_%285494564740%29.jpg",
"1989 Nissan 300ZX Turbo Z" : "https://www.supercars.net/blog/wp-content/uploads/2016/01/Andoniscars-Z32-pic-cropped-and-resized.jpg",
"2018 Nissan GT-R50 by Italdesign": "https://car-images.bauersecure.com/pagefiles/83286/050_gt-r50.jpg",
"2018 Nissan GT-R NISMO": "https://www.nissanusa.com/content/dam/Nissan/us/vehicles/gtr/r35/2_minor_change/nismo/18tdi-gtrhelios510.jpg.ximg.l_full_m.smart.jpg",
"2018 Nissan Maxima Platinum": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/media/672264/2018-nissan-maxima-in-depth-model-review-car-and-driver-photo-694249-s-original.jpg",
"2018 Nissan Sentra SR Turbo": "https://pictures.dealer.com/n/nissanofvannuys/0569/fe76342ae5070bcf67128768bd7e8066x.jpg",
"2017 Nissan Leaf": "https://images.hgmsites.net/hug/2017-nissan-leaf_100581915_h.jpg",
"1973 Nissan Skyline H/T 2000GT-R": "https://rmsothebys-cache.azureedge.net/1/8/d/f/4/7/18df479b256f2d2853a31ff6232073a232ef4fb7.jpg",
"1987 Nissan Skyline GTSR R31": "https://www.rightdriveusa.com/wp-content/uploads/2014/08/Nissan-Skyline-GTS-R-b.jpg",
"1989 Nissan Skyline GTS-4 R32": "https://assets.hemmings.com/blog/wp-content/uploads//2010/02/1989-Nissan-Skyline-GTS-t-Type-M-RCR32.JPG",
"1998 Nissan Skyline 25GT-X Turbo R34": "https://www.autodata1.com/media/nissan/pics/nissan-skyline-x-r34-[7361].jpg",
"1965 Nissan Silvia 1600 Coupe": "https://upload.wikimedia.org/wikipedia/commons/1/12/1965_Nissan_Silvia_01.jpg",
"1990 Nissan Silvia S13": "https://i.pinimg.com/originals/91/0b/4a/910b4af11d8016a8cc06ffcfc7d29299.jpg",
"1999 Nissan Silvia Spec-R S15": "http://www.jm-imports.co.uk/wp-content/uploads/2017/08/IMG_3397-Copy.jpg",
"1995 Nissan GT-R Skyline R33 LM": "https://i.pinimg.com/originals/7d/e0/b2/7de0b28f35fa388a6f1f8c02cfdbd5e7.jpg",
"1998 Nissan R390 GT1": "https://cdn.motor1.com/images/mgl/M2MjX/s1/1998-nissan-r390-gt1-road-car-concept.jpg",
"1992 Nissan Cefiro 2.0 Turbo": "https://www.mad4wheels.com/img/free-car-images/mobile/6824/nissan-cefiro-a31--1988-291707.jpg",
"1990 Nissan Laurel Turbo Medalist": "https://montumotors.com/media/DSC_0667.jpg",
"2015 Nissan Juke": "https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/14q4/638371/2015-nissan-juke-official-photos-and-info-news-car-and-driver-photo-650808-s-original.jpg?fill=2:1&resize=1200:*",
"2021 Nissan Altima 2.0 SR": "https://s3.us-east-2.amazonaws.com/dealer-inspire-vps-vehicle-images/110007331/1N4AL4CV3MN363224/41eb0aca1aed88f4d9e1a6c5aea6111a.jpg",
"2021 Nissan Altima 2.5 Platinum": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2021-altima-11-source-1602596569.jpg?crop=0.696xw:0.696xh;0.0595xw,0.122xh&resize=640:*",
"2022 Nissan GT-R T-Spec": "https://cimg1.ibsrv.net/ibimg/hgm/1920x1080-1/100/806/2021-nissan-gt-r_100806461.jpg",
"2003 Lamborghini Gallardo" : "https://www.carsinvasion.com/gallery/2003-lamborghini-gallardo/2003-lamborghini-gallardo-01.jpg",
"2007 Lamborghini Gallardo SL" : "https://images.auto55.be/popup/29044-17_Gallardo_Superleggera.jpg",
"2008 Lamborghini Gallardo LP560-4" : "https://car-images.bauersecure.com/upload/8965/images/00015b91876e-169c-4def-8.jpg",
"2010 Lamborgini Gallardo LP570-4 SL ": "http://cloudlakes.com/data_images/models/lamborghini-gallardo-lp570-4-superleggera/lamborghini-gallardo-lp570-4-superleggera-14.jpg",
"2013 Lamborghini Gallardo LP570-4 SC" : "https://www.6speedonline.com/wp-content/uploads/2013/09/Lamborghini-Gallardo-SquadraCorse-3.jpg",
"2014 Lamborghini Huracan LP610-4" : "https://enthusiastnetwork.s3.amazonaws.com/uploads/sites/5/2015/03/2014-Lamborghini-Huracan-promo.jpg?impolicy=entryimage",
"2017 Lamborghini Huracan Performante" : "https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/news/innovation-award-2017/innovation-award.jpg",
"2001 Lamborghini Murcielago" : "https://vignette.wikia.nocookie.net/topgear/images/0/03/2002_lamborghini_murcielago_2.jpg/revision/latest?cb=20111203192849",
"2006 Lamborghini Murcielago LP640" : "http://www.lambocars.com/images/murcielago/mur640_101.jpg",
"2009 Lamborghini Murcielago LP670-4 SV" : "http://www.dragtimes.com/images/19576-2010-Lamborghini-Murcielago.jpg",
"2015 Lamborghini Aventador SV" : "https://st.motortrend.ca/uploads/sites/42/2016/02/2015-Lamborghini-Aventador-LP750-4-SV-rear-three-quarter.jpg",
"2016 Lamborghini Aventador S" : "http://imagesvc.timeincapp.com/v3/foundry/image/?q=70&w=1440&url=http%3A%2F%2Fd254andzyoxz3f.cloudfront.net%2Flamborghini-aventador-s-730-horsepower-hero.jpg",
"1971 Lamborghini Miura P400SV" : "https://rmsothebys-cache.azureedge.net/a/5/7/b/0/8/a57b0886656d42cd99fb87fd23aaa7ee0fe1b9da.jpg",
"1996 Lamborghini Diablo SV" : "https://s1.cdn.autoevolution.com/images/gallery/LAMBORGHINI-Diablo-SV-2805_12.jpg",
"1985 Lamborghini Countach LP5000s QV" : "https://s3.amazonaws.com/the-drive-staging/message-editor%2F1508165366160-countach_lp_500s.jpg",
"2020 Lamborghini Sian": "https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_detail/og_image/sian_fkp_37_og.jpg", 
"2021 Lamborghini Urus": "https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_detail/urus/2021/03_16/urus_s2_m.jpg",
"2021 Lamborghini Huracan Evo": "https://www.motortrend.com/uploads/sites/5/2020/12/2020-Lamborghini-Huracan-Evo-AWD-17.jpg?fit=around%7C875:492",  
"1995 Lamborghini Diablo SE30 Jota": "https://www.lambocars.com/wp-content/uploads/2021/03/yavg41uh1oe61.jpg", 
"2000 Lamborghini Diablo GTR": "https://cdn.motor1.com/images/mgl/o7re0/s1/1999-lamborghini-diablo-gtr.webp", 
"2017 Bentley Continental GT" : "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/17q3/685272/2019-bentley-continental-gt-photos-and-info-news-car-and-driver-photo-689618-s-original.jpg",
"2015 Bentley Bentayga" : "https://www.gannett-cdn.com/-mm-/fc3a8bd2914cc900b105edb76c86789f4bf5114c/c=426-2775-4596-5131/local/-/media/2015/09/10/USATODAY/USATODAY/635775007438491082-18183961255ef021973748.jpg?width=3200&height=1680&fit=crop",
"2015 Koenigsegg Regera" : "https://cdn1.mestmotor.se/YTo2OntzOjI6ImlkIjtpOjEwMzg5NzM7czoxOiJ3IjtpOjMyMDA7czoxOiJoIjtpOjMyMDA7czoxOiJjIjtpOjA7czoxOiJzIjtpOjA7czoxOiJrIjtzOjQwOiI5YTM0Zjc3YmZkMmFhNzRkMDhmZTUwZWNjOWU0ZTJhMzIzMTBiN2Q2Ijt9",
"2010 Koenigsegg Agera" : "https://i.wheelsage.org/pictures/koenigsegg/agera/autowp.ru_koenigsegg_agera_14.jpg",
"2007 Koenigsegg CCX" : "https://pictures.topspeed.com/IMG/jpg/201605/2007-koenigsegg-ccx-20.jpg",
"2005 Bugatti Veyron 16.4" : "http://www.carsaddiction.com/files/cars/05__Veyron_16.4.jpg",
"2016 Bugatti Chiron" : "https://pictures.topspeed.com/IMG/jpg/201602/2018-bugatti-chiron-10.jpg",
"2017 Porsche 911 GT2 RS" : "https://files1.porsche.com/filestore/image/multimedia/none/jdp-2016-modelseries-911-gt2-rs-intro-01/normal/097b0fad-a8f5-11e7-b591-0019999cd470/porsche-normal.jpg",
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : "https://www.cstatic-images.com/stock/1170x1170/39/img2003469154-1500663386739.JPG",
"2016 Porsche 911 Turbo" : "https://st.motortrend.com/uploads/sites/10/2015/09/2015-Porsche-911-Turbo-S-front-three-quarter-in-motion.jpg",
"2016 Porsche 718 Boxster" : "https://www.carmagazine.co.uk/Images/PageFiles/28157/boxstersrev-003.jpg",
"2017 Porsche 718 Cayman GTS" : "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/high-718-cayman-gts-ascari-2017-porsche-ag-1524665294.jpg",
"1975 Porsche 911 Turbo" : "https://rmsothebys-cache.azureedge.net/4/f/0/d/0/4/4f0d04fe90a9d94b0c4552c9c889442052c70c52.jpg",
"1995 Porsche 911 GT2" : "https://cimg3.ibsrv.net/ibimg/hgm/1200x675-1/100/564/1995-porsche-911-carrera_100564771.jpg",
"1987 Porsche 959" : "https://rmsothebys-cache.azureedge.net/f/4/a/d/c/7/f4adc7d4d3040bad68198abdd61489fb15591865.jpg",
"1999 Porsche 911 GT3" : "https://s1.cdn.autoevolution.com/images/gallery/PORSCHE-911-GT3--996--2925_29.jpg",
"1980 Porsche 924 Turbo": "https://bringatrailer.com/wp-content/uploads/2018/11/1980_porsche_924_turbo_1544658730f6b34c98988F952F33-FC0A-41FF-AE0E-7F5146650B49.jpeg",
"2015 Lotus Evora 400" : "http://cdn.luxuo.com/2015/03/Lotus-Evora-400-Geneva-Motor-Show.jpg",
"2011 Lotus Exige S" : "https://www.lotustalk.com/forums/attachment.php?attachmentid=437633&stc=1&d=1409609070",
"1996 Lotus Esprit V8" : "https://topgear.wwmindia.com/content/2018/nov/1996lotusespritv8twinturboside13000px1542863568.jpg",
"2006 Lotus Elise S" : "https://i.redd.it/x065eeapwtp11.jpg",
"2018 Mazda Miata MX-5 Club" : "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/media/705090/2018-mazda-mx-5-miata-warranty-review-car-and-driver-photo-705119-s-original.jpg",
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : "http://zombdrive.com/images/2004-mazda-mazdaspeed-mx-5-miata-1.jpg",
"1989 Mazda MX-5 Miata" : "https://s1.cdn.autoevolution.com/images/news/gallery/here-s-how-the-mazda-mx-5-miata-has-evolved-over-the-course-of-four-generations_3.jpeg",
"1989 Mazda RX-7 Savanna Turbo" : "http://garagedreams.net/wp-content/uploads/2018/02/1987-mazda-rx7-turbo-ii-turbo-2-t2-tii-87-s4-fc-13b-87-5.jpg",
"1992 Mazda RX-7" : "https://d32c3oe4bky4k6.cloudfront.net/articles-videos/-/media/uscamediasite/images/story-images/2018/05/mazda-rx7(31).ashx?modified=20180508133336&mw=1920&hash=D41DF1DAF9737C4C085CFBF911EEF0737BFAD490",
"1998 Mazda RX-7 RZ" : "https://pictures.topspeed.com/IMG/jpg/200512/2001-mazda-rx7-8.jpg",
"2001 Mazda RX-7 Spirit R Type A" : "https://cdntdreditorials.azureedge.net/cache/f/8/f/6/b/0/f8f6b07d6a379917f777aeeb07da1d20dac78a77.jpg",
"2009 Mazda RX-8" : "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/08q4/267373/2009-mazda-rx-8-r3-photo-232690-s-original.jpg",
"2019 Mazda6 Signature": "https://st.motortrend.com/uploads/sites/5/2018/05/2018-Mazda6-Signature-25T-front-three-quarter-09.jpg",
"2019 Mazda3 Hatch": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2020-mazda-3-hatchback-1569347781.jpg",
"2019 Mazda CX-5": "https://st.motortrend.com/uploads/sites/5/2019/01/2019-Mazda-CX-5-Turbo-front-three-quarter-in-motion-1.jpg",
"2019 Mazda CX-3": "https://cmsimages-alt.kbb.com/content/dam/kbb-editorial/make/mazda/cx-3/2019/01-2019-mazda-cx-3.jpg",
"2014 Mazda2": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/2015_Mazda2_%28DJ%29_Genki_hatchback_%282018-08-27%29_01.jpg/1200px-2015_Mazda2_%28DJ%29_Genki_hatchback_%282018-08-27%29_01.jpg",
"2015 Mazda5": "https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/15q2/657948/2015-mazda-5-review-car-and-driver-photo-659159-s-original.jpg",
"2006 Mazdaspeed 6 GT": "https://pictures.topspeed.com/IMG/jpg/200603/2006-mazdaspeed6-2.jpg",
"2013 Mazdaspeed 3": "https://www.davisenterprise.com/files/2013/03/15mazdaW.jpg",
"2001 Mazda RX-7 Spirit R Type A" : "https://pictures.topspeed.com/IMG/jpg/200512/2001-mazda-rx7-6.jpg",
"2018 Morgan Three-Wheeler" : "https://i.ytimg.com/vi/3h5SvK0k0ww/maxresdefault.jpg",
"1998 Subaru Impreza 22B STi": "https://cdn.motor1.com/images/mgl/1WOGL/s1/1998-subaru-impreza-22b-sti.jpg",
"1995 Subaru Impreza WRX STi Version II": "https://upload.wikimedia.org/wikipedia/commons/1/10/1995_WRX_STI_RA_GC8.jpg",
"2002 Subaru Impreza WRX STi": "https://www.wallpaperup.com/uploads/wallpapers/2014/02/08/249885/d221d707d9368aee2c00ce0ada73d87a.jpg",
"2003 Subaru Impreza WRX STi": "https://upload.wikimedia.org/wikipedia/commons/8/86/04-05_Subaru_WRX_STi_2.jpg",
"2005 Subaru Impreza WRX STi": "https://www.conceptcarz.com/images/Subaru/06_subaru_wrx_sti_manu_b003.jpg",
"2010 Subaru Impreza WRX STi R205": "https://pictures.topspeed.com/IMG/jpg/201001/subaru-impreza-r205.jpg",
"2019 Subaru WRX STi": "https://cdn.drivemag.net/media/default/0001/85/2019-Subaru-WRX-STI-0-2853-default-large.jpeg",
"1993 Subaru SVX": "https://cdn.discordapp.com/attachments/464222580195459081/522217668305092609/image0.jpg",
"2000 Subaru Forester STI": "https://static.carthrottle.com/workspace/uploads/garage/img_20141025_153023-54ff32355e938.jpg",
"2019 Subaru WRX": "https://www.iihs.org/api/ratings/model-year-images/2956",
"2022 Subaru WRX": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2022-subaru-wrx-9-1631124812.jpg?crop=0.506xw:0.438xh;0.255xw,0.268xh&resize=1200:*",
"2018 Subaru BRZ": "https://media.ed.edmunds-media.com/subaru/brz/2018/oem/2018_subaru_brz_coupe_limited_fq_oem_1_600.jpg",
"2022 Subaru BRZ Premium": "https://www.subaru.com/content/dam/subaru/special_series/2022-brz/Track_tested_1920x1200.jpg",
"2022 Subaru BRZ Limited": "https://www.motortrend.com/uploads/sites/5/2020/11/2022-Subaru-BRZ-4.jpg?fit=around%7C875:492.1875",
"1988 Isuzu Impulse": "http://momentcar.com/images/isuzu-impulse-1988-5.jpg",
"1979 Isuzu 117 Coupe": "https://upload.wikimedia.org/wikipedia/commons/7/71/1968-1972_Isuzu_117_Coupe.jpg",
"1994 Mitsubishi Lancer Evo II": "https://s1.cdn.autoevolution.com/images/news/gallery/mitsubishi-lancer-evolution-through-the-years_4.jpg",
"2010 Mitsubishi Lancer Evo X GSR": "https://s1.cdn.autoevolution.com/images/news/gallery/mitsubishi-lancer-evolution-through-the-years_42.jpg",
"1999 Mitsubishi Lancer Evo VI GSR": "https://s1.cdn.autoevolution.com/images/news/gallery/mitsubishi-lancer-evolution-through-the-years_23.jpg",
"2004 Mitsubishi Lancer Evo VIII MR FQ400": "https://avatars.mds.yandex.net/get-pdb/69339/e98a87b7-786a-4872-a531-1adcf85f9505/s1200",
"2003 Mitsubishi Lancer Evo VIII GSR": "https://s1.cdn.autoevolution.com/images/gallery/MITSUBISHILancerEvolutionVIII-379_7.jpg",
"1994 Mitsubishi 3000 GT VR-4": "https://www.thetruthaboutcars.com/wp-content/uploads/2017/03/00808_j2JdOPlme8R_1200x900.jpg",
"1994 Mitsubishi FTO GPX": "http://www.roadsmile.com/images/mitsubishi-fto_key_10.jpg",
"1992 Mitsubishi Galant VR-4": "https://i.ytimg.com/vi/kDvOBQB6oKA/maxresdefault.jpg",
"1974 VAZ Lada 1200": "https://upload.wikimedia.org/wikipedia/commons/e/e5/1980_-_VAZ_2101.JPG",
"1975 UAZ-469": "https://i.ytimg.com/vi/k6FRdbv_qUA/maxresdefault.jpg",
"1965 GAZ Volga 21": "https://upload.wikimedia.org/wikipedia/commons/0/06/GAZ-21_%283rd_generation%29_%22Volga%22_in_Beroun_%28as_DOD_probotrans_expon%C3%A1t%29.jpg",
"1995 Hyundai Sonata 2.0i": "https://s1.cdn.autoevolution.com/images/gallery/HYUNDAI-Sonata-3205_5.jpeg",
"2013 Hyundai Genesis Coupe 3.8" : "http://4.bp.blogspot.com/-ph3n1fSVY2M/UAjQwQLuk-I/AAAAAAAAE9U/6M6_Z_CwIqA/s1600/2013-Hyundai-Genesis-Coupe-3.8-Track-front.jpg",
"2013 Hyundai Elantra GT": "http://autogeeze.techgeezecom.netdna-cdn.com/wp-content/uploads/2012/02/2013-Hyundai-Elantra-GT_002.jpg?x93271",
"2017 Hyundai Sonata Limited": "https://i.ytimg.com/vi/Ma0Lwz0txU8/maxresdefault.jpg",
"2018 Kia Stinger GT": "https://cdn.arstechnica.net/wp-content/uploads/2017/11/Kia-Stinger-5.jpg",
"2017 Kia Optima SX 2.0T": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/15q3/660572/2016-kia-optima-sx-20t-test-review-car-and-driver-photo-662265-s-original.jpg",
"2005 Hyundai Tiburon GT V6": "https://static.cargurus.com/images/site/2009/07/21/15/24/2005-hyundai-tiburon-gt-pic-40276-1600x1200.jpeg",
"2006 Audi R8": "http://xdesktopwallpapers.com/wp-content/uploads/2012/02/2006%20Audi%20R8%20Front%20Side%20Pose%20In%20Silver.jpg",
"2008 Audi R8 V10": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/09q1/267374/2010-audi-r8-52-v10-fsi-quattro-review-car-and-driver-photo-258862-s-original.jpg",
"2010 Audi R8 GT": "http://i.wheelsage.org/pictures/a/audi/r8_gt_eu-spec/audi_r8_gt_eu-spec_17.jpeg",
"2012 Audi R8 Plus": "https://www.ultimatecarpage.com/images/car/5239/Audi-R8-V10-plus-41579.jpg",
"2015 Audi R8 Coupe 5.2 FSI quattro": "https://upload.wikimedia.org/wikipedia/commons/3/36/2015_Audi_R8_Coup%C3%A9_5.2_FSI_quattro_%2819409896583%29.jpg", 
"1994 Audi RS2 Avant": "http://www.carthrottle.com/wp-content/uploads/2013/04/favcars.com_.jpg",
"2018 Audi RS5": "https://d2zibb626snxaq.cloudfront.net/wp-content/uploads/2018/08/27060742/2018-audi-rs5-first-drive-review-car-and-driver-photo-684420-s-original.jpg",
"2018 Audi RS3": "https://cdn.motor1.com/images/mgl/bJp6k/s1/2018-audi-rs3-second-drive.jpg",
"2018 Audi RS7": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/16q1/665019/2016-audi-rs7-performance-first-drive-review-car-and-driver-photo-665521-s-original.jpg",
"2018 Audi RS6 Avant": "https://www.carmagazine.co.uk/Images/PageFiles/78032/Audi_RS6_Perf_11.jpg",
"2018 Audi TTRS": "https://images.hgmsites.net/hug/2018-audi-tt_100616104_h.jpg",
"2018 Mercedes-AMG E63 S 4Matic": "https://cdn.motor1.com/images/mgl/1Wr73/s1/2017-mercedes-amg-e63-sedan.jpg",
"2018 Mercedes-Maybach S560": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/wp-content/uploads/2018/01/2018-Mercedes-Maybach-S560-4Matic-116.jpg",
"2018 Mercedes-AMG S65 Sedan": "https://cdn.motor1.com/images/mgl/ME9zY/s1/2018-mercedes-amg-s65-review.jpg",
"1990 Mercedes-Benz 190E Evolution II": "http://imagesvc.timeincapp.com/v3/foundry/image/?q=70&w=1440&url=http%3A%2F%2Fd254andzyoxz3f.cloudfront.net%2F051216-mercedes-evo-ebay-hero.jpg",
"2016 Mercedes-AMG GT S": "https://di-uploads-pod7.s3.amazonaws.com/autohausonedens/uploads/2016/08/2016-AMG-GTS-CLASS-COUPE-GALLERY-019-WR-D.jpg",
"2013 Mercedes-Benz SLS AMG GT": "http://www.musclecarszone.com/wp-content/uploads/2013/06/Mercedes-Benz-SLS-AMG-GT-2013-front-angle.jpg",
"2012 Mercedes-Benz C63 AMG Black Series": "https://st.automobilemag.com/uploads/sites/11/2011/12/2013-Mercedes-Benz-C63-AMG-Coupe-Black-Series-Side-In-Motion-2.jpg",
"2000 Mercedes-Benz C32 AMG": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Mercedes-Benz_C32_AMG_--_06-10-2011.jpg",
"2020 Mercedes-AMG A35 4Matic": "https://cdn.motor1.com/images/mgl/pO0M1/s1/2020-mercedes-amg-a-35-live-shots.jpg",
"2020 Chevy Corvette C8 Stingray Z51": "https://cdn.motor1.com/images/mgl/4glJz/s1/2020-chevrolet-corvette-stingray.jpg",
"2019 Chevy Corvette C7 ZR1": "https://i.kinja-img.com/gawker-media/image/upload/s--1eq2aLq2--/c_scale,f_auto,fl_progressive,q_80,w_800/sgzglm93ovspfpnblzuv.jpg",
"2018 Chevy Corvette C7 ZO6": "https://www.legacydiecast.com/product_images/71260.jpg",
"2018 Chevy Corvette C7 Stingray": "https://www.corvette-web-central.com/images/2014-Chevrolet-Corvette-109-medium.jpg",
"1953 Chevy Corvette": "https://ccmarketplace.azureedge.net/cc-temp/listing/64/6134/1417819-1953-chevrolet-corvette-std.jpg",
"1960 Chevy Corvette C1": "https://i.pinimg.com/originals/4e/93/7e/4e937e81b132b2f27e14cf6ad253a918.jpg",
"1963 Chevy Corvette C2 Stingray 427": "https://www.wsupercars.com/wallpapers/Chevrolet/1966-Chevrolet-Corvette-Stingray-427-V1-1080.jpg",
"1967 Chevy Corvette C3 327": "https://i.ytimg.com/vi/rglAzb8OIQw/maxresdefault.jpg",
"1970 Chevy Corvette C3 454": "https://i.ytimg.com/vi/TIH85jj8eYA/maxresdefault.jpg",
"1984 Chevy Corvette C4": "https://www.wsupercars.com/wallpapers/Chevrolet/1984-Chevrolet-Corvette-Coupe-V3-1080.jpg",
"1988 Chevy Corvette C4 ZR1": "https://assets.hemmings.com/blog/wp-content/uploads//2015/08/1990-Corvette-ZR1-C5909-R774-0007.jpg",
"2001 Chevy Corvette C5": "https://www.corvsport.com/wp-content/uploads/2017/02/2001-Chevrolet-Corvette-Coupe-left-front-1-2.jpg",
"2002 Chevy Corvette C5 Z06": "https://pictures.topspeed.com/IMG/jpg/200604/2001-chevrolet-corvette-z-26.jpg",
"2007 Chevy Corvette C6": "https://static.cargurus.com/images/site/2009/03/29/16/30/2007_chevrolet_corvette_convertible-pic-49693-1600x1200.jpeg",
"2007 Chevy Corvette C6 Z06": "https://www.corvsport.com/wp-content/uploads/2017/03/Screenshot-2017-03-06-22.39.46.png",
"2007 Chevy Corvette C6 ZR1": "https://cdn.motor1.com/images/mgl/ekYE/s1/2007-25579-2009-corvette-zr11.jpg",
"2018 Chevy Camaro 1LE": "https://cdn.motor1.com/images/mgl/jAjO7/s1/2017-chevrolet-camaro-1le-first-drive.jpg",
"2018 Chevy Camaro ZL1": "https://cdn.motor1.com/images/mgl/2ylGk/s1/2018-chevy-camaro-zl1-1le-first-drive.jpg",
"1969 Chevy Camaro SS 396": "https://www.dreamcarsellers.com/galleria_images/70/70_main_l.jpg",
"2017 Chevy Malibu 1.5 Turbo": "https://media.chevrolet.com/content/dam/Media/images/US/Vehicles/Chevrolet/Cars/Malibu/2016/Product/2016-Chevrolet-Malibu-024.jpg",
"2016 Chevy Malibu 2LT": "http://enthusiastnetwork.s3.amazonaws.com/uploads/sites/11/2015/12/2016-Chevrolet-Malibu-front-three-quarter-03.jpg",
"2017 Chevy Cruze Hatch Premier": "https://cdn.motor1.com/images/mgl/jZpwg/s1/2017-chevrolet-cruze-hatchback-review.jpg",
"2016 Chevy Impala LT": "https://static.cargurus.com/images/site/2015/06/16/12/59/2016_chevrolet_impala-pic-9060814503929031225-1600x1200.jpeg",
"2018 Alfa Romeo 4C": "https://i.ytimg.com/vi/-9FjlW-8zto/maxresdefault.jpg",
"2018 Alfa Romeo Giulia Quadrifoglio": "https://hips.hearstapps.com/hmg-prod/images/alfa-romeo-gtv-illo-christianschulte-1530629520.jpg",
"2018 Alfa Romeo Stelvio Quadrifoglio": "https://i.gaw.to/content/photos/32/69/326947_2018_Alfa_Romeo_Stelvio.jpg",
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": "https://s1.cdn.autoevolution.com/images/testdrive/gallery/alfa-romeo-giulietta-1750-tbi-quadrifoglio-verde-2011-741_1.jpg",
"2013 Alfa Romeo MiTo 1.4 8v": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Alfa_Romeo_MiTo_1.3_JTDm.JPG/1200px-Alfa_Romeo_MiTo_1.3_JTDm.JPG",
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": "http://www.hdcarwallpapers.com/walls/alfa_romeo_brera_s_2-wide.jpg",
"2006 Alfa Romeo 8c Competizione": "https://cdn.motor1.com/images/mgl/pnKr/s3/2008-13898-alfa-romeo-8c-competizione1.jpg",
"1992 Alfa Romeo 155 Q4": "https://c1.staticflickr.com/9/8725/16811318546_144670c2d7_b.jpg",
"1985 Alfa Romeo Spider Veloce": "https://www.dreamcarsellers.com/galleria_images/359/359_p7_l.jpg",
"2017 Suzuki Swift Sport": "https://car-images.bauersecure.com/pagefiles/74481/zsuzukiswiftsport.jpg",
"2016 Suzuki Alto Works": "https://s1.cdn.autoevolution.com/images/news/2015-suzuki-alto-turbo-rs-is-pocket-racer-from-japan-video-photo-gallery-93149_1.jpg",
"2016 Suzuki Hustler G 4WD": "https://i.pinimg.com/originals/2b/01/ab/2b01abc8835656cf7529091db86730a9.jpg",
"2003 Suzuki Liana 1.6 Sedan": "https://s1.cdn.autoevolution.com/images/gallery/SUZUKI-Aerio---Liana-Sedan-608_16.jpeg",
"1995 Suzuki Samurai 1.3i": "http://www.profun4x4.fr/site/images/normal/Nos-vehicules-d-occasion-4X45abe467d88dc2.JPG",
"2002 Suzuki Grand Vitara": "http://zombdrive.com/images/2002-suzuki-grand-vitara-3.jpg",
"2018 Pagani Huayra BC": "https://ag-spots-2018.o.auroraobjects.eu/2018/03/06/other/2880-1800-crop-pagani-huayra-bc-macchina-volante-c554606032018134038_1.jpg",
"2013 Pagani Huayra": "https://i.pinimg.com/originals/48/1a/35/481a35c067e9809198c187eb0919005d.jpg",
"2010 Pagani Zonda Cinque": "https://s1.cdn.autoevolution.com/images/gallery/PAGANI-Zonda-Cinque-Roadster-4141_5.jpg",
"2005 Pagani Zonda F": "https://pictures.topspeed.com/IMG/jpg/200511/2005-pagani-zonda-f-4.jpg",
"1999 Pagani Zonda C12S": "http://auto-database.com/image/pagani-zonda-c12-1999-134664.jpg",
"1970 AMC AMX": "https://cdn1.mecum.com/auctions/ha0417/ha0417-280237/images/ha0417-280237_1@2x.jpg?1488906383000",
"1972 AMC Javelin": "https://upload.wikimedia.org/wikipedia/commons/5/55/1971_AMC_Javelin_SST_red_Kenosha_street.JPG",
"1969 AMC Ambassador": "https://upload.wikimedia.org/wikipedia/commons/6/6c/1969_AMC_Ambassador_SST_sedan_with_custom_package_at_2015_AMO_meet-01.jpg",
"1970 AMC Rebel The Machine": "http://www.classiccarweekly.net/wp-content/uploads/2017/06/1970-AMC-Rebel-Machine.jpg",
"1975 AMC Pacer X": "http://cdn2.3dtuning.com/info/AMC%20Pacer%20X%201975%203%20Door%20Hatchback/factory/1.jpg",
"2018 Dodge Challenger SRT Hellcat Widebody": "https://pictures.topspeed.com/IMG/jpg/201706/dodge-challenger-srt-14.jpg",
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": "https://i.ytimg.com/vi/5jviIjjhfSk/maxresdefault.jpg",
"2018 Dodge Challenger SRT Demon": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/17q2/678296/2018-dodge-challenger-srt-demon-photos-and-info-news-car-and-driver-photo-678846-s-original.jpg",
"2008 Dodge Challenger SE": "https://upload.wikimedia.org/wikipedia/commons/0/09/2009_Dodge_Challenger_SE.jpg",
"2008 Dodge Challenger SRT8": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/08q3/204637/2008-dodge-challenger-srt8-photo-204655-s-original.jpg",
"2018 Dodge Charger Hellcat": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/17q2/678295/2017-dodge-charger-srt-hellcat-review-car-and-driver-photo-685161-s-original.jpg",
"2018 Dodge Charger GT Plus": "https://hips.hearstapps.com/hmg-prod/images/2018-dodge-charger-gt-awd-placement-1528477437.jpg",
"2011 Dodge Charger SRT8": "https://pictures.topspeed.com/IMG/jpg/201102/dodge-charger-srt8-7.jpg",
"2005 Dodge Charger SRT8": "https://pictures.topspeed.com/IMG/jpg/200607/2006-dodge-charger-srt8-7.jpg",
"2017 Dodge Viper ACR": "https://st.motortrend.com/uploads/sites/10/2016/08/2017-Dodge-Viper-ACR-with-Extreme-Aero-package-front-three-quarter.jpg",
"2017 Dodge Viper GTS": "https://st.motortrend.com/uploads/sites/10/2016/08/2017-Dodge-Viper-GTS-front-three-quarter-in-motion.jpg",
"2012 Dodge Dart R/T": "http://carinpicture.com/wp-content/uploads/2012/07/Dodge-Dart-RT-2012-Photo-06.jpg",
"2010 Dodge Avenger Express": "https://images-na.ssl-images-amazon.com/images/I/718L8Ib3cZL.jpg",
"2008 Dodge Journey SXT": "https://s1.cdn.autoevolution.com/images/gallery/DODGE-Journey-3843_34.jpeg",
"2007 Dodge Nitro 4.0 R/T": "https://i.ytimg.com/vi/Q21WjGwGkPQ/maxresdefault.jpg",
"2007 Dodge Viper SRT-10": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/02q4/267343/dodge-viper-srt-10-photo-6196-s-original.jpg",
"2007 Dodge Viper SRT10 ACR": "https://cdn.motor1.com/images/mgl/Pe0A/s1/2007-277441.jpg",
"2000 Dodge Intrepid R/T": "http://zombdrive.com/images/2000-dodge-intrepid-7.jpg",
"2003 Dodge Neon SRT-4": "https://pictures.topspeed.com/IMG/jpg/200608/2003-dodge-neon-srt4-13.jpg",
"1970 Dodge Dart Hemi Super Stock": "https://cdn1.mecum.com/auctions/fl0116/fl0116-229806/images/fl0116-229806_1@2x.jpg?1448925862000",
"1970 Dodge Dart Swinger 340": "https://cdn1.mecum.com/auctions/sc0513/sc0513-153831/images/sc0513-153831_1@2x.jpg?1368748030000",
"1970 Dodge Challenger R/T 426 Hemi": "https://cdn1.mecum.com/auctions/fl0116/fl0116-229825/images/fl0116-229825_1@2x.jpg?1466954242000",
"1969 Dodge Charger Daytona Hemi": "http://www.musclecarszone.com/wp-content/uploads/2013/07/1969-Dodge-Charger-Daytona-Hemi.jpg",
"1969 Dodge Charger R/T Hemi":"http://www.onallcylinders.com/wp-content/uploads/2017/07/20/1969-Dodge-Charger-RT-by-Terry-Shea-Parental-Guidance.jpg",
"2018 Mclaren Senna": "https://cdn.motor1.com/images/mgl/GO0WG/s1/2018-mclaren-senna.jpg",
"2018 McLaren 720S": "https://hips.hearstapps.com/amv-prod-cad-assets.s3.amazonaws.com/images/17q2/678295/2018-mclaren-720s-first-drive-review-car-and-driver-photo-680456-s-original.jpg",
"2015 McLaren 570S": "https://www.carmagazine.co.uk/Images/PageFiles/20771/McLaren-570S-52.jpg",
"2013 McLaren MP4-12C": "https://www.autoguide.com/blog/wp-content/uploads/2017/10/2013-McLaren-MP4-12C-Retro-6.jpg",
"1992 McLaren F1": "https://www.supercars.net/blog/wp-content/uploads/2016/03/Screenshot-2016-03-24-12.48.38.png",
"1997 McLaren F1 GT": "https://pictures.topspeed.com/IMG/jpg/201508/mclaren-f1-gt.jpg",
"1995 McLaren F1 LM": "https://cars.mclaren.com/files/live/sites/mclaren/files/cars-mclaren-com-Main/Featured%20Articles/Road%20Racer%20F1%20LM/F1LM%20Front.jpg?t=w1440",
"2013 McLaren P1": "https://www.supercars.net/blog/wp-content/uploads/2016/04/2013_McLaren_P1-1-1536.jpg",
"1974 MG Midget": "http://bestcarmag.com/sites/default/files/1974-mg-midget-1314013-570624.jpg",
"1928 MG M-Type Midget": "https://www.carolenash.com/wp-content/uploads/2017/09/history-mg-m-midget.jpg",
"2007 Aston Martin DBS": "http://cdntbs.astonmartin.com/sitefinity/beauty/rga_astonmartin_cars_beauty_dbscoupe_03.jpg?sfvrsn=0",
"2016 Aston Martin DB11": "https://st.motortrend.ca/uploads/sites/10/2016/10/2017-Aston-Martin-DB11-front-three-quarter-in-motion-02-3.jpg",
"2016 Aston Martin V12 Vantage S": "http://bestcarmag.com/sites/default/files/2016-aston-martin-v12-vantage-s-1879689-7796850.jpg",
"2018 Aston Martin DBS Superleggera": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2019-aston-martin-dbs-superleggera-placement-1529685438.jpg",
"2013 Aston Martin V8 Vantage": "https://st.motortrend.com/uploads/sites/10/2015/09/2014-Aston-Martin-V8-Vantage-three-quarters-back-side-view-001.jpg",
"2011 Aston Martin One-77": "https://2.bp.blogspot.com/_3Nq7CKYaRdQ/TJ85hueSBUI/AAAAAAAAU4s/xjqWIJC6dro/s1600/aston-martin-one-77.jpg",
"2004 Aston Martin Vanquish S": "http://i.wheelsage.org/pictures/a/aston_martin/vanquish/aston_martin_v12_vanquish_s_1.jpg",
"2008 Aston Martin DB9": "http://bestcarmag.com/sites/default/files/489700aston-martin_db9_2006_wallpapers_1.jpg",
"2019 Aston Martin Valkyrie": "https://car-images.bauersecure.com/pagefiles/31389/01_aston_martin_valkyrie.jpg",
"2018 Range Rover Supercharged": "https://st.motortrend.com/uploads/sites/11/2017/06/Range-Rover-SVO-Design-Pack.jpg",
"2018 Range Rover Velar R-Dynamic": "https://599b5008ca72485ab0d3-38ace3a7b08bb983087bc3af7dc82f19.ssl.cf1.rackcdn.com/SALYL2EX3KA779511/ddf6f7148ada9e8f9505e865ffce9517.jpg",
"2018 Range Rover Sport SVR": "https://cdn2.autoexpress.co.uk/sites/autoexpressuk/files/2018/03/rrs_svr_velocityblue_001.jpg",
"2016 Land Rover Defender 70th Edition": "https://assets.hemmings.com/blog/wp-content/uploads//2018/01/lrclassicdefenderworksv817011804.jpg",
"1957 Land Rover Series 1": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Land_Rover_Series_I.jpg",
"2003 Infiniti G35": "https://static.cargurus.com/images/site/2009/01/25/02/29/2003_infiniti_g35_coupe-pic-27424-1600x1200.jpeg",
"2017 Infiniti Q60 Red Sport": "https://cdn.motor1.com/images/mgl/PRXvW/s1/2018-infiniti-q60s-review.jpg",
"2015 Infiniti Q50 Eau Rouge": "https://enthusiastnetwork.s3.amazonaws.com/uploads/sites/5/2014/06/Infiniti-Q50-Eau-Rouge-concept-in-Hong-Kong.jpg?impolicy=entryimage",
"2019 Infiniti Q50": "https://www.louisvilleinfiniti.com/inventoryphotos/2204/jn1ev7ar4km555352/ip/14.jpg",
"2019 Tesla Model S Ludicrous Performance": "https://ev-database.org/img/auto/Tesla_Model_S_2016/Tesla_Model_S_2016-01.jpg",
"2019 Tesla Model S Standard Range": "https://d3h256n3bzippp.cloudfront.net/models-75d-white_190218_162125.jpg",
"2019 Tesla Model 3 Performance": "https://cnet2.cbsistatic.com/img/mWQ4Pj9hEsqGX3XPGWR4ZpeB9wg=/2018/07/22/d57d15f6-c6dd-4aa7-9452-3d639c52b5c1/003-tesla-model-3-performance.jpg",
"2019 Tesla Model 3 Standard Range": "https://di-uploads-pod5.dealerinspire.com/currentautomotive1/uploads/2019/04/Header-Image-1024x683.png",
"2019 Tesla Model X Ludicrous Performance": "https://st.motortrend.com/uploads/sites/5/2016/03/2016-Tesla-Model-X-P90D-front-three-quarter-in-motion-turn-e1459445400802.jpg?fit=around|875:492",
"2019 Tesla Model X Standard Range": "https://ev-database.org/img/auto/Tesla_Model_X/Tesla_Model_X-01.jpg",
"2019 Mini Cooper S": "https://static.cargurus.com/images/site/2018/04/11/16/46/2019_mini_cooper-pic-5038995412468575912-1600x1200.png",
"2019 Mini John Cooper Works": "https://cdn.motor1.com/images/mgl/eLOnA/s1/2019-mini-cooper-john-cooper-works.jpg",
"1969 Morris Mini Cooper S": "https://www.historics.co.uk/media/1591026/1969-morris-mini-cooper-s-mk-ii-1.jpg?anchor=center&mode=crop&width=1000",
"2020 Cadillac CT4-V": "https://www.thedetroitbureau.com/wp-content/uploads/2020/07/2020-Cadillac-CT4-V-rear.jpg",
"2019 Cadillac CTS-V": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/3-2018-cadillac-cts-v-jameslipman-slide2-1527109001.jpg?crop=1.00xw:0.822xh;0,0.154xh&resize=1200:*",
"2019 Cadillac CTS 3.6L V6": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2017-cadillac-cts-rwd-v6-1545072218.jpg?crop=0.819xw:1.00xh;0.0929xw,0&resize=640:*",
"2019 Cadillac ATS-V Coupe": "https://media-cf.assets-cdk.com/websites/content/95ba37b22e3b4f919f17f3f61bcaffb8_c0x0-900x386_x900.jpg",
"2016 Cadillac ELR": "https://media.ed.edmunds-media.com/cadillac/elr/2016/oem/2016_cadillac_elr_coupe_base_fq_oem_2_1600.jpg",
"2020 Cadillac CT6 Platinum": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2020-cadillac-ct6-v-3-front-quarter-1564851658.jpg?crop=0.843xw:0.632xh;0.149xw,0.224xh&resize=1200:*",
"2020 Cadillac Escalade": "https://gmauthority.com/blog/wp-content/uploads/2019/06/2019-Cadillac-Escalade-Sport-Edition-exterior-04.jpg",
"2020 Cadillac XT5": "https://cdn.jdpower.com/JDPA_2020%20Cadillac%20XT5%20Premium%20Luxury%20350T%20Silver%20Front%20View.jpg",
"2014 Cadillac CTS-V Sport Wagon": "https://i.kinja-img.com/gawker-media/image/upload/c_scale,f_auto,fl_progressive,pg_1,q_80,w_800/v09luud5jfl7n7r4b0jl.jpg",
"2004 Cadillac Seville": "https://www.cstatic-images.com/stock/400x500/232393.png",
"2011 Cadillac DTS": "https://spct2000.files.wordpress.com/2015/02/2011-cadillac-dts-sedan-1sa-4dr-sedan-exterior-1.jpg",
"1975 Cadillac Fleetwood Brougham": "https://cdn.dealeraccelerate.com/pedigree/1/506/7537/1920x1440/1975-cadillac-fleetwood-brougham",
"1976 Cadillac Eldorado": "https://automotivemileposts.com/eldorado/images/1976/eldo1976coupecommodoreblue.jpg",
"1959 Cadillac Eldorado Brougham": "https://live.staticflickr.com/5729/22283711010_71020cf7a2_b.jpg",
"Renault R35 Tank": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Renault-R-35-latrun-2.jpg/1200px-Renault-R-35-latrun-2.jpg",
"2019 Renault Clio Iconic TCe 100": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/11/29/14/clio-front.jpg",
"2019 Renault Clio RS Line TCe 130": "https://s35.wheelsage.org/format/picture/picture-preview-large/r/renault/clio_r.s._line/renault_clio_r.s._line_20_07ee03bb0b3f07a3.jpg",
"2019 Renault Clio E-TECH Launch Edition": "https://www.electrichunter.com/sites/default/files/field/gallery/Renault-Clio-E-Tech-hybrid-2020-car-02-245.jpg",
"2018 Renault Clio RS Trophy": "https://i.ytimg.com/vi/_sYzKrvAz5c/maxresdefault.jpg",
"2003 Renault Clio V6": "https://upload.wikimedia.org/wikipedia/commons/3/35/RenaultClioV6.jpg",
"1993 Renault Clio Williams": "https://hothatch.com.au/wp-content/uploads/2018/04/Renault-Clio-I-Williams-1.jpg",
"1993 Renault Clio": "https://static.cargurus.com/images/site/2008/07/11/03/24/1993_renault_clio-pic-61619-1600x1200.jpeg",
"1993 Renault Twingo": "https://www.carsinvasion.com/gallery/1993-renault-twingo/1993-renault-twingo-01.jpg",
"2010 Renault Twingo RS 133 Cup": "https://o.aolcdn.com/images/dims3/GLOB/legacy_thumbnail/800x450/format/jpg/quality/85/http://www.blogcdn.com/www.autoblog.com/media/2009/09/web1twingorscup.jpg",
"2010 Renault Twingo RS": "https://www.conceptcarz.com/images/Renault/Renault-Twingo_RS_2009_015-800.jpg",
"2020 Renault Twingo": "https://2021renault.com/wp-content/uploads/2019/06/2020-Renault-Twingo-Exterior.jpg",
"2020 Renault Megane RS 300 Trophy": "https://upload.wikimedia.org/wikipedia/commons/c/c6/2019_Renault_Megane_R.S._300_Trophy_1.8_Front.jpg",
"2020 Renault Megane RS Trophy R": "https://www.carpixel.net/w/d4107784ca7d764436b4286f517b134d/renault-megane-rs-trophy-r-car-wallpaper-92171.jpg",
"2020 Renault Megane RS Line TCe 140": "https://i.ytimg.com/vi/FLp7VjWMVCc/maxresdefault.jpg",
"2005 Renault Megane Sport 225 Cup": "https://parkers-images.bauersecure.com/pagefiles/194258/cut-out/570x380/ren_megane_rs06.jpg",
"LIGHNING MCQUEEN":"https://lumiere-a.akamaihd.net/v1/images/open-uri20150608-27674-1eblt9q_d27f8dc6.jpeg?region=0%2C0%2C1580%2C880",
"2018 Fortnite Shopping Cart GT-S": "https://cdn.vox-cdn.com/thumbor/1Mxus3k-y994ZrtmYpw-PLlIyiM=/0x0:1920x1080/1200x0/filters:focal(0x0:1920x1080):no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/11447765/Fortnite_05.30.2018___08.32.11.03.png",
"2019 Fortnite ATK GT-4R": "https://static3.thegamerimages.com/wordpress/wp-content/uploads/2018/08/Fortnite-ATK.jpg",
"1009 Thanos Car": "https://pbs.twimg.com/media/Dmht2YwVAAAfHN3.jpg"
}

Car_Offroad = {
"2000 Honda Integra" : 3.5,
"2000 Honda Integra Type R" : 3,
"1999 Honda Civic Type R EK9" : 3,
"2003 Honda Civic Type R EP3" : 3,
"2003 Honda NSX R" : 1,
"2001 Honda S2000" : 2,
"2021 Honda Civic Type R FK8" : 2,
"1991 Honda Civic EG6 SiR": 3,
"1999 Honda Civic LX": 3,
"2006 Honda Civic Si": 3,
"2018 Honda Civic Sport": 2.5,
"2018 Honda Civic Si Coupe": 2.5,
"2006 Honda Accord 3.0 EX": 3,
"2010 Honda Accord EX-L V6": 3,
"2015 Honda Accord Sport": 3,
"2015 Honda Accord EX-L V6": 3,
"2018 Honda Accord Sport": 3,
"2021 Honda CR-V": 5,
"1999 Honda CR-V": 6,
"2005 Honda Pilot": 5,
"2010 Honda Crosstour": 4,
"2005 Honda Element": 4.5,
"2001 Honda Odyssey Absolute": 2.5,
"2021 Honda N-ONE RS": 1,
"2021 Honda StepWGN Spada": 2,
"1999 Honda StepWGN": 3,
"2016 Honda CR-Z": 2,
"2021 Honda HR-V": 4, 
"2005 Honda Stream": 2.5,
"2014 Honda Stream": 2.5,
"2021 Honda Clarity": 2,
"2000 Honda Insight": 1,
"2021 Honda Insight": 2,
"2000 Honda ACTY": 3,
"2021 Honda ACTY": 3,
"2021 Honda Fit": 2.5,
"2001 Honda Life Dunk": 2,
"1992 Honda Vigor": 3,
"1989 Honda Accord": 3,
"2003 Acura RSX Type S" : 3,
"2017 Acura NSX" : 1,
"2005 Acura TL Type S": 2.5,
"2007 Acura TL": 3,
"2018 Acura TLX 3.5": 3,
"2018 Acura MDX": 4,
"2018 Acura ILX": 3,
"2021 Acura TLX Type S": 3,
"1995 Acura Legend": 2,
"2014 Acura TSX Sport Wagon": 3,
"1990 Ford Mustang Foxbody" : 2,
"2010 Ford Mustang GT500" : 2,
"2015 Ford Mustang GT" : 2,
"1975 Ford Pinto": 3,
"1999 Ford Crown Victoria": 3,
"2017 Ford Focus Hatch": 3,
"2017 Ford Focus RS": 3,
"2017 Ford Fusion Titanium": 3,
"2017 Ford Fusion Sport": 3,
"2018 Ford F-150 Super Cab": 6,
"2018 Ford F-150 Raptor": 9,
"2016 Shelby Mustang GT350R" : 2,
"1992 Volkswagen Golf GTi MK2" : 3.5,
"2017 Volkswagen Golf GTi MK7" : 3,
"2015 Volkswagen Scirocco R" : 3,
"2018 Volkswagen Passat R-Line": 3,
"1969 Volkswagen Beetle": 3,
"1999 BMW M3" : 2,
"2003 BMW M3" : 2,
"2008 BMW M3" : 2,
"2017 BMW M3" : 1.5,
"2005 BMW M5" : 2,
"2018 BMW M5" : 2,
"2017 BMW M4" : 1.5,
"2017 BMW M6" : 1.5,
"2018 BMW i8" : 1,
"1959 BMW 507": 1.5,
"2018 BMW 530i": 3,
"2018 BMW X3": 5,
"2018 BMW 750i": 3,
"1974 BMW 2002 Turbo": 2,
"2011 BMW 1M": 1.5,
"2018 BMW 330i": 3,
"2020 BMW M235i xDrive Gran Coupe": 4,
"2007 Saturn Ion": 3,
"2001 Saturn SL2": 3,
"1998 Saturn SW2": 3,
"2017 Ferrari 488GTB" : 1,
"2017 Ferrari F12" : 1,
"2003 Ferrari 575M Maranello" : 1.5,
"1999 Ferrari 360" : 1,
"1995 Ferrari F355" : 1,
"1965 Ferrari 250 GTO" : 1,
"1968 Ferrari Dino" : 1,
"1970 Ferrari 365 GTB/4 Daytona" : 1,
"2008 Ferrari F430" : 1,
"2008 Ferrari California" : 1,
"2016 Ferrari LaFerrari" : 1,
"2010 Ferrari 458 Italia": 1,
"1993 Toyota MR2 GT-S" : 2,
"1986 Toyota Corolla Sprinter Trueno" : 3,
"1993 Toyota Supra Twin Turbo" : 2,
"1998 Toyota Chaser Tourer V" : 3,
"1997 Toyota Soarer" : 2.5,
"1998 Toyota Altezza RS200" : 2,
"1996 Toyota Cresta 2.5 Twin Turbo": 2,
"1984 Toyota Landcruiser 60 3F" : 8.5,
"2003 Toyota Tundra" : 7,
"2018 Toyota Land Cruiser Prado" : 7.5,
"2018 Toyota 4Runner TRD Pro" : 9,
"2018 Toyota Tundra TRD Pro" : 9,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 7.5,
"2017 Toyota Century": 3,
"2019 Toyota Corolla Hatch XSE": 2,
"2019 Toyota Corolla Hatch SE": 3,
"2019 Toyota Corolla Touring Sport": 3.5,
"2021 Toyota GR Supra": 1.5,
"2008 Toyota Sequoia V8": 7,
"2005 Toyota Camry LE V6": 3,
"1999 Toyota Corolla LE": 3,
"2002 Toyota Sienna 5D Symphony": 3,
"2010 Toyota Camry LE": 3, 
"2016 Toyota Avalon Limited": 3,
"2018 Toyota Camry XSE": 3,
"2018 Toyota Corolla XLE": 3,
"1969 Toyota 2000GT": 1,
"2001 Toyota Camry LE V6": 3,
"2006 Toyota Sienna Limited": 3,
"2017 Toyota Sienna SE": 2,
"2018 Toyota Sienta": 3,
"2018 Toyota Alphard": 3,
"2018 Toyota Crown Majesta": 3,
"2018 Toyota Tundra SR5 5.7L V8": 7.5,
"2018 Toyota Hiace": 4,
"1993 Toyota Hiace": 4, 
"1997 Toyota Celica GT-Four": 5,
"1998 Toyota GT-one TS020": 1,
"2018 Toyota GT86": 2,
"1997 Toyota Tercel": 3,
"1993 Toyota Mark II Tourer V JZX90": 2,
"1997 Toyota Celica GT": 2.5,
"2016 Toyota Land Cruiser": 8.5,
"2019 Toyota Tacoma SR5": 7,
"2019 Toyota Tacoma TRD Pro": 9,
"1993 Toyota Sera": 1.5,
"2020 Toyota Avalon Touring": 3,
"2020 Toyota Avalon Limited": 3,
"2020 Toyota Avalon Limited Hybrid": 3,
"2020 Toyota Avalon TRD": 2.5,
"2020 Toyota Camry LE": 3,
"2020 Toyota Camry SE Hybrid": 3,
"2011 Toyota Prius": 2.5,
"2020 Toyota Prius XLE AWD": 4,
"2021 Toyota GR Yaris": 5,
"2022 Toyota GR86 Base": 2,
"2022 Toyota GR86 Premium": 2.5,
"2018 Toyota Camry SE": 3,
"2009 Lexus LFA" : 1,
"2007 Lexus ISF" : 2,
"1998 Lexus GS300" : 2.5,
"2018 Lexus LC500" : 2,
"2019 Lexus ES300h": 2.5,
"2018 Lexus GS F": 2,
"2003 Lexus LS430": 3,
"2019 Lexus RX350": 4,
"1999 Lexus RX300 4WD": 3.5,
"2019 Lexus LX570": 8,
"2018 Lexus LS500 AWD" : 3,
"2022 Lexus IS500 F Sport Performance": 2,
"2022 Lexus IS350 F Sport": 2,
"1990 Nissan Skyline GTR R32" : 3.5,
"1994 Nissan Skyline GTR R33 Spec-V" : 3.5,
"1999 Nissan Skyline GTR R34": 3,
"2002 Nissan Skyline GTR V-Spec II Nur" : 3,
"1996 Nissan 180SX" : 2,
"1993 Nissan Silvia K's Type S S14" : 2,
"2018 Nissan GTR Track Edition R35" : 3,
"2007 Nissan Fairlady Z" : 2,
"2018 Nissan Fairlady Z NISMO" : 2,
"2018 Nissan Fairlady Z" : 2,
"1989 Nissan 300ZX Turbo Z" : 2,
"2018 Nissan GT-R50 by Italdesign": 2,
"2018 Nissan GT-R NISMO": 2,
"2018 Nissan Maxima Platinum": 3,
"2018 Nissan Sentra SR Turbo": 3,
"2017 Nissan Leaf": 2.5,
"1973 Nissan Skyline H/T 2000GT-R": 3,
"1987 Nissan Skyline GTSR R31": 3,
"1989 Nissan Skyline GTS-4 R32": 3,
"1998 Nissan Skyline 25GT-X Turbo R34": 3,
"1965 Nissan Silvia 1600 Coupe": 1.5,
"1990 Nissan Silvia S13": 2,
"1999 Nissan Silvia Spec-R S15": 2,
"1995 Nissan GT-R Skyline R33 LM": 1,
"1998 Nissan R390 GT1": 1,
"1992 Nissan Cefiro 2.0 Turbo": 2,
"1990 Nissan Laurel Turbo Medalist": 2.5,
"2017 Nissan Armada Platinum": 7,
"1994 Nissan Hardbody": 7,
"2018 Nissan Titan Platinum Reserve": 7,
"2003 Nissan Skyline GT-R R34 Z-Tune": 1,
"2015 Nissan Juke": 3,
"2021 Nissan Altima 2.0 SR": 2,
"2021 Nissan Altima 2.5 Platinum": 3,
"2022 Nissan GT-R T-Spec": 3,
"2015 Lamborghini Veneno": 1,
"2003 Lamborghini Gallardo" : 1,
"2007 Lamborghini Gallardo SL" : 1,
"2008 Lamborghini Gallardo LP560-4" : 1,
"2010 Lamborgini Gallardo LP570-4 SL ": 1,
"2013 Lamborghini Gallardo LP570-4 SC" : 1,
"2014 Lamborghini Huracan LP610-4" : 1,
"2017 Lamborghini Huracan Performante" : 1,
"2001 Lamborghini Murcielago" : 1,
"2006 Lamborghini Murcielago LP640" : 1,
"2009 Lamborghini Murcielago LP670-4 SV" : 1,
"2015 Lamborghini Aventador SV" : 1,
"2016 Lamborghini Aventador S" : 1,
"1971 Lamborghini Miura P400SV" : 1,
"1996 Lamborghini Diablo SV" : 1,
"1985 Lamborghini Countach LP5000s QV" : 1,
"2020 Lamborghini Sian": 1, 
"2021 Lamborghini Urus": 4,
"2021 Lamborghini Huracan Evo": 1,  
"1995 Lamborghini Diablo SE30 Jota": 1, 
"2000 Lamborghini Diablo GTR": 1, 
"2017 Bentley Continental GT" : 5,
"2015 Bentley Bentayga" : 5,
"2015 Koenigsegg Regera" : 1,
"2010 Koenigsegg Agera" : 1,
"2007 Koenigsegg CCX" : 1,
"2005 Bugatti Veyron 16.4" : 1.5,
"2016 Bugatti Chiron" : 1,
"2017 Porsche 911 GT2 RS" : 2,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : 3,
"2016 Porsche 911 Turbo" : 2,
"2016 Porsche 718 Boxster" : 2,
"2017 Porsche 718 Cayman GTS" : 2,
"1975 Porsche 911 Turbo" : 2,
"1995 Porsche 911 GT2" : 2,
"1987 Porsche 959" : 4,
"1980 Porsche 924 Turbo": 2,
"1999 Porsche 911 GT3" : 2,
"2015 Lotus Evora 400" : 2,
"2011 Lotus Exige S" : 2,
"1996 Lotus Esprit V8" : 2,
"2006 Lotus Elise S" : 2,
"2018 Mazda Miata MX-5 Club" : 2,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 2,
"1989 Mazda MX-5 Miata" : 2,
"1989 Mazda RX-7 Savanna Turbo" : 2,
"1992 Mazda RX-7" : 2,
"1998 Mazda RX-7 RZ" : 2,
"2009 Mazda RX-8" : 2,
"2019 Mazda6 Signature": 3,
"2019 Mazda3 Hatch": 3,
"2019 Mazda CX-5": 5,
"2019 Mazda CX-3": 4,
"2014 Mazda2": 3,
"2015 Mazda5": 3,
"2006 Mazdaspeed 6 GT": 2,
"2013 Mazdaspeed 3": 2,
"2001 Mazda RX-7 Spirit R Type A": 1,
"2018 Morgan Three-Wheeler" : 1,
"1998 Subaru Impreza 22B STi": 5,
"1995 Subaru Impreza WRX STi Version II": 6,
"2002 Subaru Impreza WRX STi": 6,
"2003 Subaru Impreza WRX STi": 6,
"2005 Subaru Impreza WRX STi": 6,
"2010 Subaru Impreza WRX STi R205": 5.5,
"2019 Subaru WRX STi": 5.5,
"2019 Subaru WRX": 5.5,
"2022 Subaru WRX": 5.5,
"2018 Subaru BRZ": 2,
"2022 Subaru BRZ Premium": 2,
"2022 Subaru BRZ Limited": 2,
"1993 Subaru SVX": 4,
"2000 Subaru Forester STI": 6,
"1988 Isuzu Impulse": 2,
"1979 Isuzu 117 Coupe": 2,
"1994 Mitsubishi Lancer Evo II": 6,
"2010 Mitsubishi Lancer Evo X GSR": 6,
"1999 Mitsubishi Lancer Evo VI GSR": 6,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 5,
"2003 Mitsubishi Lancer Evo VIII GSR": 5.5,
"1994 Mitsubishi 3000 GT VR-4": 4,
"1994 Mitsubishi FTO GPX": 3,
"1992 Mitsubishi Galant VR-4": 5.5,
"1974 VAZ Lada 1200": 7,
"1975 UAZ-469": 7.5,
"1965 GAZ Volga 21": 4,
"1995 Hyundai Sonata 2.0i": 3,
"2013 Hyundai Genesis Coupe 3.8" : 2,
"2013 Hyundai Elantra GT": 3,
"2017 Hyundai Sonata Limited": 3,
"2018 Kia Stinger GT": 2,
"2017 Kia Optima SX 2.0T": 3,
"2005 Hyundai Tiburon GT V6": 2.5,
"2006 Audi R8": 2.5,
"2008 Audi R8 V10": 2.5,
"2010 Audi R8 GT": 2,
"2012 Audi R8 Plus": 2.5,
"2015 Audi R8 Coupe 5.2 FSI quattro": 2.5, 
"1994 Audi RS2 Avant": 5,
"2018 Audi RS5": 4.5,
"2018 Audi RS3": 4,
"2018 Audi RS7": 3.5,
"2018 Audi RS6 Avant": 4.5,
"2018 Audi TTRS": 3,
"2018 Mercedes-AMG E63 S 4Matic": 2,
"2018 Mercedes-Maybach S560": 2,
"2018 Mercedes-AMG S65 Sedan": 2,
"1990 Mercedes-Benz 190E Evolution II": 1.5,
"2016 Mercedes-AMG GT S": 1.5,
"2013 Mercedes-Benz SLS AMG GT": 1,
"2012 Mercedes-Benz C63 AMG Black Series": 1.5,
"2000 Mercedes-Benz C32 AMG": 2,
"2020 Mercedes-AMG A35 4Matic": 3,
"2020 Chevy Corvette C8 Stingray Z51": 1,
"2019 Chevy Corvette C7 ZR1": 1,
"2018 Chevy Corvette C7 ZO6": 1,
"2018 Chevy Corvette C7 Stingray": 1.5,
"1953 Chevy Corvette": 2,
"1960 Chevy Corvette C1": 2,
"1963 Chevy Corvette C2 Stingray 427": 1.5,
"1967 Chevy Corvette C3 327": 1,
"1970 Chevy Corvette C3 454": 1,
"1984 Chevy Corvette C4": 1.5,
"1988 Chevy Corvette C4 ZR1": 1,
"2001 Chevy Corvette C5": 1.5,
"2002 Chevy Corvette C5 Z06": 1,
"2007 Chevy Corvette C6": 1.5,
"2007 Chevy Corvette C6 Z06": 1,
"2007 Chevy Corvette C6 ZR1": 1,
"2018 Chevy Camaro 1LE": 2,
"2018 Chevy Camaro ZL1": 1,
"1969 Chevy Camaro SS 396": 2,
"2017 Chevy Malibu 1.5 Turbo": 3,
"2016 Chevy Malibu 2LT": 3,
"2017 Chevy Cruze Hatch Premier": 3,
"2016 Chevy Impala LT": 3,
"2018 Alfa Romeo 4C": 1,
"2018 Alfa Romeo Giulia Quadrifoglio": 2.5,
"2018 Alfa Romeo Stelvio Quadrifoglio": 5,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 3,
"2013 Alfa Romeo MiTo 1.4 8v": 3,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 3,
"2006 Alfa Romeo 8c Competizione": 1.5,
"1992 Alfa Romeo 155 Q4": 4,
"1985 Alfa Romeo Spider Veloce": 125,
"2017 Suzuki Swift Sport": 3,
"2016 Suzuki Alto Works": 2.5,
"2016 Suzuki Hustler G 4WD": 3.5,
"2003 Suzuki Liana 1.6 Sedan": 3,
"1995 Suzuki Samurai 1.3i": 7.5,
"2002 Suzuki Grand Vitara": 5,
"2018 Pagani Huayra BC": 1,
"2013 Pagani Huayra": 1,
"2010 Pagani Zonda Cinque": 1,
"2005 Pagani Zonda F": 1,
"1999 Pagani Zonda C12S": 1,
"1970 AMC AMX": 3,
"1972 AMC Javelin": 3,
"1969 AMC Ambassador": 3,
"1970 AMC Rebel The Machine": 3,
"1975 AMC Pacer X": 2.5,
"2018 Dodge Challenger SRT Hellcat Widebody": 2,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 2.5,
"2018 Dodge Challenger SRT Demon": 1,
"2008 Dodge Challenger SE": 3,
"2008 Dodge Challenger SRT8": 3,
"2018 Dodge Charger Hellcat": 2.5,
"2018 Dodge Charger GT Plus": 4,
"2011 Dodge Charger SRT8": 3,
"2005 Dodge Charger SRT8": 3,
"2017 Dodge Viper ACR": 1,
"2017 Dodge Viper GTS": 1,
"2012 Dodge Dart R/T": 3,
"2010 Dodge Avenger Express": 3,
"2008 Dodge Journey SXT": 4,
"2007 Dodge Nitro 4.0 R/T": 4,
"2007 Dodge Viper SRT-10": 1,
"2007 Dodge Viper SRT10 ACR": 1,
"2000 Dodge Intrepid R/T": 3,
"2003 Dodge Neon SRT-4": 2,
"1970 Dodge Dart Hemi Super Stock": 2,
"1970 Dodge Dart Swinger 340": 2,
"1970 Dodge Challenger R/T 426 Hemi": 2,
"1969 Dodge Charger Daytona Hemi": 1,
"1969 Dodge Charger R/T Hemi":2,
"2018 Mclaren Senna": 1,
"2018 McLaren 720S": 1,
"2015 McLaren 570S": 1,
"2013 McLaren MP4-12C": 1,
"1992 McLaren F1": 1,
"1997 McLaren F1 GT": 1,
"1995 McLaren F1 LM": 1,
"2013 McLaren P1": 1,
"1974 MG Midget": 2,
"1928 MG M-Type Midget": 1,
"2007 Aston Martin DBS": 1.5,
"2016 Aston Martin DB11": 1,
"2016 Aston Martin V12 Vantage S": 1,
"2018 Aston Martin DBS Superleggera": 1,
"2013 Aston Martin V8 Vantage": 1.5,
"2011 Aston Martin One-77": 1,
"2004 Aston Martin Vanquish S": 1.5,
"2008 Aston Martin DB9": 2,
"2019 Aston Martin Valkyrie": 1,
"2018 Range Rover Supercharged": 6,
"2018 Range Rover Velar R-Dynamic": 4,
"2018 Range Rover Sport SVR": 5,
"2016 Land Rover Defender 70th Edition": 7.5,
"1957 Land Rover Series 1": 6,
"2003 Infiniti G35": 2,
"2017 Infiniti Q60 Red Sport": 1.5,
"2015 Infiniti Q50 Eau Rouge": 1,
"2019 Infiniti Q50": 2,
"2019 Tesla Model S Ludicrous Performance": 2,
"2019 Tesla Model S Standard Range": 2,
"2019 Tesla Model 3 Performance": 2,
"2019 Tesla Model 3 Standard Range": 2,
"2019 Tesla Model X Ludicrous Performance": 5,
"2019 Tesla Model X Standard Range": 5,
"2019 Mini Cooper S": 4,
"2019 Mini John Cooper Works": 3,
"1969 Morris Mini Cooper S": 5,
"2020 Cadillac CT4-V": 3,
"2019 Cadillac CTS-V": 2,
"2019 Cadillac CTS 3.6L V6": 3,
"2019 Cadillac ATS-V Coupe": 2,
"2016 Cadillac ELR": 2,
"2020 Cadillac CT6 Platinum": 3,
"2020 Cadillac Escalade": 5,
"2020 Cadillac XT5": 4,
"2014 Cadillac CTS-V Sport Wagon": 2,
"2004 Cadillac Seville": 3,
"2011 Cadillac DTS": 2,
"1975 Cadillac Fleetwood Brougham": 3,
"1976 Cadillac Eldorado": 2,
"1959 Cadillac Eldorado Brougham": 2,
"Renault R35 Tank": 10,
"2019 Renault Clio Iconic TCe 100": 3,
"2019 Renault Clio RS Line TCe 130": 3,
"2019 Renault Clio E-TECH Launch Edition": 3,
"2018 Renault Clio RS Trophy": 2,
"2003 Renault Clio V6": 1,
"1993 Renault Clio Williams": 4,
"1993 Renault Clio": 4,
"1993 Renault Twingo": 3,
"2010 Renault Twingo RS 133 Cup": 2,
"2010 Renault Twingo RS": 2,
"2020 Renault Twingo": 2,
"2020 Renault Megane RS 300 Trophy": 2,
"2020 Renault Megane RS Trophy R": 2,
"2020 Renault Megane RS Line TCe 140": 2,
"2005 Renault Megane Sport 225 Cup": 2,
"LIGHNING MCQUEEN":9999999999999999999999999999999999999999,
"2018 Fortnite Shopping Cart GT-S": 69696969699696969696969,
"2019 Fortnite ATK GT-4R": 3045789034753478587578237587234857234895723485723489577897589347589023478589347582347582347890,
"1009 Thanos Car": 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555.5
}

Car_Upgradable = {
"2000 Honda Integra" : 5,
"2000 Honda Integra Type R" : 5,
"1999 Honda Civic Type R EK9" : 5,
"2003 Honda Civic Type R EP3" : 5,
"2003 Honda NSX R" : 4,
"2001 Honda S2000" : 5,
"2021 Honda Civic Type R FK8" : 3,
"1991 Honda Civic EG6 SiR": 5,
"1999 Honda Civic LX": 5,
"2006 Honda Civic Si": 4,
"2018 Honda Civic Sport": 1,
"2018 Honda Civic Si Coupe": 2,
"2006 Honda Accord 3.0 EX": 0,
"2010 Honda Accord EX-L V6": 0,
"2015 Honda Accord Sport": 0,
"2015 Honda Accord EX-L V6": 0,
"2018 Honda Accord Sport": 0,
"2021 Honda CR-V": 0,
"1999 Honda CR-V": 2,
"2005 Honda Pilot": 0,
"2010 Honda Crosstour": 0,
"2005 Honda Element": 1,
"2001 Honda Odyssey Absolute": 3,
"2021 Honda N-ONE RS": 2,
"2021 Honda StepWGN Spada": 1,
"1999 Honda StepWGN": 2,
"2016 Honda CR-Z": 2,
"2021 Honda HR-V": 1, 
"2005 Honda Stream": 1,
"2014 Honda Stream": 1,
"2021 Honda Clarity": 0,
"2000 Honda Insight": 2,
"2021 Honda Insight": 0,
"2000 Honda ACTY": 3,
"2021 Honda ACTY": 3,
"2021 Honda Fit": 2,
"2001 Honda Life Dunk": 3,
"1992 Honda Vigor": 3,
"1989 Honda Accord": 4,
"2003 Acura RSX Type S" : 3,
"2017 Acura NSX" : 1,
"2005 Acura TL Type S": 2,
"2007 Acura TL": 0,
"2018 Acura TLX 3.5": 1,
"2018 Acura MDX": 0,
"2018 Acura ILX": 0,
"2021 Acura TLX Type S": 1,
"1995 Acura Legend": 2,
"2014 Acura TSX Sport Wagon": 1,
"1990 Ford Mustang Foxbody" : 5,
"2010 Ford Mustang GT500" : 2,
"2015 Ford Mustang GT" : 4,
"1975 Ford Pinto": 1,
"1999 Ford Crown Victoria": 4,
"2017 Ford Focus Hatch": 4,
"2017 Ford Focus RS": 3,
"2017 Ford Fusion Titanium": 1,
"2017 Ford Fusion Sport": 1,
"2018 Ford F-150 Super Cab": 2,
"2018 Ford F-150 Raptor": 2,
"2016 Shelby Mustang GT350R" : 2,
"1992 Volkswagen Golf GTi MK2" : 4,
"2017 Volkswagen Golf GTi MK7" : 4,
"2015 Volkswagen Scirocco R" : 4,
"2018 Volkswagen Passat R-Line": 0,
"1969 Volkswagen Beetle": 4,
"1999 BMW M3" : 5,
"2003 BMW M3" : 5,
"2008 BMW M3" : 4,
"2017 BMW M3" : 1,
"2005 BMW M5" : 1,
"2018 BMW M5" : 1,
"2017 BMW M4" : 3,
"2017 BMW M6" : 1,
"2018 BMW i8" : 0,
"1959 BMW 507": 0,
"2018 BMW 530i": 0,
"2018 BMW X3": 0,
"2018 BMW 750i": 0,
"1974 BMW 2002 Turbo": 1,
"2011 BMW 1M": 1,
"2018 BMW 330i": 1,
"2020 BMW M235i xDrive Gran Coupe": 1,
"2007 Saturn Ion": 0,
"2001 Saturn SL2": 0,
"1998 Saturn SW2": 0,
"2017 Ferrari 488GTB" : 2,
"2017 Ferrari F12" : 1,
"2003 Ferrari 575M Maranello" : 1,
"1999 Ferrari 360" : 3,
"1995 Ferrari F355" : 4,
"1965 Ferrari 250 GTO" : 0,
"1968 Ferrari Dino" : 0,
"1970 Ferrari 365 GTB/4 Daytona" : 0,
"2008 Ferrari F430" : 2,
"2008 Ferrari California" : 0,
"2016 Ferrari LaFerrari" : 0,
"2010 Ferrari 458 Italia": 2,
"1993 Toyota MR2 GT-S" : 4,
"1986 Toyota Corolla Sprinter Trueno" : 5,
"1993 Toyota Supra Twin Turbo" : 5,
"1998 Toyota Chaser Tourer V" : 5,
"1997 Toyota Soarer" : 5,
"1996 Toyota Cresta 2.5 Twin Turbo": 5,
"1998 Toyota Altezza RS200" : 5,
"1984 Toyota Landcruiser 60 3F" : 5,
"2003 Toyota Tundra" : 3,
"2018 Toyota Land Cruiser Prado" : 2,
"2018 Toyota 4Runner TRD Pro" : 1,
"2018 Toyota Tundra TRD Pro" : 1,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 3,
"2017 Toyota Century": 0,
"2019 Toyota Corolla Hatch XSE": 2,
"2019 Toyota Corolla Hatch SE": 2,
"2019 Toyota Corolla Touring Sport": 1,
"2021 Toyota GR Supra": 4,
"2008 Toyota Sequoia V8": 2,
"2005 Toyota Camry LE V6": 1,
"1999 Toyota Corolla LE": 1,
"2002 Toyota Sienna 5D Symphony": 0,
"2010 Toyota Camry LE": 0, 
"2016 Toyota Avalon Limited": 0,
"2018 Toyota Camry XSE": 1,
"2018 Toyota Corolla XLE": 0,
"1969 Toyota 2000GT": 0,
"2001 Toyota Camry LE V6": 0,
"2006 Toyota Sienna Limited": 0,
"2017 Toyota Sienna SE": 0,
"2018 Toyota Sienta": 0,
"2018 Toyota Alphard": 0,
"2018 Toyota Crown Majesta": 1,
"2018 Toyota Tundra SR5 5.7L V8": 3,
"2018 Toyota Hiace": 3,
"1993 Toyota Hiace": 2, 
"1997 Toyota Celica GT-Four": 3,
"1998 Toyota GT-one TS020": 0,
"1993 Toyota Mark II Tourer V JZX90": 5,
"2018 Toyota GT86": 5,
"1997 Toyota Tercel": 1,
"1997 Toyota Celica GT": 2,
"2016 Toyota Land Cruiser": 2,
"2019 Toyota Tacoma SR5": 2,
"2019 Toyota Tacoma TRD Pro": 0,
"1993 Toyota Sera": 2,
"2020 Toyota Avalon Touring": 2,
"2020 Toyota Avalon Limited": 1,
"2020 Toyota Avalon Limited Hybrid": 0,
"2020 Toyota Avalon TRD": 1,
"2020 Toyota Camry LE": 0,
"2020 Toyota Camry SE Hybrid": 0,
"2011 Toyota Prius": 2,
"2020 Toyota Prius XLE AWD": 0,
"2021 Toyota GR Yaris": 2,
"2022 Toyota GR86 Base": 5,
"2022 Toyota GR86 Premium": 5,
"2018 Toyota Camry SE": 1,
"2009 Lexus LFA" : 0,
"2007 Lexus ISF" : 3,
"1998 Lexus GS300" : 5,
"2018 Lexus LC500" : 2,
"2018 Lexus LS500 AWD" : 0,
"2019 Lexus ES300h": 0,
"2018 Lexus GS F": 2,
"2003 Lexus LS430": 0,
"2019 Lexus RX350": 0,
"1999 Lexus RX300 4WD": 0,
"2019 Lexus LX570": 0,
"2022 Lexus IS500 F Sport Performance": 2,
"2022 Lexus IS350 F Sport": 1,
"1990 Nissan Skyline GTR R32" : 5,
"1994 Nissan Skyline GTR R33 Spec-V" : 5,
"1999 Nissan Skyline GTR R34": 5,
"2002 Nissan Skyline GTR V-Spec II Nur" : 5,
"1996 Nissan 180SX" : 5,
"1993 Nissan Silvia K's Type S S14" : 5,
"2018 Nissan GTR Track Edition R35" : 3,
"2007 Nissan Fairlady Z" : 4,
"2018 Nissan Fairlady Z NISMO" : 3,
"2018 Nissan Fairlady Z" : 3,
"1989 Nissan 300ZX Turbo Z" : 4,
"2018 Nissan GT-R50 by Italdesign": 2,
"2018 Nissan GT-R NISMO": 3,
"2018 Nissan Maxima Platinum": 0,
"2018 Nissan Sentra SR Turbo": 0,
"2017 Nissan Leaf": 0,
"1973 Nissan Skyline H/T 2000GT-R": 4,
"1987 Nissan Skyline GTSR R31": 3,
"1989 Nissan Skyline GTS-4 R32": 4,
"1998 Nissan Skyline 25GT-X Turbo R34": 4,
"1965 Nissan Silvia 1600 Coupe": 0,
"1990 Nissan Silvia S13": 5,
"1999 Nissan Silvia Spec-R S15": 5,
"1995 Nissan GT-R Skyline R33 LM": 4,
"1998 Nissan R390 GT1": 0,
"1992 Nissan Cefiro 2.0 Turbo": 4,
"1990 Nissan Laurel Turbo Medalist": 5,
"2017 Nissan Armada Platinum": 0,
"1994 Nissan Hardbody": 5,
"2018 Nissan Titan Platinum Reserve": 0,
"2003 Nissan Skyline GT-R R34 Z-Tune": 5,
"2015 Nissan Juke": 1,
"2021 Nissan Altima 2.0 SR": 1,
"2021 Nissan Altima 2.5 Platinum": 1,
"2022 Nissan GT-R T-Spec": 3,
"2015 Lamborghini Veneno": 0,
"2003 Lamborghini Gallardo" : 3,
"2007 Lamborghini Gallardo SL" : 2,
"2008 Lamborghini Gallardo LP560-4" : 3,
"2010 Lamborgini Gallardo LP570-4 SL ": 2,
"2013 Lamborghini Gallardo LP570-4 SC" : 2,
"2014 Lamborghini Huracan LP610-4" : 3,
"2017 Lamborghini Huracan Performante" : 2,
"2001 Lamborghini Murcielago" : 2,
"2006 Lamborghini Murcielago LP640" : 2,
"2009 Lamborghini Murcielago LP670-4 SV" : 1,
"2015 Lamborghini Aventador SV" : 1,
"2016 Lamborghini Aventador S" : 2,
"1971 Lamborghini Miura P400SV" : 0,
"1996 Lamborghini Diablo SV" : 1,
"1985 Lamborghini Countach LP5000s QV" : 1,
"2020 Lamborghini Sian": 0, 
"2021 Lamborghini Urus": 1,
"2021 Lamborghini Huracan Evo": 3,  
"1995 Lamborghini Diablo SE30 Jota": 0, 
"2000 Lamborghini Diablo GTR": 0, 
"2017 Bentley Continental GT" : 1,
"2015 Bentley Bentayga" : 0,
"2015 Koenigsegg Regera" : 0,
"2010 Koenigsegg Agera" : 1,
"2007 Koenigsegg CCX" : 1,
"2005 Bugatti Veyron 16.4" : 0,
"2016 Bugatti Chiron" : 0,
"2017 Porsche 911 GT2 RS" : 1,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : 1,
"2016 Porsche 911 Turbo" : 2,
"2016 Porsche 718 Boxster" : 3,
"2017 Porsche 718 Cayman GTS" : 3,
"1975 Porsche 911 Turbo" : 3,
"1995 Porsche 911 GT2" : 3,
"1987 Porsche 959" : 0,
"1999 Porsche 911 GT3" : 2,
"1980 Porsche 924 Turbo": 3,
"2015 Lotus Evora 400" : 0,
"2011 Lotus Exige S" : 2,
"1996 Lotus Esprit V8" : 1,
"2006 Lotus Elise S" : 3,
"2018 Mazda Miata MX-5 Club" : 4,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 3,
"1989 Mazda MX-5 Miata" : 5,
"1989 Mazda RX-7 Savanna Turbo" : 5,
"1992 Mazda RX-7" : 5,
"1998 Mazda RX-7 RZ" : 5,
"2009 Mazda RX-8" : 3,
"2019 Mazda6 Signature": 1,
"2019 Mazda3 Hatch": 1,
"2019 Mazda CX-5": 0,
"2019 Mazda CX-3": 0,
"2014 Mazda2": 1,
"2015 Mazda5": 0,
"2006 Mazdaspeed 6 GT": 3,
"2013 Mazdaspeed 3": 3,
"2001 Mazda RX-7 Spirit R Type A": 5,
"2018 Morgan Three-Wheeler" : 0,
"1998 Subaru Impreza 22B STi": 4,
"1995 Subaru Impreza WRX STi Version II": 5,
"2002 Subaru Impreza WRX STi": 5,
"2003 Subaru Impreza WRX STi": 5,
"2005 Subaru Impreza WRX STi": 5,
"2010 Subaru Impreza WRX STi R205": 4,
"2019 Subaru WRX STi": 4,
"1993 Subaru SVX": 2,
"2000 Subaru Forester STI": 3,
"2019 Subaru WRX": 4,
"2022 Subaru WRX": 4,
"2018 Subaru BRZ": 5,
"2022 Subaru BRZ Premium": 5,
"2022 Subaru BRZ Limited": 5,
"1988 Isuzu Impulse": 0,
"1979 Isuzu 117 Coupe": 0,
"1994 Mitsubishi Lancer Evo II": 4,
"2010 Mitsubishi Lancer Evo X GSR": 5,
"1999 Mitsubishi Lancer Evo VI GSR": 5,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 4,
"2003 Mitsubishi Lancer Evo VIII GSR": 5,
"1994 Mitsubishi 3000 GT VR-4": 4,
"1994 Mitsubishi FTO GPX": 2,
"1992 Mitsubishi Galant VR-4": 2,
"1974 VAZ Lada 1200": 4,
"1975 UAZ-469": 4,
"1965 GAZ Volga 21": 3,
"1995 Hyundai Sonata 2.0i": 0,
"2013 Hyundai Genesis Coupe 3.8" : 1,
"2013 Hyundai Elantra GT": 0,
"2017 Hyundai Sonata Limited": 0,
"2018 Kia Stinger GT": 1,
"2017 Kia Optima SX 2.0T": 0,
"2005 Hyundai Tiburon GT V6": 1,
"2006 Audi R8": 3,
"2008 Audi R8 V10": 3,
"2010 Audi R8 GT": 3,
"2012 Audi R8 Plus": 3,
"2015 Audi R8 Coupe 5.2 FSI quattro": 3, 
"1994 Audi RS2 Avant": 3,
"2018 Audi RS5": 1,
"2018 Audi RS3": 1,
"2018 Audi RS7": 1,
"2018 Audi RS6 Avant": 1,
"2018 Audi TTRS": 1,
"2018 Mercedes-AMG E63 S 4Matic": 1,
"2018 Mercedes-Maybach S560": 0,
"2018 Mercedes-AMG S65 Sedan": 0,
"1990 Mercedes-Benz 190E Evolution II": 0,
"2016 Mercedes-AMG GT S": 0,
"2013 Mercedes-Benz SLS AMG GT": 0,
"2012 Mercedes-Benz C63 AMG Black Series": 0,
"2000 Mercedes-Benz C32 AMG": 1,
"2020 Mercedes-AMG A35 4Matic": 0,
"2020 Chevy Corvette C8 Stingray Z51": 0,
"2019 Chevy Corvette C7 ZR1": 0,
"2018 Chevy Corvette C7 ZO6": 1,
"2018 Chevy Corvette C7 Stingray": 2,
"1953 Chevy Corvette": 0,
"1960 Chevy Corvette C1": 0,
"1963 Chevy Corvette C2 Stingray 427": 3,
"1967 Chevy Corvette C3 327": 3,
"1970 Chevy Corvette C3 454": 3,
"1984 Chevy Corvette C4": 3,
"1988 Chevy Corvette C4 ZR1": 1,
"2001 Chevy Corvette C5": 3,
"2002 Chevy Corvette C5 Z06": 3,
"2007 Chevy Corvette C6": 3,
"2007 Chevy Corvette C6 Z06": 3,
"2007 Chevy Corvette C6 ZR1": 2,
"2018 Chevy Camaro 1LE": 2,
"2018 Chevy Camaro ZL1": 0,
"1969 Chevy Camaro SS 396": 5,
"2017 Chevy Malibu 1.5 Turbo": 0,
"2016 Chevy Malibu 2LT": 0,
"2017 Chevy Cruze Hatch Premier": 0,
"2016 Chevy Impala LT": 0,
"2018 Alfa Romeo 4C": 0,
"2018 Alfa Romeo Giulia Quadrifoglio": 0,
"2018 Alfa Romeo Stelvio Quadrifoglio": 0,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 0,
"2013 Alfa Romeo MiTo 1.4 8v": 0,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 0,
"2006 Alfa Romeo 8c Competizione": 0,
"1992 Alfa Romeo 155 Q4": 0,
"1985 Alfa Romeo Spider Veloce": 0,
"2017 Suzuki Swift Sport": 2,
"2016 Suzuki Alto Works": 2,
"2016 Suzuki Hustler G 4WD": 0,
"2003 Suzuki Liana 1.6 Sedan": 1,
"1995 Suzuki Samurai 1.3i": 4,
"2002 Suzuki Grand Vitara": 0,
"2018 Pagani Huayra BC": 0,
"2013 Pagani Huayra": 0,
"2010 Pagani Zonda Cinque": 0,
"2005 Pagani Zonda F": 0,
"1999 Pagani Zonda C12S": 0,
"1970 AMC AMX": 4,
"1972 AMC Javelin": 3,
"1969 AMC Ambassador": 2,
"1970 AMC Rebel The Machine": 4,
"1975 AMC Pacer X": 1,
"2018 Dodge Challenger SRT Hellcat Widebody": 2,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 3,
"2018 Dodge Challenger SRT Demon": 1,
"2008 Dodge Challenger SE": 1,
"2008 Dodge Challenger SRT8": 3,
"2018 Dodge Charger Hellcat": 2,
"2018 Dodge Charger GT Plus": 1,
"2011 Dodge Charger SRT8": 1,
"2005 Dodge Charger SRT8": 1,
"2017 Dodge Viper ACR": 0,
"2017 Dodge Viper GTS": 1,
"2012 Dodge Dart R/T": 1,
"2010 Dodge Avenger Express": 0,
"2008 Dodge Journey SXT": 0,
"2007 Dodge Nitro 4.0 R/T": 1,
"2007 Dodge Viper SRT-10": 1,
"2007 Dodge Viper SRT10 ACR": 1,
"2000 Dodge Intrepid R/T": 0,
"2003 Dodge Neon SRT-4": 2,
"1970 Dodge Dart Hemi Super Stock": 4,
"1970 Dodge Dart Swinger 340": 4,
"1970 Dodge Challenger R/T 426 Hemi": 4,
"1969 Dodge Charger Daytona Hemi": 0,
"1969 Dodge Charger R/T Hemi": 4,
"2018 Mclaren Senna": 0,
"2018 McLaren 720S": 1,
"2015 McLaren 570S": 2,
"2013 McLaren MP4-12C": 2,
"1992 McLaren F1": 1,
"1997 McLaren F1 GT": 0,
"1995 McLaren F1 LM": 0,
"2013 McLaren P1": 0,
"1974 MG Midget": 1,
"1928 MG M-Type Midget": 0,
"2007 Aston Martin DBS": 0,
"2016 Aston Martin DB11": 0,
"2016 Aston Martin V12 Vantage S": 0,
"2018 Aston Martin DBS Superleggera": 0,
"2013 Aston Martin V8 Vantage": 1,
"2011 Aston Martin One-77": 0,
"2004 Aston Martin Vanquish S": 0,
"2008 Aston Martin DB9": 1,
"2019 Aston Martin Valkyrie": 0,
"2018 Range Rover Supercharged": 1,
"2018 Range Rover Velar R-Dynamic": 0,
"2018 Range Rover Sport SVR": 1,
"2016 Land Rover Defender 70th Edition": 4,
"1957 Land Rover Series 1": 3,
"2003 Infiniti G35": 3,
"2017 Infiniti Q60 Red Sport": 2,
"2015 Infiniti Q50 Eau Rouge": 0,
"2019 Infiniti Q50": 0,
"2019 Tesla Model S Ludicrous Performance": 1,
"2019 Tesla Model S Standard Range": 0,
"2019 Tesla Model 3 Performance": 1,
"2019 Tesla Model 3 Standard Range": 0,
"2019 Tesla Model X Ludicrous Performance": 1,
"2019 Tesla Model X Standard Range": 0,
"2019 Mini Cooper S": 3,
"2019 Mini John Cooper Works": 3,
"1969 Morris Mini Cooper S": 5,
"2020 Cadillac CT4-V": 1,
"2019 Cadillac CTS-V": 1,
"2019 Cadillac CTS 3.6L V6": 1,
"2019 Cadillac ATS-V Coupe": 1,
"2016 Cadillac ELR": 0,
"2020 Cadillac CT6 Platinum": 0,
"2020 Cadillac Escalade": 1,
"2020 Cadillac XT5": 1,
"2014 Cadillac CTS-V Sport Wagon": 2,
"2004 Cadillac Seville": 2,
"2011 Cadillac DTS": 1,
"1975 Cadillac Fleetwood Brougham": 3,
"1976 Cadillac Eldorado": 1,
"1959 Cadillac Eldorado Brougham": 2,
"Renault R35 Tank": 5,
"2019 Renault Clio Iconic TCe 100": 1,
"2019 Renault Clio RS Line TCe 130": 1,
"2019 Renault Clio E-TECH Launch Edition": 0,
"2018 Renault Clio RS Trophy": 3,
"2003 Renault Clio V6": 3,
"1993 Renault Clio Williams": 5,
"1993 Renault Clio": 3,
"1993 Renault Twingo": 1,
"2010 Renault Twingo RS 133 Cup": 4,
"2010 Renault Twingo RS": 4,
"2020 Renault Twingo": 1,
"2020 Renault Megane RS 300 Trophy": 3,
"2020 Renault Megane RS Trophy R": 3,
"2020 Renault Megane RS Line TCe 140": 1,
"2005 Renault Megane Sport 225 Cup": 3,
"LIGHNING MCQUEEN":0,
"2018 Fortnite Shopping Cart GT-S": 0,
"2019 Fortnite ATK GT-4R": 0,
"1009 Thanos Car": 4
}

Car_Drive = {
"2000 Honda Integra" : 0,
"2000 Honda Integra Type R" : 0,
"1999 Honda Civic Type R EK9" : 0,
"2003 Honda Civic Type R EP3" : 0,
"2003 Honda NSX R" : 1,
"2001 Honda S2000" : 1,
"2021 Honda Civic Type R FK8" : 0,
"1991 Honda Civic EG6 SiR": 0,
"1999 Honda Civic LX": 0,
"2006 Honda Civic Si": 0,
"2018 Honda Civic Sport": 0,
"2018 Honda Civic Si Coupe": 0,
"2006 Honda Accord 3.0 EX": 0,
"2010 Honda Accord EX-L V6": 0,
"2015 Honda Accord Sport": 0,
"2015 Honda Accord EX-L V6": 0,
"2018 Honda Accord Sport": 0,
"2021 Honda CR-V": 2,
"1999 Honda CR-V": 2.,
"2005 Honda Pilot": 2,
"2010 Honda Crosstour": 2,
"2005 Honda Element": 2,
"2001 Honda Odyssey Absolute": 2,
"2021 Honda N-ONE RS": 0,
"2021 Honda StepWGN Spada": 0,
"1999 Honda StepWGN": 0,
"2016 Honda CR-Z": 0,
"2021 Honda HR-V": 2, 
"2005 Honda Stream": 0,
"2014 Honda Stream": 0,
"2021 Honda Clarity": 0,
"2000 Honda Insight": 0,
"2021 Honda Insight": 0,
"2000 Honda ACTY": 2,
"2021 Honda ACTY": 2,
"2021 Honda Fit": 0,
"2001 Honda Life Dunk": 0,
"1992 Honda Vigor": 0,
"1989 Honda Accord": 0,
"2003 Acura RSX Type S" : 0,
"2017 Acura NSX" : 2,
"2005 Acura TL Type S": 0,
"2007 Acura TL": 0,
"2018 Acura TLX 3.5": 0,
"2018 Acura MDX": 2,
"2018 Acura ILX": 0,
"2021 Acura TLX Type S": 2,
"1995 Acura Legend": 0,
"2014 Acura TSX Sport Wagon": 0,
"1990 Ford Mustang Foxbody" : 1,
"2010 Ford Mustang GT500" : 1,
"2015 Ford Mustang GT" : 1,
"1975 Ford Pinto": 1,
"1999 Ford Crown Victoria": 1,
"2017 Ford Focus Hatch": 0,
"2017 Ford Focus RS": 2,
"2017 Ford Fusion Titanium": 0,
"2017 Ford Fusion Sport": 0,
"2018 Ford F-150 Super Cab": 2,
"2018 Ford F-150 Raptor": 2,
"2016 Shelby Mustang GT350R" : 1,
"1992 Volkswagen Golf GTi MK2" : 0,
"2017 Volkswagen Golf GTi MK7" : 0,
"2015 Volkswagen Scirocco R" : 2,
"2018 Volkswagen Passat R-Line": 0,
"1969 Volkswagen Beetle": 1,
"1999 BMW M3" : 1,
"2003 BMW M3" : 1,
"2008 BMW M3" : 1,
"2017 BMW M3" : 1,
"2005 BMW M5" : 1,
"2018 BMW M5" : 1,
"2017 BMW M4" : 1,
"2017 BMW M6" : 1,
"2018 BMW i8" : 1,
"1959 BMW 507": 1,
"2018 BMW 530i": 1,
"2018 BMW X3": 2,
"2018 BMW 750i": 1,
"1974 BMW 2002 Turbo": 1,
"2011 BMW 1M": 1,
"2018 BMW 330i": 1,
"2020 BMW M235i xDrive Gran Coupe": 2,
"2007 Saturn Ion": 0,
"2001 Saturn SL2": 0,
"1998 Saturn SW2": 0,
"2017 Ferrari 488GTB" : 1,
"2017 Ferrari F12" : 1,
"2003 Ferrari 575M Maranello" : 1,
"1999 Ferrari 360" : 1,
"1995 Ferrari F355" : 1,
"1965 Ferrari 250 GTO" : 1,
"1968 Ferrari Dino" : 1,
"1970 Ferrari 365 GTB/4 Daytona" : 1,
"2008 Ferrari F430" : 1,
"2008 Ferrari California" : 1,
"2016 Ferrari LaFerrari" : 1,
"2010 Ferrari 458 Italia": 1,
"1993 Toyota MR2 GT-S" : 1,
"1986 Toyota Corolla Sprinter Trueno" : 1,
"1993 Toyota Supra Twin Turbo" : 1,
"1998 Toyota Chaser Tourer V" : 1,
"1997 Toyota Soarer" : 1,
"1996 Toyota Cresta 2.5 Twin Turbo": 1,
"1998 Toyota Altezza RS200" : 1,
"1984 Toyota Landcruiser 60 3F" : 2,
"2003 Toyota Tundra" : 2,
"2018 Toyota Land Cruiser Prado" : 2,
"2018 Toyota 4Runner TRD Pro" : 2,
"2018 Toyota Tundra TRD Pro" : 2,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 2,
"2017 Toyota Century": 1,
"2019 Toyota Corolla Hatch XSE": 0,
"2019 Toyota Corolla Hatch SE": 0,
"2019 Toyota Corolla Touring Sport": 0,
"2021 Toyota GR Supra": 1,
"2008 Toyota Sequoia V8": 2,
"2005 Toyota Camry LE V6": 0,
"1999 Toyota Corolla LE": 0,
"2002 Toyota Sienna 5D Symphony": 0,
"2010 Toyota Camry LE": 0, 
"2016 Toyota Avalon Limited": 0,
"2018 Toyota Camry XSE": 0,
"2018 Toyota Corolla XLE": 0,
"1969 Toyota 2000GT": 1,
"2001 Toyota Camry LE V6": 0,
"2006 Toyota Sienna Limited": 0,
"2017 Toyota Sienna SE": 0,
"2018 Toyota Sienta": 0,
"2018 Toyota Alphard": 0,
"2018 Toyota Crown Majesta": 1,
"2018 Toyota Tundra SR5 5.7L V8": 3,
"2018 Toyota Hiace": 0,
"1993 Toyota Hiace": 0, 
"1997 Toyota Celica GT-Four": 2,
"1998 Toyota GT-one TS020": 1,
"1993 Toyota Mark II Tourer V JZX90": 1,
"2018 Toyota GT86": 1,
"1997 Toyota Tercel": 0,
"1997 Toyota Celica GT": 0,
"2016 Toyota Land Cruiser": 2,
"2019 Toyota Tacoma SR5": 2,
"2019 Toyota Tacoma TRD Pro": 2,
"1993 Toyota Sera": 1,
"2020 Toyota Avalon Touring": 0,
"2020 Toyota Avalon Limited": 0,
"2020 Toyota Avalon Limited Hybrid": 0,
"2020 Toyota Avalon TRD": 0,
"2020 Toyota Camry LE": 0,
"2020 Toyota Camry SE Hybrid": 0,
"2011 Toyota Prius": 0,
"2020 Toyota Prius XLE AWD": 2,
"2021 Toyota GR Yaris": 2,
"2022 Toyota GR86 Base": 1,
"2022 Toyota GR86 Premium": 1,
"2018 Toyota Camry SE": 0,
"2009 Lexus LFA" : 1,
"2007 Lexus ISF" : 1,
"1998 Lexus GS300" : 4,
"2018 Lexus LC500" : 1,
"2018 Lexus LS500 AWD" : 2,
"2019 Lexus ES300h": 0,
"2018 Lexus GS F": 1,
"2003 Lexus LS430": 1,
"2019 Lexus RX350": 2,
"1999 Lexus RX300 4WD": 2,
"2019 Lexus LX570": 2,
"2022 Lexus IS500 F Sport Performance": 1,
"2022 Lexus IS350 F Sport": 1,
"1990 Nissan Skyline GTR R32" : 2,
"1994 Nissan Skyline GTR R33 Spec-V" : 2,
"1999 Nissan Skyline GTR R34": 2,
"2002 Nissan Skyline GTR V-Spec II Nur" : 2,
"1996 Nissan 180SX" : 1,
"1993 Nissan Silvia K's Type S S14" : 1,
"2018 Nissan GTR Track Edition R35" : 2,
"2007 Nissan Fairlady Z" : 1,
"2018 Nissan Fairlady Z NISMO" : 1,
"2018 Nissan Fairlady Z" : 1,
"1989 Nissan 300ZX Turbo Z" : 1,
"2018 Nissan GT-R50 by Italdesign": 2,
"2018 Nissan GT-R NISMO": 2,
"2018 Nissan Maxima Platinum": 0,
"2018 Nissan Sentra SR Turbo": 0,
"2017 Nissan Leaf": 0,
"1973 Nissan Skyline H/T 2000GT-R": 1,
"1987 Nissan Skyline GTSR R31": 1,
"1989 Nissan Skyline GTS-4 R32": 2,
"1998 Nissan Skyline 25GT-X Turbo R34": 2,
"1965 Nissan Silvia 1600 Coupe": 1,
"1990 Nissan Silvia S13": 1,
"1999 Nissan Silvia Spec-R S15": 1,
"1995 Nissan GT-R Skyline R33 LM": 2,
"1998 Nissan R390 GT1": 1,
"1992 Nissan Cefiro 2.0 Turbo": 1,
"1990 Nissan Laurel Turbo Medalist": 1,
"2017 Nissan Armada Platinum": 2,
"1994 Nissan Hardbody": 2,
"2018 Nissan Titan Platinum Reserve": 2,
"2003 Nissan Skyline GT-R R34 Z-Tune": 2,
"2015 Nissan Juke": 0,
"2021 Nissan Altima 2.0 SR": 0,
"2021 Nissan Altima 2.5 Platinum": 2,
"2022 Nissan GT-R T-Spec": 2,
"2015 Lamborghini Veneno": 2,
"2003 Lamborghini Gallardo" : 1,
"2007 Lamborghini Gallardo SL" : 1,
"2008 Lamborghini Gallardo LP560-4" : 2,
"2010 Lamborgini Gallardo LP570-4 SL ": 2,
"2013 Lamborghini Gallardo LP570-4 SC" : 2,
"2014 Lamborghini Huracan LP610-4" : 2,
"2017 Lamborghini Huracan Performante" : 2,
"2001 Lamborghini Murcielago" : 1,
"2006 Lamborghini Murcielago LP640" : 1,
"2009 Lamborghini Murcielago LP670-4 SV" : 2,
"2015 Lamborghini Aventador SV" : 2,
"2016 Lamborghini Aventador S" : 2,
"1971 Lamborghini Miura P400SV" : 1,
"1996 Lamborghini Diablo SV" : 1,
"1985 Lamborghini Countach LP5000s QV" : 1,
"2020 Lamborghini Sian": 2, 
"2021 Lamborghini Urus": 2,
"2021 Lamborghini Huracan Evo": 2,  
"1995 Lamborghini Diablo SE30 Jota": 1, 
"2000 Lamborghini Diablo GTR": 1, 
"2017 Bentley Continental GT" : 2,
"2015 Bentley Bentayga" : 2,
"2015 Koenigsegg Regera" : 1,
"2010 Koenigsegg Agera" : 1,
"2007 Koenigsegg CCX" : 1,
"2005 Bugatti Veyron 16.4" : 2,
"2016 Bugatti Chiron" : 2,
"2017 Porsche 911 GT2 RS" : 1,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : 1,
"2016 Porsche 911 Turbo" : 1,
"2016 Porsche 718 Boxster" : 1,
"2017 Porsche 718 Cayman GTS" : 1,
"1975 Porsche 911 Turbo" : 1,
"1995 Porsche 911 GT2" : 1,
"1987 Porsche 959" : 2,
"1999 Porsche 911 GT3" : 1,
"1980 Porsche 924 Turbo": 1,
"2015 Lotus Evora 400" : 1,
"2011 Lotus Exige S" : 1,
"1996 Lotus Esprit V8" :1,
"2006 Lotus Elise S" : 1,
"2018 Mazda Miata MX-5 Club" : 1,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 1,
"1989 Mazda MX-5 Miata" : 1,
"1989 Mazda RX-7 Savanna Turbo" : 1,
"1992 Mazda RX-7" : 1,
"1998 Mazda RX-7 RZ" : 1,
"2009 Mazda RX-8" : 1,
"2019 Mazda6 Signature": 0,
"2019 Mazda3 Hatch": 0,
"2019 Mazda CX-5": 2,
"2019 Mazda CX-3": 2,
"2014 Mazda2": 0,
"2015 Mazda5": 0,
"2006 Mazdaspeed 6 GT": 2,
"2013 Mazdaspeed 3": 0,
"2001 Mazda RX-7 Spirit R Type A": 1,
"2018 Morgan Three-Wheeler" : 0,
"1998 Subaru Impreza 22B STi": 2,
"1995 Subaru Impreza WRX STi Version II": 2,
"2002 Subaru Impreza WRX STi": 2,
"2003 Subaru Impreza WRX STi": 2,
"2005 Subaru Impreza WRX STi": 2,
"2010 Subaru Impreza WRX STi R205": 2,
"2019 Subaru WRX STi": 2,
"1993 Subaru SVX": 2,
"2000 Subaru Forester STI": 2,
"2019 Subaru WRX": 2,
"2022 Subaru WRX": 2,
"2018 Subaru BRZ": 1,
"2022 Subaru BRZ Premium": 1,
"2022 Subaru BRZ Limited": 1,
"1988 Isuzu Impulse": 1,
"1979 Isuzu 117 Coupe": 1,
"1994 Mitsubishi Lancer Evo II": 2,
"2010 Mitsubishi Lancer Evo X GSR": 2,
"1999 Mitsubishi Lancer Evo VI GSR": 2,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 2,
"2003 Mitsubishi Lancer Evo VIII GSR": 2,
"1994 Mitsubishi 3000 GT VR-4": 2,
"1994 Mitsubishi FTO GPX": 0,
"1992 Mitsubishi Galant VR-4": 2,
"1974 VAZ Lada 1200": 1,
"1975 UAZ-469": 2,
"1965 GAZ Volga 21": 1,
"1995 Hyundai Sonata 2.0i": 0,
"2013 Hyundai Genesis Coupe 3.8" : 1,
"2013 Hyundai Elantra GT": 0,
"2017 Hyundai Sonata Limited": 0,
"2018 Kia Stinger GT": 1,
"2017 Kia Optima SX 2.0T": 0,
"2005 Hyundai Tiburon GT V6": 0,
"2006 Audi R8": 2,
"2008 Audi R8 V10": 2,
"2010 Audi R8 GT": 2,
"2012 Audi R8 Plus": 2,
"2015 Audi R8 Coupe 5.2 FSI quattro": 2, 
"1994 Audi RS2 Avant": 2,
"2018 Audi RS5": 2,
"2018 Audi RS3": 2,
"2018 Audi RS7": 2,
"2018 Audi RS6 Avant": 2,
"2018 Audi TTRS": 2,
"2018 Mercedes-AMG E63 S 4Matic": 2,
"2018 Mercedes-Maybach S560": 2,
"2018 Mercedes-AMG S65 Sedan": 2,
"1990 Mercedes-Benz 190E Evolution II": 1,
"2016 Mercedes-AMG GT S": 1,
"2013 Mercedes-Benz SLS AMG GT": 1,
"2012 Mercedes-Benz C63 AMG Black Series": 1,
"2000 Mercedes-Benz C32 AMG": 1,
"2020 Mercedes-AMG A35 4Matic": 2,
"2020 Chevy Corvette C8 Stingray Z51": 1,
"2019 Chevy Corvette C7 ZR1": 1,
"2018 Chevy Corvette C7 ZO6": 1,
"2018 Chevy Corvette C7 Stingray": 1,
"1953 Chevy Corvette": 1,
"1960 Chevy Corvette C1": 1,
"1963 Chevy Corvette C2 Stingray 427": 1,
"1967 Chevy Corvette C3 327": 1,
"1970 Chevy Corvette C3 454": 1,
"1984 Chevy Corvette C4": 1,
"1988 Chevy Corvette C4 ZR1": 1,
"2001 Chevy Corvette C5": 1,
"2002 Chevy Corvette C5 Z06": 1,
"2007 Chevy Corvette C6": 1,
"2007 Chevy Corvette C6 Z06": 1,
"2007 Chevy Corvette C6 ZR1": 1,
"2018 Chevy Camaro 1LE": 1,
"2018 Chevy Camaro ZL1": 1,
"1969 Chevy Camaro SS 396": 1,
"2017 Chevy Malibu 1.5 Turbo": 0,
"2016 Chevy Malibu 2LT": 0,
"2017 Chevy Cruze Hatch Premier": 0,
"2016 Chevy Impala LT": 0,
"2018 Alfa Romeo 4C": 1,
"2018 Alfa Romeo Giulia Quadrifoglio": 1,
"2018 Alfa Romeo Stelvio Quadrifoglio": 2,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 0,
"2013 Alfa Romeo MiTo 1.4 8v": 0,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 1,
"2006 Alfa Romeo 8c Competizione": 1,
"1992 Alfa Romeo 155 Q4": 2,
"1985 Alfa Romeo Spider Veloce": 1,
"2017 Suzuki Swift Sport": 0,
"2016 Suzuki Alto Works": 0,
"2016 Suzuki Hustler G 4WD": 0,
"2003 Suzuki Liana 1.6 Sedan": 0, 	
"1995 Suzuki Samurai 1.3i": 2,
"2002 Suzuki Grand Vitara": 0,
"2018 Pagani Huayra BC": 1,
"2013 Pagani Huayra": 1,
"2010 Pagani Zonda Cinque": 1,
"2005 Pagani Zonda F": 1,
"1999 Pagani Zonda C12S": 1,
"1970 AMC AMX": 1,
"1972 AMC Javelin": 1,
"1969 AMC Ambassador": 1,
"1970 AMC Rebel The Machine": 1,
"1975 AMC Pacer X": 1,
"2018 Dodge Challenger SRT Hellcat Widebody": 1,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 1,
"2018 Dodge Challenger SRT Demon": 1,
"2008 Dodge Challenger SE": 1,
"2008 Dodge Challenger SRT8": 1,
"2018 Dodge Charger Hellcat": 1,
"2018 Dodge Charger GT Plus": 2,
"2011 Dodge Charger SRT8": 1,
"2005 Dodge Charger SRT8": 1,
"2017 Dodge Viper ACR": 1,
"2017 Dodge Viper GTS": 1,
"2012 Dodge Dart R/T": 0,
"2010 Dodge Avenger Express": 0,
"2008 Dodge Journey SXT": 0,
"2007 Dodge Nitro 4.0 R/T": 0,
"2007 Dodge Viper SRT-10": 1,
"2007 Dodge Viper SRT10 ACR": 1,
"2000 Dodge Intrepid R/T": 0,
"2003 Dodge Neon SRT-4": 2,
"1970 Dodge Dart Hemi Super Stock": 1,
"1970 Dodge Dart Swinger 340": 1,
"1970 Dodge Challenger R/T 426 Hemi": 1,
"1969 Dodge Charger Daytona Hemi": 1,
"1969 Dodge Charger R/T Hemi": 1,
"2018 Mclaren Senna": 1,
"2018 McLaren 720S": 1,
"2015 McLaren 570S": 1,
"2013 McLaren MP4-12C": 1,
"1992 McLaren F1": 1,
"1997 McLaren F1 GT": 1,
"1995 McLaren F1 LM": 1,
"2013 McLaren P1": 1,
"1974 MG Midget": 1,
"1928 MG M-Type Midget": 1,
"2007 Aston Martin DBS": 1,
"2016 Aston Martin DB11":1,
"2016 Aston Martin V12 Vantage S": 1,
"2018 Aston Martin DBS Superleggera": 1,
"2013 Aston Martin V8 Vantage": 1,
"2011 Aston Martin One-77": 1,
"2004 Aston Martin Vanquish S": 1,
"2008 Aston Martin DB9": 1,
"2019 Aston Martin Valkyrie": 1,
"2018 Range Rover Supercharged": 2,
"2018 Range Rover Velar R-Dynamic": 2,
"2018 Range Rover Sport SVR": 2,
"2016 Land Rover Defender 70th Edition": 2,
"1957 Land Rover Series 1": 2,
"2003 Infiniti G35": 1,
"2017 Infiniti Q60 Red Sport": 1,
"2015 Infiniti Q50 Eau Rouge": 2,
"2019 Infiniti Q50": 2,
"2019 Tesla Model S Ludicrous Performance": 2,
"2019 Tesla Model S Standard Range": 1,
"2019 Tesla Model 3 Performance": 2,
"2019 Tesla Model 3 Standard Range": 1,
"2019 Tesla Model X Ludicrous Performance": 2,
"2019 Tesla Model X Standard Range": 1,
"2019 Mini Cooper S": 0,
"2019 Mini John Cooper Works": 0,
"1969 Morris Mini Cooper S": 0,
"2020 Cadillac CT4-V": 1,
"2019 Cadillac CTS-V": 1,
"2019 Cadillac CTS 3.6L V6": 1,
"2019 Cadillac ATS-V Coupe": 1,
"2016 Cadillac ELR": 2,
"2020 Cadillac CT6 Platinum": 2,
"2020 Cadillac Escalade": 2,
"2020 Cadillac XT5": 2,
"2014 Cadillac CTS-V Sport Wagon": 1,
"2004 Cadillac Seville": 0,
"2011 Cadillac DTS": 0,
"1975 Cadillac Fleetwood Brougham": 1,
"1976 Cadillac Eldorado": 1,
"1959 Cadillac Eldorado Brougham": 1,
"Renault R35 Tank": 2,
"2019 Renault Clio Iconic TCe 100": 0,
"2019 Renault Clio RS Line TCe 130": 0,
"2019 Renault Clio E-TECH Launch Edition": 0,
"2018 Renault Clio RS Trophy": 0,
"2003 Renault Clio V6": 1,
"1993 Renault Clio Williams": 0,
"1993 Renault Clio": 0,
"1993 Renault Twingo": 0,
"2010 Renault Twingo RS 133 Cup": 0,
"2010 Renault Twingo RS": 0,
"2020 Renault Twingo": 0,
"2020 Renault Megane RS 300 Trophy": 0,
"2020 Renault Megane RS Trophy R": 0,
"2020 Renault Megane RS Line TCe 140": 0,
"2005 Renault Megane Sport 225 Cup": 0,
"LIGHNING MCQUEEN": 2,
"2018 Fortnite Shopping Cart GT-S": 2,
"2019 Fortnite ATK GT-4R": 2,
"1009 Thanos Car": 2
}

Nat_Cat = {
"2000 Honda Integra" : 0,
"2000 Honda Integra Type R" : 0,
"1999 Honda Civic Type R EK9" : 0,
"2003 Honda Civic Type R EP3" : 0,
"2003 Honda NSX R" : 0,
"2001 Honda S2000" : 0,
"2021 Honda Civic Type R FK8" : 0,
"1991 Honda Civic EG6 SiR": 0,
"1999 Honda Civic LX": 0,
"2006 Honda Civic Si": 0,
"2018 Honda Civic Sport": 0,
"2018 Honda Civic Si Coupe": 0,
"2006 Honda Accord 3.0 EX": 0,
"2010 Honda Accord EX-L V6": 0,
"2015 Honda Accord Sport": 0,
"2015 Honda Accord EX-L V6": 0,
"2018 Honda Accord Sport": 0,
"2021 Honda CR-V": 0,
"1999 Honda CR-V": 0,
"2005 Honda Pilot": 0,
"2010 Honda Crosstour": 0,
"2005 Honda Element": 0,
"2001 Honda Odyssey Absolute": 0,
"2021 Honda N-ONE RS": 0,
"2021 Honda StepWGN Spada": 0,
"1999 Honda StepWGN": 0,
"2016 Honda CR-Z": 0,
"2021 Honda HR-V": 0, 
"2005 Honda Stream": 0,
"2014 Honda Stream": 0,
"2021 Honda Clarity": 0,
"2000 Honda Insight": 0,
"2021 Honda Insight": 0,
"2000 Honda ACTY": 0,
"2021 Honda ACTY": 0,
"2021 Honda Fit": 0,
"2001 Honda Life Dunk": 0,
"1992 Honda Vigor": 0,
"1989 Honda Accord": 0,
"2003 Acura RSX Type S" : 0,
"2017 Acura NSX" : 0,
"2005 Acura TL Type S": 0,
"2007 Acura TL": 0,
"2018 Acura TLX 3.5": 0,
"2018 Acura MDX": 0,
"2018 Acura ILX": 0,
"2021 Acura TLX Type S": 0,
"1995 Acura Legend": 0,
"2014 Acura TSX Sport Wagon": 0,
"1990 Ford Mustang Foxbody" : 1,
"2010 Ford Mustang GT500" : 1,
"2015 Ford Mustang GT" : 1,
"1975 Ford Pinto": 1,
"1999 Ford Crown Victoria": 1,
"2017 Ford Focus Hatch": 1,
"2017 Ford Focus RS": 1,
"2017 Ford Fusion Titanium": 1,
"2017 Ford Fusion Sport": 1,
"2018 Ford F-150 Super Cab": 1,
"2018 Ford F-150 Raptor": 1,
"2016 Shelby Mustang GT350R" : 1,
"1992 Volkswagen Golf GTi MK2" : 2,
"2017 Volkswagen Golf GTi MK7" : 2,
"2015 Volkswagen Scirocco R" : 2,
"2018 Volkswagen Passat R-Line": 2,
"1969 Volkswagen Beetle": 2,
"1999 BMW M3" : 2,
"2003 BMW M3" : 2,
"2008 BMW M3" : 2,
"2017 BMW M3" : 2,
"2005 BMW M5" : 2,
"2018 BMW M5" : 2,
"2017 BMW M4" : 2,
"2017 BMW M6" : 2,
"2018 BMW i8" : 2,
"1959 BMW 507": 2,
"2018 BMW 530i": 2,
"2018 BMW X3": 2,
"2018 BMW 750i": 2,
"1974 BMW 2002 Turbo": 2,
"2011 BMW 1M": 2,
"2018 BMW 330i": 2,	
"2020 BMW M235i xDrive Gran Coupe": 2,
"2007 Saturn Ion": 1,
"2001 Saturn SL2": 1,
"1998 Saturn SW2": 1,
"2017 Ferrari 488GTB" : 2,
"2017 Ferrari F12" : 2,
"2003 Ferrari 575M Maranello" : 2,
"1999 Ferrari 360" : 2,
"1995 Ferrari F355" : 2,
"1965 Ferrari 250 GTO" : 2,
"1968 Ferrari Dino" : 2,
"1970 Ferrari 365 GTB/4 Daytona" : 2,
"2008 Ferrari F430" : 2,
"2008 Ferrari California" : 2,
"2016 Ferrari LaFerrari" : 2,
"2010 Ferrari 458 Italia": 2,
"1993 Toyota MR2 GT-S" : 2,
"1986 Toyota Corolla Sprinter Trueno" : 0,
"1993 Toyota Supra Twin Turbo" : 0,
"1998 Toyota Chaser Tourer V" : 0,
"1997 Toyota Soarer" : 0,
"1996 Toyota Cresta 2.5 Twin Turbo": 0,
"1998 Toyota Altezza RS200" : 0,
"1984 Toyota Landcruiser 60 3F" : 0,
"2003 Toyota Tundra" : 0,
"2018 Toyota Land Cruiser Prado" : 0,
"2018 Toyota 4Runner TRD Pro" : 0,
"2018 Toyota Tundra TRD Pro" : 0,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 0,
"2017 Toyota Century": 0,
"2019 Toyota Corolla Hatch XSE": 0,
"2019 Toyota Corolla Hatch SE": 0,
"2019 Toyota Corolla Touring Sport": 0,
"2021 Toyota GR Supra": 0,
"2008 Toyota Sequoia V8": 0,
"2005 Toyota Camry LE V6": 0,
"1999 Toyota Corolla LE": 0,
"2002 Toyota Sienna 5D Symphony": 0,
"2010 Toyota Camry LE": 0, 
"2016 Toyota Avalon Limited": 0,
"2018 Toyota Camry XSE": 0,
"2018 Toyota Corolla XLE": 0,
"1969 Toyota 2000GT": 0,
"2001 Toyota Camry LE V6": 0,
"2006 Toyota Sienna Limited": 0,
"2017 Toyota Sienna SE": 0,
"2018 Toyota Sienta": 0,
"2018 Toyota Alphard": 0,
"2018 Toyota Crown Majesta": 0,
"2018 Toyota Tundra SR5 5.7L V8": 0,
"2018 Toyota Hiace": 0,
"1993 Toyota Hiace": 0, 
"1997 Toyota Celica GT-Four": 0,
"1998 Toyota GT-one TS020": 0,
"1993 Toyota Mark II Tourer V JZX90": 0,
"2018 Toyota GT86": 0,
"1997 Toyota Tercel": 0,
"1997 Toyota Celica GT": 0,
"2016 Toyota Land Cruiser": 0,
"2019 Toyota Tacoma SR5": 0,
"2019 Toyota Tacoma TRD Pro": 0,
"1993 Toyota Sera": 0,
"2020 Toyota Avalon Touring": 0,
"2020 Toyota Avalon Limited": 0,
"2020 Toyota Avalon Limited Hybrid": 0,
"2020 Toyota Avalon TRD": 0,
"2020 Toyota Camry LE": 0,
"2020 Toyota Camry SE Hybrid": 0,
"2011 Toyota Prius": 0,
"2020 Toyota Prius XLE AWD": 0,
"2021 Toyota GR Yaris": 0,
"2022 Toyota GR86 Base": 0,
"2022 Toyota GR86 Premium": 0,
"2018 Toyota Camry SE": 0,
"2009 Lexus LFA" : 0,
"2007 Lexus ISF" : 0,
"1998 Lexus GS300" : 0,
"2018 Lexus LC500" : 0,
"2018 Lexus LS500 AWD" : 0,
"2019 Lexus ES300h": 0,
"2018 Lexus GS F": 0,
"2003 Lexus LS430": 0,
"2019 Lexus RX350": 0,
"1999 Lexus RX300 4WD": 0,
"2019 Lexus LX570": 0,
"2022 Lexus IS500 F Sport Performance": 0,
"2022 Lexus IS350 F Sport": 0,
"1990 Nissan Skyline GTR R32" : 0,
"1994 Nissan Skyline GTR R33 Spec-V" : 0,
"1999 Nissan Skyline GTR R34": 0,
"2002 Nissan Skyline GTR V-Spec II Nur" : 0,
"1996 Nissan 180SX" : 0,
"1993 Nissan Silvia K's Type S S14" : 0,
"2018 Nissan GTR Track Edition R35" : 0,
"2007 Nissan Fairlady Z" : 0,
"2018 Nissan Fairlady Z NISMO" : 0,
"2018 Nissan Fairlady Z" : 0,
"1989 Nissan 300ZX Turbo Z" : 0,
"2018 Nissan GT-R50 by Italdesign": 0,
"2018 Nissan GT-R NISMO": 0,
"2018 Nissan Maxima Platinum": 0,
"2018 Nissan Sentra SR Turbo": 0,
"2017 Nissan Leaf": 0,
"1973 Nissan Skyline H/T 2000GT-R": 0,
"1987 Nissan Skyline GTSR R31": 0,
"1989 Nissan Skyline GTS-4 R32": 0,
"1998 Nissan Skyline 25GT-X Turbo R34": 0,
"1965 Nissan Silvia 1600 Coupe": 0,
"1990 Nissan Silvia S13": 0,
"1999 Nissan Silvia Spec-R S15": 0,
"1995 Nissan GT-R Skyline R33 LM": 0,
"1998 Nissan R390 GT1": 0,
"1992 Nissan Cefiro 2.0 Turbo": 0,
"1990 Nissan Laurel Turbo Medalist": 0,
"2017 Nissan Armada Platinum": 0,
"1994 Nissan Hardbody": 0,
"2018 Nissan Titan Platinum Reserve": 0,
"2003 Nissan Skyline GT-R R34 Z-Tune": 0,
"2015 Nissan Juke": 0,
"2021 Nissan Altima 2.0 SR": 0,
"2021 Nissan Altima 2.5 Platinum": 0,
"2022 Nissan GT-R T-Spec": 0,
"2015 Lamborghini Veneno": 2,
"2003 Lamborghini Gallardo" : 2,
"2007 Lamborghini Gallardo SL" : 2,
"2008 Lamborghini Gallardo LP560-4" : 2,
"2010 Lamborgini Gallardo LP570-4 SL ": 2,
"2013 Lamborghini Gallardo LP570-4 SC" : 2,
"2014 Lamborghini Huracan LP610-4" : 2,
"2017 Lamborghini Huracan Performante" : 2,
"2001 Lamborghini Murcielago" : 2,
"2006 Lamborghini Murcielago LP640" : 2,
"2009 Lamborghini Murcielago LP670-4 SV" : 2,
"2015 Lamborghini Aventador SV" : 2,
"2016 Lamborghini Aventador S" : 2,
"1971 Lamborghini Miura P400SV" : 2,
"1996 Lamborghini Diablo SV" : 2,
"1985 Lamborghini Countach LP5000s QV" : 2,
"2020 Lamborghini Sian": 2, 
"2021 Lamborghini Urus": 2,
"2021 Lamborghini Huracan Evo": 2,  
"1995 Lamborghini Diablo SE30 Jota": 2, 
"2000 Lamborghini Diablo GTR": 2, 
"2017 Bentley Continental GT" : 2,
"2015 Bentley Bentayga" : 2,
"2015 Koenigsegg Regera" : 2,
"2010 Koenigsegg Agera" : 2,
"2007 Koenigsegg CCX" : 2,
"2005 Bugatti Veyron 16.4" : 2,
"2016 Bugatti Chiron" : 2,
"2017 Porsche 911 GT2 RS" : 2,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : 2,
"2016 Porsche 911 Turbo" : 2,
"2016 Porsche 718 Boxster" : 2,
"2017 Porsche 718 Cayman GTS" : 2,
"1975 Porsche 911 Turbo" : 2,
"1995 Porsche 911 GT2" : 2,
"1987 Porsche 959" : 2,
"1999 Porsche 911 GT3" : 2,
"1980 Porsche 924 Turbo": 2,
"2015 Lotus Evora 400" : 2,
"2011 Lotus Exige S" : 2,
"1996 Lotus Esprit V8" :2,
"2006 Lotus Elise S" : 2,
"2018 Mazda Miata MX-5 Club" : 0,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 0,
"1989 Mazda MX-5 Miata" : 0,
"1989 Mazda RX-7 Savanna Turbo" : 0,
"1992 Mazda RX-7" : 0,
"1998 Mazda RX-7 RZ" : 0,
"2009 Mazda RX-8" : 0,
"2019 Mazda6 Signature": 0,
"2019 Mazda3 Hatch": 0,
"2019 Mazda CX-5": 0,
"2019 Mazda CX-3": 0,
"2014 Mazda2": 0,
"2015 Mazda5": 0,
"2006 Mazdaspeed 6 GT": 0,
"2013 Mazdaspeed 3": 0,
"2001 Mazda RX-7 Spirit R Type A": 0,
"2018 Morgan Three-Wheeler" : 0,
"1998 Subaru Impreza 22B STi": 0,
"1995 Subaru Impreza WRX STi Version II": 0,
"2002 Subaru Impreza WRX STi": 0,
"2003 Subaru Impreza WRX STi": 0,
"2005 Subaru Impreza WRX STi": 0,
"2010 Subaru Impreza WRX STi R205": 0,
"2019 Subaru WRX STi": 0,
"1993 Subaru SVX": 0,
"2000 Subaru Forester STI": 0,
"2019 Subaru WRX": 0,
"2022 Subaru WRX": 0,
"2018 Subaru BRZ": 0,
"2022 Subaru BRZ Premium": 0,
"2022 Subaru BRZ Limited": 0,
"1988 Isuzu Impulse": 0,
"1979 Isuzu 117 Coupe": 0,
"1994 Mitsubishi Lancer Evo II": 0,
"2010 Mitsubishi Lancer Evo X GSR": 0,
"1999 Mitsubishi Lancer Evo VI GSR": 0,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 0,
"2003 Mitsubishi Lancer Evo VIII GSR": 0,
"1994 Mitsubishi 3000 GT VR-4": 0,
"1994 Mitsubishi FTO GPX": 0,
"1992 Mitsubishi Galant VR-4": 0,
"1974 VAZ Lada 1200": 2,
"1975 UAZ-469": 2,
"1965 GAZ Volga 21": 2,
"1995 Hyundai Sonata 2.0i": 0,
"2013 Hyundai Genesis Coupe 3.8" : 0,
"2013 Hyundai Elantra GT": 0,
"2017 Hyundai Sonata Limited": 0,
"2018 Kia Stinger GT": 0,
"2017 Kia Optima SX 2.0T": 0,
"2005 Hyundai Tiburon GT V6": 0,
"2006 Audi R8": 2,
"2008 Audi R8 V10": 2,
"2010 Audi R8 GT": 2,
"2012 Audi R8 Plus": 2,
"2015 Audi R8 Coupe 5.2 FSI quattro": 2, 
"1994 Audi RS2 Avant": 2,
"2018 Audi RS5": 2,
"2018 Audi RS3": 2,
"2018 Audi RS7": 2,
"2018 Audi RS6 Avant": 2,
"2018 Audi TTRS": 2,
"2018 Mercedes-AMG E63 S 4Matic": 2,
"2018 Mercedes-Maybach S560": 2,
"2018 Mercedes-AMG S65 Sedan": 2,
"1990 Mercedes-Benz 190E Evolution II": 2,
"2016 Mercedes-AMG GT S": 2,
"2013 Mercedes-Benz SLS AMG GT": 2,
"2012 Mercedes-Benz C63 AMG Black Series": 2,
"2000 Mercedes-Benz C32 AMG": 2,
"2020 Mercedes-AMG A35 4Matic": 2,
"2020 Chevy Corvette C8 Stingray Z51": 1,
"2019 Chevy Corvette C7 ZR1": 1,
"2018 Chevy Corvette C7 ZO6": 1,
"2018 Chevy Corvette C7 Stingray": 1,
"1953 Chevy Corvette": 1,
"1960 Chevy Corvette C1": 1,
"1963 Chevy Corvette C2 Stingray 427": 1,
"1967 Chevy Corvette C3 327": 1,
"1970 Chevy Corvette C3 454": 1,
"1984 Chevy Corvette C4": 1,
"1988 Chevy Corvette C4 ZR1": 1,
"2001 Chevy Corvette C5": 1,
"2002 Chevy Corvette C5 Z06": 1,
"2007 Chevy Corvette C6": 1,
"2007 Chevy Corvette C6 Z06": 1,
"2007 Chevy Corvette C6 ZR1": 1,
"2018 Chevy Camaro 1LE": 1,
"2018 Chevy Camaro ZL1": 1,
"1969 Chevy Camaro SS 396": 1,
"2017 Chevy Malibu 1.5 Turbo": 1,
"2016 Chevy Malibu 2LT": 1,
"2017 Chevy Cruze Hatch Premier": 1,
"2016 Chevy Impala LT": 1,
"2018 Alfa Romeo 4C": 2,
"2018 Alfa Romeo Giulia Quadrifoglio": 2,
"2018 Alfa Romeo Stelvio Quadrifoglio": 2,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 2,
"2013 Alfa Romeo MiTo 1.4 8v": 2,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 2,
"2006 Alfa Romeo 8c Competizione": 2,
"1992 Alfa Romeo 155 Q4": 2,
"1985 Alfa Romeo Spider Veloce": 2,
"2017 Suzuki Swift Sport": 0,
"2016 Suzuki Alto Works": 0,
"2016 Suzuki Hustler G 4WD": 0,
"2003 Suzuki Liana 1.6 Sedan": 0, 	
"1995 Suzuki Samurai 1.3i": 0,
"2002 Suzuki Grand Vitara": 0,
"2018 Pagani Huayra BC": 2,
"2013 Pagani Huayra": 2,
"2010 Pagani Zonda Cinque": 2,
"2005 Pagani Zonda F": 2,
"1999 Pagani Zonda C12S": 2,
"1970 AMC AMX": 1,
"1972 AMC Javelin": 1,
"1969 AMC Ambassador": 1,
"1970 AMC Rebel The Machine": 1,
"1975 AMC Pacer X": 1,
"2018 Dodge Challenger SRT Hellcat Widebody": 1,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 1,
"2018 Dodge Challenger SRT Demon": 1,
"2008 Dodge Challenger SE": 1,
"2008 Dodge Challenger SRT8": 1,
"2018 Dodge Charger Hellcat": 1,
"2018 Dodge Charger GT Plus": 1,
"2011 Dodge Charger SRT8": 1,
"2005 Dodge Charger SRT8": 1,
"2017 Dodge Viper ACR": 1,
"2017 Dodge Viper GTS": 1,
"2012 Dodge Dart R/T": 1,
"2010 Dodge Avenger Express": 1,
"2008 Dodge Journey SXT": 1,
"2007 Dodge Nitro 4.0 R/T": 1,
"2007 Dodge Viper SRT-10": 1,
"2007 Dodge Viper SRT10 ACR": 1,
"2000 Dodge Intrepid R/T": 1,
"2003 Dodge Neon SRT-4": 1,
"1970 Dodge Dart Hemi Super Stock": 1,
"1970 Dodge Dart Swinger 340": 1,
"1970 Dodge Challenger R/T 426 Hemi": 1,
"1969 Dodge Charger Daytona Hemi": 1,
"1969 Dodge Charger R/T Hemi": 1,
"2018 Mclaren Senna": 2,
"2018 McLaren 720S": 2,
"2015 McLaren 570S": 2,
"2013 McLaren MP4-12C": 2,
"1992 McLaren F1": 2,
"1997 McLaren F1 GT": 2,
"1995 McLaren F1 LM": 2,
"2013 McLaren P1": 2,
"1974 MG Midget": 2,
"1928 MG M-Type Midget": 2,
"2007 Aston Martin DBS": 2,
"2016 Aston Martin DB11":2,
"2016 Aston Martin V12 Vantage S": 2,
"2018 Aston Martin DBS Superleggera": 2,
"2013 Aston Martin V8 Vantage": 2,
"2011 Aston Martin One-77": 2,
"2004 Aston Martin Vanquish S": 2,
"2008 Aston Martin DB9": 2,
"2019 Aston Martin Valkyrie": 2,
"2018 Range Rover Supercharged": 2,
"2018 Range Rover Velar R-Dynamic": 2,
"2018 Range Rover Sport SVR": 2,
"2016 Land Rover Defender 70th Edition": 2,
"1957 Land Rover Series 1": 2,
"2003 Infiniti G35": 0,
"2017 Infiniti Q60 Red Sport": 0,
"2015 Infiniti Q50 Eau Rouge": 0,
"2019 Infiniti Q50": 0,
"2019 Tesla Model S Ludicrous Performance": 1,
"2019 Tesla Model S Standard Range": 1,
"2019 Tesla Model 3 Performance": 1,
"2019 Tesla Model 3 Standard Range": 1,
"2019 Tesla Model X Ludicrous Performance": 1,
"2019 Tesla Model X Standard Range": 1,
"2019 Mini Cooper S": 2,
"2019 Mini John Cooper Works": 2,
"1969 Morris Mini Cooper S": 2,
"2020 Cadillac CT4-V": 1,
"2019 Cadillac CTS-V": 1,
"2019 Cadillac CTS 3.6L V6": 1,
"2019 Cadillac ATS-V Coupe": 1,
"2016 Cadillac ELR": 1,
"2020 Cadillac CT6 Platinum": 1,
"2020 Cadillac Escalade": 1,
"2020 Cadillac XT5": 1,
"2014 Cadillac CTS-V Sport Wagon": 1,
"2004 Cadillac Seville": 1,
"2011 Cadillac DTS": 1,
"1975 Cadillac Fleetwood Brougham": 1,
"1976 Cadillac Eldorado": 1,
"1959 Cadillac Eldorado Brougham": 1,
"Renault R35 Tank": 2,
"2019 Renault Clio Iconic TCe 100": 2,
"2019 Renault Clio RS Line TCe 130": 2,
"2019 Renault Clio E-TECH Launch Edition": 2,
"2018 Renault Clio RS Trophy": 2,
"2003 Renault Clio V6": 2,
"1993 Renault Clio Williams": 2,
"1993 Renault Clio": 2,
"1993 Renault Twingo": 2,
"2010 Renault Twingo RS 133 Cup": 2,
"2010 Renault Twingo RS": 2,
"2020 Renault Twingo": 2,
"2020 Renault Megane RS 300 Trophy": 2,
"2020 Renault Megane RS Trophy R": 2,
"2020 Renault Megane RS Line TCe 140": 2,
"2005 Renault Megane Sport 225 Cup": 2,
"LIGHNING MCQUEEN": 1,
"2018 Fortnite Shopping Cart GT-S": 1,
"2019 Fortnite ATK GT-4R": 1,
"1009 Thanos Car": 1
}

Car_Seats = {
"2000 Honda Integra" : 4,
"2000 Honda Integra Type R" : 2,
"1999 Honda Civic Type R EK9" : 4,
"2003 Honda Civic Type R EP3" : 4,
"2003 Honda NSX R" : 2,
"2001 Honda S2000" : 2,
"2021 Honda Civic Type R FK8" : 4,
"1991 Honda Civic EG6 SiR": 4,
"1999 Honda Civic LX": 4,
"2006 Honda Civic Si": 4,
"2018 Honda Civic Sport": 4,
"2018 Honda Civic Si Coupe": 4,
"2006 Honda Accord 3.0 EX": 4,
"2010 Honda Accord EX-L V6": 4,
"2015 Honda Accord Sport": 4,
"2015 Honda Accord EX-L V6": 4,
"2018 Honda Accord Sport": 4,
"2021 Honda CR-V": 4,
"1999 Honda CR-V": 4,
"2005 Honda Pilot": 6,
"2010 Honda Crosstour": 4,
"2005 Honda Element": 4,
"2001 Honda Odyssey Absolute": 6,
"2021 Honda N-ONE RS": 4,
"2021 Honda StepWGN Spada": 8,
"1999 Honda StepWGN": 8,
"2016 Honda CR-Z": 2,
"2021 Honda HR-V": 4, 
"2005 Honda Stream": 6,
"2014 Honda Stream": 6,
"2021 Honda Clarity": 4,
"2000 Honda Insight": 4,
"2021 Honda Insight": 2,
"2000 Honda ACTY": 2,
"2021 Honda ACTY": 2,
"2021 Honda Fit": 4,
"2001 Honda Life Dunk": 4,
"1992 Honda Vigor": 4,
"1989 Honda Accord": 4,
"2003 Acura RSX Type S" : 2,
"2017 Acura NSX" : 2,
"2005 Acura TL Type S": 4,
"2007 Acura TL": 4,
"2018 Acura TLX 3.5": 4,
"2018 Acura MDX": 6,
"2018 Acura ILX": 4,
"2021 Acura TLX Type S": 4,
"1995 Acura Legend": 4,
"2014 Acura TSX Sport Wagon": 4,
"1990 Ford Mustang Foxbody" : 2,
"2010 Ford Mustang GT500" : 2,
"2015 Ford Mustang GT" : 2,
"1975 Ford Pinto": 4,
"1999 Ford Crown Victoria": 4,
"2017 Ford Focus Hatch": 4,
"2017 Ford Focus RS": 4,
"2017 Ford Fusion Titanium": 4,
"2017 Ford Fusion Sport": 4,
"2018 Ford F-150 Super Cab": 4,
"2018 Ford F-150 Raptor": 4,
"2016 Shelby Mustang GT350R" : 2,
"1992 Volkswagen Golf GTi MK2" : 4,
"2017 Volkswagen Golf GTi MK7" : 4,
"2015 Volkswagen Scirocco R" : 4,
"2018 Volkswagen Passat R-Line": 4,
"1969 Volkswagen Beetle": 2,
"1999 BMW M3" : 4,
"2003 BMW M3" : 4,
"2008 BMW M3" : 4,
"2017 BMW M3" : 4,
"2005 BMW M5" : 4,
"2018 BMW M5" : 4,
"2017 BMW M4" : 4,
"2017 BMW M6" : 4,
"2018 BMW i8" : 2,
"1959 BMW 507": 2,
"2018 BMW 530i": 4,
"2018 BMW X3": 4,
"2018 BMW 750i": 4,
"1974 BMW 2002 Turbo": 4,
"2011 BMW 1M": 4,
"2018 BMW 330i": 4,	
"2020 BMW M235i xDrive Gran Coupe": 4,
"2007 Saturn Ion": 4,
"2001 Saturn SL2": 4,
"1998 Saturn SW2": 4,
"2017 Ferrari 488GTB" : 2,
"2017 Ferrari F12" : 2,
"2003 Ferrari 575M Maranello" : 2,
"1999 Ferrari 360" : 2,
"1995 Ferrari F355" : 2,
"1965 Ferrari 250 GTO" : 2,
"1968 Ferrari Dino" : 2,
"1970 Ferrari 365 GTB/4 Daytona" : 2,
"2008 Ferrari F430" : 2,
"2008 Ferrari California" : 2,
"2016 Ferrari LaFerrari" : 2,
"2010 Ferrari 458 Italia": 2,
"1993 Toyota MR2 GT-S" : 2,
"1986 Toyota Corolla Sprinter Trueno" : 2,
"1993 Toyota Supra Twin Turbo" : 2,
"1998 Toyota Chaser Tourer V" : 4,
"1997 Toyota Soarer" : 2,
"1996 Toyota Cresta 2.5 Twin Turbo": 4,
"1998 Toyota Altezza RS200" : 4,
"1984 Toyota Landcruiser 60 3F" : 4,
"2003 Toyota Tundra" : 4,
"2018 Toyota Land Cruiser Prado" : 4,
"2018 Toyota 4Runner TRD Pro" : 4,
"2018 Toyota Tundra TRD Pro" : 4,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 4,
"2017 Toyota Century": 4,
"2019 Toyota Corolla Hatch XSE": 4,
"2019 Toyota Corolla Hatch SE": 4,
"2019 Toyota Corolla Touring Sport": 4,
"2021 Toyota GR Supra": 2,
"2008 Toyota Sequoia V8": 6,
"2005 Toyota Camry LE V6": 4,
"1999 Toyota Corolla LE": 4,
"2002 Toyota Sienna 5D Symphony": 6,
"2010 Toyota Camry LE": 4, 
"2016 Toyota Avalon Limited": 4,
"2018 Toyota Camry XSE": 4,
"2018 Toyota Corolla XLE": 4,
"1969 Toyota 2000GT": 2,
"2001 Toyota Camry LE V6": 4,
"2006 Toyota Sienna Limited": 4,
"2017 Toyota Sienna SE": 6,
"2018 Toyota Sienta": 6,
"2018 Toyota Alphard": 6,
"2018 Toyota Crown Majesta": 4,
"2018 Toyota Tundra SR5 5.7L V8": 4,
"2018 Toyota Hiace": 6,
"1993 Toyota Hiace": 6, 
"1997 Toyota Celica GT-Four": 2,
"1998 Toyota GT-one TS020": 2,
"1993 Toyota Mark II Tourer V JZX90": 4,
"2018 Toyota GT86": 2,
"1997 Toyota Tercel": 4,
"1997 Toyota Celica GT": 2,
"2016 Toyota Land Cruiser": 4,
"2019 Toyota Tacoma SR5": 4,
"2019 Toyota Tacoma TRD Pro": 4,
"1993 Toyota Sera": 2,
"2020 Toyota Avalon Touring": 4,
"2020 Toyota Avalon Limited": 4,
"2020 Toyota Avalon Limited Hybrid": 4,
"2020 Toyota Avalon TRD": 4,
"2020 Toyota Camry LE": 4,
"2020 Toyota Camry SE Hybrid": 4,
"2011 Toyota Prius": 4,
"2020 Toyota Prius XLE AWD": 4,
"2021 Toyota GR Yaris": 4,
"2022 Toyota GR86 Base": 2,
"2022 Toyota GR86 Premium": 2,
"2018 Toyota Camry SE": 4,
"2009 Lexus LFA" : 2,
"2007 Lexus ISF" : 4,
"1998 Lexus GS300" : 4,
"2018 Lexus LC500" : 2,
"2018 Lexus LS500 AWD" : 4,
"2019 Lexus ES300h": 4,
"2018 Lexus GS F": 4,
"2003 Lexus LS430": 4,
"2019 Lexus RX350": 4,
"1999 Lexus RX300 4WD": 4,
"2019 Lexus LX570": 6,
"2022 Lexus IS500 F Sport Performance": 4,
"2022 Lexus IS350 F Sport": 4,
"1990 Nissan Skyline GTR R32" : 2,
"1994 Nissan Skyline GTR R33 Spec-V" : 2,
"1999 Nissan Skyline GTR R34": 2,
"2002 Nissan Skyline GTR V-Spec II Nur" : 2,
"1996 Nissan 180SX" : 2,
"1993 Nissan Silvia K's Type S S14" : 2,
"2018 Nissan GTR Track Edition R35" : 2,
"2007 Nissan Fairlady Z" : 2,
"2018 Nissan Fairlady Z NISMO" : 2,
"2018 Nissan Fairlady Z" : 2,
"1989 Nissan 300ZX Turbo Z" : 2,
"2018 Nissan GT-R50 by Italdesign": 2,
"2018 Nissan GT-R NISMO": 2,
"2018 Nissan Maxima Platinum": 4,
"2018 Nissan Sentra SR Turbo": 4,
"2017 Nissan Leaf": 4,
"1973 Nissan Skyline H/T 2000GT-R": 2,
"1987 Nissan Skyline GTSR R31": 2,
"1989 Nissan Skyline GTS-4 R32": 4,
"1998 Nissan Skyline 25GT-X Turbo R34": 4,
"1965 Nissan Silvia 1600 Coupe": 2,
"1990 Nissan Silvia S13": 2,
"1999 Nissan Silvia Spec-R S15": 2,
"1995 Nissan GT-R Skyline R33 LM": 2,
"1998 Nissan R390 GT1": 2,
"1992 Nissan Cefiro 2.0 Turbo": 4,
"1990 Nissan Laurel Turbo Medalist": 4,
"2017 Nissan Armada Platinum": 6,
"1994 Nissan Hardbody": 2,
"2018 Nissan Titan Platinum Reserve": 4,
"2003 Nissan Skyline GT-R R34 Z-Tune": 2,
"2015 Nissan Juke": 4,
"2021 Nissan Altima 2.0 SR": 4,
"2021 Nissan Altima 2.5 Platinum": 4,
"2022 Nissan GT-R T-Spec": 2,
"2015 Lamborghini Veneno": 2,
"2003 Lamborghini Gallardo" : 2,
"2007 Lamborghini Gallardo SL" : 2,
"2008 Lamborghini Gallardo LP560-4" : 2,
"2010 Lamborgini Gallardo LP570-4 SL ": 2,
"2013 Lamborghini Gallardo LP570-4 SC" : 2,
"2014 Lamborghini Huracan LP610-4" : 2,
"2017 Lamborghini Huracan Performante" : 2,
"2001 Lamborghini Murcielago" : 2,
"2006 Lamborghini Murcielago LP640" : 2,
"2009 Lamborghini Murcielago LP670-4 SV" : 2,
"2015 Lamborghini Aventador SV" : 2,
"2016 Lamborghini Aventador S" : 2,
"1971 Lamborghini Miura P400SV" : 2,
"1996 Lamborghini Diablo SV" : 2,
"1985 Lamborghini Countach LP5000s QV" : 2,
"2020 Lamborghini Sian": 2, 
"2021 Lamborghini Urus": 4,
"2021 Lamborghini Huracan Evo": 2,  
"1995 Lamborghini Diablo SE30 Jota": 2, 
"2000 Lamborghini Diablo GTR": 2, 
"2017 Bentley Continental GT" : 4,
"2015 Bentley Bentayga" : 4,
"2015 Koenigsegg Regera" : 2,
"2010 Koenigsegg Agera" : 2,
"2007 Koenigsegg CCX" : 2,
"2005 Bugatti Veyron 16.4" : 2,
"2016 Bugatti Chiron" : 2,
"2017 Porsche 911 GT2 RS" : 2,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : 4,
"2016 Porsche 911 Turbo" : 2,
"2016 Porsche 718 Boxster" : 2,
"2017 Porsche 718 Cayman GTS" : 2,
"1975 Porsche 911 Turbo" : 2,
"1995 Porsche 911 GT2" : 2,
"1987 Porsche 959" : 2,
"1999 Porsche 911 GT3" : 2,
"1980 Porsche 924 Turbo": 2,
"2015 Lotus Evora 400" : 2,
"2011 Lotus Exige S" : 2,
"1996 Lotus Esprit V8" :2,
"2006 Lotus Elise S" : 2,
"2018 Mazda Miata MX-5 Club" : 2,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 2,
"1989 Mazda MX-5 Miata" : 2,
"1989 Mazda RX-7 Savanna Turbo" : 2,
"1992 Mazda RX-7" : 2,
"1998 Mazda RX-7 RZ" : 2,
"2009 Mazda RX-8" : 4,
"2019 Mazda6 Signature": 4,
"2019 Mazda3 Hatch": 4,
"2019 Mazda CX-5": 4,
"2019 Mazda CX-3": 4,
"2014 Mazda2": 4,
"2015 Mazda5": 6,
"2006 Mazdaspeed 6 GT": 4,
"2013 Mazdaspeed 3": 4,
"2001 Mazda RX-7 Spirit R Type A": 2,
"2018 Morgan Three-Wheeler" : 2,
"1998 Subaru Impreza 22B STi": 2,
"1995 Subaru Impreza WRX STi Version II": 4,
"2002 Subaru Impreza WRX STi": 4,
"2003 Subaru Impreza WRX STi": 4,
"2005 Subaru Impreza WRX STi": 4,
"2010 Subaru Impreza WRX STi R205": 4,
"2019 Subaru WRX STi": 4,
"1993 Subaru SVX": 2,
"2000 Subaru Forester STI": 4,
"2019 Subaru WRX": 4,
"2022 Subaru WRX": 4,
"2018 Subaru BRZ": 2,
"2022 Subaru BRZ Premium": 2,
"2022 Subaru BRZ Limited": 2,
"1988 Isuzu Impulse": 2,
"1979 Isuzu 117 Coupe": 2,
"1994 Mitsubishi Lancer Evo II": 4,
"2010 Mitsubishi Lancer Evo X GSR": 4,
"1999 Mitsubishi Lancer Evo VI GSR": 4,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 4,
"2003 Mitsubishi Lancer Evo VIII GSR": 4,
"1994 Mitsubishi 3000 GT VR-4": 2,
"1994 Mitsubishi FTO GPX": 2,
"1992 Mitsubishi Galant VR-4": 4,
"1974 VAZ Lada 1200": 4,
"1975 UAZ-469": 4,
"1965 GAZ Volga 21": 4,
"1995 Hyundai Sonata 2.0i": 4,
"2013 Hyundai Genesis Coupe 3.8" : 2,
"2013 Hyundai Elantra GT": 4,
"2017 Hyundai Sonata Limited": 4,
"2018 Kia Stinger GT": 4,
"2017 Kia Optima SX 2.0T": 4,
"2005 Hyundai Tiburon GT V6": 2,
"2006 Audi R8": 2,
"2008 Audi R8 V10": 2,
"2010 Audi R8 GT": 2,
"2012 Audi R8 Plus": 2,
"2015 Audi R8 Coupe 5.2 FSI quattro": 2, 
"1994 Audi RS2 Avant": 4,
"2018 Audi RS5": 4,
"2018 Audi RS3": 4,
"2018 Audi RS7": 4,
"2018 Audi RS6 Avant": 4,
"2018 Audi TTRS": 2,
"2018 Mercedes-AMG E63 S 4Matic": 4,
"2018 Mercedes-Maybach S560": 4,
"2018 Mercedes-AMG S65 Sedan": 4,
"1990 Mercedes-Benz 190E Evolution II": 4,
"2016 Mercedes-AMG GT S": 2,
"2013 Mercedes-Benz SLS AMG GT": 2,
"2012 Mercedes-Benz C63 AMG Black Series": 4,
"2000 Mercedes-Benz C32 AMG": 4,
"2020 Mercedes-AMG A35 4Matic": 4,
"2020 Chevy Corvette C8 Stingray Z51": 2,
"2019 Chevy Corvette C7 ZR1": 2,
"2018 Chevy Corvette C7 ZO6": 2,
"2018 Chevy Corvette C7 Stingray": 2,
"1953 Chevy Corvette": 2,
"1960 Chevy Corvette C1": 2,
"1963 Chevy Corvette C2 Stingray 427": 1,
"1967 Chevy Corvette C3 327": 2,
"1970 Chevy Corvette C3 454": 2,
"1984 Chevy Corvette C4": 2,
"1988 Chevy Corvette C4 ZR1": 2,
"2001 Chevy Corvette C5": 2,
"2002 Chevy Corvette C5 Z06": 2,
"2007 Chevy Corvette C6": 2,
"2007 Chevy Corvette C6 Z06": 2,
"2007 Chevy Corvette C6 ZR1": 2,
"2018 Chevy Camaro 1LE": 2,
"2018 Chevy Camaro ZL1": 2,
"1969 Chevy Camaro SS 396": 2,
"2017 Chevy Malibu 1.5 Turbo": 4,
"2016 Chevy Malibu 2LT": 4,
"2017 Chevy Cruze Hatch Premier": 4,
"2016 Chevy Impala LT": 4,
"2018 Alfa Romeo 4C": 2,
"2018 Alfa Romeo Giulia Quadrifoglio": 4,
"2018 Alfa Romeo Stelvio Quadrifoglio": 4,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 4,
"2013 Alfa Romeo MiTo 1.4 8v": 4,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 4,
"2006 Alfa Romeo 8c Competizione": 2,
"1992 Alfa Romeo 155 Q4": 4,
"1985 Alfa Romeo Spider Veloce": 2,
"2017 Suzuki Swift Sport": 4,
"2016 Suzuki Alto Works": 4,
"2016 Suzuki Hustler G 4WD": 4,
"2003 Suzuki Liana 1.6 Sedan": 4, 	
"1995 Suzuki Samurai 1.3i": 2,
"2002 Suzuki Grand Vitara": 4,
"2018 Pagani Huayra BC": 2,
"2013 Pagani Huayra": 2,
"2010 Pagani Zonda Cinque": 2,
"2005 Pagani Zonda F": 2,
"1999 Pagani Zonda C12S": 2,
"1970 AMC AMX": 2,
"1972 AMC Javelin": 2,
"1969 AMC Ambassador": 4,
"1970 AMC Rebel The Machine": 2,
"1975 AMC Pacer X": 4,
"2018 Dodge Challenger SRT Hellcat Widebody": 2,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 2,
"2018 Dodge Challenger SRT Demon": 2,
"2008 Dodge Challenger SE": 2,
"2008 Dodge Challenger SRT8": 2,
"2018 Dodge Charger Hellcat": 2,
"2018 Dodge Charger GT Plus": 2,
"2011 Dodge Charger SRT8": 2,
"2005 Dodge Charger SRT8": 2,
"2017 Dodge Viper ACR": 2,
"2017 Dodge Viper GTS": 2,
"2012 Dodge Dart R/T": 4,
"2010 Dodge Avenger Express": 4,
"2008 Dodge Journey SXT": 4,
"2007 Dodge Nitro 4.0 R/T": 4,
"2007 Dodge Viper SRT-10": 2,
"2007 Dodge Viper SRT10 ACR": 2,
"2000 Dodge Intrepid R/T": 4,
"2003 Dodge Neon SRT-4": 4,
"1970 Dodge Dart Hemi Super Stock": 2,
"1970 Dodge Dart Swinger 340": 2,
"1970 Dodge Challenger R/T 426 Hemi": 2,
"1969 Dodge Charger Daytona Hemi": 2,
"1969 Dodge Charger R/T Hemi": 2,
"2018 Mclaren Senna": 2,
"2018 McLaren 720S": 2,
"2015 McLaren 570S": 2,
"2013 McLaren MP4-12C": 2,
"1992 McLaren F1": 3,
"1997 McLaren F1 GT": 3,
"1995 McLaren F1 LM": 3,
"2013 McLaren P1": 2,
"1974 MG Midget": 2,
"1928 MG M-Type Midget": 2,
"2007 Aston Martin DBS": 2,
"2016 Aston Martin DB11":2,
"2016 Aston Martin V12 Vantage S": 2,
"2018 Aston Martin DBS Superleggera": 2,
"2013 Aston Martin V8 Vantage": 2,
"2011 Aston Martin One-77": 2,
"2004 Aston Martin Vanquish S": 2,
"2008 Aston Martin DB9": 2,
"2019 Aston Martin Valkyrie": 2,
"2018 Range Rover Supercharged": 4,
"2018 Range Rover Velar R-Dynamic": 4,
"2018 Range Rover Sport SVR": 4,
"2016 Land Rover Defender 70th Edition": 4,
"1957 Land Rover Series 1": 2,
"2003 Infiniti G35": 2,
"2017 Infiniti Q60 Red Sport": 2,
"2015 Infiniti Q50 Eau Rouge": 4,
"2019 Infiniti Q50": 4,
"2019 Tesla Model S Ludicrous Performance": 4,
"2019 Tesla Model S Standard Range": 4,
"2019 Tesla Model 3 Performance": 4,
"2019 Tesla Model 3 Standard Range": 4,
"2019 Tesla Model X Ludicrous Performance": 4,
"2019 Tesla Model X Standard Range": 4,
"2019 Mini Cooper S": 4,
"2019 Mini John Cooper Works": 4,
"1969 Morris Mini Cooper S": 2,
"2020 Cadillac CT4-V": 4,
"2019 Cadillac CTS-V": 4,
"2019 Cadillac CTS 3.6L V6": 4,
"2019 Cadillac ATS-V Coupe": 4,
"2016 Cadillac ELR": 2,
"2020 Cadillac CT6 Platinum": 4,
"2020 Cadillac Escalade": 6,
"2020 Cadillac XT5": 4,
"2014 Cadillac CTS-V Sport Wagon": 4,
"2004 Cadillac Seville": 4,
"2011 Cadillac DTS": 4,
"1975 Cadillac Fleetwood Brougham": 4,
"1976 Cadillac Eldorado": 4,
"1959 Cadillac Eldorado Brougham": 4,
"Renault R35 Tank": 3,
"2019 Renault Clio Iconic TCe 100": 4,
"2019 Renault Clio RS Line TCe 130": 4,
"2019 Renault Clio E-TECH Launch Edition": 4,
"2018 Renault Clio RS Trophy": 4,
"2003 Renault Clio V6": 2,
"1993 Renault Clio Williams": 4,
"1993 Renault Clio": 4,
"1993 Renault Twingo": 4,
"2010 Renault Twingo RS 133 Cup": 4,
"2010 Renault Twingo RS": 4,
"2020 Renault Twingo": 4,
"2020 Renault Megane RS 300 Trophy": 4,
"2020 Renault Megane RS Trophy R": 4,
"2020 Renault Megane RS Line TCe 140": 4,
"2005 Renault Megane Sport 225 Cup": 4,
"LIGHNING MCQUEEN": 1,
"2018 Fortnite Shopping Cart GT-S": 1,
"2019 Fortnite ATK GT-4R": 1,
"1009 Thanos Car": 1
}

Car_Comfort = {
"2000 Honda Integra" : 4,
"2000 Honda Integra Type R" : 2,
"1999 Honda Civic Type R EK9" : 2,
"2003 Honda Civic Type R EP3" : 2,
"2003 Honda NSX R" : 1,
"2001 Honda S2000" : 2,
"2021 Honda Civic Type R FK8" : 3,
"1991 Honda Civic EG6 SiR": 2,
"1999 Honda Civic LX": 3,
"2006 Honda Civic Si": 4,
"2018 Honda Civic Sport": 4,
"2018 Honda Civic Si Coupe": 4,
"2006 Honda Accord 3.0 EX": 5,
"2010 Honda Accord EX-L V6": 5,
"2015 Honda Accord Sport": 5,
"2015 Honda Accord EX-L V6": 5,
"2018 Honda Accord Sport": 5,
"2021 Honda CR-V": 5,
"1999 Honda CR-V": 3,
"2005 Honda Pilot": 4,
"2010 Honda Crosstour": 4.5,
"2005 Honda Element": 3,
"2001 Honda Odyssey Absolute": 4,
"2021 Honda N-ONE RS": 2,
"2021 Honda StepWGN Spada": 5.5,
"1999 Honda StepWGN": 3.5,
"2016 Honda CR-Z": 3,
"2021 Honda HR-V": 5, 
"2005 Honda Stream": 4.5,
"2014 Honda Stream": 5,
"2021 Honda Clarity": 5,
"2000 Honda Insight": 3,
"2021 Honda Insight": 5.5,
"2000 Honda ACTY": 2,
"2021 Honda ACTY": 2,
"2021 Honda Fit": 4,
"2001 Honda Life Dunk": 2.5,
"1992 Honda Vigor": 5,
"1989 Honda Accord": 3.5,
"2003 Acura RSX Type S" : 3,
"2017 Acura NSX" : 3,
"2005 Acura TL Type S": 5,
"2007 Acura TL": 5,
"2018 Acura TLX 3.5": 6,
"2018 Acura MDX": 6,
"2018 Acura ILX": 5,
"2021 Acura TLX Type S": 5.5,
"1995 Acura Legend": 6,
"2014 Acura TSX Sport Wagon": 5,
"1990 Ford Mustang Foxbody" : 3,
"2010 Ford Mustang GT500" : 3,
"2015 Ford Mustang GT" : 4,
"1975 Ford Pinto": 3,
"1999 Ford Crown Victoria": 4,
"2017 Ford Focus Hatch": 4,
"2017 Ford Focus RS": 3,
"2017 Ford Fusion Titanium": 5,
"2017 Ford Fusion Sport": 4,
"2018 Ford F-150 Super Cab": 6,
"2018 Ford F-150 Raptor": 4,
"2016 Shelby Mustang GT350R" : 2,
"1992 Volkswagen Golf GTi MK2" : 3,
"2017 Volkswagen Golf GTi MK7" : 5,
"2015 Volkswagen Scirocco R" : 5,
"2018 Volkswagen Passat R-Line": 6,
"1969 Volkswagen Beetle": 2,
"1999 BMW M3" : 3,
"2003 BMW M3" : 4,
"2008 BMW M3" : 5,
"2017 BMW M3" : 6,
"2005 BMW M5" : 5,
"2018 BMW M5" : 6,
"2017 BMW M4" : 6,
"2017 BMW M6" : 7,
"2018 BMW i8" : 5,
"1959 BMW 507": 2,
"2018 BMW 530i": 8,
"2018 BMW X3": 7,
"2018 BMW 750i": 9,
"1974 BMW 2002 Turbo": 2,
"2011 BMW 1M": 4,
"2018 BMW 330i": 7,	
"2020 BMW M235i xDrive Gran Coupe": 5,
"2007 Saturn Ion": 2,
"2001 Saturn SL2": 2,
"1998 Saturn SW2": 2,
"2017 Ferrari 488GTB" : 4,
"2017 Ferrari F12" : 5,
"2003 Ferrari 575M Maranello" : 5,
"1999 Ferrari 360" : 2,
"1995 Ferrari F355" : 2,
"1965 Ferrari 250 GTO" : 2,
"1968 Ferrari Dino" : 2,
"1970 Ferrari 365 GTB/4 Daytona" : 3,
"2008 Ferrari F430" : 3,
"2008 Ferrari California" : 5,
"2016 Ferrari LaFerrari" : 2,
"2010 Ferrari 458 Italia": 3,
"1993 Toyota MR2 GT-S" : 1,
"1986 Toyota Corolla Sprinter Trueno" : 2,
"1993 Toyota Supra Twin Turbo" : 3,
"1998 Toyota Chaser Tourer V" : 5,
"1997 Toyota Soarer" : 3,
"1996 Toyota Cresta 2.5 Twin Turbo": 4,
"1998 Toyota Altezza RS200" : 4,
"1984 Toyota Landcruiser 60 3F" : 5,
"2003 Toyota Tundra" : 4,
"2018 Toyota Land Cruiser Prado" : 5,
"2018 Toyota 4Runner TRD Pro" : 4,
"2018 Toyota Tundra TRD Pro" : 5,
"1992 Toyota Hilux Surf SSR-G Wide Body" : 4,
"2017 Toyota Century": 10,
"2019 Toyota Corolla Hatch XSE": 4,
"2019 Toyota Corolla Hatch SE": 4,
"2019 Toyota Corolla Touring Sport": 5,
"2021 Toyota GR Supra": 3,
"2008 Toyota Sequoia V8": 5,
"2005 Toyota Camry LE V6": 5,
"1999 Toyota Corolla LE": 4,
"2002 Toyota Sienna 5D Symphony": 6,
"2010 Toyota Camry LE": 4, 
"2016 Toyota Avalon Limited": 8,
"2018 Toyota Camry XSE": 5,
"2018 Toyota Corolla XLE": 6,
"1969 Toyota 2000GT": 3,
"2001 Toyota Camry LE V6": 4,
"2006 Toyota Sienna Limited": 5,
"2017 Toyota Sienna SE": 6,
"2018 Toyota Sienta": 5,
"2018 Toyota Alphard": 8,
"2018 Toyota Crown Majesta": 8,
"2018 Toyota Tundra SR5 5.7L V8": 4,
"2018 Toyota Hiace": 6,
"1993 Toyota Hiace": 4, 
"1997 Toyota Celica GT-Four": 3,
"1998 Toyota GT-one TS020": 1,
"1993 Toyota Mark II Tourer V JZX90": 5,
"2018 Toyota GT86": 3,
"1997 Toyota Tercel": 2,
"1997 Toyota Celica GT": 2,
"2016 Toyota Land Cruiser": 6,
"2019 Toyota Tacoma SR5": 4,
"2019 Toyota Tacoma TRD Pro": 4,
"1993 Toyota Sera": 2,
"2020 Toyota Avalon Touring": 7,
"2020 Toyota Avalon Limited": 8,
"2020 Toyota Avalon Limited Hybrid": 8,
"2020 Toyota Avalon TRD": 6,
"2020 Toyota Camry LE": 6,
"2020 Toyota Camry SE Hybrid": 7,
"2011 Toyota Prius": 3,
"2020 Toyota Prius XLE AWD": 5,
"2021 Toyota GR Yaris": 3,
"2022 Toyota GR86 Base": 4,
"2022 Toyota GR86 Premium": 5,
"2018 Toyota Camry SE": 5,
"2009 Lexus LFA" : 2,
"2007 Lexus ISF" : 6,
"1998 Lexus GS300" : 4,
"2018 Lexus LC500" : 9,
"2018 Lexus LS500 AWD" : 10,
"2019 Lexus ES300h": 8,
"2018 Lexus GS F": 8,
"2003 Lexus LS430": 7,
"2019 Lexus RX350": 6,
"1999 Lexus RX300 4WD": 5,
"2019 Lexus LX570": 9,
"2022 Lexus IS500 F Sport Performance": 7,
"2022 Lexus IS350 F Sport": 7,
"1990 Nissan Skyline GTR R32" : 2,
"1994 Nissan Skyline GTR R33 Spec-V" : 2,
"1999 Nissan Skyline GTR R34": 3,
"2002 Nissan Skyline GTR V-Spec II Nur" : 2,
"1996 Nissan 180SX" : 2,
"1993 Nissan Silvia K's Type S S14" : 2,
"2018 Nissan GTR Track Edition R35" : 5,
"2007 Nissan Fairlady Z" : 2,
"2018 Nissan Fairlady Z NISMO" : 2,
"2018 Nissan Fairlady Z" : 3,
"1989 Nissan 300ZX Turbo Z" : 3,
"2018 Nissan GT-R50 by Italdesign": 4,
"2018 Nissan GT-R NISMO": 4,
"2018 Nissan Maxima Platinum": 7,
"2018 Nissan Sentra SR Turbo": 4,
"2017 Nissan Leaf": 5,
"1973 Nissan Skyline H/T 2000GT-R": 2,
"1987 Nissan Skyline GTSR R31": 2,
"1989 Nissan Skyline GTS-4 R32": 4,
"1998 Nissan Skyline 25GT-X Turbo R34": 5,
"1965 Nissan Silvia 1600 Coupe": 2,
"1990 Nissan Silvia S13": 2,
"1999 Nissan Silvia Spec-R S15": 3,
"1995 Nissan GT-R Skyline R33 LM": 2,
"1998 Nissan R390 GT1": 1,
"1992 Nissan Cefiro 2.0 Turbo": 4,
"1990 Nissan Laurel Turbo Medalist": 5,
"2017 Nissan Armada Platinum": 7,
"1994 Nissan Hardbody": 2,
"2018 Nissan Titan Platinum Reserve": 7,
"2003 Nissan Skyline GT-R R34 Z-Tune": 2,
"2015 Nissan Juke": 4,
"2021 Nissan Altima 2.0 SR": 5,
"2021 Nissan Altima 2.5 Platinum": 6,
"2022 Nissan GT-R T-Spec": 5,
"2015 Lamborghini Veneno": 3,
"2003 Lamborghini Gallardo" : 3,
"2007 Lamborghini Gallardo SL" : 3,
"2008 Lamborghini Gallardo LP560-4" : 3,
"2010 Lamborgini Gallardo LP570-4 SL ": 3,
"2013 Lamborghini Gallardo LP570-4 SC" : 3,
"2014 Lamborghini Huracan LP610-4" : 4,
"2017 Lamborghini Huracan Performante" : 3,
"2001 Lamborghini Murcielago" : 3,
"2006 Lamborghini Murcielago LP640" : 3,
"2009 Lamborghini Murcielago LP670-4 SV" : 2,
"2015 Lamborghini Aventador SV" : 3,
"2016 Lamborghini Aventador S" : 4,
"1971 Lamborghini Miura P400SV" : 2,
"1996 Lamborghini Diablo SV" : 2,
"1985 Lamborghini Countach LP5000s QV" : 1,
"2020 Lamborghini Sian": 3, 
"2021 Lamborghini Urus": 6,
"2021 Lamborghini Huracan Evo": 4,  
"1995 Lamborghini Diablo SE30 Jota": 2, 
"2000 Lamborghini Diablo GTR": 1, 
"2017 Bentley Continental GT" : 8,
"2015 Bentley Bentayga" : 9,
"2015 Koenigsegg Regera" : 4,
"2010 Koenigsegg Agera" : 2,
"2007 Koenigsegg CCX" : 1,
"2005 Bugatti Veyron 16.4" : 5,
"2016 Bugatti Chiron" : 7,
"2017 Porsche 911 GT2 RS" : 2,
"2017 Porsche Panamera Turbo Sport Turismo Sport Plus" : 7,
"2016 Porsche 911 Turbo" : 3,
"2016 Porsche 718 Boxster" : 2,
"2017 Porsche 718 Cayman GTS" : 2,
"1975 Porsche 911 Turbo" : 2,
"1995 Porsche 911 GT2" : 2,
"1987 Porsche 959" : 3,
"1999 Porsche 911 GT3" : 2,
"1980 Porsche 924 Turbo": 3,
"2015 Lotus Evora 400" : 4,
"2011 Lotus Exige S" : 1,
"1996 Lotus Esprit V8" : 3,
"2006 Lotus Elise S" : 2,
"2018 Mazda Miata MX-5 Club" : 3,
"2004 Mazda Mazdaspeed MX-5 Miata Turbo" : 1,
"1989 Mazda MX-5 Miata" : 2,
"1989 Mazda RX-7 Savanna Turbo" : 2,
"1992 Mazda RX-7" : 2,
"1998 Mazda RX-7 RZ" : 2,
"2009 Mazda RX-8" : 4,
"2019 Mazda6 Signature": 7,
"2019 Mazda3 Hatch": 5,
"2019 Mazda CX-5": 4,
"2019 Mazda CX-3": 4,
"2014 Mazda2": 4,
"2015 Mazda5": 6,
"2006 Mazdaspeed 6 GT": 4,
"2013 Mazdaspeed 3": 4,
"2001 Mazda RX-7 Spirit R Type A": 2,
"2018 Morgan Three-Wheeler" : 1,
"1998 Subaru Impreza 22B STi": 2,
"1995 Subaru Impreza WRX STi Version II": 3,
"2002 Subaru Impreza WRX STi": 3,
"2003 Subaru Impreza WRX STi": 3,
"2005 Subaru Impreza WRX STi": 3,
"2010 Subaru Impreza WRX STi R205": 2,
"2019 Subaru WRX STi": 3,
"1993 Subaru SVX": 4,
"2000 Subaru Forester STI": 4,
"2019 Subaru WRX": 4,
"2022 Subaru WRX": 5,
"2018 Subaru BRZ": 3.5,
"2022 Subaru BRZ Premium": 4,
"2022 Subaru BRZ Limited": 5,
"1988 Isuzu Impulse": 2,
"1979 Isuzu 117 Coupe": 2,
"1994 Mitsubishi Lancer Evo II": 2,
"2010 Mitsubishi Lancer Evo X GSR": 3,
"1999 Mitsubishi Lancer Evo VI GSR": 2,
"2004 Mitsubishi Lancer Evo VIII MR FQ400": 2,
"2003 Mitsubishi Lancer Evo VIII GSR": 3,
"1994 Mitsubishi 3000 GT VR-4": 2,
"1994 Mitsubishi FTO GPX": 2,
"1992 Mitsubishi Galant VR-4": 3,
"1974 VAZ Lada 1200": 1,
"1975 UAZ-469": 1,
"1965 GAZ Volga 21": 4,
"1995 Hyundai Sonata 2.0i": 2,
"2013 Hyundai Genesis Coupe 3.8" : 4,
"2013 Hyundai Elantra GT": 4,
"2017 Hyundai Sonata Limited": 5,
"2018 Kia Stinger GT": 6,
"2017 Kia Optima SX 2.0T": 5,
"2005 Hyundai Tiburon GT V6": 2,
"2006 Audi R8": 4,
"2008 Audi R8 V10": 4,
"2010 Audi R8 GT": 3,
"2012 Audi R8 Plus": 4,
"2015 Audi R8 Coupe 5.2 FSI quattro": 4, 
"1994 Audi RS2 Avant": 4,
"2018 Audi RS5": 7,
"2018 Audi RS3": 6,
"2018 Audi RS7": 8,
"2018 Audi RS6 Avant": 7,
"2018 Audi TTRS": 3,
"2018 Mercedes-AMG E63 S 4Matic": 7,
"2018 Mercedes-Maybach S560": 10,
"2018 Mercedes-AMG S65 Sedan": 9,
"1990 Mercedes-Benz 190E Evolution II": 2,
"2016 Mercedes-AMG GT S": 4,
"2013 Mercedes-Benz SLS AMG GT": 3,
"2012 Mercedes-Benz C63 AMG Black Series": 2,
"2000 Mercedes-Benz C32 AMG": 5,
"2020 Mercedes-AMG A35 4Matic": 4,
"2020 Chevy Corvette C8 Stingray Z51": 3,
"2019 Chevy Corvette C7 ZR1": 2,
"2018 Chevy Corvette C7 ZO6": 2,
"2018 Chevy Corvette C7 Stingray": 2,
"1953 Chevy Corvette": 2,
"1960 Chevy Corvette C1": 2,
"1963 Chevy Corvette C2 Stingray 427": 1,
"1967 Chevy Corvette C3 327": 2,
"1970 Chevy Corvette C3 454": 2,
"1984 Chevy Corvette C4": 2,
"1988 Chevy Corvette C4 ZR1": 2,
"2001 Chevy Corvette C5": 2,
"2002 Chevy Corvette C5 Z06": 2,
"2007 Chevy Corvette C6": 2,
"2007 Chevy Corvette C6 Z06": 2,
"2007 Chevy Corvette C6 ZR1": 2,
"2018 Chevy Camaro 1LE": 2,
"2018 Chevy Camaro ZL1": 2,
"1969 Chevy Camaro SS 396": 2,
"2017 Chevy Malibu 1.5 Turbo": 5,
"2016 Chevy Malibu 2LT": 5,
"2017 Chevy Cruze Hatch Premier": 4,
"2016 Chevy Impala LT": 6,
"2018 Alfa Romeo 4C": 2,
"2018 Alfa Romeo Giulia Quadrifoglio": 6,
"2018 Alfa Romeo Stelvio Quadrifoglio": 6,
"2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde": 4,
"2013 Alfa Romeo MiTo 1.4 8v": 3,
"2010 Alfa Romeo Brera 3.2 JTS V6 24v": 3,
"2006 Alfa Romeo 8c Competizione": 2,
"1992 Alfa Romeo 155 Q4": 3,
"1985 Alfa Romeo Spider Veloce": 1,
"2017 Suzuki Swift Sport": 4,
"2016 Suzuki Alto Works": 3,
"2016 Suzuki Hustler G 4WD": 4,
"2003 Suzuki Liana 1.6 Sedan": 4, 	
"1995 Suzuki Samurai 1.3i": 2,
"2002 Suzuki Grand Vitara": 4,
"2018 Pagani Huayra BC": 2,
"2013 Pagani Huayra": 3,
"2010 Pagani Zonda Cinque": 1,
"2005 Pagani Zonda F": 2,
"1999 Pagani Zonda C12S": 2,
"1970 AMC AMX": 2,
"1972 AMC Javelin": 2,
"1969 AMC Ambassador": 4,
"1970 AMC Rebel The Machine": 2,
"1975 AMC Pacer X": 4,
"2018 Dodge Challenger SRT Hellcat Widebody": 3,
"2018 Dodge Challenger 392 HEMI Scat Pack Shaker": 4,
"2018 Dodge Challenger SRT Demon": 2,
"2008 Dodge Challenger SE": 4,
"2008 Dodge Challenger SRT8": 3,
"2018 Dodge Charger Hellcat": 4,
"2018 Dodge Charger GT Plus": 5,
"2011 Dodge Charger SRT8": 5,
"2005 Dodge Charger SRT8": 4,
"2017 Dodge Viper ACR": 1,
"2017 Dodge Viper GTS": 3,
"2012 Dodge Dart R/T": 4,
"2010 Dodge Avenger Express": 4,
"2008 Dodge Journey SXT": 3,
"2007 Dodge Nitro 4.0 R/T": 3,
"2007 Dodge Viper SRT-10": 2,
"2007 Dodge Viper SRT10 ACR": 1,
"2000 Dodge Intrepid R/T": 3,
"2003 Dodge Neon SRT-4": 3,
"1970 Dodge Dart Hemi Super Stock": 1,
"1970 Dodge Dart Swinger 340": 3,
"1970 Dodge Challenger R/T 426 Hemi": 3,
"1969 Dodge Charger Daytona Hemi": 2,
"1969 Dodge Charger R/T Hemi": 4,
"2018 Mclaren Senna": 1,
"2018 McLaren 720S": 3,
"2015 McLaren 570S": 4,
"2013 McLaren MP4-12C": 4,
"1992 McLaren F1": 3,
"1997 McLaren F1 GT": 2,
"1995 McLaren F1 LM": 1,
"2013 McLaren P1": 2,
"1974 MG Midget": 2,
"1928 MG M-Type Midget": 1,
"2007 Aston Martin DBS": 5,
"2016 Aston Martin DB11": 6,
"2016 Aston Martin V12 Vantage S": 4,
"2018 Aston Martin DBS Superleggera": 4,
"2013 Aston Martin V8 Vantage": 5,
"2011 Aston Martin One-77": 3,
"2004 Aston Martin Vanquish S": 5,
"2008 Aston Martin DB9": 6,
"2019 Aston Martin Valkyrie": 1,
"2018 Range Rover Supercharged": 8,
"2018 Range Rover Velar R-Dynamic": 7,
"2018 Range Rover Sport SVR": 7,
"2016 Land Rover Defender 70th Edition": 7,
"1957 Land Rover Series 1": 3,
"2003 Infiniti G35": 4,
"2017 Infiniti Q60 Red Sport": 6,
"2015 Infiniti Q50 Eau Rouge": 6,
"2019 Infiniti Q50": 7,
"2019 Tesla Model S Ludicrous Performance": 6,
"2019 Tesla Model S Standard Range": 6,
"2019 Tesla Model 3 Performance": 5,
"2019 Tesla Model 3 Standard Range": 6,
"2019 Tesla Model X Ludicrous Performance": 6,
"2019 Tesla Model X Standard Range": 6,
"2019 Mini Cooper S": 4,
"2019 Mini John Cooper Works": 3,
"1969 Morris Mini Cooper S": 2,
"2020 Cadillac CT4-V": 6,
"2019 Cadillac CTS-V": 5,
"2019 Cadillac CTS 3.6L V6": 7,
"2019 Cadillac ATS-V Coupe": 5,
"2016 Cadillac ELR": 3,
"2020 Cadillac CT6 Platinum": 9,
"2020 Cadillac Escalade": 7,
"2020 Cadillac XT5": 6,
"2014 Cadillac CTS-V Sport Wagon": 5,
"2004 Cadillac Seville": 6,
"2011 Cadillac DTS": 6,
"1975 Cadillac Fleetwood Brougham": 5,
"1976 Cadillac Eldorado": 5,
"1959 Cadillac Eldorado Brougham": 4,
"Renault R35 Tank": 2,
"2019 Renault Clio Iconic TCe 100": 3,
"2019 Renault Clio RS Line TCe 130": 4,
"2019 Renault Clio E-TECH Launch Edition": 4,
"2018 Renault Clio RS Trophy": 3,
"2003 Renault Clio V6": 2,
"1993 Renault Clio Williams": 2,
"1993 Renault Clio": 2,
"1993 Renault Twingo": 2,
"2010 Renault Twingo RS 133 Cup": 2,
"2010 Renault Twingo RS": 3,
"2020 Renault Twingo": 4,
"2020 Renault Megane RS 300 Trophy": 3,
"2020 Renault Megane RS Trophy R": 2,
"2020 Renault Megane RS Line TCe 140": 5,
"2005 Renault Megane Sport 225 Cup": 2,
"LIGHNING MCQUEEN": 1,
"2018 Fortnite Shopping Cart GT-S": 1,
"2019 Fortnite ATK GT-4R": 1,
"1009 Thanos Car": 1
}

region = {
"0": "Asia",
"1": "North America",
"2": "Europe"
}

raritylevel_1 = ["2003 Toyota Tundra", "2018 Toyota Camry SE", "1993 Renault Clio", "2021 Honda CR-V", "2020 Toyota Camry LE", "2021 Honda HR-V", "2019 Renault Clio Iconic TCe 100", "1999 Honda CR-V", "2005 Honda Pilot", "2020 Renault Twingo", "2021 Honda Insight", "2000 Honda ACTY", "2021 Honda ACTY", "2020 Toyota Camry SE Hybrid", "2011 Toyota Prius", "2020 Toyota Prius XLE AWD", "2019 Mini Cooper S", "2011 Cadillac DTS", "2019 Tesla Model 3 Standard Range", "2019 Mazda CX-5", "2019 Mazda6 Signature", "2020 Cadillac XT5", "2015 Mazda5", "2014 Mazda2", "2019 Mazda CX-3", "2019 Mazda3 Hatch", "2019 Mazda3 Hatch", "2019 Toyota Tacoma SR5", "2018 Volkswagen Passat R-Line", "2007 Saturn Ion", "2001 Saturn SL2", "1998 Saturn SW2", "2018 BMW 330i", "2019 Toyota Corolla Hatch SE", "1997 Toyota Tercel", "2018 BMW 530i","2018 BMW X3","2012 Dodge Dart R/T", "2010 Dodge Avenger Express", "2008 Dodge Journey SXT", "2018 Nissan Maxima Platinum", "2018 Dodge Charger GT Plus", "2018 Nissan Sentra SR Turbo", "2017 Nissan Leaf", "2005 Toyota Camry LE V6", "1999 Toyota Corolla LE", "2002 Toyota Sienna 5D Symphony", "2010 Toyota Camry LE", "2016 Toyota Avalon Limited", "2018 Toyota Camry XSE", "2018 Toyota Corolla XLE", "2001 Toyota Camry LE V6", "2006 Toyota Sienna Limited", "2008 Toyota Sequoia V8", "2017 Ford Fusion Titanium", "2007 Acura TL", "2017 Ford Fusion Sport", "2018 Acura MDX", "2018 Acura ILX", "1999 Ford Crown Victoria", "2017 Ford Focus Hatch", "1999 Honda Civic LX", "2015 Honda Accord Sport", "2018 Honda Accord Sport", "2018 Honda Civic Sport", "2019 Toyota Corolla Hatch XSE", "2019 Toyota Corolla Hatch XSE", "2019 Lexus RX350", "1999 Lexus RX300 4WD", "1995 Hyundai Sonata 2.0i", "2013 Hyundai Elantra GT", "2017 Hyundai Sonata Limited", "2017 Kia Optima SX 2.0T", "2017 Chevy Malibu 1.5 Turbo", "2016 Chevy Malibu 2LT", "2017 Chevy Cruze Hatch Premier",  "2016 Chevy Impala LT", "2017 Suzuki Swift Sport", "2016 Suzuki Hustler G 4WD", "2002 Suzuki Grand Vitara"]
raritylevel_2 = ["2019 Toyota Corolla Touring Sport", "2015 Nissan Juke", "2005 Honda Element", "2021 Nissan Altima 2.0 SR", "1993 Renault Twingo", "2021 Nissan Altima 2.5 Platinum", "1989 Honda Accord", "2020 Renault Megane RS Line TCe 140", "2019 Renault Clio E-TECH Launch Edition", "1969 Volkswagen Beetle", "2019 Tesla Model S Standard Range", "2019 Renault Clio RS Line TCe 130", "2021 Honda Fit", "2019 Infiniti Q50", "1994 Nissan Hardbody", "2004 Cadillac Seville", "2018 Nissan Titan Platinum Reserve", "2000 Dodge Intrepid R/T",  "2008 Dodge Challenger SE", "2018 Ford F-150 Super Cab", "2018 Acura TLX 3.5", "2006 Honda Accord 3.0 EX", "2015 Honda Accord EX-L V6", "1998 Lexus GS300",  "2010 Honda Accord EX-L V6", "2003 Lexus LS430", "2019 Lexus ES300h", "2016 Suzuki Alto Works", "2003 Suzuki Liana 1.6 Sedan", "1995 Suzuki Samurai 1.3i", "2018 Toyota Hiace", "1993 Toyota Hiace", ]
raritylevel_3 = ["2000 Honda Integra", "2022 Lexus IS350 F Sport", "2019 Subaru WRX", "2022 Subaru WRX", "2018 Subaru BRZ", "2022 Subaru BRZ Premium", "2022 Subaru BRZ Limited", "2022 Toyota GR86 Base",  "2022 Toyota GR86 Premium", "2020 Toyota Avalon Touring", "2021 Honda StepWGN Spada", "1999 Honda StepWGN", "2005 Honda Stream", "2019 Cadillac CTS 3.6L V6", "2021 Honda Clarity", "2020 Toyota Avalon Limited", "2020 Toyota Avalon Limited Hybrid", "2010 Honda Crosstour", "2019 Tesla Model X Standard Range", "2018 Honda Civic Si Coupe", "1997 Toyota Celica GT" ,"2018 Toyota GT86", "2007 Dodge Nitro 4.0 R/T", "1992 Volkswagen Golf GTi MK2", "2018 Mazda Miata MX-5 Club", "2001 Chevy Corvette C5", "2006 Honda Civic Si", "2017 Toyota Sienna SE", "2018 Toyota Sienta", "2018 Toyota Alphard", "2018 Toyota Crown Majesta", "2018 Toyota Tundra SR5 5.7L V8", ]
raritylevel_4 = ["1990 Ford Mustang Foxbody", "1995 Acura Legend", "2021 Honda N-ONE RS", "2014 Acura TSX Sport Wagon", "2016 Honda CR-Z", "2014 Honda Stream", "2020 Toyota Avalon TRD", "2019 Mini John Cooper Works",  "2013 Mazdaspeed 3", "2003 Infiniti G35", "2015 Mazda5", "2017 Nissan Armada Platinum", "2018 BMW 750i", "1980 Porsche 924 Turbo", "2011 Dodge Charger SRT8", "2020 Cadillac CT6 Platinum", "2020 Cadillac Escalade", "2018 Dodge Challenger 392 HEMI Scat Pack Shaker", "2008 Dodge Challenger SRT8", "1972 AMC Javelin", "1969 AMC Ambassador", "1975 Ford Pinto", "2015 Ford Mustang GT", "2017 Volkswagen Golf GTi MK7", "1992 Nissan Cefiro 2.0 Turbo", "2015 Volkswagen Scirocco R", "2019 Lexus LX570", "2018 Nissan Fairlady Z", "2016 Porsche 718 Boxster", "1989 Mazda MX-5 Miata", "1984 Chevy Corvette C4", "2007 Chevy Corvette C6", "2018 Toyota Land Cruiser Prado", "1992 Toyota Hilux Surf SSR-G Wide Body"]
raritylevel_5 = ["2001 Honda S2000", "1992 Honda Vigor", "2001 Honda Life Dunk", "2001 Honda Odyssey Absolute", "2021 Acura TLX Type S", "2018 Renault Clio RS Trophy", "2010 Renault Twingo RS", "2020 Renault Megane RS 300 Trophy", "2000 Honda Insight", "2005 Renault Megane Sport 225 Cup", "1969 Morris Mini Cooper S", "2005 Subaru Impreza WRX STi", "2020 Mercedes-AMG A35 4Matic", "2006 Mazdaspeed 6 GT", "2020 BMW M235i xDrive Gran Coupe", "2015 Mazda5", "2019 Toyota Tacoma TRD Pro", "2017 Infiniti Q60 Red Sport", "2016 Toyota Land Cruiser", "2020 Chevy Corvette C8 Stingray Z51", "2003 Dodge Neon SRT-4", "2018 Range Rover Supercharged",  "1994 Mitsubishi 3000 GT VR-4", "2018 Range Rover Velar R-Dynamic", "1974 MG Midget", "1993 Subaru SVX", "1970 AMC AMX",  "1990 Nissan Silvia S13", "2005 Dodge Charger SRT8", "1999 Nissan Silvia Spec-R S15", "1990 Nissan Laurel Turbo Medalist", "1989 Nissan Skyline GTS-4 R32", "1998 Nissan Skyline 25GT-X Turbo R34", "2013 Hyundai Genesis Coupe 3.8", "2005 Acura TL Type S", "2003 Acura RSX Type S", "2003 BMW M3", "2008 BMW M3", "2017 BMW M3", "2017 BMW M4","2017 Ford Focus RS", "1997 Toyota Soarer", "1998 Toyota Altezza RS200", "2018 Lexus LS500 AWD", "2007 Nissan Fairlady Z", "1989 Nissan 300ZX Turbo Z", "2017 Porsche 718 Cayman GTS", "2015 Lotus Evora 400", "2006 Lotus Elise S","2003 Subaru Impreza WRX STi", "2004 Mazda Mazdaspeed MX-5 Miata Turbo", "1974 VAZ Lada 1200", "1975 UAZ-469", "2005 Hyundai Tiburon GT V6", "2018 Chevy Camaro 1LE", "2000 Honda Integra Type R", "2003 Honda Civic Type R EP3", "2021 Honda Civic Type R FK8", "2010 Ford Mustang GT500", "1999 BMW M3", "2018 Toyota 4Runner TRD Pro", "2018 Toyota Tundra TRD Pro", "1996 Nissan 180SX", "1993 Nissan Silvia K's Type S S14", "1995 Subaru Impreza WRX STi Version II", "2002 Subaru Impreza WRX STi", "2019 Subaru WRX STi", "1994 Mitsubishi Lancer Evo II", "2010 Mitsubishi Lancer Evo X GSR", "1999 Mitsubishi Lancer Evo VI GSR", "2003 Mitsubishi Lancer Evo VIII GSR", "1999 Honda Civic Type R EK9", "2009 Mazda RX-8" ]
raritylevel_6 = ["2005 BMW M5", "2022 Lexus IS500 F Sport Performance", "2010 Renault Twingo RS 133 Cup", "2011 BMW 1M", "2021 Toyota GR Yaris", "2020 Renault Megane RS Trophy R", "2019 Tesla Model S Ludicrous Performance", "2019 Cadillac CTS-V", "2019 Tesla Model 3 Performance", "2019 Tesla Model X Ludicrous Performance", "2000 Mercedes-Benz C32 AMG", "2020 Cadillac CT4-V", "1992 Mitsubishi Galant VR-4", "2008 Aston Martin DB9", "2018 BMW i8", "2013 Aston Martin V8 Vantage", "2018 Range Rover Sport SVR", "1994 Mitsubishi FTO GPX", "2018 Dodge Charger Hellcat",  "2018 Dodge Challenger SRT Hellcat Widebody", "2018 Ford F-150 Raptor", "1985 Alfa Romeo Spider Veloce", "2018 BMW M5", "1993 Toyota MR2 GT-S", "1993 Toyota Mark II Tourer V JZX90", "2018 Kia Stinger GT", "1996 Toyota Cresta 2.5 Twin Turbo", "1998 Toyota Chaser Tourer V", "1984 Toyota Landcruiser 60 3F",  "2018 Nissan Fairlady Z NISMO", "2017 Porsche Panamera Turbo Sport Turismo Sport Plus", "2016 Porsche 911 Turbo", "2011 Lotus Exige S", "2018 Audi RS5", "2018 Audi RS3", "2018 Audi RS7", "2018 Audi RS6 Avant", "2018 Audi TTRS", "2018 Mercedes-AMG E63 S 4Matic", "2018 Chevy Corvette C7 Stingray", "1967 Chevy Corvette C3 327", "2002 Chevy Corvette C5 Z06", "2018 Alfa Romeo Stelvio Quadrifoglio", "2013 Alfa Romeo MiTo 1.4 8v", "1991 Honda Civic EG6 SiR", "1989 Mazda RX-7 Savanna Turbo", "1992 Mazda RX-7",  "2018 Kia Stinger GT", ]
raritylevel_7 = ["2017 Acura NSX", "2021 Lamborghini Urus", "1993 Toyota Sera", "2000 Subaru Forester STI", "2015 McLaren 570S", "2016 Land Rover Defender 70th Edition", "1993 Renault Clio Williams", "1975 Cadillac Fleetwood Brougham", "2004 Aston Martin Vanquish S",  "2007 Aston Martin DBS", "2016 Aston Martin DB11", "2016 Aston Martin V12 Vantage S", "2016 Cadillac ELR", "2013 McLaren MP4-12C", "1928 MG M-Type Midget", "1970 Dodge Dart Swinger 340", "1969 Dodge Charger R/T Hemi", "1975 AMC Pacer X", "1970 Dodge Challenger R/T 426 Hemi", "2017 Dodge Viper GTS", "2007 Dodge Viper SRT-10", "2016 Shelby Mustang GT350R", "2017 BMW M6", "1999 Ferrari 360", "1995 Ferrari F355", "2008 Ferrari F430", "1986 Toyota Corolla Sprinter Trueno", "1993 Toyota Supra Twin Turbo", "2021 Toyota GR Supra", "2007 Lexus ISF", "2018 Lexus LC500", "2018 Lexus GS F", "1990 Nissan Skyline GTR R32", "1994 Nissan Skyline GTR R33 Spec-V", "1999 Nissan Skyline GTR R34", "2018 Nissan GTR Track Edition R35", "2003 Lamborghini Gallardo", "2008 Lamborghini Gallardo LP560-4", "2014 Lamborghini Huracan LP610-4", "2017 Bentley Continental GT", "2015 Bentley Bentayga", "1975 Porsche 911 Turbo", "1995 Porsche 911 GT2", "1999 Porsche 911 GT3", "1996 Lotus Esprit V8", "1998 Mazda RX-7 RZ", "2010 Subaru Impreza WRX STi R205", "1965 GAZ Volga 21", "2006 Audi R8", "2008 Audi R8 V10", "2012 Audi R8 Plus", "1994 Audi RS2 Avant", "2015 Audi R8 Coupe 5.2 FSI quattro", "2018 Mercedes-AMG S65 Sedan", "1990 Mercedes-Benz 190E Evolution II", "2016 Mercedes-AMG GT S", "2013 Mercedes-Benz SLS AMG GT", "2012 Mercedes-Benz C63 AMG Black Series", "2018 Chevy Corvette C7 ZO6", "1970 Chevy Corvette C3 454", "2007 Chevy Corvette C6 Z06", "2018 Chevy Camaro ZL1", "1969 Chevy Camaro SS 396", "2018 Alfa Romeo 4C", "2018 Alfa Romeo Giulia Quadrifoglio", "2010 Alfa Romeo Brera 3.2 JTS V6 24v" ]
raritylevel_8 = ["2003 Honda NSX R", "2021 Lamborghini Huracan Evo", "2022 Nissan GT-R T-Spec", "2004 Mitsubishi Lancer Evo VIII MR FQ400", "2001 Mazda RX-7 Spirit R Type A", "2015 Infiniti Q50 Eau Rouge", "1974 BMW 2002 Turbo", "2003 Renault Clio V6", "1957 Land Rover Series 1", "1976 Cadillac Eldorado", "2018 Aston Martin DBS Superleggera", "2017 Dodge Viper ACR", "2014 Cadillac CTS-V Sport Wagon", "2018 McLaren 720S", "2010 Ferrari 458 Italia", "2007 Dodge Viper SRT10 ACR", "2018 Dodge Challenger SRT Demon", "1970 AMC Rebel The Machine", "1965 Nissan Silvia 1600 Coupe", "1987 Nissan Skyline GTSR R31", "2017 Ferrari 488GTB", "2003 Ferrari 575M Maranello", "1968 Ferrari Dino", "2008 Ferrari California", "2017 Toyota Century", "2007 Lamborghini Gallardo SL" , "2010 Lamborgini Gallardo LP570-4 SL ", "2017 Lamborghini Huracan Performante", "2001 Lamborghini Murcielago", "2006 Lamborghini Murcielago LP640", "2016 Lamborghini Aventador S", "1996 Lamborghini Diablo SV", "1985 Lamborghini Countach LP5000s QV", "2017 Porsche 911 GT2 RS",  "1979 Isuzu 117 Coupe", "2018 Mercedes-Maybach S560", "2019 Chevy Corvette C7 ZR1", "1960 Chevy Corvette C1", "1963 Chevy Corvette C2 Stingray 427", "1988 Chevy Corvette C4 ZR1", "2007 Chevy Corvette C6 ZR1", "2014 Alfa Romeo Giulietta 1.8 TBi Quadrifoglio Verde", "1992 Alfa Romeo 155 Q4" ]
raritylevel_9 = ["2017 Ferrari F12", "1998 Subaru Impreza 22B STi", "1970 Dodge Dart Hemi Super Stock", "2011 Aston Martin One-77", "1973 Nissan Skyline H/T 2000GT-R", "2005 Pagani Zonda F", "1970 Ferrari 365 GTB/4 Daytona", "1999 Pagani Zonda C12S", "2009 Lexus LFA", "2013 Pagani Huayra", "2002 Nissan Skyline GTR V-Spec II Nur", "1997 Toyota Celica GT-Four", "2013 Lamborghini Gallardo LP570-4 SC", "2009 Lamborghini Murcielago LP670-4 SV", "2015 Lamborghini Aventador SV", "2018 Morgan Three-Wheeler", "2018 Nissan GT-R NISMO", "1988 Isuzu Impulse", "2006 Alfa Romeo 8c Competizione" ]
raritylevel_10 = ["1965 Ferrari 250 GTO", "1995 Lamborghini Diablo SE30 Jota", "2000 Lamborghini Diablo GTR", "2010 Audi R8 GT", "2016 Ferrari LaFerrari", "2020 Lamborghini Sian", "2015 Lamborghini Veneno", "1959 BMW 507", "1959 Cadillac Eldorado Brougham", "2015 Koenigsegg Regera", "2019 Aston Martin Valkyrie", "1992 McLaren F1", "1997 McLaren F1 GT", "1995 McLaren F1 LM", "2013 McLaren P1", "1987 Porsche 959", "2010 Koenigsegg Agera", "2007 Koenigsegg CCX", "2003 Nissan Skyline GT-R R34 Z-Tune", "2018 Mclaren Senna", "1969 Dodge Charger Daytona Hemi", "2018 Pagani Huayra BC", "2010 Pagani Zonda Cinque", "1995 Nissan GT-R Skyline R33 LM", "1998 Nissan R390 GT1", "2005 Bugatti Veyron 16.4", "2018 Nissan GT-R50 by Italdesign", "2016 Bugatti Chiron", "1953 Chevy Corvette", "1971 Lamborghini Miura P400SV", "1969 Toyota 2000GT", "1998 Toyota GT-one TS020", "Renault R35 Tank"]
raritylevel_11 = ["2019 Fortnite ATK GT-4R", "1009 Thanos Car", "LIGHNING MCQUEEN", "2018 Fortnite Shopping Cart GT-S"]


First_Names=[
"Keigo",
"Noriko",
"Taeko",
"Jack",
"Kenta",
"Ayako",
"Chiyo",
"Kanato",
"Hikaru",
"Hideki",
"Hayate",
"Itsuki",
"John",
"Ian",
"Jennifer",
"Philip",
"Randy",
"Midori",
"Takumi",
"Sakura",
"Takashi",
"Shiro",
"Naomi",
"Heisuke",
"Hideshi",
"Hiroshige",
"Fumio",
"Shigeo",
"Natsumi",
"Jessica",
"Johnathan",
"Louis",
"Stanley",
"Ed",
"Edward",
"Eddy",
"Jenny",
"Matt",
"Shigeru",
"Makoto",
"Natsu",
"Nami",
"Natsuo",
"Takao",
"Takako",
"Tarou",
"Alexei",
"Olga",
"Sergei",
"Valentin",
"Paul",
"Nick",
"Nicholas",
"Vladmir",
"Dmitry",
"Dan",
"Daniel",
"Peter",
"Ivan",
"Konstantin",
"Angelo",
"Angela",
"Michelle",
"Mike",
"Micheal"
]

Last_Names=[
"Miyamoto",
"Nakayama",
"Yamanaka",
"Ikeda",
"Shimizu",
"Honda",
"Toyoda",
"Matsumoto",
"Atkins",
"McMillan",
"Brown",
"Prasad",
"Roberts",
"West",
"Neuman",
"Rice",
"Green",
"Wood",
"Suzuki",
"Yamashita",
"Yamamoto",
"Yamada",
"Arai",
"Sasaki",
"Ishikawa",
"Fujita",
"Inoue",
"Ito",
"Kimura",
"Tanaka",
"Watanabe",
"Yamaguchi",
"Sukinov",
"Pavlov",
"Petrov",
"Ivanov",
"Skorobogatov",
"Jackson"
]

Degenerate_Names = ["Alex Cheng", "Sonny Lan", "Billie Jones Jean John", "Hunter Rogers", "George Miller", "Willy Ben Chen", "Shakira Beyonce", "Murica", "Raeleigh Smith", "Jihad", "Cliddus Danger", "Colon Mason", "Jakob Yote", "Jeffery Epstein", "William He", "Hilary Lui", "Ian Atkins", "Matvey Kirkun"]
Simp_Names = ["Derry Yu", "Maximus Agustus Rojas", "Pablo Escobar", "Barack Obama", "Emperor Hirohito", "Juan De Jesus Fernando Cortez", "Aiden Kelly", "Adam Klein", "Calven Harvey", "Malcom X", "Kanye West", "Travis Scott", "Tyler Plebins", "Jared Kane", "Mary Juana", "Linus Sebastian", "Sebastian Lam", "Angelo Macayan", "Vince Chen"]
Unstable_Names = ["Kyle Sein", "Cristal Meth", "Yennefer of Vengerberg", "Adolf Hitler"]

house_price = {
"Small Apartment": 0,
"Regular Apartment": 25000,
"Small Condo": 30000,
"Trailer": 20000,
"Tiny Mobile Home": 40000,
"Regular Condo": 70000,
"Nice Apartment": 80000,
"Small Cottage": 100000,
"Nice Condo": 105000,
"Regular Duplex": 110000,
"Nice Townhouse": 120000,
"Bungalow": 200000,
"Quaint Cottage": 250000,
"Log Cabin": 300000,
"Ranch Style Home": 350000,
"Medium Sized House": 400000,
"Houseboat": 420000,
"Fancy Apartment": 370000,
"Fancy Condo": 400000,
"Beach House": 420000,
"McMansion": 550000,
"Chalet": 500000,
"Barndominium": 520000,
"Large House": 600000,
"Fancy Penthouse Apartment": 650000,
"Newport Cottage": 750000,
"Ranch": 900000,
"Historic Mansion": 1000000,
"Contemporary Mansion": 1000000,
"Medium Size Military Bunker": 1000000,
"Large Cave": 1100000,
"Fancy Yacht": 1200000,
"Fancy Megayacht": 3000000,
"Large Military Bunker": 3000000,
"Historic Castle": 8000000,
"Historic Megamansion": 7000000,
"Contemporary Megamansion": 7000000,
"Historic Palace": 9000000,
"Historic Chateau": 9000000,
"Historic Villa": 9000000,
"Historic Manor": 9000000,
"Aircraft Carrier": 9000000,
"Privatized Military Base": 11000000,
"Megalith": 15000000
}

house_slot = {
"Small Apartment": 1,
"Regular Apartment": 2,
"Small Condo": 2,
"Trailer": 2,
"Tiny Mobile Home": 2,
"Regular Condo": 3,
"Nice Apartment": 3,
"Small Cottage": 3,
"Nice Condo": 3,
"Regular Duplex": 4,
"Nice Townhouse": 4,
"Bungalow": 5,
"Quaint Cottage": 5,
"Log Cabin": 5,
"Ranch Style Home": 5,
"Medium Sized House": 6,
"Houseboat": 6,
"Fancy Apartment": 6,
"Fancy Condo": 6,
"Beach House": 6,
"McMansion": 7,
"Chalet": 7,
"Barndominium": 7,
"Large House": 8,
"Fancy Penthouse Apartment": 8,
"Newport Cottage": 9,
"Ranch": 10,
"Historic Mansion": 12,
"Contemporary Mansion": 12,
"Medium Size Military Bunker": 12,
"Large Cave": 12,
"Fancy Yacht": 12,
"Fancy Megayacht": 15,
"Large Military Bunker": 15,
"Historic Castle": 25,
"Historic Megamansion": 20,
"Contemporary Megamansion": 20,
"Historic Palace": 35,
"Historic Chateau": 35,
"Historic Villa": 35,
"Historic Manor": 35,
"Aircraft Carrier": 35,
"Privatized Military Base": 40,
"Megalith": 50
}

house_protection = {
"Small Apartment": 2,
"Regular Apartment": 3,
"Small Condo": 2,
"Trailer": 1,
"Tiny Mobile Home": 2,
"Regular Condo": 3,
"Nice Apartment": 4,
"Small Cottage": 4,
"Nice Condo": 4,
"Regular Duplex": 4,
"Nice Townhouse": 5,
"Bungalow": 4,
"Quaint Cottage": 4,
"Log Cabin": 4,
"Ranch Style Home": 6,
"Medium Sized House": 6,
"Houseboat": 7,
"Fancy Apartment": 6,
"Fancy Condo": 6,
"Beach House": 6,
"McMansion": 6,
"Chalet": 7,
"Barndominium": 6,
"Large House": 7,
"Fancy Penthouse Apartment": 9,
"Newport Cottage": 7,
"Ranch": 10,
"Historic Mansion": 12,
"Contemporary Mansion": 13,
"Medium Size Military Bunker": 15,
"Large Cave": 15,
"Fancy Yacht": 15,
"Fancy Megayacht": 17,
"Large Military Bunker": 17,
"Historic Castle": 19,
"Historic Megamansion": 18,
"Contemporary Megamansion": 19,
"Historic Palace": 18,
"Historic Chateau": 18,
"Historic Villa": 18,
"Historic Manor": 18,
"Aircraft Carrier": 20,
"Privatized Military Base": 20,
"Megalith": 20
}

Straight_Words = [
"accelerator",
"gas pedal",
"vroom vroom",
"upshift",
"shift up",
"wheelspin",
"forward",
"speedometer",
"redline",
"straight",
"acceleration",
"clutch pedal",
"forward g",
"pedal to the medal",
"gearshift",
"overdrive",
"transmission",
"backfire"
]

Shallow_Corner_Words = [
"steering",
"accelerator",
"slight left",
"slight right",
"grip",
"brake pedal",
"gas pedal",
"clutch pedal",
"downshift",
"upshift",
"redline",
"sideways g",
"coasting",
"slide",
"oversteer",
"understeer",
"tires"
]

Tight_Corner_Words = [
"steering",
"handbrake",
"brake pedal",
"wheelspin",
"downshift",
"grip",
"drifting",
"reverse-steer",
"heel-toe",
"clutch pedal",
"throttle blip",
"gas pedal",
"power-over",
"torque-steer",
"oversteer",
"understeer",
"tires"
]

Calming_Sentences = [
"There there.",
"It's okay, you'll be fine.",
"Don't cry...",
"Here, have a candy."
]

Fun_Sentences = [
"Woah there!",
"Can I see that too?",
"Do you want to play a game?",
"How about we play for a little bit?"
]

Punishing_Sentences = [
"Don't do that.",
"That's a bad thing to do, you know.",
"Bad!",
"How about you stop doing that?"
]

Sneaking_Sentences = [
"I need to sneak behind that wall.",
"I've gotta hide!",
"Soft steps, soft steps.",
"I need to climb that wall.",
"I need to go through that window.",
"Gotta get behind that wall quick!",
"I need to hide behind that bush!",
"Hide in plain sight.",
"Don't make any noise, me."
]

Lockpick_Sentences = [
"The pin tumbler lock makes up about 90% of locks used today and is what you will find on about every deadbolt, door lock, and padlock. They are extremely simple in their design and essentially 6,000-year-old technology.",
"The basic concepts and techniques of lock picking can be learned and applied easily within minutes. Imagine for a moment that you have two pieces of paper, one sitting on top of the other.",
"There are a ton of different types of locks roaming the world today—from the tubular locks that you find on vending machines to combination locks securing safes. But of all these different types of locks, only one is king, the pin tumbler lock!",
"After I picked my first lock within two minutes of learning how to do it, I realized that locks don’t really do much except provide the illusion of security. Locks make us feel safe, but if someone really wanted to get in your house, they could easily pick the lock on your front door.",
"Almost any lock that you encounter in the real world is going to be a basic pin tumbler lock. Whether it is a deadbolt, door knob, or padlock, the most common type of lock uses this type of mechanical setup."
"I like to say that lock picking works a little like a key in slow motion, and with the sequence of events jumbled up. For example, you start with adding a bit of turning pressure to the plug. This puts tension on the pin stacks, which you will feel released as the lock is picked."
]

Hiding_Sentences = [
"Can't advance right now.",
"I need to quiet my breathing.",
"I hope they don't see me.",
"Can't have them see me.",
"I must erase my presence."
]

Panic_Sentences = [
"Oh shit! I need to hide!",
"I've gotta dip!",
"You didn't see me!"
]

Escape_Sentences = [
"Adios.",
"I'm out.",
"Goodbye."
]

job_wage = {
"Unemployed": 0,
"Musician": 750,
"Cashier": 500,
"Scientist": 10000,
"Software Engineer": 2000,
"Mechanic": 1000,
"Waiter/Waitress": 1000,
"Chef": 3000,
"Drug Dealer": 0,
"Thief": 0,
"Babysitter": 200,
"Boober Driver": 500
}

Music_Notes = [
"5|--d---------------d-------|\n4|dd--a--G-g-f-dfgcc--a--G-g|",
"4|---------d---------------f|/n3|b-b-ba-b---b-Fa-b-b-ba-b--|/n3|---------d---------------f|/n|b-b-ba-b---b-Fa-b-b-ba-b--|",
"5|d-D-d-D-d-D-c-d-c-d-c-d---|/n4|------------------------A-|",
"5|----c-D-f-F-f-D-c------dc-|/n4|----------------------A---|/n2|c-------------------------|",
"4|e-D-e-D-e---d-c-----------|/n3|----------b-----a-----c-e-|/n2|------------------e-a-----|/n1|----------------a---------|",
"5|-C-eD-CD-Cc-Ce-G---------C|/n4|G-----------------Ga-Gg-G-|/n4|C-------C-e-C-------C-e-C-|/n3|--G-e-G-------G-C-G-------|",
"5|--e-d-dd----ddddddc-d-ddd-|/n4|-a---------a-------a------|",
"4|--e-F-g-e---------e-F-g-e-|/n3|b---------------b---------|/n3|--------e---e---e---e---e-|/n3|--------g---g---g---g---g-|/n2|------e-------e-------e---|/n1|----------b-------b-------|",
"4|--------------------e-----|/n4|----F-----G---------C-----|/n4|----C-----D---------a-----|/n3|--C-F-C-e-F-e-C---C-F-C-e-|/n3|----a-----b---------------|/n2|b---------------b---------|",
"5|--GFGFe-C--Ce-GFC-e---e-C-|/n4|----------b---------------|",
"6|---------------------c----|/n5|-------------------------b|/n4|-----------------b--------|/n3|--b-bb----b-bb------------|/n3|-----e-------e------------|/n3|deg-gg--deg-gg--Fg--gF--Fe|",
"5|------C-------------------|/n4|F---a-----a---F-d-d-d-----|",
"5|f-----f-GA-A---G--------f-|",
"4|-----e-----------c--------|/n3|c-b---e--b--e--g--b--g--c-|",
"5|--------------------C---d-|/n4|----------------b---------|/n3|------------e-------------|/n2|------------e-------------|"
]

Music_Sentences = [
"Megalovania - Undertale, Toby Fox",
"Il Vento d'oro - Jojo's Bizarre Adventure Part 5, Yugo Kanno",
"Merry Go Round of Life - Howl's Moving Castle, Joe Hisaishi",
"Among Us Drip - Amogus",
"Fur Elise - Beethoven",
"Fantasie-Impromptu - Chopin",
"New Rules - Dua Lipa",
"Bella Ciao - La Casa De Papel, Anti-Fascist Protestors",
"Billie Jean - Michael Jackson",
"DNA - BTS",
"Doctor Who Theme - Murray Gold",
"Mii Channel Theme - Kazumi Totaka",
"Fortnite Default Dance - Fortnite",
"Aria Math - Minecraft, C418",
"Halo Theme - Halo: Combat Evolved, Martin O'Donnell, Michael Salvatori"
]


skilllist = ["Acceleration Skill", "Handling Skill", "Car Tuning Skill", "Computer Skill", "Service Skill", "Research Skill"]
classlist = ["X", "R", "S", "A", "B", "C", "D", "F"]
jobkey = ["Unemployed", "Musician", "Cashier", "Scientist", "Software Engineer", "Mechanic", "Waiter/Waitress", "Chef", "Drug Dealer", "Thief", "Babysitter", "Boober Driver"]
users = []
usersTemp = []
garages = []
mods = []
conditions = []
carNumbers = []
carTotal = {}
money = []
skill_points = []
levels = []
xps = []
storylevels = []
meetagains = []
skills = []
prestiges = []
prestigepoints = []
purity = []
houses = []
jobs = []
Idealercars = []
Idealernum = []
Adealercars = []
Adealernum = []
Odealercars = []
Odealernum = []
Sdealercars = []
Sdealernum = []
Housemarket = []
UsersInCommand = []
UsersInWork = []
WorkCooldown = []
saveNum = 0 

    
async def levelup(ctx, xpamount):
    global xps
    global levels
    global skill_points
    xps[users.index(ctx.author)] += xpamount
    xps[users.index(ctx.author)] = math.floor(xps[users.index(ctx.author)])
    await ctx.send(ctx.author.mention + " +" + str(xpamount) + " XP")
    if xps[users.index(ctx.author)] >= 1000*(1.09 ** (levels[users.index(ctx.author)])):
       xps[users.index(ctx.author)] = xps[users.index(ctx.author)] - (1000*(1.09**(levels[users.index(ctx.author)])))
       xps[users.index(ctx.author)] = math.floor(xps[users.index(ctx.author)])
       levels[users.index(ctx.author)] += 1
       skill_points[users.index(ctx.author)] += 1
       await ctx.send(ctx.author.mention + " LEVEL UP! You are now level " + str(levels[users.index(ctx.author)]) + ".\nSkillpoints: " + str(skill_points[users.index(ctx.author)]) + "\nLevel Progress: " + levelprogress(ctx.author))
    else:
        await ctx.send("Level Progress: " + levelprogress(ctx.author))
async def levelupuser(ctx, user, xpamount):
    global xps
    global levels
    global skill_points
    xps[users.index(user)] += xpamount
    xps[users.index(user)] = math.floor(xps[users.index(user)])
    await ctx.send(user.mention + " +" + str(xpamount) + " XP")
    if xps[users.index(user)] >= 1000*(1.09**(levels[users.index(user)])):
       xps[users.index(user)] = xps[users.index(user)] - (1000*(1.09**(levels[users.index(user)])))
       xps[users.index(user)] = math.floor(xps[users.index(user)])
       levels[users.index(user)] += 1
       skill_points[users.index(user)] += 1
       await ctx.send(user.mention + " LEVEL UP! You are now level " + str(levels[users.index(user)]) + ".\nSkillpoints: " + str(skill_points[users.index(user)]) + "\nLevel Progress: " + levelprogress(user))
    else:
        await ctx.send("Level Progress: " + levelprogress(user))
def levelprogress(user):
    return(str(xps[users.index(user)]) + "/" + str(math.floor(1000*(1.09**(levels[users.index(user)])))) + "XP")
def emojitonum(emoji):
    if str(emoji) == "1️⃣":
        num = 0
    elif str(emoji) == "2️⃣":
        num = 1
    elif str(emoji) == "3️⃣":
        num = 2
    elif str(emoji) == "4️⃣":
        num = 3
    elif str(emoji) == "5️⃣":
        num = 4
    elif str(emoji) == "6️⃣":
        num = 5
    elif str(emoji) == "7️⃣":
        num = 6
    elif str(emoji) == "8️⃣":
        num = 7
    elif str(emoji) == "9️⃣":
        num = 8
    elif str(emoji) == "🔟":
        num = 9
    else:
        num = None
    return num
def housestostr():
    finalstr = ""
    num = 0
    while(num < 10):
        finalstr += str(num+1) + ". " + str(Housemarket[num]) + ": Garage Slots: " + str(house_slot[Housemarket[num]]) + "\nSecurity Level: " + str(house_protection[Housemarket[num]]) +  "/20 \nPrice: $" + str(house_price[Housemarket[num]]) + "\n"
        num += 1
    return finalstr
def driveNumToStr(num):
    if num == 0:
        return "FWD"
    if num == 1:
        return "RWD"
    if num == 2:
        return "AWD"

def natNumToStr(num):
    if num == 0:
        return "Asia"
    if num == 1:
        return "North America"
    if num == 2:
        return "Europe"
def CalcDealerPR(carChoice):
    streetPRnum=10*(Car_Handling[carChoice])+(Car_HP[carChoice])/50
    offroadPRnum=Car_Offroad[carChoice]*(5*(Car_Handling[carChoice])+(Car_HP[carChoice])/50)
    if streetPRnum>26:
        streetPRgrade="X"
    elif streetPRnum>24 and streetPRnum <=26:
        streetPRgrade="R"
    elif streetPRnum<=24 and streetPRnum>=20:
        streetPRgrade="S"
    elif streetPRnum<20 and streetPRnum>=17:
        streetPRgrade="A"
    elif streetPRnum<17 and streetPRnum>=15:
        streetPRgrade="B"
    elif streetPRnum<15 and streetPRnum>=13:
        streetPRgrade="C"
    elif streetPRnum<13 and streetPRnum>=11:
        streetPRgrade="D"
    elif streetPRnum<11:
        streetPRgrade="F"
    return streetPRgrade
def DealerCarCard(car, numLeft):
    embed = discord.Embed(title = car, description = Car_Description[car], colour = discordRarityColor(car))
    embed.set_footer(text = "Rarity: " + rarityToString(car) + " " + RarityColor(car) + " " + str(numLeft) + " left in dealership")
    embed.set_image(url = Car_Exterior_Images[car])
    embed.add_field(name = "Power", value = str(Car_HP[car]) + " HP", inline = True)
    embed.add_field(name = "Handling Score", value = str(Car_Handling[car]), inline = True)
    embed.add_field(name = "Offroad", value = str(Car_Offroad[car]) + "/10", inline = True)
    embed.add_field(name = "Drivetrain", value = driveNumToStr(Car_Drive[car]), inline = True)
    embed.add_field(name = "Car Upgradability", value = "Max Stage: " + str(Car_Upgradable[car]), inline = True)
    embed.add_field(name = "Performance Grade", value = CalcDealerPR(car), inline = True)
    embed.add_field(name = "Cool Factor", value = str(Car_Cool[car]) + "/10", inline = True)
    embed.add_field(name = "Comfort", value = str(Car_Comfort[car]) + "/10", inline = True)
    embed.add_field(name = "Seats", value = str(Car_Seats[car]) + " Seats", inline = True)
    embed.add_field(name = "Price: $", value = "$" + str(Car_Price[car]), inline = True)
    embed.add_field(name = "Market", value = natNumToStr(Nat_Cat[car]), inline = True)
    return embed
def GarageCarCard(ctx, index):
    car = garages[users.index(ctx.author)][index]
    embed = discord.Embed(title = ctx.author.name + "'s " + car, description = Car_Description[car], colour = discordRarityColor(car))
    embed.set_footer(text = "Rarity: " + rarityToString(car) + " " + RarityColor(car) + ", #" + str(carNumbers[users.index(ctx.author)][index]) + "/" + str(carTotal[car]))
    url = Car_Exterior_Images[car]
    embed.set_image(url = url)
    print(url)
    embed.add_field(name = "Power", value = str(round(CalcHP(ctx, garages[users.index(ctx.author)], index), 2)) + " HP", inline = True)
    embed.add_field(name = "Handling Score", value = str(round(CalcHandling(ctx, garages[users.index(ctx.author)], index), 3)), inline = True)
    embed.add_field(name = "Offroad", value = str(CalcOffroad(ctx, garages[users.index(ctx.author)], index)) + "/10", inline = True)
    embed.add_field(name = "Drivetrain", value = driveNumToStr(Car_Drive[car]), inline = True)
    embed.add_field(name = "Mods", value = mods[users.index(ctx.author)][index] + "/" + str(Car_Upgradable[car]), inline = True)
    embed.add_field(name = "Performance Grade", value = CalcPR(ctx, garages[users.index(ctx.author)], index), inline = True)
    embed.add_field(name = "Cool Factor", value = str(CalcCool(ctx, garages[users.index(ctx.author)], index)) + "/10", inline = True)
    embed.add_field(name = "Comfort", value = str(CalcComfort(ctx, garages[users.index(ctx.author)], index)) + "/10", inline = True)
    embed.add_field(name = "Seats", value = str(CalcSeats(ctx, garages[users.index(ctx.author)], index)) + " Seats", inline = True)
    embed.add_field(name = "Price: $", value = "$" + str(round(CalcPrice(ctx, garages[users.index(ctx.author)], index))), inline = True)
    embed.add_field(name = "Market", value = natNumToStr(Nat_Cat[car]), inline = True)
    embed.add_field(name = "Car Condition", value = str(conditions[users.index(ctx.author)][index]) + "/10", inline = True)
    return embed
def EnemyCarCard(name, car, upg):
    embed = discord.Embed(title = name + "'s " + car, description = Car_Description[car], colour = discordRarityColor(car))
    embed.set_footer(text = "Rarity: " + rarityToString(car) + " " + RarityColor(car))
    embed.set_image(url = Car_Exterior_Images[car])
    embed.add_field(name = "Power", value = str(round(CalcHPFromData(car, upg), 2)) + " HP", inline = True)
    embed.add_field(name = "Handling Score", value = str(round(CalcHandlingFromData(car, upg), 3)), inline = True)
    embed.add_field(name = "Offroad", value = str(CalcOffroadFromData(car, upg)) + "/10", inline = True)
    embed.add_field(name = "Drivetrain", value = driveNumToStr(Car_Drive[car]), inline = True)
    embed.add_field(name = "Mods", value = upg + "/" + str(Car_Upgradable[car]), inline = True)
    embed.add_field(name = "Performance Grade", value = CalcPRFromData(car, upg), inline = True)
    embed.add_field(name = "Cool Factor", value = str(CalcCoolFromData(car, upg)) + "/10", inline = True)
    embed.add_field(name = "Comfort", value = str(CalcComfortFromData(car, upg)) + "/10", inline = True)
    embed.add_field(name = "Seats", value = str(CalcSeatsFromData(car, upg)) + " Seats", inline = True)
    embed.add_field(name = "Price: $", value = "$" + str(round(CalcPriceFromData(car, upg))), inline = True)
    embed.add_field(name = "Market", value = natNumToStr(Nat_Cat[car]), inline = True)
    embed.add_field(name = "Car Condition", value = str(10) + "/10", inline = True)
    return embed

def UserCarCard(user, car, upg):
    embed = discord.Embed(title = user.name + "'s " + car, description = Car_Description[car], colour = discordRarityColor(car))
    embed.set_footer(text = "Rarity: " + rarityToString(car) + " " + RarityColor(car))
    embed.set_image(url = Car_Exterior_Images[car])
    embed.add_field(name = "Power", value = str(round(CalcHPFromData(car, upg), 2)) + " HP", inline = True)
    embed.add_field(name = "Handling Score", value = str(round(CalcHandlingFromData(car, upg), 3)), inline = True)
    embed.add_field(name = "Offroad", value = str(CalcOffroadFromData(car, upg)) + "/10", inline = True)
    embed.add_field(name = "Drivetrain", value = driveNumToStr(Car_Drive[car]), inline = True)
    embed.add_field(name = "Mods", value = upg + "/" + str(Car_Upgradable[car]), inline = True)
    embed.add_field(name = "Performance Grade", value = CalcPRFromData(car, upg), inline = True)
    embed.add_field(name = "Cool Factor", value = str(CalcCoolFromData(car, upg)) + "/10", inline = True)
    embed.add_field(name = "Comfort", value = str(CalcComfortFromData(car, upg)) + "/10", inline = True)
    embed.add_field(name = "Seats", value = str(CalcSeatsFromData(car, upg)) + " Seats", inline = True)
    embed.add_field(name = "Price: $", value = "$" + str(round(CalcPriceFromData(car, upg))), inline = True)
    embed.add_field(name = "Market", value = natNumToStr(Nat_Cat[car]), inline = True)
    embed.add_field(name = "Car Condition", value = str(10) + "/10", inline = True)
    return embed

def pveRaceCard(ctx, playerpoint, opponentpoint, energy, zone, car, mod, PR, carcond, cornertype, turn, max):
    embed = discord.Embed(title = "Race Stats for " + ctx.author.name + ": ", description = "Driving a " + mod + " " + car, color = discordRarityColor(car))
    cornertypeplaintext = ""
    postext = ""
    plussign = ""
    if cornertype==0:
            cornertypeplaintext="Straight"
    elif cornertype==1:
            cornertypeplaintext="Shallow Corner"
    elif cornertype==2:
            cornertypeplaintext="Tight Corner"
    if playerpoint>opponentpoint:
            postext="1st"
    elif playerpoint<opponentpoint:
            postext="2nd"
    elif playerpoint==opponentpoint:
            postext="Tied"
    if postext=="1st":
        plussign="+"
    embed.add_field(name = "Position", value = postext, inline = True)
    embed.add_field(name = "Point Difference", value = plussign + str(round(playerpoint - opponentpoint , 3)), inline = True)
    embed.add_field(name = "Upcoming Road Type", value = cornertypeplaintext, inline = True)
    embed.add_field(name = "Energy", value = str(energy) + "/100", inline = True)
    embed.add_field(name = "Focus", value = str(zone) + "/10", inline = True)
    embed.add_field(name = "Car Condition", value = str(carcond) + "/10", inline = True)
    embed.set_footer(text = "Class " + PR + ": Area " + str(turn) + "/" + str(max))
    return embed

def pvpRaceCard(user, enemy, playerpoint, opponentpoint, energy, zone, car, mod, PR, carcond, cornertype, turn, max):
    embed = discord.Embed(title = "Race Stats for " + user.name + ": ", description = "Driving a " + mod + " " + car + " against " + enemy.name, color = discordRarityColor(car))
    cornertypeplaintext = ""
    postext = ""
    plussign = ""
    if cornertype==0:
            cornertypeplaintext="Straight"
    elif cornertype==1:
            cornertypeplaintext="Shallow Corner"
    elif cornertype==2:
            cornertypeplaintext="Tight Corner"
    if playerpoint>opponentpoint:
            postext="1st"
    elif playerpoint<opponentpoint:
            postext="2nd"
    elif playerpoint==opponentpoint:
            postext="Tied"
    if postext=="1st":
        plussign="+"
    embed.add_field(name = "Position", value = postext, inline = True)
    embed.add_field(name = "Point Difference", value = plussign + str(round(playerpoint - opponentpoint , 3)), inline = True)
    embed.add_field(name = "Upcoming Road Type", value = cornertypeplaintext, inline = True)
    embed.add_field(name = "Energy", value = str(energy) + "/100", inline = True)
    embed.add_field(name = "Focus", value = str(zone) + "/10", inline = True)
    embed.add_field(name = "Car Condition", value = str(carcond) + "/10", inline = True)
    embed.set_footer(text = "Class " + PR + ": Area " + str(turn) + "/" + str(max))
    return embed

def CalcHP(ctx, list, index):
    stockpwr=Car_HP[list[index]]
    car_index = index
    hpbonus = 0
    upgradeval = mods[users.index(ctx.author)][car_index]
    if "Stage 1" in upgradeval:
        hpbonus = 100
    elif "Stage 2" in upgradeval:
        hpbonus = 150
    elif "Stage 3" in upgradeval:
        hpbonus = 200
    elif "Stage 4" in upgradeval:
        hpbonus = 250
    elif "Stage 5" in upgradeval:
        hpbonus = 275
    elif "Stock" in upgradeval:
        hpbonus = 0
    
    condition = conditions[users.index(ctx.author)][car_index]
    return (stockpwr*Upgrade_path_hp[upgradeval] + hpbonus) - (10 - condition)*(stockpwr * 0.02)
def CalcHPFromData(car, upgrade):
    stockpwr=Car_HP[car]
    upgradeval = upgrade
    if "Stage 1" in upgradeval:
        hpbonus = 100
    elif "Stage 2" in upgradeval:
        hpbonus = 150
    elif "Stage 3" in upgradeval:
        hpbonus = 200
    elif "Stage 4" in upgradeval:
        hpbonus = 250
    elif "Stage 5" in upgradeval:
        hpbonus = 275
    elif "Stock" in upgradeval:
        hpbonus = 0
    return stockpwr*Upgrade_path_hp[upgradeval] + hpbonus
def CalcHandling(ctx, list, index):
    stockhandling=Car_Handling[list[index]]
    car_index = index
    upgradeval = mods[users.index(ctx.author)][car_index]
    condition = conditions[users.index(ctx.author)][car_index]
    return (stockhandling+Upgrade_path_handling[upgradeval]) - (10 - condition)*(stockhandling * 0.02)
def CalcHandlingFromData(car, upgrade):
    stockhandling=Car_Handling[car]
    upgradeval = upgrade
    return (stockhandling+Upgrade_path_handling[upgradeval])
def CalcPrice(ctx, list, index):
    stockprice=Car_Price[list[index]]
    car_index = index
    upgradeval = mods[users.index(ctx.author)][car_index]
    condition = conditions[users.index(ctx.author)][car_index]
    return stockprice+(stockprice*Upgrade_path_price[upgradeval] - (10 - condition)*(stockprice * 0.02))
def CalcPriceFromData(car, upgrade):
    stockprice=Car_Price[car]
    upgradeval = upgrade
    return stockprice+(stockprice*Upgrade_path_price[upgradeval])
def CalcCool(ctx, list, index):
    stockcool=Car_Cool[list[index]]
    car_index = index
    upgradeval = mods[users.index(ctx.author)][car_index]
    prereturn=stockcool+Upgrade_path_cool[upgradeval]
    if prereturn > 10:
        return 10
    elif prereturn < 1:
        return 1
    else:
        return prereturn
def CalcCoolFromData(car, upgrade):
    stockcool=Car_Cool[car]
    upgradeval = upgrade
    prereturn=stockcool+Upgrade_path_cool[upgradeval]
    if prereturn > 10:
        return 10
    elif prereturn < 1:
        return 1
    else:
        return prereturn
def CalcOffroad(ctx, list, index):
    stockoffroad=Car_Offroad[list[index]]
    car_index = index
    upgradeval = mods[users.index(ctx.author)][car_index]
    prereturn=stockoffroad+Upgrade_path_offroad[upgradeval]
    if prereturn > 10:
        return 10
    elif prereturn < 1:
        return 1
    else:
        return prereturn

def CalcOffroadFromData(car, upgrade):
    stockoffroad=Car_Offroad[car]
    upgradeval = upgrade
    prereturn=stockoffroad+Upgrade_path_offroad[upgradeval]
    if prereturn > 10:
        return 10
    elif prereturn < 1:
        return 1
    else:
        return prereturn
def CalcComfort(ctx, list, index):
    stockcomfort=Car_Comfort[list[index]]
    car_index = index
    upgradeval = mods[users.index(ctx.author)][car_index]
    prereturn=stockcomfort+Upgrade_path_comfort[upgradeval]
    if prereturn > 10:
        return 10
    elif prereturn < 1:
        return 1
    else:
        return prereturn
def CalcComfortFromData(car, upgrade):
    stockcomfort=Car_Comfort[car]
    upgradeval = upgrade
    prereturn=stockcomfort+Upgrade_path_comfort[upgradeval]
    if prereturn > 10:
        return 10
    elif prereturn < 1:
        return 1
    else:
        return prereturn
def CalcSeats(ctx, list, index):
    stockseats=Car_Seats[list[index]]
    car_index = index
    upgradeval = mods[users.index(ctx.author)][car_index]
    prereturn=stockseats+Upgrade_path_seats[upgradeval]
    if prereturn < 2:
        return 2
    else:
        return prereturn
def CalcSeatsFromData(car, upgrade):
    stockseats=Car_Seats[car]
    upgradeval = upgrade
    prereturn=stockseats+Upgrade_path_seats[upgradeval]
    if prereturn < 2:
        return 2
    else:
        return prereturn
def CalcPRFromData(car, upgrade):
    stockpwr = Car_HP[car]
    stockhandling=Car_Handling[car]
    stockoffroad=Car_Offroad[car]
    upgradeval = upgrade
    modhandling = CalcHandlingFromData(car, upgrade)
    modpwr = CalcHPFromData(car, upgrade)
    prereturn=stockoffroad+Upgrade_path_offroad[upgradeval]
    if prereturn > 10:
        modoffroad= 10
    elif prereturn < 1:
        modoffroad= 1
    else:
        modoffroad= prereturn
    streetPRnum=10*(modhandling)+(modpwr)/50
    offroadPRnum=modoffroad*(5*(modhandling)+(modpwr)/50)
    if streetPRnum>26 and streetPRnum < 100:
        streetPRgrade="X"
    elif streetPRnum>24 and streetPRnum <=26:
        streetPRgrade="R"
    elif streetPRnum<=24 and streetPRnum>=20:
        streetPRgrade="S"
    elif streetPRnum<20 and streetPRnum>=17:
        streetPRgrade="A"
    elif streetPRnum<17 and streetPRnum>=15:
        streetPRgrade="B"
    elif streetPRnum<15 and streetPRnum>=13:
        streetPRgrade="C"
    elif streetPRnum<13 and streetPRnum>=11:
        streetPRgrade="D"
    elif streetPRnum<11:
        streetPRgrade="F"
    else:
        streetPRgrade="PP"
    return streetPRgrade

def carTotalAdd(car):
    if car not in carTotal:
        carTotal[car] = 1
    else:
        carTotal[car] += 1

def CalcPR(ctx, list, index):
    modhandling=CalcHandling(ctx, list, index)
    modpwr=CalcHP(ctx, list, index)
    streetPRnum=10*(modhandling)+(modpwr)/50
    if streetPRnum>26:
        streetPRgrade="X"
    elif streetPRnum>24 and streetPRnum <=26:
        streetPRgrade="R"
    elif streetPRnum<=24 and streetPRnum>=20:
        streetPRgrade="S"
    elif streetPRnum<20 and streetPRnum>=17:
        streetPRgrade="A"
    elif streetPRnum<17 and streetPRnum>=15:
        streetPRgrade="B"
    elif streetPRnum<15 and streetPRnum>=13:
        streetPRgrade="C"
    elif streetPRnum<13 and streetPRnum>=11:
        streetPRgrade="D"
    elif streetPRnum<11:
        streetPRgrade="F"
    return streetPRgrade    

async def typingGame(ctx, zone, speed, cornertype, num):
    def check(m):
        return ctx.author == m.author and m.channel == ctx.channel
    wordlist = []
    basetime = 0
    if cornertype == 0:
        wordList = Straight_Words
    elif cornertype == 1:
        wordList = Shallow_Corner_Words
    elif cornertype == 2:
        wordlist = Tight_Corner_Words
    if speed == 2:
        basetime = 7
    if speed == 3:
        basetime = 5
    timelimit = basetime + (zone - 5)
    word = random.choice(wordlist)
    typeMsg = await ctx.send(ctx.author.mention + " Type the word '" + word + "' in chat! You get " + timelimit + " seconds!")
    try:
        msg = await client.wait_for('message', timeout = timelimit, check = check)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention + " Too late! You mess up, damaging your car slightly. \n-1 Car Condition")
        conditions[users.index(ctx.author)][num] -= 1
        return 0.8
    else:
        if msg != word:
            await ctx.send(ctx.author.mention + " You mess up, damaging your car slightly. \n-1 Car Condition")
            conditions[users.index(ctx.author)][num] -= 1
            return 0.8

        else:
            await ctx.send(ctx.author.mention + ", nice job.")
            if speed == 2:
                return 1
            if speed == 3:
                return 1.2
def convert(seconds): 
    return time.strftime("%H:%M:%S", time.gmtime(seconds)) 
def carDealerPrint(carlist, numlist):
     finalstring = ""
     num = 1
     for i in carlist:
        if num < 10:
            finalstring = finalstring + str(num) + ".  " + RarityColor(i) + " " + i + "  $" + str(Car_Price[i]) +  " **" + str(numlist[num-1]) + " left**" + " (Grade: **" + str(CalcPRFromData(i, "Stock")) + "**)\n"
        else:
            finalstring = finalstring + str(num) + ". " + RarityColor(i) + " " + i + "  $" + str(Car_Price[i]) + " **" + str(numlist[num-1]) + " left**" + " (Grade: **" + str(CalcPRFromData(i, "Stock")) + "**)\n"
        num += 1
     return finalstring
def carGaragePrint(ctx, carlist):
     finalstring = ""
     if carlist == None:
         return "You don't have any cars!"
     x = 0
     while(x < len(carlist)):
        if x < 10:
            finalstring = finalstring + str(x+1) + ".  " + RarityColor(carlist[x]) + " " + carlist[x] + ":\nPerformance Grade: " + str(CalcPR(ctx, carlist, x)) + "\n"
        else:
            finalstring = finalstring + str(x+1) + ". " + RarityColor(carlist[x]) + " " + carlist[x] + ":\nPerformance Grade: " + str(CalcPR(ctx, carlist, x)) + "\n"
        x += 1
     return finalstring

def carGaragePrintEnemy(user, carlist):
     finalstring = ""
     if carlist == None:
         return "You don't have any cars!"
     x = 0
     while(x < len(carlist)):
        if x < 10:
            finalstring = finalstring + str(x+1) + ".  " + RarityColor(carlist[x]) + " " + carlist[x] + ":\nPerformance Grade: " + str(CalcPRFromData(carlist[x], mods[users.index(user)][x])) + "\n"
        else:
            finalstring = finalstring + str(x+1) + ". " + RarityColor(carlist[x]) + " " + carlist[x] + ":\nPerformance Grade: " + str(CalcPRFromData(carlist[x], mods[users.index(user)][x])) + "\n"
        x += 1            
     return finalstring
def carRarityPrint(carlist):
    finalstring = ""
    for i in carlist:
        finalstring = finalstring + RarityColor(i) + " " + i + "\n"
    return finalstring
def rarityToString(car):
    if car in raritylevel_1 or car in raritylevel_2:
             return "Common"    
    elif car in raritylevel_3 or car in raritylevel_4:
             return "Uncommon"
    elif car in raritylevel_5 or car in raritylevel_6:
             return "Rare"
    elif car in raritylevel_7 or car in raritylevel_8:
             return "Legendary"
    elif car in raritylevel_9 or car in raritylevel_10:
             return "Exotic"
    else:
             return "Mythical"
def discordRarityColor(car):
     if car in raritylevel_1 or car in raritylevel_2:
             return discord.Colour.lighter_grey()    
     elif car in raritylevel_3 or car in raritylevel_4:
             return discord.Colour.green()
     elif car in raritylevel_5 or car in raritylevel_6:
             return discord.Colour.blue()
     elif car in raritylevel_7 or car in raritylevel_8:
             return discord.Colour.purple()
     elif car in raritylevel_9 or car in raritylevel_10:
             return discord.Colour.gold()
     else:
             return discord.Colour.red()
def refreshOtto():
    Odealercar=0
    Orar10=0
    Orar9=0
    Orar8=0
    Orar7=0
    Orar6=0
    Orar5=0
    Oraru=0
    Orarc=0
    Odealercars.clear()
    Odealernum.clear()
    while(Odealercar<10):
        tfc = False
        rngcar=random.randint(1,451)
        if rngcar==1:
            while tfc == False:
                cartoadd=random.choice(list(raritylevel_10))
                if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(1)
                                                    Odealercar=Odealercar+1
                                                    Orar10=Orar10+1
        if rngcar>1 and rngcar<=11:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_9))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(1, 3))
                                                    Odealercar=Odealercar+1
                                                    Orar9=Orar9+1
        if rngcar>11 and rngcar<=21:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_8))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(5, 20))
                                                    Odealercar=Odealercar+1
                                                    Orar8=Orar8+1
        if rngcar>21 and rngcar<=41:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_7))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(20, 100))
                                                    Odealercar=Odealercar+1
                                                    Orar7=Orar7+1
        if rngcar>41 and rngcar<=71:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_6))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True
                                                    Odealernum.append(random.randint(100, 200))
                                                    Odealercars.append(cartoadd)
                                                    Odealercar=Odealercar+1
                                                    Orar6=Orar6+1
        if rngcar>71 and rngcar<=131:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_5))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(200, 300))
                                                    Odealercar=Odealercar+1
                                                    Orar5=Orar5+1
        if rngcar>131 and rngcar<=211:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_4))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(300, 350))
                                                    Odealercar=Odealercar+1
                                                    Oraru=Oraru+1
        if rngcar>211 and rngcar<=281:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_3))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(350, 500))
                                                    Odealercar=Odealercar+1
                                                    Oraru=Oraru+1
        if rngcar>281 and rngcar<=361:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_2))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(500, 700))
                                                    Odealercar=Odealercar+1
                                                    Orarc=Orarc+1
        if rngcar>361 and rngcar<=451:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_1))
                                            if Nat_Cat[cartoadd] == 2:
                                                    tfc = True                                                              
                                                    Odealercars.append(cartoadd)
                                                    Odealernum.append(random.randint(500, 1000))
                                                    Odealercar=Odealercar+1
                                                    Orarc=Orarc+1
def refreshSally():
    Sdealercar=0
    Srar10=0
    Srar9=0
    Srar8=0
    Srar7=0
    Srar6=0
    Srar5=0
    Sraru=0
    Srarc=0
    Sdealercars.clear()
    Sdealernum.clear()
    while(Sdealercar<10):
        tfc = False
        rngcar=random.randint(1,451)
        if rngcar==1:
            while tfc == False:
                cartoadd=random.choice(list(raritylevel_10))
                if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(1)
                                                    Sdealercar=Sdealercar+1
                                                    Srar10=Srar10+1
        if rngcar>1 and rngcar<=11:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_9))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(1, 3))
                                                    Sdealercar=Sdealercar+1
                                                    Srar9=Srar9+1
        if rngcar>11 and rngcar<=21:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_8))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(5, 20))
                                                    Sdealercar=Sdealercar+1
                                                    Srar8=Srar8+1
        if rngcar>21 and rngcar<=41:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_7))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(20, 100))
                                                    Sdealercar=Sdealercar+1
                                                    Srar7=Srar7+1
        if rngcar>41 and rngcar<=71:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_6))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(100, 200))
                                                    Sdealercar=Sdealercar+1
                                                    Srar6=Srar6+1
        if rngcar>71 and rngcar<=131:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_5))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(200, 300))
                                                    Sdealercar=Sdealercar+1
                                                    Srar5=Srar5+1
        if rngcar>131 and rngcar<=211:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_4))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(300, 350))
                                                    Sdealercar=Sdealercar+1
                                                    Sraru=Sraru+1
        if rngcar>211 and rngcar<=281:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_3))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(350, 500))
                                                    Sdealercar=Sdealercar+1
                                                    Sraru=Sraru+1
        if rngcar>281 and rngcar<=361:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_2))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(500, 700))
                                                    Sdealercar=Sdealercar+1
                                                    Srarc=Srarc+1
        if rngcar>361 and rngcar<=451:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_1))
                                            if Nat_Cat[cartoadd] == 1:
                                                    tfc = True                                                              
                                                    Sdealercars.append(cartoadd)
                                                    Sdealernum.append(random.randint(500, 1000))
                                                    Sdealercar=Sdealercar+1
                                                    Srarc=Srarc+1
def refreshIshibashi():
    Idealercar=0
    Irar10=0
    Irar9=0
    Irar8=0
    Irar7=0
    Irar6=0
    Irar5=0
    Iraru=0
    Irarc=0
    Idealercars.clear()
    Idealernum.clear()
    while(Idealercar < 10):
        rngcar=random.randint(1,451)
        if rngcar==1:
                cartoadd=random.choice(list(raritylevel_10))
                Idealercars.append(cartoadd)
                Idealernum.append(1)
                Idealercar=Idealercar+1
                Irar10=Irar10+1
        if rngcar>1 and rngcar<=11:
                cartoadd=random.choice(list(raritylevel_9))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(1, 3))
                Idealercar=Idealercar+1
                Irar9=Irar9+1
        if rngcar>11 and rngcar<=21:
                cartoadd=random.choice(list(raritylevel_8))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(5, 20))
                Idealercar=Idealercar+1
                Irar8=Irar8+1
        if rngcar>21 and rngcar<=41:
                cartoadd=random.choice(list(raritylevel_7))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(20, 100))
                Idealercar=Idealercar+1
                Irar7=Irar7+1
        if rngcar>41 and rngcar<=71:
                cartoadd=random.choice(list(raritylevel_6))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(100, 200))
                Idealercar=Idealercar+1
                Irar6=Irar6+1
        if rngcar>71 and rngcar<=131:
                cartoadd=random.choice(list(raritylevel_5))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(200, 300))
                Idealercar=Idealercar+1
                Irar5=Irar5+1
        if rngcar>131 and rngcar<=211:
                cartoadd=random.choice(list(raritylevel_4))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(300, 350))
                Idealercar=Idealercar+1
                Iraru=Iraru+1
        if rngcar>211 and rngcar<=281:
                cartoadd=random.choice(list(raritylevel_3))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(350, 500))
                Idealercar=Idealercar+1
                Iraru=Iraru+1
        if rngcar>281 and rngcar<=361:
                cartoadd=random.choice(list(raritylevel_2))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(500, 700))
                Idealercar=Idealercar+1
                Irarc=Irarc+1
        if rngcar>361 and rngcar<=451:
                cartoadd=random.choice(list(raritylevel_1))
                Idealercars.append(cartoadd)
                Idealernum.append(random.randint(500, 1000))
                Idealercar=Idealercar+1
                Irarc=Irarc+1
def refreshAkechi():
    Adealercar=0
    Arar10=0
    Arar9=0
    Arar8=0
    Arar7=0
    Arar6=0
    Arar5=0
    Araru=0
    Ararc=0
    Adealercars.clear()
    Adealernum.clear()
    while(Adealercar < 10):
        tfc = False
        rngcar=random.randint(1,451)
        if rngcar==1:
            while tfc == False:
                cartoadd=random.choice(list(raritylevel_10))
                if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(1)
                                                    Adealercar=Adealercar+1
                                                    Arar10=Arar10+1
        if rngcar>1 and rngcar<=11:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_9))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(1, 3))
                                                    Adealercar=Adealercar+1
                                                    Arar9=Arar9+1
        if rngcar>11 and rngcar<=21:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_8))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(5, 20))
                                                    Adealercar=Adealercar+1
                                                    Arar8=Arar8+1
        if rngcar>21 and rngcar<=41:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_7))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(20, 100))
                                                    Adealercar=Adealercar+1
                                                    Arar7=Arar7+1
        if rngcar>41 and rngcar<=71:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_6))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(100, 200))
                                                    Adealercar=Adealercar+1
                                                    Arar6=Arar6+1
        if rngcar>71 and rngcar<=131:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_5))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(200, 300))
                                                    Adealercar=Adealercar+1
                                                    Arar5=Arar5+1
        if rngcar>131 and rngcar<=211:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_4))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(300, 350))
                                                    Adealercar=Adealercar+1
                                                    Araru=Araru+1
        if rngcar>211 and rngcar<=281:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_3))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(350, 500))
                                                    Adealercar=Adealercar+1
                                                    Araru=Araru+1
        if rngcar>281 and rngcar<=361:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_2))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(500, 700))
                                                    Adealercar=Adealercar+1
                                                    Ararc=Ararc+1
        if rngcar>361 and rngcar<=451:
            while tfc == False:
                                            cartoadd=random.choice(list(raritylevel_1))
                                            if Nat_Cat[cartoadd] == 0:
                                                    tfc = True                                                              
                                                    Adealercars.append(cartoadd)
                                                    Adealernum.append(random.randint(500, 1000))
                                                    Adealercar=Adealercar+1
                                                    Ararc=Ararc+1
def RarityColor(car):
        if car in raritylevel_1 or car in raritylevel_2:
                return "🔲"    
        elif car in raritylevel_3 or car in raritylevel_4:
                return "🟩"
        elif car in raritylevel_5 or car in raritylevel_6:
                return "🟦"
        elif car in raritylevel_7 or car in raritylevel_8:
                return "🟪"
        elif car in raritylevel_9 or car in raritylevel_10:
                return "🟨"
        else:
                return "🟥"
def Return10(list, page):
    returnlist = []
    x = 10*(page-1)
    max = len(list)
    if max <= 10*(page-1):
        return None
    while(x < max and x < 10*(page)):
        returnlist.append(list[x])
        x += 1
    return returnlist

@tasks.loop(minutes = 30)
async def refreshDealers():
    refreshIshibashi()
    refreshAkechi()
    refreshOtto()
    refreshSally()

def refreshHouse():
    x = 0
    Housemarket.clear()
    while(x < 10):
        Housemarket.append(str(random.choice(list(house_price.keys()))))
        x += 1
@tasks.loop(hours = 1)
async def refreshRealEstate():
    refreshHouse()

@tasks.loop(seconds = 30)
async def saveLoop():
    global saveNum
    saveNum += 1
    print("Saving... Iteration " + str(saveNum))
    saveGame()

def fillTemp():
    if users == []:
        return
    usersTemp.clear()
    for i in users:
        usersTemp.append(i.id)
async def fillUsers():
    users.clear()
    for i in usersTemp:
        users.append(await client.fetch_user(i))


def saveGame():
    fillTemp()
    with open("users.txt", "w") as outfile:
        json.dump(usersTemp, outfile)
    with open("garages.txt", "w") as outfile:
        json.dump(garages, outfile)
    with open("mods.txt", "w") as outfile:
        json.dump(mods, outfile)
    with open("conditions.txt", "w") as outfile:
        json.dump(conditions, outfile)
    with open("carNumbers.txt", "w") as outfile:
        json.dump(carNumbers, outfile)
    with open ("carTotal.txt", "w") as outfile:
        json.dump(carTotal, outfile)
    with open("money.txt", "w") as outfile:
        json.dump(money, outfile)
    with open("skill_points.txt", "w") as outfile:
        json.dump(skill_points, outfile)
    with open("levels.txt", "w") as outfile:
        json.dump(levels, outfile)
    with open("xps.txt", "w") as outfile:
        json.dump(xps, outfile)
    with open("storylevels.txt", "w") as outfile:
        json.dump(storylevels, outfile)
    with open("meetagains.txt", "w") as outfile:
        json.dump(meetagains, outfile)
    with open("skills.txt", "w") as outfile:
        json.dump(skills, outfile)
    with open("prestiges.txt", "w") as outfile:
        json.dump(prestiges, outfile)
    with open("prestigepoints.txt", "w") as outfile:
        json.dump(prestigepoints, outfile)
    with open("houses.txt", "w") as outfile:
        json.dump(houses, outfile)
    with open("jobs.txt", "w") as outfile:
        json.dump(jobs, outfile)
    with open("purity.txt", "w") as outfile:
        json.dump(purity, outfile)
async def loadSave():
    global garages
    global conditions
    global carNumbers
    global carTotal
    global users
    global usersTemp
    global mods
    global money
    global skill_points
    global levels
    global xps
    global storylevels
    global meetagains
    global skills
    global prestiges
    global prestigepoints
    global houses
    global jobs
    global purity
    with open("users.txt") as outfile:
        usersTemp = json.load(outfile)
    await fillUsers()   
    with open("garages.txt") as outfile:
        garages = json.load(outfile)
    with open("mods.txt") as outfile:
        mods = json.load(outfile)
    with open("conditions.txt") as outfile:
        conditions = json.load(outfile)
    with open("carNumbers.txt") as outfile:
        carNumbers = json.load(outfile)
    with open("carTotal.txt") as outfile:
        carTotal = json.load(outfile)
    with open("money.txt") as outfile:
        money = json.load(outfile)
    with open("skill_points.txt") as outfile:
        skill_points = json.load(outfile)
    with open("levels.txt") as outfile:
        levels = json.load(outfile)
    with open("xps.txt") as outfile:
        xps = json.load(outfile)
    with open("storylevels.txt") as outfile:
        storylevels = json.load(outfile)
    with open("meetagains.txt") as outfile:
        meetagains = json.load(outfile)
    with open("skills.txt") as outfile:
        skills = json.load(outfile)
    with open("prestiges.txt") as outfile:
        prestiges = json.load(outfile)
    with open("prestigepoints.txt") as outfile:
        prestigepoints = json.load(outfile)
    with open("houses.txt") as outfile:
        houses = json.load(outfile)
    with open("jobs.txt") as outfile:
        jobs = json.load(outfile)
    with open("purity.txt") as outfile:
        purity = json.load(outfile)
@client.event
async def on_ready():
    if os.path.exists("users.txt"):
        print("Loadsave working")
        if not (os.path.exists("prestiges.txt")):
            with open("users.txt") as outfile:
                users = json.load(outfile)
            list1 = [0,0,0,0,0,0]
            prestigelist = []
            prestigepointlist = []
            for i in users:
                prestigelist.append(list1)
                prestigepointlist.append(0)
            with open("prestiges.txt", "w") as outfile:
                json.dump(prestigelist, outfile)
            with open("prestigepoints.txt", "w") as outfile:
                json.dump(prestigepointlist, outfile)
        if not (os.path.exists("purity.txt")):
            with open("users.txt") as outfile:
                users = json.load(outfile)
            for i in users:
                purity.append(1)
            with open("purity.txt", "w") as outfile:
                json.dump(purity, outfile)
        if not (os.path.exists("jobs.txt")):
            with open("users.txt") as outfile:
                users = json.load(outfile)
            jobslistthing = []
            for i in users:
                jobslistthing.append("Unemployed")
            with open("jobs.txt", "w") as outfile:
                json.dump(jobslistthing, outfile)
        await loadSave()
        
    client.remove_command('help')
    refreshDealers.start()
    saveLoop.start()
    refreshRealEstate.start()
    refreshHouse()
    refreshIshibashi()
    refreshAkechi()
    refreshOtto()
    refreshSally()
    await client.change_presence(activity=discord.Game('Selling virtual vehicles- type "*commandlist" for list of commands.'))
    Dealersubject = None
    Dealermessage = None

async def allowedCommand(ctx):
    a = ctx.author not in UsersInCommand
    if a:
        UsersInCommand.append(ctx.author)
    else:
        await ctx.send(ctx.author.mention + " you already have a command active.")
    return a

async def is_owner(ctx):
    return ctx.author.id == 367684893385162752
    
@client.command()
@commands.check(is_owner)
async def nuke(ctx):
    def check1(reaction, user):
        return user == ctx.author
    await ctx.send("So it's come to this, huh...")
    yesnomsg = await ctx.send("Are you sure you want to press the button? Everything will be destroyed.")
    await yesnomsg.add_reaction('✅')
    await yesnomsg.add_reaction('❌')
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        return
    else:
        if str(reaction.emoji) == "✅":
            nukebutton = await ctx.send("Well, " + ctx.author.name + ", the button is right in front of you, what are you waiting for?")
            await nukebutton.add_reaction('☢️')
            await nukebutton.add_reaction('🙅‍♂️')
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                return
            else:
                if str(reaction.emoji) == "☢️":
                    await ctx.send("Oh god.")
                    if os.path.exists("users.txt"):
                        os.remove("users.txt")
                    if os.path.exists("garages.txt"):
                        os.remove("garages.txt")
                    if os.path.exists("garages.txt"):
                        os.remove("garages.txt")
                    if os.path.exists("mods.txt"):
                        os.remove("mods.txt")
                    if os.path.exists("conditions.txt"):
                        os.remove("conditions.txt")
                    if os.path.exists("carNumbers.txt"):
                        os.remove("carNumbers.txt")
                    if os.path.exists("carTotal.txt"):
                        os.remove("carTotal.txt")
                    if os.path.exists("money.txt"):
                        os.remove("money.txt")
                    if os.path.exists("skill_points.txt"):
                        os.remove("skill_points.txt")
                    if os.path.exists("levels.txt"):
                        os.remove("levels.txt")
                    if os.path.exists("xps.txt"):
                        os.remove("xps.txt")
                    if os.path.exists("storylevels.txt"):
                        os.remove("storylevels.txt")
                    if os.path.exists("meetagains.txt"):
                        os.remove("meetagains.txt")
                    if os.path.exists("skills.txt"):
                        os.remove("skills.txt")
                    if os.path.exists("houses.txt"):
                        os.remove("houses.txt")
                    if os.path.exists("prestiges.txt"):
                        os.remove("prestiges.txt")
                    if os.path.exists("prestigepoints.txt"):
                        os.remove("prestigepoints.txt")
                    if os.path.exists("jobs.txt"):
                        os.remove("jobs.txt")
                    if os.path.exists("purity.txt"):
                        os.remove("purity.txt")
                    await ctx.send("And everything has been reduced to nothing.")
                    await ctx.send("Goodbye.")
                    sys.exit()
                else:
                    await ctx.send("Thank God. I thought you were gonna go through with it for a sec there.")
        else:
            await ctx.send("Phew.")
@client.command()
@commands.check(allowedCommand)
async def gift(ctx):
    if ctx.author not in users:
        await setup(ctx, True)
    def check(m):
        return ctx.author == m.author and m.channel == ctx.channel
    def check1(reaction, user):
        return user == ctx.author
    await ctx.send("Mention the user that you want to gift something to below.")
    try:
        msg = await client.wait_for('message', timeout = 30, check = check)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        mentionlist = msg.mentions
    if len(mentionlist) != 1:
        if len(mentionlist) == 0:
            await ctx.send(ctx.author.mention+ " Please actually mention someone to gift to.")
        else:
            await ctx.send(ctx.author.mention+ " don't mention multiple users.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return    
    else:
        enemy = client.get_user(mentionlist[0].id)
        if enemy not in users:
            await ctx.send(ctx.author.mention+ " you have to pick somebody who's used the bot before.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        if enemy == ctx.author:
            await ctx.send(ctx.author.mention + ", you can't gift things to yourself, idiot.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
    yesnomsg = await ctx.send("What do you want to gift to " + enemy.mention + "?")
    await yesnomsg.add_reaction('🚗')
    await yesnomsg.add_reaction('💸')
    await yesnomsg.add_reaction('🔙')
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
         if str(reaction.emoji) == "🚗":
            await ctx.send(ctx.author.mention + " Which car will you gift?")
            page = 1
            num = 0
            while(True):
                embed = discord.Embed(title = ctx.author.name + "'s Garage", description = houses[users.index(ctx.author)] + ": Available garage slots " + str(house_slot[houses[users.index(ctx.author)]] - len(garages[users.index(ctx.author)])) + "/" + str(house_slot[houses[users.index(ctx.author)]]), colour = discord.Colour.blurple())
                templist = Return10(garages[users.index(ctx.author)], page)
                tempthing = carGaragePrint(ctx, templist)
                embed.add_field(name = "Garage", value = tempthing, inline = True)
                if math.ceil(len(garages[users.index(ctx.author)])) != 0:
                    embed.set_footer(text = "Page " + str(page) + " of " + str(math.ceil(len(garages[users.index(ctx.author)]) / 10)))
                garagemsg = await ctx.send(embed = embed)
                allowedResponses = []
                if templist == None:
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                if len(templist) > 0:
                    await garagemsg.add_reaction('1️⃣')
                    allowedResponses.append("1️⃣")
                if len(templist) > 1:
                    await garagemsg.add_reaction('2️⃣')
                    allowedResponses.append("2️⃣")
                if len(templist) > 2:
                    await garagemsg.add_reaction('3️⃣')
                    allowedResponses.append("3️⃣")
                if len(templist) > 3:
                    await garagemsg.add_reaction('4️⃣')
                    allowedResponses.append("4️⃣")
                if len(templist) > 4:
                    await garagemsg.add_reaction('5️⃣')
                    allowedResponses.append("5️⃣")
                if len(templist) > 5:
                    await garagemsg.add_reaction('6️⃣')
                    allowedResponses.append("6️⃣")
                if len(templist) > 6:
                    await garagemsg.add_reaction('7️⃣')
                    allowedResponses.append("7️⃣")
                if len(templist) > 7:
                    await garagemsg.add_reaction('8️⃣')
                    allowedResponses.append("8️⃣")
                if len(templist) > 8:
                    await garagemsg.add_reaction('9️⃣')
                    allowedResponses.append("9️⃣")
                if len(templist) > 9:
                    await garagemsg.add_reaction('🔟')
                    allowedResponses.append("🔟")
                if(10*page < len(garages[users.index(ctx.author)])):
                    await garagemsg.add_reaction('➡️')
                    allowedResponses.append("➡️")
                if(page != 1):
                    await garagemsg.add_reaction('⬅️')
                    allowedResponses.append("⬅️")
                await garagemsg.add_reaction('🔙')
                allowedResponses.append("🔙")
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                else:
                    if str(reaction.emoji) in allowedResponses:
                        if str(reaction) == "🔙":
                            await ctx.send("You decide not to gift a car.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        elif str(reaction) == "➡️":
                            page+=1
                        elif str(reaction) == "⬅️":
                            page-=1
                        else:
                            allowedResponses.clear()
                            num = emojitonum(str(reaction.emoji))
                            break
            car = garages[users.index(ctx.author)][num]
            mod = mods[users.index(ctx.author)][num]
            carnum = carNumbers[users.index(ctx.author)][num]
            cond = conditions[users.index(ctx.author)][num]
            garagecard = await ctx.send(embed = GarageCarCard(ctx, num))
            yesnomsg = await ctx.send("Are you sure you want to gift this car to " + enemy.mention + "?")
            await yesnomsg.add_reaction('✅')
            allowedResponses.append("✅")
            await yesnomsg.add_reaction('❌')
            allowedResponses.append("❌")
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            
            else:
                if str(reaction.emoji) not in allowedResponses:
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                elif str(reaction.emoji) == "✅":
                    if house_slot[houses[users.index(enemy)]] >= len(garages[users.index(enemy)]) + 1:
                        await ctx.send("Now gifting your " + car + " to " + enemy.mention + ".")
                        garages[users.index(ctx.author)].pop(num)
                        mods[users.index(ctx.author)].pop(num)
                        carNumbers[users.index(ctx.author)].pop(num)
                        conditions[users.index(ctx.author)].pop(num)
                        garages[users.index(enemy)].append(car)
                        mods[users.index(enemy)].append(mod)
                        carNumbers[users.index(enemy)].append(carnum)
                        conditions[users.index(enemy)].append(cond)
                        await ctx.send("Gift complete.")
                    else:
                        await ctx.send(enemy.mention + "does not have enough space in their garage for your gift.")
                else:
                    await ctx.send("You decide not to gift your car.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
    
         if str(reaction.emoji) == "💸":
            await ctx.send(ctx.author.mention + " How much money do you want to gift?")
            try:
                msg = await client.wait_for('message', timeout = 30, check = check)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            else:
                if not str(msg.content).isnumeric():
                    await ctx.send("That's not a number.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                winning = int(msg.content)
                if winning > money[users.index(ctx.author)]:
                    await ctx.send(ctx.author.mention + "You don't have that much money to gift. The gift has been canceled.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
            if winning <= 0:
                return
            else:
                money[users.index(ctx.author)] -= winning
                money[users.index(enemy)] += winning
                await ctx.send(ctx.author.mention + ", you have gifted $" + str(winning) + " to " + enemy.mention + ".")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return

    
@client.command()
@commands.check(is_owner)
async def shutdown(ctx):
    yesnomsg = await ctx.send("Bot shutting down... all progress will be saved.")
    saveGame()
    sys.exit()

@client.command()
@commands.check(allowedCommand)
async def joblist(ctx):
    if ctx.author not in users:
        await setup(ctx, True)
    def check1(reaction, user):
        return user == ctx.author
    if ctx.author in UsersInWork:
        if datetime.datetime.now() > WorkCooldown[UsersInWork.index(ctx.author)]:
            WorkCooldown.pop(users.index(ctx.author))
            UsersInWork.pop(users.index(ctx.author))
        else:
            timetoreset= str(convert(datetime.timedelta.total_seconds(WorkCooldown[UsersInWork.index(ctx.author)] - datetime.datetime.now())))
            await ctx.send("You may not sign up for a job for another " + timetoreset + ". Come back later.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
    embed = discord.Embed(title = "Jobs List", description = "Jobs are available!", colour = discord.Colour.blurple()) 
    embed.add_field(name = "0. Babysitter", value = "An extremely low tier job, has no stat requirement, and wage does not scale up with stats. Base Wage: $200", inline = True)
    embed.add_field(name = "1. Cashier", value = "A low tier job, requires low Service stat, but wage does not scale up with stats. Base Wage: $500", inline = True)
    embed.add_field(name = "2. Boober Driver", value = "A low to high tier job, No stat requirement, wage enhanced with Service stat and car. Base Wage: $500", inline = True)
    embed.add_field(name = "3. Musician", value = "A low to high tier job, requires moderately low Service stat. Scales up extremely well with stats. Heavy RNG. Base Wage: $750", inline = True)
    embed.add_field(name = "4. Waiter/Waitress", value = "A mid tier job, requires moderately low Service stat, scales up alright with stats. Small amount of RNG in the form of tips. Base Wage: $1000", inline = True)
    embed.add_field(name = "5. Mechanic", value = "A mid to high tier job, requires moderate Car Tuning stat and low service and research stat. Extremely heavy RNG. Base Wage: $1000", inline = True)
    embed.add_field(name = "6. Software Engineer", value = "A mid to high tier job, requires moderately high Computer and moderate Research stat, scales up alright with stats. Heavy RNG, chance for extremely high pay. Base Wage: $2000", inline = True)
    embed.add_field(name = "7. Chef", value = "A mid to high tier job, requires moderately high Research stat and moderate Service stat. Scales up extremely well with stats. Small amount of RNG. Base Wage: $3000", inline = True)
    embed.add_field(name = "8. Scientist", value = "A high tier job, requires high Computer and Research stat. Scales up alright with stats. Small amount of RNG, but small chance for extremely high pay. Base Wage: $10000", inline = True)
    embed.add_field(name = "9. Drug Dealer", value = "A criminal job, no stat requirements. High risk, high reward, the Drug Dealer job comes with the chance of getting heavily fined. Extremely Heavy RNG, no way of knowing what you'll get out of it. Base Wage: $0", inline = True)
    embed.add_field(name = "10. Thief", value = "A criminal job, no stat requirements. The Thief job will allow you to steal from other players. Invest enough money into your heists with enough Research Skill, and you can walk off with a good chunk of your opponent's money. Just make sure you don't get caught, because that'll be very, very bad. Base Wage: $0", inline = True)
    Dealermessage = await ctx.send(embed = embed)
    allowedresponses = []
    await Dealermessage.add_reaction('0️⃣')
    allowedresponses.append("0️⃣")
    await Dealermessage.add_reaction('1️⃣')
    allowedresponses.append("1️⃣")
    await Dealermessage.add_reaction('2️⃣')
    allowedresponses.append("2️⃣")
    await Dealermessage.add_reaction('3️⃣')
    allowedresponses.append("3️⃣")
    await Dealermessage.add_reaction('4️⃣')
    allowedresponses.append("4️⃣")
    await Dealermessage.add_reaction('5️⃣')
    allowedresponses.append("5️⃣")
    await Dealermessage.add_reaction('6️⃣')
    allowedresponses.append("6️⃣")
    await Dealermessage.add_reaction('7️⃣')
    allowedresponses.append("7️⃣")
    await Dealermessage.add_reaction('8️⃣')
    allowedresponses.append("8️⃣")
    await Dealermessage.add_reaction('9️⃣')
    allowedresponses.append("9️⃣")
    await Dealermessage.add_reaction('🔟')
    allowedresponses.append("🔟")
    await Dealermessage.add_reaction('🔙')
    allowedresponses.append("🔙")
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        if str(reaction.emoji) == "0️⃣":
            await ctx.send(ctx.author.mention + ", you are now a Babysitter.")
            jobs[users.index(ctx.author)] = "Babysitter"
        elif str(reaction.emoji) == "1️⃣":
            if skills[users.index(ctx.author)][4] >= 2:
                await ctx.send(ctx.author.mention + ", you are now a Cashier.")
                jobs[users.index(ctx.author)] = "Cashier"
            else:
                await ctx.send(ctx.author.mention + ", you have failed your interview and have been rejected from the position of Cashier. You require a Service Skill of at least 2.")
        elif str(reaction.emoji) == "2️⃣":
            await ctx.send(ctx.author.mention + ", you are now a Boober Driver.")
            jobs[users.index(ctx.author)] = "Boober Driver"
        elif str(reaction.emoji) == "3️⃣":
            if skills[users.index(ctx.author)][4] >= 4:
                await ctx.send(ctx.author.mention + ", you are now a Musician.")
                jobs[users.index(ctx.author)] = "Musician"
            else:
                await ctx.send(ctx.author.mention + ", you have failed your interview and have been rejected from the position of Musician. You require a Service Skill of at least 4.")
        elif str(reaction.emoji) == "4️⃣":
            if skills[users.index(ctx.author)][4] >= 3:
                await ctx.send(ctx.author.mention + ", you are now a Waiter/Waitress.")
                jobs[users.index(ctx.author)] = "Waiter/Waitress"
            else:
                await ctx.send(ctx.author.mention + ", you have failed your interview and have been rejected from the position of Waiter/Waitress. You require a Service Skill of at least 3.")
        elif str(reaction.emoji) == "5️⃣":
            if skills[users.index(ctx.author)][2] >= 5 and skills[users.index(ctx.author)][4] >= 3:
                await ctx.send(ctx.author.mention + ", you are now a Mechanic.")
                jobs[users.index(ctx.author)] = "Mechanic"
            else:
                await ctx.send(ctx.author.mention + ", you have failed your interview and have been rejected from the position of Mechanic. You require a Car Tuning Skill of at least 5, and a Service Skill of at least 3.")
        elif str(reaction.emoji) == "6️⃣":
            if skills[users.index(ctx.author)][3] >= 7 and skills[users.index(ctx.author)][5] >= 5:
                await ctx.send(ctx.author.mention + ", you are now a Software Engineer.")
                jobs[users.index(ctx.author)] = "Software Engineer"
            else:
                await ctx.send(ctx.author.mention + ", you have failed your interview and have been rejected from the position of Software Engineer. You require a Computer Skill of at least 7, and a Research Skill of at least 5.")
        elif str(reaction.emoji) == "7️⃣":
            if skills[users.index(ctx.author)][5] >= 7 and skills[users.index(ctx.author)][4] >= 5:
                await ctx.send(ctx.author.mention + ", you are now a Chef.")
                jobs[users.index(ctx.author)] = "Chef"
            else:
                await ctx.send(ctx.author.mention + ", you have failed your interview and have been rejected from the position of Chef. You require a Research Skill of at least 7, and a Service Skill of at least 5.")
        elif str(reaction.emoji) == "8️⃣":
            if skills[users.index(ctx.author)][5] >= 9 and skills[users.index(ctx.author)][3] >= 8:
                await ctx.send(ctx.author.mention + ", you are now an Scientist.")
                jobs[users.index(ctx.author)] = "Scientist"
            else:
                await ctx.send(ctx.author.mention + ", you have failed your interview and have been rejected from the position of Scientist. You require a Research Skill of at least 9, and a Computer Skill of at least 8.")
        elif str(reaction.emoji) == "9️⃣":
            await ctx.send(ctx.author.mention + ", you have abandoned good conscience and have now become a Drug Dealer.")
            jobs[users.index(ctx.author)] = "Drug Dealer"
        elif str(reaction.emoji) == "🔟":
            await ctx.send(ctx.author.mention + ", you have abandoned good conscience and have now become a Thief.")
            jobs[users.index(ctx.author)] = "Thief"
        else:
            await ctx.send("You decided not to sign up for a new job today.")
    UsersInCommand.pop(UsersInCommand.index(ctx.author))
@client.command()
@commands.check(allowedCommand)
async def work(ctx):
    if ctx.author not in users:
        await setup(ctx, True)
    def check(m):
        return ctx.author == m.author and m.channel == ctx.channel
    def check1(reaction, user):
        return user == ctx.author
    if jobs[users.index(ctx.author)] == "Babysitter":
        await ctx.send(ctx.author.mention + "You have started your babysitting job.")
        maxagitated = random.randint(7, 12)
        maxbored = random.randint(7, 12)
        maxtrouble = random.randint(7, 12)
        turns = random.randint(5,8)
        agitated = random.randint(0, 3)
        bored = random.randint(0, 3)
        trouble = random.randint(0, 3)
        name = random.choice(First_Names)
        energy = 100
        x = 0
        while(x < turns):
            numthing = 0
            embed = discord.Embed(title = "Little " + name + "'s current status", description = "Don't let any of these numbers get to their maximum value, " + ctx.author.name + ".", color = discord.Colour.magenta())
            embed.add_field(name = "Agitation", value = str(agitated) + "/" + str(maxagitated), inline = True)
            embed.add_field(name = "Boredom", value = str(bored) + "/" + str(maxbored), inline = True)
            embed.add_field(name = "Trouble", value = str(trouble) + "/" + str(maxtrouble), inline = True)
            embed.add_field(name = "Your Energy", value = str(energy) + "/100", inline = True)
            embed.add_field(name = "Remaining Time", value = str(turns - x) + " Turns", inline = True)
            embed.set_footer(text = "Babysitting isn't an easy job, is it now?")
            await ctx.send(embed = embed)
            randomaction = random.randint(0, 3)
            if randomaction == 0 or randomaction == 1:
                await ctx.send("+1 Boredom")
                bored += 1
                await ctx.send(ctx.author.mention + ", " + "Little " + name + " is doing nothing! He seems bored!")
            elif randomaction == 2:
                await ctx.send("+1 Agitation")
                agitated += 1
                await ctx.send(ctx.author.mention + ", " + "Little " + name + " has fallen over and hurt themselves!")
            elif randomaction == 3:
                await ctx.send("+1 Trouble")
                trouble += 1
                await ctx.send(ctx.author.mention + ", " + "Little " + name + " is causing trouble!")
            actionmsg = await ctx.send(ctx.author.mention + ", what will you do? 1. Calm the kid down (-25 Energy) 2. Get the kid to have fun (-25 Energy) 3. Yell at the kid (-25 Energy) 4. Do nothing (+30 Energy)")
            thing = 3
            sentence = None
            allowedResponses = []
            await actionmsg.add_reaction('1️⃣')
            allowedResponses.append("1️⃣")
            await actionmsg.add_reaction('2️⃣')
            allowedResponses.append("2️⃣")
            await actionmsg.add_reaction('3️⃣')
            allowedResponses.append("3️⃣")
            await actionmsg.add_reaction('4️⃣')
            allowedResponses.append("4️⃣")
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time. 'Do nothing' has been automatically selected.")
            else:
                if str(reaction.emoji) in allowedResponses:
                    numthing = emojitonum(str(reaction.emoji))
                else:
                    await ctx.send(ctx.author.mention + " I did not recognize that response. 'Do nothing' has been automatically selected.")
            if energy < 25 and numthing != 3:
                await ctx.send(ctx.author.mention + " You don't have enough Energy. 'Do nothing' has been automatically selected.")
                numthing = 3
            if numthing == 0:
                sentence = random.choice(Calming_Sentences)
                await ctx.send("-25 Energy")
                energy -= 25
            elif numthing == 1:
                sentence = random.choice(Fun_Sentences)
                await ctx.send("-25 Energy")
                energy -= 25
            elif numthing == 2:
                sentence = random.choice(Punishing_Sentences)
                await ctx.send("-25 Energy")
                energy -= 25
            elif numthing == 3:
                if energy > 70:
                    await ctx.send("+" + str(100 - energy) + " Energy")
                    energy = 100
                else:
                    await ctx.send("+30 Energy")
                    energy += 30
            success = False
            if numthing !=3:
                await ctx.send(ctx.author.mention + " Type '" + sentence + "' in chat! You get 10 seconds!")
                try:
                    msg = await client.wait_for('message', timeout = 10, check = check)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention + " Too late! You say nothing.")
                    numthing = 3
                    
                else:
                    if str(msg.content) != sentence:
                        await ctx.send(ctx.author.mention + " You fumble in your language, and Little " + name + " now just thinks you're weird!")
                    else:
                        await ctx.send(ctx.author.mention + " you say '" + sentence + "'.")
                        success = True
            if not success:
                failnum = random.randint(0,1)
                if randomaction == 0 or randomaction == 1:
                    if failnum == 0 and numthing != 3:
                        await ctx.send(ctx.author.mention + " In fact, Little " + name + " doesn't just think that you're weird, they think that you're kind of funny!")
                        bored -= 1
                        await ctx.send("Boredom -1")
                    else:
                        await ctx.send(ctx.author.mention + " The situation gets worse. Little " + name + " continues to be bored.")
                        bored += 1
                        await ctx.send("Boredom +1")
                elif randomaction == 2: 
                    if failnum == 0 and numthing != 3:
                        await ctx.send(ctx.author.mention + " In fact, Little " + name + " doesn't just think that you're weird, they think that you're making fun of them for falling over!")
                        agitated += 2
                        await ctx.send("Agitation +2")
                    else:
                        await ctx.send(ctx.author.mention + " The situation gets worse. Little " + name + " continues to become more agitated.")
                        agitated += 1
                        await ctx.send("Agitation +1")
                elif randomaction == 3:
                    if failnum == 0 and numthing != 3:
                        await ctx.send(ctx.author.mention + " Little " + name + " thinks that you're stupid, and causes even more trouble just to spite you!")
                        trouble += 2
                        await ctx.send("Trouble +2")
                    else:
                        await ctx.send(ctx.author.mention + " The situation gets worse. Little " + name + " continues to cause trouble.")
                        trouble += 1
                        await ctx.send("Trouble +1")
            if success:
                if randomaction == 0 or randomaction == 1:
                    if numthing == 0:
                        await ctx.send(ctx.author.mention + ", why are you trying to console the kid? He's just bored!")
                    elif numthing == 1:
                        await ctx.send(ctx.author.mention + ", that was the right call. You play a game with Little " + name + ".")
                        if bored <= 1:
                            await ctx.send("Boredom -" + str(bored))
                            bored = 0
                        else:
                            await ctx.send("Boredom -2")
                            bored -= 2
                        await ctx.send("Trouble +1")
                        trouble += 1
                    elif numthing == 2:
                        await ctx.send(ctx.author.mention + ", why are you yelling at the kid? He's just bored!")
                        agitated += 2
                        await ctx.send("Agitation +2")
                elif randomaction == 2: 
                    if numthing == 1:
                        await ctx.send(ctx.author.mention + ", the kid doesn't hear you!")
                        agitated += 1
                        await ctx.send("Agitation +1")
                    elif numthing == 0:
                        await ctx.send(ctx.author.mention + ", that was the right call. You comfort Little " + name + ".")
                        if agitated <= 1:
                            await ctx.send("Agitation -" + str(agitated))
                            agitated = 0
                        else:
                            await ctx.send("Agitation -2")
                            agitated -=2
                    elif numthing == 2:
                        await ctx.send(ctx.author.mention + ", why are you yelling at the kid? You're making everything worse!")
                        agitated += 3
                        await ctx.send("Agitation +3")
                elif randomaction == 3:
                    if numthing == 1:
                        await ctx.send(ctx.author.mention + " Little " + name + " thinks that you're stupid, and causes even more trouble just to spite you!")
                        trouble += 2
                        await ctx.send("Trouble +2")
                    elif numthing == 2:
                        await ctx.send(ctx.author.mention + ", that was the right call. You scold Little " + name + ".")
                        if trouble <= 1:
                            await ctx.send("Trouble -" + str(trouble))
                            trouble = 0
                        else:
                            await ctx.send("Trouble -2")
                            trouble -= 2
                        await ctx.send("Agitation +1")
                        agitated += 1
                    elif numthing == 0:
                        await ctx.send(ctx.author.mention + ", the kid can't hear you!")
            if agitated > maxagitated or trouble > maxtrouble or bored > maxbored:
                await ctx.send(ctx.author.mention + ", you have failed your job. You get half of your base wage, and are now unemployed. You cannot sign up for another job for 30 minutes.")
                money[users.index(ctx.author)] += job_wage["Babysitter"]/2
                jobs[users.index(ctx.author)] = "Unemployed"
                await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                UsersInWork.append(ctx.author)
                await levelup(ctx, 100)
                WorkCooldown.append(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            x += 1
        await ctx.send("You have completed your job, and have earned your salary of $" + str(job_wage["Babysitter"]) + "! Harder than you thought, huh.")
        money[users.index(ctx.author)] += job_wage["Babysitter"]
        await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
        await levelup(ctx, 500)
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Cashier":
        strikes = 0
        bonus = 0
        if ctx.author not in users:
            await setup(ctx, True)
        def check(m):
            return ctx.author == m.author and m.channel == ctx.channel
        def check1(reaction, user):
            return user == ctx.author
        if jobs[users.index(ctx.author)] == "Cashier":
            await ctx.send(ctx.author.mention + "You have started your cashier job.")
            turns = random.randint(3,8)
            x = 1
            while(x <= turns):
                failure = False
                await ctx.send("Customer " + str(x) + "/" + str(turns))
                await ctx.send(ctx.author.mention + " next customer...")
                chancebonus = 0
                eventtype = 0
                randomeventchance = random.randint(1, 5)
                if randomeventchance == 1:
                    randomeventchance2 = random.randint(1, 500)
                    if randomeventchance2 <= 100:
                        eventtype = 3
                        await ctx.send(ctx.author.mention + " RANDOM EVENT! A KAREN APPROACHES!")
                        await asyncio.sleep(2)
                        karenlist = ["This place has no cleaning products.", "This place smells like fish.", "One of the employees ASSAULTED me."]
                        randomint = random.randint(0, 2)
                        await ctx.send(ctx.author.mention + " Karen: Can I speak to your manager? " + karenlist[randomint])
                        if randomint == 0:
                            sentence = "Ma'am, this is a grocery store. We carry no cleaning products."
                            typetime = 15
                        elif randomint == 1:
                            sentence = "Unfortunately, there is not much we can do about the smell, as we sell fresh fish."
                            typetime = 17
                        elif randomint == 2:
                            sentence = "Okay, I'll get the manager right now."
                            typetime = 10
                        await ctx.send(ctx.author.mention + " Type '" + sentence + "' in chat! You get " + str(typetime) + " seconds!")
                        try:
                            msg = await client.wait_for('message', timeout = typetime, check = check)
                        except asyncio.TimeoutError:
                            await ctx.send(ctx.author.mention + " Too late! You say nothing. The Karen gets angry, thinking that you are ignoring her.")
                            await asyncio.sleep(1)
                            await ctx.send(ctx.author.mention + " Karen: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH YOU'RE IGNORING MEEEEEEEEEE!!!!!!!!")
                            await asyncio.sleep(1)
                            strikes += 1
                            await ctx.send(ctx.author.mention + " Strikes: **" + str(strikes) + "**")
                        else:
                            if str(msg.content) != sentence:
                                await ctx.send(ctx.author.mention + " You fumble in your language, and the Karen grows impatient and attacks another customer. You get blamed.")
                                await asyncio.sleep(1)
                                strikes += 1
                                await ctx.send(ctx.author.mention + " Strikes: **" + str(strikes) + "**")
                            else:
                                await ctx.send(ctx.author.mention + " you say '" + sentence + "', and successfully defuse the situation. Nice job.")
                                bonus += 100
                                await ctx.send(ctx.author.mention + " Total Bonus: **$" + str(bonus) + "**")
                    elif randomeventchance2 <= 200:
                        await ctx.send(ctx.author.mention + " RANDOM EVENT! A NOVEAU RICHE APPROACHES!")
                        chancebonus = random.randint(100, 1000)
                        eventtype = 1
                    elif randomeventchance2 <= 300:
                        await ctx.send(ctx.author.mention + " RANDOM EVENT! YOUR MANAGER APPROACHES!")
                        chancebonus = random.randint(0, 100)
                        eventtype = 2
                    elif randomeventchance2 < 500:
                        eventtype = 4
                        await ctx.send(ctx.author.mention + " RANDOM EVENT! A HOBO APPROACHES!")
                        await ctx.send(ctx.author.mention + " Type 'Sir, could you please leave?' in chat! You get 7 seconds!")
                        try:
                            msg = await client.wait_for('message', timeout = 10, check = check)
                        except asyncio.TimeoutError:
                            await ctx.send(ctx.author.mention + " Too late! You say nothing. The hobo throws up all over your register. You are blamed.")
                            strikes += 1
                            await ctx.send(ctx.author.mention + " Strikes: **" + str(strikes) + "**")
                        else:
                            if not (str(msg.content)==("Sir, could you please leave?")):
                                await ctx.send(ctx.author.mention + " You fumble in your language, causing the hobo to start running. He stumbles and pushes over a customer. You get blamed.")
                                await asyncio.sleep(1)
                                strikes += 1
                                await ctx.send(ctx.author.mention + " Strikes: **" + str(strikes) + "**")
                            else:
                                await ctx.send(ctx.author.mention + " you say 'Sir, could you please leave?', and the hobo actually leaves. Nice job.")
                                bonus += 50
                                await ctx.send(ctx.author.mention + " Total Bonus: **$" + str(bonus) + "**")
                    elif randomeventchance2 == 500:
                        await ctx.send(ctx.author.mention + " R̴͕̝͈̱̭̠͆Ȁ̸̡̨̭̝̉͘N̵̛̼̺̙̩̿̐͐︠́́͐̓͡D̶̡͕̖̺̱̼͔̜͔̟̓ͧ᷃̉ͮ̾͐͞O̴̬̱̦̝᷈M̸͔̹̮̺̰̹͖͎͆ͥ̆͛̽͟͢ Ȩ̴̱̦̰̬̣̾̽ͫ̀͑͞͠͠V̵̰̰͐Ẹ̷̢͕͖͎̻͇᷉᷆̓͟͝Ņ̵͆᷈ͩͨ͋̃̾͞Ț̸̛̣̫̤̟̯̬͎ͯ͆̉︠͋̆͘͟!̵̻͎̝͕̍︢᷉̽͐͋᷉̌ **ⰀⰁⰂⰃⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰠⰡⰢⰣⰫⰬⰭⰮ** Ă̷̲̣̺͚̫̖᷉͜P̴᷿̼̘͉ͬ᷄͋᷈ͪͭ︢͠P̸͖̲̫͓̬͂R̴̦͖̞͈̗̭̹̐̔ͬ͊᷅͟͜ Ò̸͈͇︡ͥ͛᷀̆̕Ą̴͚̬̙͇͉͛̈́̂͊̏̔̏͘͟͜C̵̻̘͓̳͒ͥ͐H̶̻̘̠̭̲᷂̮̙ͬ̅͛ͥ͟ Ḛ̵᷿̗ͫ᷅̚S̷̛̞̞͉̬̼̯̪̟̩︢᷄")
                        await asyncio.sleep(1)
                        yesnomsg = await ctx.send(ctx.author.mention + "**ⰀⰁⰂⰃⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰠⰡⰢⰣⰫⰬⰭⰮ:** D̶̢̢̡̛͓̞̰̻̖͈͍̖͕̣̖͇̼̠͎̭̗̳̋̎̾̓̎̏̂͒̀͒͠O̶̠͚̯͈͔̝̹̥̣̫̺̩̱̺̮̥̳̟͎̠̲̩̲̦͇̘̲͊͆̃̈́͆̃́̽̈́̄̎͂͌̎̿̄̌̽͋̓͛̀̈́́̎̇̚̕̚͜͝͠ͅ ̵̢̛̘͛̈́̓̆̌̅̈́͠ Y̸̡̧̧̼͇̲͍̹̭͖̬͙̯̗̮̺͚̰͈̲̺̳̗̩̤͕̲͉͆͑̈́̌̽̓̓̆̈́͜͝Ò̵͈̺̬̒̈̊͌͌̇͂̉̽̒͂̆̑̌͗̄͒̿̊̍̕͘͘̚͝͝͠ͅ U̷̢͓̫͎̜͈̯̖̹̥̣̯̭̯̞͕͎̬̜̙̱̱͓͈̠̮͚͉͍̥̐͌́̈́̑́̊̃̉̉̓̀ ̴̨̛̼̲͎̳̰̱͚̙̺̜͚̭̜͖͖̈́̋̍̈͌̏͛̃̽̃̍̎́̅͌̂̓̒̓͐̈̐̃̏̌̐͛͛̓̎̑͗́̇͘͠A̶͍̺̺̦̲͍̘̯͌̐̃͜͜C̵̡̢̧̧̢̧̻̫̳̙̳̝͎̬̖̰͕̘̖͉̮̗̤͓̝̰̥̣͉̦͈̰͉̖̈́̒̐͐̅̅̆̑̐͌̀̏̓̾̀̈́̎̾̒̋̅̈́̔̐̈́́̾̀̌̂̕̕̚͝͠͝͝C̸̢̢̢̡̩̙̖̠̬͍̘͖̗̦̹̭̯̟͇̼̱̤̣̟̲̩̘̪̣̣̭̟̔̃̃́̑̈́̈́͗̋̀̌̃͑̽̾̈́͂̏̈͛̆͋̎̚͘͜͝ͅ Ȩ̶̢̛̼̗͖̻͍̮̰̙̻̻͚̟̼͈̗̺̬̬̬͖̺̣̭̜͓̋̓́̌̀̿͛̓͋̒͌̀͊̈́̓͂͗̈́͊̅͋͂̚̚͠ͅͅP̵̼̪̤͔̑͌͜T̷̡̡̖̲̲̹̟̜̠̥͕͍̝͓̝̹̗̪̮͍͇̱̜̠͖͕͇̟͈͈̣̥͇̹͈̩̖͈̦͚̤̒͒͗̏͜ͅ ̸̛͎͉̬͛̒̆̉̓̅̒̆̈̀̓̐̃̐̐̉̏̽͛̅͂͛̆͝ͅḦ̵̡̧̨̡̧̜̻̝̟̞̣̟̜̩͖͓̦̠̫̪̺̱͔̞̮͉̮͈͖̹͖́̾̒͂̓͐͋ I̸̭͓̪͍̲̗̠͈̰̽͊̉̽́̓̎͛̍͆̃́́̿̑̋̐̚̕̕̕͜͝͝ͅM̶̡̛̼̩͕͍͔̖̦̘̬̬͕̻̻̓̽͒͊͆͋̈́̉̈́̆̓͑̎͑̇̐̈́̈̒̀̀̋̾̽̏̂̔̔́̀͑̎̀̎̄̿͘̕̕͠͝͝")
                        await yesnomsg.add_reaction('✅')
                        await yesnomsg.add_reaction('❌')
                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                        except asyncio.TimeoutError:
                            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        else:
                            if str(reaction.emoji) == "✅":
                                yesnomsg = await ctx.send(ctx.author.mention + "**ⰀⰁⰂⰃⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰠⰡⰢⰣⰫⰬⰭⰮ:** S̵̛͖͇̘͚͈̔͗͂̔͂͗̂̈́͋͒̏̀̊̐͐̆̋̆̐̀̉͋̒̕̚͝͠ ̵̝͒̍̄̇̒̿̂͝͝E̸̢̫͇͍͇̮̫̹̝̣̫̞̠͍̫͎͖̰̟͈͈̥̰͕̽̿̈́̔̔͌̏̄̐̒̓̉̚̕͜ͅ ̸̧̧̢̧̢̧̣̩̦͓̤̩͚̘͙͈̗̰͖͔͉̳̥̻̮̙̟̪̙̝̘͈̭̟̥̥͇̞̥̫̇̐͌̇͛̎̓̍̀̎͗̈́̅͛̅̿͒̐͊̈́̋͑̎̀̎͋̅́́́̌́̉͊̓̕͜L̷̨̡͙̲̣̹̲͖̥͔̹͙̦̫̜̼͖͉͕̣͖̖̰̈̈̍̋͌̔́̇͋͒́̌͜L̴̢̡̢̧̛͚̙͖͎̗͎̞͉̫̤͖̱̝͉͖̼͎͕̘̣̫̝͉͎̳̮̺͈͈̰͍̹̱̯̫̗̣̿̿͐̿̾̽̈́͛́̓̔̌̄ ̶̢͎͈̰̖̣̀͒͊̒̍̆̊̒͑̂̅̍̈́̔Ṭ̸̨̨̡̘̱̮̯̫̙̝̼̝͖̫͓͙̠̰̰͕͉̩͎̼͚͍̺̬͚̜̪̠̹̱͈͙̻̜͙̭̌̊͊̄̇͑̈́̈́̚ͅḨ̵̧̛̛͚̺͎̠̥̝̠̯̟̠̤̱̣͓͙̘͓̻̘͉̳̪̻̺̣͎͔͕͕̥̱̇͂͐̀͊̎̑̅̾̌̈͑̃̀͗̀̑̓͋̿̾̔̉̀̿́͊͒̇͂̄͂̆́̐̌̚͘͘͜ͅͅͅ ̴̨̧̨̧̯̻̝̺̟͎̖̣͙̪͚̭̠͉̖͍̬͚̗̤̫̤̦̫̦̦͈̝̫̬̯̖̱̖̪̜̝̆͊͑̐̾̈́̏̋̔̆͜ͅY̵̧̨̡̛̤̩̫̠͙͍̟̘̝͈̝͚̟̻͈̪̟̦̬̙̪̩̤͎͔̤͙͗̃̎̀̂̋̽͆̅̂̄́̌̓̒̅͌̂̏̃̉͘͜͜͝͝͝͝͝ͅͅͅ ̴̧̡̧̥̝̹̰̙̜͖̤̥̼͍͍̟̜͓̬̬͇̯͇̜͔͓̣͓̝͚͔̭̞̰̞̻͖̲̙͉̫͖̃͒̆̃Ș̸̢̧̡̧̨̣̦͇͈͎̞͙̘̤̖̱͔̹̙̪͍̺̱̠̟̥͍̳̥͇͈̘̜͙͎̱̟̌̈́̀̾͗̐͒͑̔͛́̒͂̉̔̓̍̈́͊̕͜͜͝ͅỎ̶̡̡̨̡̡̫͎̼͔͔̻̠̣͉̝̘̝͈̻͖̮̹̝͖̝̬̯́͂̀̊̾̾̉̎̑̈̓̑͒͘͘͝Ų̷̡̡̢̡̢̯̭̺͕̰̟̫̜̱͎̖̻̹̟̫̙͉̖͔̯͙͍̖̣̥͈̺͊̾̑̈́̄̃ ̸̨̡̧̢̨̢̻͔͙̜̣̗̩̥̯͖̦̦̗͎̗͓̩͓̳͉̫͔͍̳̔̈́̏̈́͐͒̉̈́͜Ļ̶̢̢͍͚̺̼̮̖̹͙̭̱͇̼̞̫̺͚́̒̚͝.̵̫̖͓͍̀͛̀͐͆")
                                await yesnomsg.add_reaction('✅')
                                await yesnomsg.add_reaction('❌')
                                try:
                                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                                except asyncio.TimeoutError:
                                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                    return
                                if str(reaction.emoji) == "✅":
                                    await ctx.send(ctx.author.mention + "**ⰀⰁⰂⰃⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰠⰡⰢⰣⰫⰬⰭⰮ:** Ŗ̵̹̰̟̺̠̲̼̝̲̦̳͖̘̜͍͈͔͚͍̤̺̻̜̮̤͎́͋̈͜͜ͅͅĘ̵̛̗̘̫̮̩̻̤͈̫͌̅̋̑̄͐̍͗̃̅̀̄͗̀̽̅̉̚̚̚͝͠ ̷̡̢̦̝͎͉̮͕͙̼̲̠̩͖͈̗̖͚̙̻͙͍̖̪̞̼̹̫̗̗͚͙̪̮͙̜̩̌̀̌́̕Ḁ̸̧̢͉̦̺͉̘̗̭̀͗̽͒̚͠P̴̨̧̡̨̧̪͙̲̼̰͖͓̭̫̫̞̖͖̭̟̳̝͚͈͖͕̬̮̻͉̠͔͍̙̦͇͎͉̝͖͊͑̆̈́̔̎̈́̿̓́̈́͜͜͝͠ͅ ̶̧̡̡̛̛̛̞̯̬̝̪̻̘̰̫͖̹̙͙͈͔̝̣̖̩͎̔̎̎̏̔͌̊͐́̄̂́̉̏̂͂̽̽͑͌͆͋̋̾͋̊̽͊̚͝͝͝ ̷̡̢̛̼̩̘̺͚̪͖̟͈̾̿̓̀̈͑̂̚T̵̮̱̼̲̻̳̥̩̫̞͉̩͉̤̞̣̹̻͖̻͕̗̫̪̐̐̋́̈́̅̈́̅̚ͅͅͅH̴͔͖̬͉̞̟͈̻̖̠̭͕̑̔̆̈́͛̓̊̊̂́͗̈́̇͒͒̌̕͘͠͠Y̵̧̡̨̖̹̳̗̞͔̲̰͇̮͔̹̹̠͉͉͈̺̣̺͐̈̃̒͐̂̈́̈́̑̓̈́͐͊͂͗̈̊̔̇̄͝͝ ̷̘͚̬͕̹̖̪̳̋̽̆̔̔͊̋͐̾͝Ṙ̷̡̢̧̨̛͔̺͉̩̗̙͎̭͔̤͉̙̠͙͑̿̆͗̈́͒͐͑̓̃̓̋͆̏̈́̋͛̓͋̾̾̀̐͑͛̎͒̍̀̿̿͒̐͘̕É̵̬̠̜͉̀͌̃̃̎̉̃͜ ̴̢̭̭̞̞̜̦͓̳̣̝̻̺̮̜̒͆͊̽̇͑͂̈́́͗̆W̵̡̢̢͇̠̤̙̬̖̞͙͎̘̹͈͍͊ͅĄ̶̨̧̘̯̫̖̯̱̫̟͇̻͙̭̃̂̈̄̓̓͊͗͛́̂̐̀̏͗͆̕͘͜͝͝ͅR̶̯̱̮͖̺̈̽͂́̅̂̆̏͝͠͝D̷̢̢̨̛̪̳͇̰̜̦͙͖͙̯̲̩͙͍̼̦͉͙͗̿̀̿̈̇͋̓̒̅̈́͗̈́͌̂̐́̑͗͑ ̵̨̢̧̨̝͕̭͉̘̺͎̤̻̭̭̱̲͚̼͙̭͉̿̄̃̂͋̀͂̃̀̅̅̎̀́͋̄̀͐͆͋̋̅͊͛͑̀͂́̾͌̿͑̎̿͊͌́̕͘͝͝͝ͅS̷͉̜͗̅̀̅̋̔͋͊̆̀̄̽̾̓̐̚͝")
                                    await ctx.send(ctx.author.mention + "+ $1000000")
                                    await ctx.send(ctx.author.mention + "**-1 S̵̡̡̡̨̛̲̻͔̩̣̣͍̙̯͍̺̦̖͚̪̦̣͎̰̩͈̙̝̮͖͎͔̪̪̠͓̬̭̆͐̽̓̇͐͐͐͆̔͐̈́̑͒͆̊̅͗̐̇́̈̊͆͂͐̚͠ͅǪ̷̨̛̜͚̤͈̩̻̣̣̣̯͕̣̮̩̞̦̙͚̠̖͖̝̻͉͉͕̼͆̉̏͊̑̃̇̾̋͗̈́̌̉͐͗̔́̏́̐̎̇̌̄̚̚͜͜͝ ̴̡̰̣͖̥̗̹͍͉͔̦̭͈̝͔̠̻̊̋̌͋͂̾̉͊̅̏͗͑̈̈́̿̂̈̚Ṳ̴̡̧̖̤̙͈̬͙̥̖̗͇͓̠̱̗̳͉͙͖̘͖̲͎̫̬͚̻̯͍͈͉̣̮͍̫͉̲̝̰̀̆ ̸͎͕͎̘̻̙̔̂͝L̵̨̡̛͕̱̠̣͎͎̩̻̥̺̞̩͕̦͚̝̦̥̙͛̓̓͑̐̈́́̅͋͂͛͌̎̈͗̉̆͂̆̄̃͘̕͝͠ͅͅ**")
                                    money[users.index(ctx.author)] += 1000000
                                    purity[users.index(ctx.author)] = 0
                                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                    return

                if eventtype <= 2:
                    failure = False
                    purchase = 0
                    if eventtype == 1:
                        await ctx.send(ctx.author.mention + " Noveau Riche: I expect you to be fast and accurate.")
                        purchase = round(random.randint(1000, 50000)/100, 2)
                        pay = round(random.randint(math.ceil((purchase*100) * .1), math.ceil((purchase*100) * 2))/100 + purchase, 2)
                        paytime = 15
                    if eventtype == 2:
                        await ctx.send(ctx.author.mention + " Manager: I hope you're doing well.")
                        purchase = round(random.randint(1000, 10000)/100, 2)
                        pay = round(random.randint(math.ceil((purchase*100) * .1), math.ceil((purchase*100) * .5))/100 + purchase, 2)
                        paytime = 17
                    else:
                        purchase = round(random.randint(1000, 10000)/100, 2)
                        pay = round(random.randint(math.ceil((purchase*100) * .1), math.ceil((purchase*100) * .5))/100 + purchase, 2)
                        paytime = 20
                    await ctx.send(ctx.author.mention + " The customer bought $" + str(purchase) + " worth of merchandise, and paid $" + str(pay) + ".")
                    await ctx.send(ctx.author.mention + " Assuming a 10% sales tax, how much change should you give? Leave out the '$' in your answer. You have " + str(paytime) + " seconds.")
                    try:
                        msg = await client.wait_for('message', timeout = paytime, check = check)
                    except asyncio.TimeoutError:
                        await ctx.send("You run out of time.")
                        if eventtype == 1: 
                            await ctx.send(ctx.author.mention + " Noveau Riche: I expected you to be fast. It appears that you weren't.")
                            failure = True
                        elif eventtype == 2:
                            await ctx.send(ctx.author.mention + " Manager: Come on dude... I don't need slow people like you.")
                            failure = True
                        else:
                            strikes += 1
                            await ctx.send(ctx.author.mention + " Strikes: **" + str(strikes) + "**")
                    else:
                        try:
                            winning = float(msg.content)
                            await ctx.send(ctx.author.mention + "You give $" + str(winning) + " in change.")
                            if 0.01 >= winning - abs((pay - 1.1*(purchase))):
                                await ctx.send(ctx.author.mention + ", this was the correct amount.")
                                if eventtype == 1: 
                                    await ctx.send(ctx.author.mention + " Noveau Riche: Nice. You earned this tip.")
                                    bonus += chancebonus
                                    await ctx.send(ctx.author.mention + " Total Bonus: **$" + str(bonus) + "**")
                                    
                                elif eventtype == 2:
                                    await ctx.send(ctx.author.mention + " Manager: Nice job. Here's a bonus for your trouble.")
                                    bonus += chancebonus
                                    await ctx.send(ctx.author.mention + " Total Bonus: **$" + str(bonus) + "**")
                            else:
                                await ctx.send(ctx.author.mention + ", this was the wrong amount. The customer complains.")
                                if eventtype == 1: 
                                    await ctx.send(ctx.author.mention + " Noveau Riche: I expected you to be accurate. You weren't.")
                                    failure = True
                                elif eventtype == 2:
                                    await ctx.send(ctx.author.mention + " Manager: Dude, do you have a brain in there? Screw off.")
                                    failure = True
                                strikes += 1
                                await ctx.send(ctx.author.mention + " Strikes: **" + str(strikes) + "**")
                        except:
                            await ctx.send("That's not a number. You give no change.")
                            if eventtype == 1: 
                                await ctx.send(ctx.author.mention + " Noveau Riche: I expected you to be accurate. Dude, I need my change.")
                                failure = True
                            elif eventtype == 2:
                                await ctx.send(ctx.author.mention + " Manager: You treat our customers like this? Dude. Get out.")
                                failure = True
                            else:
                                strikes += 1
                                await ctx.send(ctx.author.mention + " Strikes: **" + str(strikes) + "**")
                            

                if strikes >= 3:
                    failure = True
                if failure:
                    await ctx.send(ctx.author.mention + ", you have failed your job. You get half of your base wage, and are now unemployed. You cannot sign up for another job for 30 minutes.")
                    money[users.index(ctx.author)] += job_wage["Cashier"]/2
                    jobs[users.index(ctx.author)] = "Unemployed"
                    await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                    UsersInWork.append(ctx.author)
                    await levelup(ctx, 100)
                    WorkCooldown.append(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                x += 1
                
            
            await ctx.send("You have completed your job, and have earned your salary of $" + str(job_wage["Cashier"]) + " plus your bonus of $" + str(bonus) + "!")
            money[users.index(ctx.author)] += job_wage["Cashier"] + bonus
            await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
            await levelup(ctx, 750)
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
    elif jobs[users.index(ctx.author)] == "Waiter/Waitress":
        await ctx.send("I have not added this job yet. The only job that I have added currently is Babysitter, Thief, and Cashier.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Boober Driver":
        await ctx.send("I have not added this job yet. The only job that I have added currently is Babysitter, Thief, and Cashier.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Chef":
        await ctx.send("I have not added this job yet. The only job that I have added currently is Babysitter, Thief, and Cashier.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Musician":
        await ctx.send("You have started your Musician job.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Software Engineer":
        await ctx.send("I have not added this job yet. The only job that I have added currently is Babysitter, Thief, and Cashier.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Mechanic":
        await ctx.send(ctx.author.mention + "You have started your mechanic job.")
        return
    elif jobs[users.index(ctx.author)] == "Scientist":
        await ctx.send("I have not added this job yet. The only job that I have added currently is Babysitter, Thief, and Cashier.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Drug Dealer":
        await ctx.send("I have not added this job yet. The only job that I have added currently is Babysitter, Thief, and Cashier.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Thief":
        await ctx.send("I have not added this job yet. The only job that I have added currently is Babysitter, Thief, and Cashier.")
        await ctx.send("Mention the user that you want to steal from below.")
        try:
            msg = await client.wait_for('message', timeout = 30, check = check)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        else:
            mentionlist = msg.mentions
            if len(mentionlist) != 1:
                if len(mentionlist) == 0:
                    await ctx.send(ctx.author.mention+ " Please actually mention someone.")
                else:
                    await ctx.send(ctx.author.mention+ " don't mention multiple users.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return

            else:
                enemy = client.get_user(mentionlist[0].id)
                if enemy not in users:
                    await ctx.send(ctx.author.mention+ " you have to pick somebody who's used the bot before.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                if enemy == ctx.author:
                    await ctx.send(ctx.author.mention + ", don't mention yourself, idiot.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                embed = discord.Embed(title = "Stats for " + enemy.name, description = "Check these stats to decide if you want to rob this person. If your Research Stat is lower than their Security level, the heist may be difficult.", colour = discord.Colour.blurple())
                embed.add_field(name = "Liquid Assets", value = "$" + str(money[users.index(enemy)]), inline = False)
                embed.add_field(name = "House Data", value = houses[users.index(enemy)] + "\nSecurity: " + str(house_protection[houses[users.index(enemy)]]) + "/20", inline = False)
                embed.add_field(name = "Your Research Stat", value = skills[users.index(ctx.author)][5])
                embed.set_footer(text = "Stealing is bad, you know.")
                await ctx.send(embed = embed)
                yesnomsg = await ctx.send("Are you sure you want to steal from " + enemy.mention + "?")
                await yesnomsg.add_reaction('✅')
                await yesnomsg.add_reaction('❌')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                else:
                    if str(reaction.emoji) != "✅":
                        await ctx.send(ctx.author.mention + " you decide not to steal things today.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
        await ctx.send("How much will you invest? Enter a number below:")
        try:
            msg = await client.wait_for('message', timeout = 30, check = check)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        else:
            if not str(msg.content).isnumeric():
                await ctx.send("That's not a number.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            winning = int(msg.content)
            if winning > money[users.index(ctx.author)]:
                await ctx.send(ctx.author.mention + "You don't have that much money to invest. The heist has been canceled.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
        money[users.index(ctx.author)] -= winning
        x = 0
        energy = skills[users.index(ctx.author)][5]
        budget = winning
        while(x < house_protection[houses[users.index(enemy)]]):
            num = 0
            embed = discord.Embed(title = ctx.author.name + "'s Heist Progress", description = "Stealing from " + enemy.name + "'s " + houses[users.index(enemy)])
            embed.add_field(name = "Energy", value = str(energy) + "/" + str(skills[users.index(ctx.author)][5]), inline = True)
            embed.add_field(name = "Remaining Budget", value = "$" + str(budget), inline = True)
            embed.set_footer(text = "Area " + str(x) + "/" + str(house_protection[houses[users.index(enemy)]]))
            await ctx.send(embed = embed)
            event = random.randint(0,4)
            if event <= 3:
                await ctx.send(ctx.author.mention + ", doesn't seem like anybody's here.")
            elif event == 4:
                await ctx.send(ctx.author.mention + ", I think I hear someone.")
            elif event == 5:
                await ctx.send(ctx.author.mention + ", I see someone.")
            thiefmsg = await ctx.send(ctx.author.mention + " 1. Sneak Forward (-1 Energy, -$1000 Budget) 2. Stay Hidden (+2 Energy, -$500 Budget) 3. Retreat (-2 Energy, -$500 Budget)")
            allowedResponses = []
            await thiefmsg.add_reaction('1️⃣')
            allowedResponses.append("1️⃣")
            await thiefmsg.add_reaction('2️⃣')
            allowedResponses.append("2️⃣")
            await thiefmsg.add_reaction('3️⃣')
            allowedResponses.append("3️⃣")
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time. Stay Hidden has been automatically selected.")
                num = 1
            else:
                if str(reaction.emoji) not in allowedResponses:
                    num = 1
                else:
                    num = emojitonum(str(reaction.emoji))
            if num == 0:
                if energy < 1 and budget > 500:
                    await ctx.send(ctx.author.mention + " you don't have enough Energy to advance. Stay Hidden has been automatically selected.")
                    num = 1
                elif budget < 1000 and budget > 500 and energy > 1:
                    await ctx.send(ctx.author.mention + " you don't have enough budget to advance. Retreat has been automatically selected.")
                    num = 2
                elif budget < 500:
                    if math.ceil(budget/2) > money[users.index(ctx.author)]:
                        fine = money[users.index(ctx.author)]
                    else:
                        fine = math.ceil(budget/2)
                    money[users.index(ctx.author)] -= fine
                    await ctx.send(ctx.author.mention + " you didn't have sufficient equipment to complete this heist, and so were caught. You lose the money you put into the heist, and are fined $" + str(fine) + ". You are no longer in the Thief job, and cannot sign up for a new job for another 30 minutes.")
                    jobs[users.index(ctx.author)] = "Unemployed"
                    await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                    UsersInWork.append(ctx.author)
                    WorkCooldown.append(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
            elif num == 1:
                if budget < 500:
                     if math.ceil(budget/2) > money[users.index(ctx.author)]:
                         fine = money[users.index(ctx.author)]
                     else:
                         fine = math.ceil(budget/2)
                     money[users.index(ctx.author)] -= fine
                     await ctx.send(ctx.author.mention + " you didn't have sufficient equipment to complete this heist, and so were caught. You lose the money you put into the heist, and are fined $" + str(fine) + ". You are no longer in the Thief job, and cannot sign up for a new job for another 30 minutes.")
                     jobs[users.index(ctx.author)] = "Unemployed"
                     await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                     UsersInWork.append(ctx.author)
                     WorkCooldown.append(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                     UsersInCommand.pop(UsersInCommand.index(ctx.author))
                     return
            elif num == 2:
                if budget < 500:
                     if math.ceil(budget/2) > money[users.index(ctx.author)]:
                         fine = money[users.index(ctx.author)]
                     else:
                         fine = math.ceil(budget/2)
                     money[users.index(ctx.author)] -= fine
                     await ctx.send(ctx.author.mention + " you didn't have sufficient equipment to complete this heist, and so were caught. You lose the money you put into the heist, and are fined $" + str(fine) + ". You are no longer in the Thief job, and cannot sign up for a new job for another 30 minutes.")
                     jobs[users.index(ctx.author)] = "Unemployed"
                     await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                     UsersInWork.append(ctx.author)
                     WorkCooldown.append(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                     UsersInCommand.pop(UsersInCommand.index(ctx.author))
                     return
                elif energy < 2:
                     await ctx.send(ctx.author.mention + " you don't have enough Energy to retreat. Stay Hidden has been automatically selected.")
                     num = 1
            if num == 0:
                energy -= 1
                budget -= 1000
                await ctx.send("Energy -1")
                await ctx.send("Budget -$1000")
                timeth = 7 +(math.floor(energy-3))
                sentence = random.choice(Sneaking_Sentences)
            elif num == 1:
                if energy + 2 > skills[users.index(ctx.author)][5]:
                    await ctx.send("Energy +" + str(skills[users.index(ctx.author)][5]-energy))
                    energy = skills[users.index(ctx.author)][5]
                else:
                    energy += 2
                    await ctx.send("Energy +2")
                budget -= 500
                await ctx.send("Budget -$500")
                timeth = 10 + (math.floor(energy-3))
                sentence = random.choice(Hiding_Sentences)
            elif num == 2:
                energy -= 2
                budget -= 500
                await ctx.send("Energy -2")
                await ctx.send("Budget -$500")
                timeth = 4 + (math.floor(energy-3))
                sentence = random.choice(Escape_Sentences)
            success = False
            await ctx.send(ctx.author.mention + " Type '" + sentence + "' in chat! You get " + str(timeth) + " seconds!")
            try:
                msg = await client.wait_for('message', timeout = timeth, check = check)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention + " Too late! You slip up!")
            else:
                if str(msg.content) != sentence:
                    await ctx.send(ctx.author.mention + " You slip up!")
                else:
                    success = True
            leave = False
            caught = False
            if success:
                rng = random.randint(0, 2)
                rng2 = random.randint(0, 5)
                if event <= 3:
                    if num == 0:
                        await ctx.send(ctx.author.mention + " you advance 1 Area successfully.")
                        x+=1
                    elif num == 1:
                        await ctx.send(ctx.author.mention + " you stay hidden successfully.")
                    elif num == 2:
                        await ctx.send(ctx.author.mention + " you retreat successfully.")
                        leave = True
                elif event == 4:
                    if num == 0:
                        if rng > 0:
                            await ctx.send(ctx.author.mention + " you advance 1 Area successfully.")
                            x+=1
                        else:
                            await ctx.send(ctx.author.mention + ", someone saw you.")
                            caught = True
                    elif num == 1:
                        await ctx.send(ctx.author.mention + " you stay hidden successfully.")
                    elif num == 2:
                         if rng > 0:
                            await ctx.send(ctx.author.mention + " you retreat successfully.")
                            leave = True
                         else:
                            await ctx.send(ctx.author.mention + ", someone saw you.")
                            caught = True
                elif event == 5:
                    if num == 0:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
                    elif num == 1:
                        if rng2 > 0:
                            await ctx.send(ctx.author.mention + " you stay hidden successfully.")
                        else:
                            await ctx.send(ctx.author.mention + ", someone saw you.")
                            caught = True
                    elif num == 2:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
            elif not success:
                rng = random.randint(0, 2)
                if event < 3:
                    if num == 0:
                        if rng > 1:
                            await ctx.send(ctx.author.mention + " luckily, there was nobody there to see you slip up. You advance 1 Area successfully.")
                            x+=1
                        else:
                            await ctx.send(ctx.author.mention + ", someone saw you.")
                            caught = True
                    elif num == 1:
                        if rng > 0:
                            await ctx.send(ctx.author.mention + " luckily, there was nobody there to see you slip up. You stay hidden successfully.")
                        else:
                            await ctx.send(ctx.author.mention + ", someone saw you.")
                            caught = True
                    elif num == 2:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
                elif event == 4:
                    if num == 0:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
                    elif num == 1:
                        if rng > 1:
                            await ctx.send(ctx.author.mention + " you stay hidden successfully.")
                        else:
                            await ctx.send(ctx.author.mention + ", someone saw you.")
                            caught = True
                    elif num == 2:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
                elif event == 5:
                    if num == 0:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
                    elif num == 1:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
                    elif num == 2:
                        await ctx.send(ctx.author.mention + ", someone saw you.")
                        caught = True
            if caught:
                if math.ceil(budget/2) > money[users.index(ctx.author)]:
                    fine = money[users.index(ctx.author)]
                else:
                    fine = math.ceil(budget/2)
                money[users.index(ctx.author)] -= fine
                await ctx.send(ctx.author.mention + " You have been caught. You lose the money you put into the heist, and are fined $" + str(fine) + ". You are no longer in the Thief job, and cannot sign up for a new job for another 30 minutes.")
                jobs[users.index(ctx.author)] = "Unemployed"
                await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                UsersInWork.append(ctx.author)
                WorkCooldown.append(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                await levelup(ctx, 50)
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            elif leave:
                await ctx.send(ctx.author.mention + " You retreat. Although you lose the money you put into the heist, you are not fined. You also do not lose your Thief job.")
                await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                await levelup(ctx, 100)
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
        await ctx.send(ctx.author.mention + " You made it! Now all you have to do is pick the lock.")
        sentence = random.choice(Lockpick_Sentences)
        timeth = 50 - house_protection[houses[users.index(enemy)]] + skills[users.index(ctx.author)][5]
        success = False
        await ctx.send(ctx.author.mention + " Type '" + sentence + "' in chat! You get " + str(timeth) + " seconds!")
        try:
            msg = await client.wait_for('message', timeout = timeth, check = check)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention + " Too late! You slip up!")
        else:
            if str(msg.content) != sentence:
                await ctx.send(ctx.author.mention + " You slip up!")
            else:
                success = True
        if success:
            stealmoney = math.floor(money[users.index(enemy)] * 0.3 + money[users.index(enemy)] * 0.02 * energy)
            await ctx.send(ctx.author.mention + " You succeed in lockpicking! You steal $" + str(stealmoney) + " and run away!")
            money[users.index(ctx.author)] += stealmoney
            money[users.index(enemy)] -= stealmoney
            await levelup(ctx, 2000)
            await ctx.send(enemy.mention + ", you have been stolen from!")
        elif not success:
            await ctx.send(ctx.author.mention + " You have broken your lockpicks! You run away, stealing nothing!")
            await levelup(ctx, 1000)
        await ctx.send(ctx.author.mention + " You now have $" + str(money[users.index(ctx.author)]) + ".")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    elif jobs[users.index(ctx.author)] == "Unemployed":
        await ctx.send("You can't work! You're unemployed!")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    UsersInCommand.pop(UsersInCommand.index(ctx.author))
@client.command()
@commands.check(allowedCommand)
async def commandlist(ctx):
    if ctx.author not in users:
        await setup(ctx, True)
    embed = discord.Embed(title = "Command List", description = "Prefix = *", colour = discord.Colour.blurple()) 
    embed.add_field(name = "*playerinfo", value = "Displays your stats and bank balance.", inline = True)
    embed.add_field(name = "*garage", value = "Opens the garage menu, where you can view, upgrade, repair, and sell your cars.", inline = True)
    embed.add_field(name = "*dealership", value = "Opens the dealership menu, where you can purchase cars from various dealers.", inline = True)
    embed.add_field(name = "*realestate", value = "Opens the real estate menu, where you can buy houses.", inline = True)
    embed.add_field(name = "*skillup", value = "Opens the skill menu, where you can trade in skill points for skill upgrades.", inline = True)
    embed.add_field(name = "*race", value = "Opens the race menu, where you can race.", inline = True)
    embed.add_field(name = "*prestige", value = "Opens the prestige menu, where you can prestige to gain prestige points.")
    embed.add_field(name = "*prestigeshop", value = "Opens the prestige shop, where you can trade in prestige points for max skill upgrades.", inline = True)
    embed.add_field(name = "*joblist", value = "Sign up for jobs here.", inline = True)
    embed.add_field(name = "*work", value = "Work at your job here.")
    embed.add_field(name = "*suicide", value = "A command to kill yourself, resetting all of your stats. A good way to get out of early game soft-locking.", inline = True)
    embed.add_field(name = "*commandlist", value = "This command lol", inline = True)
    await ctx.send(embed = embed)
    UsersInCommand.pop(UsersInCommand.index(ctx.author))
@client.command()
@commands.check(allowedCommand)
async def suicide(ctx):
    yn = await ctx.send(ctx.author.mention + ", are you sure that you want to kill yourself, resetting everything for no gain?")
    await yn.add_reaction('✅')
    await yn.add_reaction('❌')
    def check1(reaction, user):
        return user == ctx.author
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        if str(reaction.emoji) == "✅":
            levels[users.index(ctx.author)] = 1
            skills[users.index(ctx.author)][0] = 1
            skills[users.index(ctx.author)][1] = 1
            skills[users.index(ctx.author)][2] = 1
            skills[users.index(ctx.author)][3] = 1
            skills[users.index(ctx.author)][4] = 1
            skills[users.index(ctx.author)][5] = 1
            money[users.index(ctx.author)] = 5000
            garages[users.index(ctx.author)].clear()
            mods[users.index(ctx.author)].clear()
            skill_points[users.index(ctx.author)] = 0
            houses[users.index(ctx.author)] = "Small Apartment"
            xps[users.index(ctx.author)] = 0
            conditions[users.index(ctx.author)].clear()
            carNumbers[users.index(ctx.author)].clear()
            await ctx.send("You have killed yourself. Try to have a bit more fun in your next life, will you?")
        else:
            await ctx.send("You have decided not to kill yourself.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
@client.command()
@commands.check(allowedCommand)
async def setup(ctx, in_function = None):
    if ctx.author not in users:
        await ctx.send(ctx.author.mention + " oh! Looks like you've never played RPGStreet before! Let me set you up.")
        users.append(ctx.author)
        list1 = []
        list2 = [1,1,1,1,1,1]
        list5 = [0,0,0,0,0,0]
        list3 = []
        list4 = []
        list6 = []
        list7 = []
        garages.append(list1) 
        money.append(5000)
        skill_points.append(0)
        levels.append(1)
        xps.append(0)
        storylevels.append(0)
        houses.append("Small Apartment")
        skills.append(list2)
        mods.append(list3)
        prestiges.append(list5)
        prestigepoints.append(0)
        conditions.append(list4)
        carNumbers.append(list6)
        purity.append(1)
        jobs.append("Unemployed")
        await ctx.send("You have been given $5000 and a Small Apartment to start out. Type '*commandlist' to get a list of commands!")
        if not in_function:
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
         await ctx.send("Screw off. You're not getting any free money from me.")
         if not in_function:
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
         return

@client.command()
@commands.check(allowedCommand)
async def garage(ctx):
    if ctx.author not in users:
        await setup(ctx, True)
    page = 1
    num = 0
    while(True):
        embed = discord.Embed(title = ctx.author.name + "'s Garage", description = houses[users.index(ctx.author)] + ": Available garage slots " + str(house_slot[houses[users.index(ctx.author)]] - len(garages[users.index(ctx.author)])) + "/" + str(house_slot[houses[users.index(ctx.author)]]) + "\nSecurity Level: " + str(house_protection[houses[users.index(ctx.author)]]) + "/20", colour = discord.Colour.blurple())
        templist = Return10(garages[users.index(ctx.author)], page)
        tempthing = carGaragePrint(ctx, templist)
        embed.add_field(name = "Garage", value = tempthing, inline = True)
        if math.ceil(len(garages[users.index(ctx.author)])) != 0:
            embed.set_footer(text = "Page " + str(page) + " of " + str(math.ceil(len(garages[users.index(ctx.author)]) / 10)))
        garagemsg = await ctx.send(embed = embed)
        allowedResponses = []
        if templist == None:
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        if len(templist) > 0:
            await garagemsg.add_reaction('1️⃣')
            allowedResponses.append("1️⃣")
        if len(templist) > 1:
            await garagemsg.add_reaction('2️⃣')
            allowedResponses.append("2️⃣")
        if len(templist) > 2:
            await garagemsg.add_reaction('3️⃣')
            allowedResponses.append("3️⃣")
        if len(templist) > 3:
            await garagemsg.add_reaction('4️⃣')
            allowedResponses.append("4️⃣")
        if len(templist) > 4:
            await garagemsg.add_reaction('5️⃣')
            allowedResponses.append("5️⃣")
        if len(templist) > 5:
            await garagemsg.add_reaction('6️⃣')
            allowedResponses.append("6️⃣")
        if len(templist) > 6:
            await garagemsg.add_reaction('7️⃣')
            allowedResponses.append("7️⃣")
        if len(templist) > 7:
            await garagemsg.add_reaction('8️⃣')
            allowedResponses.append("8️⃣")
        if len(templist) > 8:
            await garagemsg.add_reaction('9️⃣')
            allowedResponses.append("9️⃣")
        if len(templist) > 9:
            await garagemsg.add_reaction('🔟')
            allowedResponses.append("🔟")
        if(10*page < len(garages[users.index(ctx.author)])):
            await garagemsg.add_reaction('➡️')
            allowedResponses.append("➡️")
        if(page != 1):
            await garagemsg.add_reaction('⬅️')
            allowedResponses.append("⬅️")
        def check1(reaction, user):
            return user == ctx.author
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        else:
            if str(reaction.emoji) in allowedResponses:
                allowedResponses.clear()
                if str(reaction.emoji) == "➡️":
                    page+=1
                elif str(reaction.emoji) == "⬅️":
                    page-=1
                else:
                    num = emojitonum(str(reaction.emoji))
                    break
    garagecard = await ctx.send(embed = GarageCarCard(ctx, num))
    car = garages[users.index(ctx.author)][num]
    mod = mods[users.index(ctx.author)][num]
    await ctx.send(ctx.author.mention + " Upgrade Vehicle 🧰 Downgrade Vehicle 🔨 Repair Vehicle 🔧 Sell Vehicle 💰 Back 🔙")
    await garagecard.add_reaction('🧰')
    allowedResponses.append("🧰")
    await garagecard.add_reaction('🔨')
    allowedResponses.append("🔨")
    await garagecard.add_reaction('🔧')
    allowedResponses.append("🔧")
    await garagecard.add_reaction('💰')
    allowedResponses.append("💰")
    await garagecard.add_reaction('🔙')
    allowedResponses.append("🔙")
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        if str(reaction.emoji) in allowedResponses:
            allowedResponses.clear()
            if str(reaction.emoji) == "🔨":
                newmod = ""
                returnval = 0
                if mod == "Stock":
                    await ctx.send("You can't downgrade this car.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                elif mod == "Race Stage 1" or mod == "Drag Stage 1" or mod == "Offroad Stage 1":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Stock"
                    yesnomsg = await ctx.send("Downgrade to Stock and get $" + str(returnval) + "?")
                elif mod == "Race Stage 2":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Race Stage 1"
                    yesnomsg = await ctx.send("Downgrade to Race Stage 1 and get $" + str(returnval) + "?") 
                elif mod == "Race Stage 3":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Race Stage 2"
                    yesnomsg = await ctx.send("Downgrade to Race Stage 2 and get $" + str(returnval) + "?")
                elif mod == "Race Stage 4":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Race Stage 3"
                    yesnomsg = await ctx.send("Downgrade to Race Stage 3 and get $" + str(returnval) + "?")
                elif mod == "Race Stage 5":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Race Stage 4"
                    yesnomsg = await ctx.send("Downgrade to Race Stage 4 and get $" + str(returnval) + "?")
                elif mod == "Drag Stage 2":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Drag Stage 1"
                    yesnomsg = await ctx.send("Downgrade to Drag Stage 1 and get $" + str(returnval) + "?") 
                elif mod == "Drag Stage 3":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Drag Stage 2"
                    yesnomsg = await ctx.send("Downgrade to Drag Stage 2 and get $" + str(returnval) + "?")
                elif mod == "Drag Stage 4":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Drag Stage 3"
                    yesnomsg = await ctx.send("Downgrade to Drag Stage 3 and get $" + str(returnval) + "?")
                elif mod == "Drag Stage 5":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Drag Stage 4"
                    yesnomsg = await ctx.send("Downgrade to Drag Stage 4 and get $" + str(returnval) + "?")
                elif mod == "Offroad Stage 2":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Offroad Stage 1"
                    yesnomsg = await ctx.send("Downgrade to Offroad Stage 1 and get $" + str(returnval) + "?") 
                elif mod == "Offroad Stage 3":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Offroad Stage 2"
                    yesnomsg = await ctx.send("Downgrade to Offroad Stage 2 and get $" + str(returnval) + "?")
                elif mod == "Offroad Stage 4":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Offroad Stage 3"
                    yesnomsg = await ctx.send("Downgrade to Offroad Stage 3 and get $" + str(returnval) + "?")
                elif mod == "Offroad Stage 5":
                    returnval = Upgrade_path_price[mod]*Car_Price[car]*.8
                    newmod = "Offroad Stage 4"
                    yesnomsg = await ctx.send("Downgrade to Offroad Stage 4 and get $" + str(returnval) + "?")
                await yesnomsg.add_reaction('✅')
                await yesnomsg.add_reaction('❌')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                else:
                    if str(reaction.emoji) == "✅":
                        money[users.index(ctx.author)] += returnval
                        mods[users.index(ctx.author)].pop(num)
                        mods[users.index(ctx.author)].insert(num, newmod)
                        await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                    else:
                        await ctx.send("You decided not to downgrade your car.")
            if str(reaction.emoji) == "🧰":
                cat = None
                upgradeval = mods[users.index(ctx.author)][num]
                if Car_Upgradable[car]==0:
                    await ctx.send("Unfortunately, this car is not upgradable.")
                    
                    
                if upgradeval=="Stock":
                    if Car_Upgradable[car]==0:
                        await ctx.send("Your car cannot be modified.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    if Car_Upgradable[car]==1:
                        await ctx.send("Your car is currently stock. Race, Drag, and Offroad Stage 1 upgrades are available for this car.")
                    if Car_Upgradable[car]==2:
                        await ctx.send("Your car is currently stock. Race, Drag, and Offroad Stage 1 and Stage 2 upgrades are available for this car.")
                    if Car_Upgradable[car]==3:
                        await ctx.send("Your car is currently stock. Race, Drag, and Offroad Stage 1, Stage 2, and Stage 3 upgrades are available for this car.")
                    if Car_Upgradable[car]==4:
                        await ctx.send("Your car is currently stock. Race, Drag, and Offroad Stage 1, Stage 2, Stage 3, and Stage 4 upgrades are available for this car.")
                    if Car_Upgradable[car]==5:
                        await ctx.send("Your car is currently stock. Race, Drag, and Offroad Stage 1, Stage 2, Stage 3, Stage 4, and Stage 5 upgrades are available for this car.")
                    upgrademsg = await ctx.send("Which upgrade category will you choose? Race 🏎 Drag 🚦 Offroad 🏞")    
                    await upgrademsg.add_reaction('🏎')
                    allowedResponses.append("🏎")
                    await upgrademsg.add_reaction('🚦')
                    allowedResponses.append("🚦")
                    await upgrademsg.add_reaction('🏞')
                    allowedResponses.append("🏞")
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                        if str(reaction.emoji) == "🏎":
                            await ctx.send("You have chosen race upgrades.")
                            cat="r1"
                            
                        if str(reaction.emoji) == "🚦":
                            await ctx.send("You have chosen drag upgrades.")
                            cat="d1"
                            
                        if str(reaction.emoji) == "🏞":
                            await ctx.send("You have chosen offroad upgrades.")
                            cat="o1"
                        
                elif upgradeval=="Race Stage 1":
                    if Car_Upgradable[car]==1:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                       
                    else:
                        await ctx.send("Stage 2 Race upgrades are available for this car.")
                        cat="r2"
                elif mod=="Drag Stage 1":
                    if Car_Upgradable[car]==1:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                       
                    else:
                        await ctx.send("Stage 2 Drag upgrades are available for this car.")
                        cat="d2"
                elif mod=="Offroad Stage 1":
                    if Car_Upgradable[car]==1:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                       
                        
                    else:
                        await ctx.send("Stage 2 Offroad upgrades are available for this car.")
                        cat="o2"
                elif mod=="Race Stage 2":
                    if Car_Upgradable[car] >= 3:
                        await ctx.send("Stage 3 Race upgrades are available for this car.")
                        cat="r3"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                        
                elif mod=="Drag Stage 2":
                    if Car_Upgradable[car] >= 3:
                        await ctx.send("Stage 3 Drag upgrades are available for this car.")
                        cat="d3"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                        
                elif mod=="Offroad Stage 2":
                    if Car_Upgradable[car] >= 3:
                        await ctx.send("Stage 3 Offroad upgrades are available for this car.")
                        cat="o3"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                        
                elif mod=="Race Stage 3":
                    if Car_Upgradable[car]>=4:
                        await ctx.send("Stage 4 Race upgrades are available for this car.")
                        cat="r4"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                        
                elif mod=="Drag Stage 3":
                    if Car_Upgradable[car]>=4:
                        await ctx.send("Stage 4 Drag upgrades are available for this car.")
                        cat="d4"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                       
                elif mod=="Offroad Stage 3":
                    if Car_Upgradable[car]>=4:
                        await ctx.send("Stage 4 Offroad upgrades are available for this car.")
                        cat="o4"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")

                elif mod=="Race Stage 4":
                    if Car_Upgradable[car]==5:
                        await ctx.send("Stage 5 Race upgrades are available for this car.")
                        cat="r5"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                        
                elif mod=="Drag Stage 4":
                    if Car_Upgradable[car]==5:
                        await ctx.send("Stage 5 Drag upgrades are available for this car.")
                        cat="d5"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                       
                elif mod=="Offroad Stage 4":
                    if Car_Upgradable[car]==5:
                        await ctx.send("Stage 5 Offroad upgrades are available for this car.")
                        cat="o5"
                    else:
                        await ctx.send("Unfortunately, you have the max amount of upgrades currently available for your car, and you cannot install any more upgrades.")
                        
                else:
                    await ctx.send("Your car is fully upgraded. No more upgrades are available.")
                    
                if(cat != None):
                        allowedResponses.clear()
                        yesnomsg = await ctx.send("Proceed? y/n:")
                        await yesnomsg.add_reaction('✅')
                        await yesnomsg.add_reaction('❌')
                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                        except asyncio.TimeoutError:
                            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        else:
                            if str(reaction.emoji) == "✅":
                                if cat=="r1":
                                    upg="Race Stage 1"
                                elif cat=="r2":
                                    upg="Race Stage 2"
                                elif cat=="r3":
                                    upg="Race Stage 3"
                                elif cat=="r4":
                                    upg="Race Stage 4"
                                elif cat=="r5":
                                    upg="Race Stage 5"
                                elif cat=="d1":
                                    upg="Drag Stage 1"
                                elif cat=="d2":
                                    upg="Drag Stage 2"
                                elif cat=="d3":
                                    upg="Drag Stage 3"
                                elif cat=="d4":
                                    upg="Drag Stage 4"
                                elif cat=="d5":
                                    upg="Drag Stage 5"
                                elif cat=="o1":
                                    upg="Offroad Stage 1"
                                elif cat=="o2":
                                    upg="Offroad Stage 2"
                                elif cat=="o3":
                                    upg="Offroad Stage 3"
                                elif cat=="o4":
                                    upg="Offroad Stage 4"
                                elif cat=="o5":
                                    upg="Offroad Stage 5"
                                
                                if skills[users.index(ctx.author)][2]>=Upgrade_path_skill[upg] and money[users.index(ctx.author)] >= Upgrade_path_price[upg]*Car_Price[car]:
                                    mods[users.index(ctx.author)].pop(num)
                                    mods[users.index(ctx.author)].insert(num, upg)
                                    await ctx.send("Upgrade complete.")
                                    money[users.index(ctx.author)] = money[users.index(ctx.author)] - (Upgrade_path_price[upg]*Car_Price[car])                                        
                                    await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                                elif money[users.index(ctx.author)] < Upgrade_path_price[upg]*Car_Price[car]:
                                    await ctx.send("You do not have enough money. The upgrade costs $" + str(Upgrade_path_price[upg]*Car_Price[car]) + ", and you only have $" + str(money[users.index(ctx.author)]) + ".")
                                else:
                                    await ctx.send("Upgrade failed.")                                            
                                    await ctx.send("You require a tuning skill level of " + str(Upgrade_path_skill[upg]) + " to complete this action. Your current tuning skill level is " + str(skills[users.index(ctx.author)][2]) + ".")
                            else:
                                await ctx.send("Canceled.")
            if str(reaction.emoji) == "💰":
                await ctx.send("Your " + car + " will sell for $" + str(CalcPrice(ctx, garages[users.index(ctx.author)], num) * 0.75) + ".")
                yesnomsg = await ctx.send("Proceed? y/n:")
                await yesnomsg.add_reaction('✅')
                await yesnomsg.add_reaction('❌')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                else:
                    if str(reaction.emoji) == "✅":
                        money[users.index(ctx.author)] += CalcPrice(ctx, garages[users.index(ctx.author)], num) * 0.75
                        garages[users.index(ctx.author)].pop(num)
                        mods[users.index(ctx.author)].pop(num)
                        conditions[users.index(ctx.author)].pop(num)
                        carNumbers[users.index(ctx.author)].pop(num)
                        
                        await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                    else:
                        await ctx.send("You didn't sell your car.")
            if str(reaction.emoji) == "🔧":
                if conditions[users.index(ctx.author)][num] != 10:
                    await ctx.send("Your " + car + " can be repaired for $" + str((10 - conditions[users.index(ctx.author)][num]) * 0.02 * Car_Price[garages[users.index(ctx.author)][num]]) + ".")
                    yesnomsg = await ctx.send("Proceed? y/n:")
                    await yesnomsg.add_reaction('✅')
                    await yesnomsg.add_reaction('❌')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                        if str(reaction.emoji) == "✅":
                            if money[users.index(ctx.author)] >= (10 - conditions[users.index(ctx.author)][num]) * 0.02 * Car_Price[garages[users.index(ctx.author)][num]]:
                                money[users.index(ctx.author)] = money[users.index(ctx.author)] - ((10 - conditions[users.index(ctx.author)][num]) * 0.02 * Car_Price[garages[users.index(ctx.author)][num]])
                                conditions[users.index(ctx.author)][num] = 10
                                await ctx.send("You now have $" + str(money[users.index(ctx.author)]) + ".")
                            else:
                                await ctx.send("You do not have enough money to repair your car.")
                        else:
                            await ctx.send("You didn't repair your car.")
                else:
                    await ctx.send("Your car is in perfect condition, and has no need to be repaired.")
            if str(reaction.emoji) == "🔙":
                await ctx.send("Leaving garage...")
    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            
@client.command()
@commands.check(allowedCommand)
async def prestige(ctx):
    global skills
    def check1(reaction, user):
        return user == ctx.author
    if ctx.author not in users:
        await setup(ctx, True)
    if (skills[users.index(ctx.author)][0] == 10 + prestiges[users.index(ctx.author)][0] and skills[users.index(ctx.author)][1] == 10 + prestiges[users.index(ctx.author)][1] and skills[users.index(ctx.author)][2] == 10 + prestiges[users.index(ctx.author)][2]) or (skills[users.index(ctx.author)][3] == 10 + prestiges[users.index(ctx.author)][3] and skills[users.index(ctx.author)][4] == 10 + prestiges[users.index(ctx.author)][4] and skills[users.index(ctx.author)][5] == 10 + prestiges[users.index(ctx.author)][5]):
        await ctx.send(ctx.author.mention + ", prestiging is available. Prestiging will reset all of your stats, and erase all your data. All of your monetary assets will be converted to prestige points.")
        totalassets = 0
        totalassets += money[users.index(ctx.author)]
        x = 0
        while(x < len(garages[users.index(ctx.author)])):
            totalassets += CalcPriceFromData(garages[users.index(ctx.author)][x], mods[users.index(ctx.author)][x])
            x += 1
        totalassets += house_price[houses[users.index(ctx.author)]]
        potentialprestige = math.floor(totalassets/500000)
        if (skills[users.index(ctx.author)][0] == 10 and skills[users.index(ctx.author)][1] == 10 and skills[users.index(ctx.author)][2]) and (skills[users.index(ctx.author)][3] == 10 and skills[users.index(ctx.author)][4] == 10 and skills[users.index(ctx.author)][5]):
            potentialprestige += 1
        
        yn = await ctx.send(ctx.author.mention + ", are you sure that you want to reset all of your stats for a mere " + str(potentialprestige) + " Prestige Points?")
        await yn.add_reaction('✅')
        await yn.add_reaction('❌')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
            
        else:
             if str(reaction.emoji) == "✅":
                 levels[users.index(ctx.author)] = 1
                 skills[users.index(ctx.author)][0] = 1
                 skills[users.index(ctx.author)][1] = 1
                 skills[users.index(ctx.author)][2] = 1
                 skills[users.index(ctx.author)][3] = 1
                 skills[users.index(ctx.author)][4] = 1
                 skills[users.index(ctx.author)][5] = 1
                 if purity[users.index(ctx.author)] == 0:
                     await ctx.send("You have no **S̵̡̡̡̨̛̲̻͔̩̣̣͍̙̯͍̺̦̖͚̪̦̣͎̰̩͈̙̝̮͖͎͔̪̪̠͓̬̭̆͐̽̓̇͐͐͐͆̔͐̈́̑͒͆̊̅͗̐̇́̈̊͆͂͐̚͠ͅǪ̷̨̛̜͚̤͈̩̻̣̣̣̯͕̣̮̩̞̦̙͚̠̖͖̝̻͉͉͕̼͆̉̏͊̑̃̇̾̋͗̈́̌̉͐͗̔́̏́̐̎̇̌̄̚̚͜͜͝ ̴̡̰̣͖̥̗̹͍͉͔̦̭͈̝͔̠̻̊̋̌͋͂̾̉͊̅̏͗͑̈̈́̿̂̈̚Ṳ̴̡̧̖̤̙͈̬͙̥̖̗͇͓̠̱̗̳͉͙͖̘͖̲͎̫̬͚̻̯͍͈͉̣̮͍̫͉̲̝̰̀̆ ̸͎͕͎̘̻̙̔̂͝L̵̨̡̛͕̱̠̣͎͎̩̻̥̺̞̩͕̦͚̝̦̥̙͛̓̓͑̐̈́́̅͋͂͛͌̎̈͗̉̆͂̆̄̃͘̕͝͠ͅͅ**. Prestige F̴̨̛͙͉͇̭̣̠̲̥̫̺̞͕̺̠̺͇̤̝̞̹͇̩̲͈̞̺̩͍̤̊̏̀́̽̈̿͒̏̓̚͜͜͝ ̴̱̜̯̗̱̯̙͑͑̊̾̈́͗̉͐͒͋̆̄̅̒͌͒͆̄̋̀̚͠ͅÁ̸̧̡̢̛͓̜̲̣͚̦͖͓̫̈́̾̇̆̀̇̂̀̂͂̃͆͘ ̷̨̢̢̢̛̹͈͎̥̦̥̙̞̪͈̜̩̩̘̭̭̫͆̂̅̋̂͛͐̍̅͛͆͂̔͜͜͝ͅĮ̷̢̻̳̠̖͚͕͚͇̖͙̙̙͎̥͖̩̳̲̩̠͉̹͍͈̫̫̂̀̀̓̀̿́̓̍̅́͑̓̌̀͒̐̔̕͜͝ ̷̧̢̡̝͉̼͍̰̦̙͇͚͙͈͖̩͔̪̯̜̼̟͖̪͕̲̤̼̊̿̈́̾̑̏̓̇̈́̽̾͑͌̀̍̊̇͜͜͝͝ͅL̸̺̤͙̭̬̻̭̪͙̟̻̭̣̱͓͚̦̤͖͖̯̪̝̜̠̺̙̬̠̘̠͙̳͙̲̰̙̝̣͕̓̑̓̍̓̈́̔̇̕͜͝͝ͅ ̷̨̢̧̧̧̛̛̣̜͙̭̞̳͍͖̘͇̹͕̼͚̖̙͍̩̳͇͇̱̠͇͎͉͈̈́̂̂̓̆̾͛̓́͛̂̈͗͋̐͌̀͂̿̈̔͊̍̕͘͠͝Ę̵̇͐̂͊̎͛̉̓̾̆̄̀͂̍̋̒̆̄̀̈̈́̿̏̒̆̐̅̐̃̾̄̔͗̋̚̕͝͠D̶̢̧̨̨̨̢̞̻͕͇̦̺̦̟̹̤͎̖̱͈͕̥̝̼̮̫̥̟̮̪̦̪̘̝͚͇͉͍͇̊͊̽̂͒͗̑͗́̈́͊̑̈́́͊́̂̒͐͐̔͐̅̔͘ͅͅ.")
                     await ctx.send("Stats reset, garage cleared, S̶̡̨̖̪͕͔̩̬̩̩̭̲̜̤̺͕͕̯̻̣̻̫̳̺̺̻̽̀͒͑́̋͑̿́̈́̍̂̑̑́̈́̋̋͗͘̚̚̕͜͠͝͝͝O̸̢̧̢̧̧͈͕̗̤͕͔͖͖̻̜̬̙͓͇͉̙̠͔̭̗͛̌̏̑̾͆͊̄̌̅̓͗͝͠Ų̵̡̛̛̳̗̗̩͙̪͓̪̲̠͎̞̭̭̰̻̺̬̞̝͔͉̱̗̩̍͊̄̏̓́̔͛̄͋͒͌̀̔͒̃̇̓̂͌̀̓̃̃͘̕͘͜͝͝͝͝͝ͅL̶̡̛̙͕̯̬̠͎̲̹̲̥̭̟̲̜͔̼̎̐͂͊̓̍͗͊̾̄̉́̆̏̊̀̑̔͋̑̽̑̑͌̓́͛̔͌̿̏͑̿̊́͘̕͜͝ͅ restored.")
                     await ctx.send("No prestige points gained.")
                     prestigepoints[users.index(ctx.author)] -= potentialprestige
                 prestigepoints[users.index(ctx.author)] += potentialprestige
                 money[users.index(ctx.author)] = 5000
                 garages[users.index(ctx.author)].clear()
                 mods[users.index(ctx.author)].clear()
                 carNumbers[users.index(ctx.author)].clear()
                 conditions[users.index(ctx.author)].clear()
                 skill_points[users.index(ctx.author)] = 0
                 houses[users.index(ctx.author)] = "Small Apartment"
                 xps[users.index(ctx.author)] = 0
                 if purity[users.index(ctx.author)] == 0:
                     purity[users.index(ctx.author)] = 1
                 await ctx.send("You have prestiged. Your stats have been reset. You now have " + str(prestigepoints[users.index(ctx.author)]) + " prestige points. Spend them at the Prestige Shop.")
             else:
                 await ctx.send("You have decided not to prestige today.")
             
    else:
        await ctx.send(ctx.author.mention + ", prestiging is not available for you. You must first max out either your driving or job skills before you can prestige.")
    UsersInCommand.pop(UsersInCommand.index(ctx.author))
@client.command()
@commands.check(allowedCommand)
async def prestigeshop(ctx):
    if ctx.author not in users:
        await setup(ctx, True)
    embed = discord.Embed(title = ctx.author.name + "'s Skill Caps", description = "Player ID #" + str(users.index(ctx.author)), colour = discord.Colour.blurple())   
    embed.add_field(name = "Prestige Points", value = str(prestigepoints[users.index(ctx.author)]), inline = True)
    embed.add_field(name = "Acceleration Skill", value = str(prestiges[users.index(ctx.author)][0] + 10), inline = True)
    embed.add_field(name = "Handling Skill", value = str(prestiges[users.index(ctx.author)][1]  + 10), inline = True)
    embed.add_field(name = "Car Tuning Skill", value = str(prestiges[users.index(ctx.author)][2] + 10), inline = True)
    embed.add_field(name = "Computer Skill", value = str(prestiges[users.index(ctx.author)][3] + 10), inline = True)
    embed.add_field(name = "Service Skill", value = str(prestiges[users.index(ctx.author)][4] + 10), inline = True)
    embed.add_field(name = "Research Skill", value = str(prestiges[users.index(ctx.author)][5] + 10), inline = True)
    await ctx.send(embed = embed)
    skillmsg = await ctx.send(ctx.author.mention + " Which skill cap will you upgrade? 1. Acceleration Skill 2. Handling Skill 3. Car Tuning Skill 4. Computer Skill 5. Service Skills 6. Research Skill")
    allowedresponses = []
    await skillmsg.add_reaction('1️⃣')
    allowedresponses.append("1️⃣")
    await skillmsg.add_reaction('2️⃣')
    allowedresponses.append("2️⃣")
    await skillmsg.add_reaction('3️⃣')
    allowedresponses.append("3️⃣")
    await skillmsg.add_reaction('4️⃣')
    allowedresponses.append("4️⃣")
    await skillmsg.add_reaction('5️⃣')
    allowedresponses.append("5️⃣")
    await skillmsg.add_reaction('6️⃣')
    allowedresponses.append("6️⃣")
    await skillmsg.add_reaction('🔙')
    allowedresponses.append("🔙")
    def check1(reaction, user):
        return user == ctx.author
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=20.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        if str(reaction.emoji) in allowedresponses:
            if str(reaction.emoji) == "🔙":
                await ctx.send("You decided not to upgrade your skills.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            num = emojitonum(str(reaction.emoji))
            if prestigepoints[users.index(ctx.author)] >= 2:
                prestigepoints[users.index(ctx.author)] -= 2
                prestiges[users.index(ctx.author)][num] += 1
                await ctx.send("You have used 2 Prestige Points to upgrade your " + skilllist[num] + " to " + str(skills[users.index(ctx.author)][num] + 10) + ".")
            else:
                await ctx.send("You require at least 2 Prestige Points for that action.")
    UsersInCommand.pop(UsersInCommand.index(ctx.author))

@client.command()
@commands.check(allowedCommand)
async def playerinfo(ctx):
    user = ctx.author
    def check(m):
        return ctx.author == m.author and m.channel == ctx.channel
    if ctx.author not in users:
        await setup(ctx, True)
    else:
        await ctx.send("Please mention one user below.")
        try:
            msg = await client.wait_for('message', timeout = 30, check = check)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        else:
            mentionlist = msg.mentions
            if len(mentionlist) != 1:
                if len(mentionlist) == 0:
                    await ctx.send(ctx.author.mention+ " Please actually mention someone.")
                else:
                    await ctx.send(ctx.author.mention+ " don't mention multiple users.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return

            else:
                user = client.get_user(mentionlist[0].id)
                if user not in users:
                    await ctx.send(ctx.author.mention+ " you have to pick somebody who's used the bot before.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
           
    embed = discord.Embed(title = user.name + "'s Stats", description = "Player ID #" + str(users.index(user)), colour = discord.Colour.blurple())  
    embed.add_field(name = "Basic info", value = "Your level and other stuff", inline = False)
    embed.add_field(name = "Level and Job", value = "Level " + str(levels[users.index(user)]) + " " + str(jobs[users.index(user)]), inline = True)
    embed.add_field(name = "Level Progress", value = levelprogress(user), inline = True)
    embed.add_field(name = "Balance", value = "$" + str(money[users.index(user)]), inline = True)
    embed.add_field(name = "Racing Skills", value = "Car related skills", inline = False)
    embed.add_field(name = "Acceleration Skill", value = str(skills[users.index(user)][0]) + "/" + str(prestiges[users.index(user)][0]+10), inline = True)
    embed.add_field(name = "Handling Skill", value = str(skills[users.index(user)][1]) + "/" + str(prestiges[users.index(user)][1]+10), inline = True)
    embed.add_field(name = "Car Tuning Skill", value = str(skills[users.index(user)][2]) + "/" + str(prestiges[users.index(user)][2]+10), inline = True)
    embed.add_field(name = "Job Skills", value = "Other job related skills", inline = False)
    embed.add_field(name = "Computer Skill", value = str(skills[users.index(user)][3]) + "/" + str(prestiges[users.index(user)][3]+10), inline = True)
    embed.add_field(name = "Service Skill", value = str(skills[users.index(user)][4]) + "/" + str(prestiges[users.index(user)][4]+10), inline = True)
    embed.add_field(name = "Research Skill", value = str(skills[users.index(user)][5]) + "/" + str(prestiges[users.index(user)][5]+10), inline = True)
    await ctx.send(embed = embed)
    UsersInCommand.pop(UsersInCommand.index(ctx.author))

@client.command()
@commands.check(allowedCommand)
async def skillup(ctx):
    global skills
    global skill_points
    if ctx.author not in users:
        await setup(ctx, True)
    embed = discord.Embed(title = ctx.author.name + "'s Skills", description = "Player ID #" + str(users.index(ctx.author)), colour = discord.Colour.blurple())   
    embed.add_field(name = "Skillpoints", value = str(skill_points[users.index(ctx.author)]), inline = True)
    embed.add_field(name = "Acceleration Skill", value = str(skills[users.index(ctx.author)][0]) + "/" + str(prestiges[users.index(ctx.author)][0]+10), inline = True)
    embed.add_field(name = "Handling Skill", value = str(skills[users.index(ctx.author)][1]) + "/" + str(prestiges[users.index(ctx.author)][1]+10), inline = True)
    embed.add_field(name = "Car Tuning Skill", value = str(skills[users.index(ctx.author)][2]) + "/" + str(prestiges[users.index(ctx.author)][2]+10), inline = True)
    embed.add_field(name = "Computer Skill", value = str(skills[users.index(ctx.author)][3]) + "/" + str(prestiges[users.index(ctx.author)][3]+10), inline = True)
    embed.add_field(name = "Service Skill", value = str(skills[users.index(ctx.author)][4]) + "/" + str(prestiges[users.index(ctx.author)][4]+10), inline = True)
    embed.add_field(name = "Research Skill", value = str(skills[users.index(ctx.author)][5]) + "/" + str(prestiges[users.index(ctx.author)][5]+10), inline = True)
    await ctx.send(embed = embed)
    skillmsg = await ctx.send(ctx.author.mention + " Which skill will you upgrade? 1. Acceleration Skill 2. Handling Skill 3. Car Tuning Skill 4. Computer Skill 5. Service Skills 6. Research Skill")
    allowedresponses = []
    await skillmsg.add_reaction('1️⃣')
    allowedresponses.append("1️⃣")
    await skillmsg.add_reaction('2️⃣')
    allowedresponses.append("2️⃣")
    await skillmsg.add_reaction('3️⃣')
    allowedresponses.append("3️⃣")
    await skillmsg.add_reaction('4️⃣')
    allowedresponses.append("4️⃣")
    await skillmsg.add_reaction('5️⃣')
    allowedresponses.append("5️⃣")
    await skillmsg.add_reaction('6️⃣')
    allowedresponses.append("6️⃣")
    await skillmsg.add_reaction('🔙')
    allowedresponses.append("🔙")
    def check1(reaction, user):
        return user == ctx.author
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=20.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        if str(reaction.emoji) in allowedresponses:
            if str(reaction.emoji) == "🔙":
                await ctx.send("You decided not to upgrade your skills.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            num = emojitonum(str(reaction.emoji))
            if skill_points[users.index(ctx.author)] > 0:
                if skills[users.index(ctx.author)][num] >= prestiges[users.index(ctx.author)][num] + 10:
                    await ctx.send("You already have the maximum amount of points in that stat. Your skillpoint has been converted to $50000.")
                    money[users.index(ctx.author)] += 50000
                    skill_points[users.index(ctx.author)] -= 1
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                skills[users.index(ctx.author)][num] += 1
                skill_points[users.index(ctx.author)] -= 1
                await ctx.send(ctx.author.mention + " You upgraded your " + skilllist[num] + " to " + str(skills[users.index(ctx.author)][num]) + ". You now have " + str(skill_points[users.index(ctx.author)]) + " skillpoints.")
            else:
                await ctx.send("You don't have enough skillpoints to upgrade a skill. Come back after you level up.")
    UsersInCommand.pop(UsersInCommand.index(ctx.author))
@client.command()
@commands.check(allowedCommand)
async def realestate(ctx):
    Dealersubject = ctx.author
    if ctx.author not in users:
        await setup(ctx, True)
    await ctx.send("Real Estate Market: " + ctx.author.name + ", you currently have a " + houses[users.index(ctx.author)] + " with " + str(house_slot[houses[users.index(ctx.author)]]) + " garage slots costing $" + str(house_price[houses[users.index(ctx.author)]]) + ". (Market refreshes in " + str(convert(datetime.timedelta.total_seconds(refreshRealEstate.next_iteration - datetime.datetime.now(datetime.timezone.utc)))) + ") Select a house: ")
    Dealermessage = await ctx.send(housestostr())
    def check1(reaction, user):
         return user == ctx.author
    allowedresponses = []
    await Dealermessage.add_reaction('1️⃣')
    allowedresponses.append("1️⃣")
    await Dealermessage.add_reaction('2️⃣')
    allowedresponses.append("2️⃣")
    await Dealermessage.add_reaction('3️⃣')
    allowedresponses.append("3️⃣")
    await Dealermessage.add_reaction('4️⃣')
    allowedresponses.append("4️⃣")
    await Dealermessage.add_reaction('5️⃣')
    allowedresponses.append("5️⃣")
    await Dealermessage.add_reaction('6️⃣')
    allowedresponses.append("6️⃣")
    await Dealermessage.add_reaction('7️⃣')
    allowedresponses.append("7️⃣")
    await Dealermessage.add_reaction('8️⃣')
    allowedresponses.append("8️⃣")
    await Dealermessage.add_reaction('9️⃣')
    allowedresponses.append("9️⃣")
    await Dealermessage.add_reaction('🔟')
    allowedresponses.append("🔟")
    await Dealermessage.add_reaction('🔙')
    allowedresponses.append("🔙")
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        if str(reaction.emoji) not in allowedresponses:
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        if str(reaction.emoji) == "🔙":
            await ctx.send("Leaving Real Estate...")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        house = Housemarket[emojitonum(str(reaction.emoji))]
        if house_price[house] > house_price[houses[users.index(ctx.author)]]:
            yn = await ctx.send(ctx.author.mention + " Will you trade in your current house for a " + house + "? It will cost you $" + str(house_price[house] - house_price[houses[users.index(ctx.author)]]) + ".")
        elif house_price[house] < house_price[houses[users.index(ctx.author)]]:
            yn = await ctx.send(ctx.author.mention + " Will you trade in your current house for a " + house + "? You will gain $" + str(house_price[houses[users.index(ctx.author)]] - house_price[house]) + ".")
        elif house_price[house] == house_price[houses[users.index(ctx.author)]]:
            await ctx.send(ctx.author.mention + " That's literally the exact same house you already have.")
        price = house_price[house] - house_price[houses[users.index(ctx.author)]]
        await yn.add_reaction('✅')
        await yn.add_reaction('❌')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
        except asyncio.TimeoutError:
            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        else:
             if str(reaction.emoji) == "✅":
                 if house_slot[house] < len(garages[users.index(ctx.author)]):
                     await ctx.send("You have too many cars in your garage. You have " + str(len(garages[users.index(ctx.author)])) + " cars, while the " + house + " only has " + str(house_slot[house]) + " garage slots. Go sell some cars or something.")
                     UsersInCommand.pop(UsersInCommand.index(ctx.author))
                     return
                 elif money[users.index(ctx.author)] < price:
                     await ctx.send("You don't have enough money to complete this transaction. You only have $" + str(money[users.index(ctx.author)]) + ", while the trade-in would've cost you $" + str(price) + ".")
                     UsersInCommand.pop(UsersInCommand.index(ctx.author))
                     return
                 else:
                     if price < 0:
                         await ctx.send("You traded in your " + houses[users.index(ctx.author)] + " for a " + house + " and gained $" + str(-1 * price) + ", leaving you with a balance of $" + str(money[users.index(ctx.author)] - price) + ". You now have a total of " + str(house_slot[house]) + " garage slots.")
                     else:
                         await ctx.send("You traded in your " + houses[users.index(ctx.author)] + " for a " + house + " and spent $" + str(-1 * price) + ", leaving you with a balance of $" + str(money[users.index(ctx.author)] - price) + ". You now have a total of " + str(house_slot[house]) + " garage slots.")
                     houses[users.index(ctx.author)] = house
                     money[users.index(ctx.author)] -= price
    UsersInCommand.pop(UsersInCommand.index(ctx.author))

@client.command()
@commands.check(allowedCommand)
async def dealership(ctx):
    if ctx.author not in users:
        await setup(ctx, True)
        
    Dealersubject = ctx.message.author
    Dealermessage = await ctx.send(Dealersubject.mention + " Shop Menu: 1. Ishibashi Global Imports, 2. Akechi Asian Imports, 3. Otto's European Imports, 4. Sally's 'Murican Vehicles, 5. Kraglist.org, 6. Pmbossbys.com")
    await Dealermessage.add_reaction('1️⃣')
    await Dealermessage.add_reaction('2️⃣')
    await Dealermessage.add_reaction('3️⃣')
    await Dealermessage.add_reaction('4️⃣')
    await Dealermessage.add_reaction('5️⃣')
    await Dealermessage.add_reaction('6️⃣')
    def check1(reaction, user):
        return user == Dealersubject
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=20.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        tf = True
        if str(reaction.emoji) == "1️⃣":
            await ctx.send("Kanato: Welcome to Ishibashi Global Imports, " + Dealersubject.mention + ". We pretty much sell whatever we can get our grubby hands on. So you might just find some really cool stuff!")
            while(tf):
                Dealermessage = await ctx.send(ctx.author.mention + " Ishibashi Global Imports Inventory 🌎 (Refreshes in " + str(convert(datetime.timedelta.total_seconds(refreshDealers.next_iteration - datetime.datetime.now(datetime.timezone.utc))) + ") : \n" + carDealerPrint(Idealercars, Idealernum)))
                allowedresponses = []
                await Dealermessage.add_reaction('1️⃣')
                allowedresponses.append("1️⃣")
                await Dealermessage.add_reaction('2️⃣')
                allowedresponses.append("2️⃣")
                await Dealermessage.add_reaction('3️⃣')
                allowedresponses.append("3️⃣")
                await Dealermessage.add_reaction('4️⃣')
                allowedresponses.append("4️⃣")
                await Dealermessage.add_reaction('5️⃣')
                allowedresponses.append("5️⃣")
                await Dealermessage.add_reaction('6️⃣')
                allowedresponses.append("6️⃣")
                await Dealermessage.add_reaction('7️⃣')
                allowedresponses.append("7️⃣")
                await Dealermessage.add_reaction('8️⃣')
                allowedresponses.append("8️⃣")
                await Dealermessage.add_reaction('9️⃣')
                allowedresponses.append("9️⃣")
                await Dealermessage.add_reaction('🔟')
                allowedresponses.append("🔟")
                await Dealermessage.add_reaction('🔙')
                allowedresponses.append("🔙")
                carnum = None
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    break
                else:
                    if str(reaction.emoji) not in allowedresponses:
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    if str(reaction.emoji) == "🔙":
                        await ctx.send(ctx.author.mention + " Leaving dealership...")
                        break
                    emojinum = emojitonum(str(reaction.emoji))
                    car = Idealercars[emojinum]
                    await ctx.send(embed = DealerCarCard(car, Idealernum[emojitonum(str(reaction.emoji))]))
                    Dealermessage = await ctx.send(Dealersubject.mention + (" Will you buy this " + car + " for $" + str(Car_Price[car]) + "?"))
                    await Dealermessage.add_reaction('✅')
                    await Dealermessage.add_reaction('❌')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                         if str(reaction.emoji) == "✅":
                            if Idealernum[emojinum] == 0:
                                await ctx.send(ctx.author.mention + " Kanato: There is no inventory left of this car. You cannot buy it.")
                            elif money[users.index(Dealersubject)] < Car_Price[car]:
                                await ctx.send(ctx.author.mention + " Kanato: You do not have enough money to complete this transaction.")
                            else:
                                if house_slot[houses[users.index(Dealersubject)]] < len(garages[users.index(Dealersubject)]) + 1:
                                    await ctx.send(ctx.author.mention + " You don't have enough space in your garage for a new car!")
                                else:
                                    money[users.index(Dealersubject)] -= Car_Price[car]
                                    await ctx.send(ctx.author.mention + " Kanato: You have bought a " + car + " for $" + str(Car_Price[car]) + ". You now have $" + str(money[users.index(Dealersubject)]) + " left.")
                                    garages[users.index(Dealersubject)].append(car)
                                    conditions[users.index(Dealersubject)].append(10)
                                    mods[users.index(Dealersubject)].append("Stock")
                                    Idealernum[emojinum] -= 1
                                    carTotalAdd(car)
                                    carNumbers[users.index(Dealersubject)].append(carTotal[car])
                                    
            


                                    


        elif str(reaction.emoji) == "2️⃣":
            while(tf):
                await ctx.send("Makoto: Wercome to Akechi Asian Imports, " + Dealersubject.mention + "! We sell onry Asian vehicles. This includes Korean, Japanese, and... that's it.")
                Dealermessage = await ctx.send(ctx.author.mention + " Akechi Asian Imports Inventory 🇯🇵 (Refreshes in " + str(convert(datetime.timedelta.total_seconds(refreshDealers.next_iteration - datetime.datetime.now(datetime.timezone.utc))) + ") : \n" + carDealerPrint(Adealercars, Adealernum)))
                allowedresponses = []
                await Dealermessage.add_reaction('1️⃣')
                allowedresponses.append("1️⃣")
                await Dealermessage.add_reaction('2️⃣')
                allowedresponses.append("2️⃣")
                await Dealermessage.add_reaction('3️⃣')
                allowedresponses.append("3️⃣")
                await Dealermessage.add_reaction('4️⃣')
                allowedresponses.append("4️⃣")
                await Dealermessage.add_reaction('5️⃣')
                allowedresponses.append("5️⃣")
                await Dealermessage.add_reaction('6️⃣')
                allowedresponses.append("6️⃣")
                await Dealermessage.add_reaction('7️⃣')
                allowedresponses.append("7️⃣")
                await Dealermessage.add_reaction('8️⃣')
                allowedresponses.append("8️⃣")
                await Dealermessage.add_reaction('9️⃣')
                allowedresponses.append("9️⃣")
                await Dealermessage.add_reaction('🔟')
                allowedresponses.append("🔟")
                await Dealermessage.add_reaction('🔙')
                allowedresponses.append("🔙")
                carnum = None
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                else:
                    if str(reaction.emoji) not in allowedresponses:
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    if str(reaction.emoji) == "🔙":
                           await ctx.send(ctx.author.mention + " Leaving dealership...")
                           break
                    emojinum = emojitonum(str(reaction.emoji))
                    car = Adealercars[emojinum]
                    await ctx.send(embed = DealerCarCard(car, Adealernum[emojitonum(str(reaction.emoji))]))
                    Dealermessage = await ctx.send(Dealersubject.mention + (" Will you buy this " + car + " for $" + str(Car_Price[car]) + "?"))
                    await Dealermessage.add_reaction('✅')
                    await Dealermessage.add_reaction('❌')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                         if str(reaction.emoji) == "✅":
                            if Adealernum[emojinum] == 0:
                                await ctx.send(ctx.author.mention + " Makoto: There is no inventory left of this car. You cannot buy it.")
                            elif money[users.index(Dealersubject)] < Car_Price[car]:
                                await ctx.send(ctx.author.mention + " Makoto: You can't trick me. I'm trained in the ninja arts. I know you don't have the money.")
                            else:
                                if house_slot[houses[users.index(Dealersubject)]] < len(garages[users.index(Dealersubject)]) + 1:
                                    await ctx.send(ctx.author.mention + " You don't have enough space in your garage for a new car!")
                                else:
                                    money[users.index(Dealersubject)] -= Car_Price[car]
                                    await ctx.send(ctx.author.mention + " Makoto: You have bought a " + car + " for $" + str(Car_Price[car]) + ". You now have $" + str(money[users.index(Dealersubject)]) + " left.")                                    
                                    garages[users.index(Dealersubject)].append(car)
                                    conditions[users.index(Dealersubject)].append(10)
                                    mods[users.index(Dealersubject)].append("Stock")
                                    Adealernum[emojinum] -= 1
                                    carTotalAdd(car)
                                    carNumbers[users.index(Dealersubject)].append(carTotal[car])
                                    
        elif str(reaction.emoji) == "3️⃣":
            while(tf):
                await ctx.send("Otto: Velcome to Otto's European Imports, " + Dealersubject.mention + "! I'm Otto. Ve only sell European vehicles.")
                Dealermessage = await ctx.send(ctx.author.mention + " Otto's European Imports Inventory 🇪🇺 (Refreshes in " + str(convert(datetime.timedelta.total_seconds(refreshDealers.next_iteration - datetime.datetime.now(datetime.timezone.utc))) + ") : \n" + carDealerPrint(Odealercars, Odealernum)))
                allowedresponses = []
                await Dealermessage.add_reaction('1️⃣')
                allowedresponses.append("1️⃣")
                await Dealermessage.add_reaction('2️⃣')
                allowedresponses.append("2️⃣")
                await Dealermessage.add_reaction('3️⃣')
                allowedresponses.append("3️⃣")
                await Dealermessage.add_reaction('4️⃣')
                allowedresponses.append("4️⃣")
                await Dealermessage.add_reaction('5️⃣')
                allowedresponses.append("5️⃣")
                await Dealermessage.add_reaction('6️⃣')
                allowedresponses.append("6️⃣")
                await Dealermessage.add_reaction('7️⃣')
                allowedresponses.append("7️⃣")
                await Dealermessage.add_reaction('8️⃣')
                allowedresponses.append("8️⃣")
                await Dealermessage.add_reaction('9️⃣')
                allowedresponses.append("9️⃣")
                await Dealermessage.add_reaction('🔟')
                allowedresponses.append("🔟")
                await Dealermessage.add_reaction('🔙')
                allowedresponses.append("🔙")
                carnum = None
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                else:
                    if str(reaction.emoji) not in allowedresponses:
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    if str(reaction.emoji) == "🔙":
                            await ctx.send(ctx.author.mention + " Leaving dealership...")
                            break
                    emojinum = emojitonum(str(reaction.emoji))
                    car = Odealercars[emojinum]
                    await ctx.send(embed = DealerCarCard(car, Odealernum[emojitonum(str(reaction.emoji))] ))
                    Dealermessage = await ctx.send(Dealersubject.mention + (" Will you buy this " + car + " for $" + str(Car_Price[car]) + "?"))
                    await Dealermessage.add_reaction('✅')
                    await Dealermessage.add_reaction('❌')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                         if str(reaction.emoji) == "✅":
                            if Odealernum[emojinum] == 0:
                                await ctx.send(ctx.author.mention + " Otto: There is no inventory left of this car. You cannot buy it.")
                            elif money[users.index(Dealersubject)] < Car_Price[car]:
                                await ctx.send(ctx.author.mention + " Otto: You smell like a Serbian. I know you don't have the money.")
                            else:
                                if house_slot[houses[users.index(Dealersubject)]] < len(garages[users.index(Dealersubject)]) + 1:
                                    await ctx.send(ctx.author.mention + " You don't have enough space in your garage for a new car!")
                                else:
                                    money[users.index(Dealersubject)] -= Car_Price[car]
                                    await ctx.send(ctx.author.mention + " Otto: You have bought a " + car + " for $" + str(Car_Price[car]) + ". You now have $" + str(money[users.index(Dealersubject)]) + " left.")                                    
                                    garages[users.index(Dealersubject)].append(car)
                                    conditions[users.index(Dealersubject)].append(10)
                                    mods[users.index(Dealersubject)].append("Stock")
                                    Odealernum[emojinum] -= 1
                                    carTotalAdd(car)
                                    carNumbers[users.index(Dealersubject)].append(carTotal[car])
                                    
        elif str(reaction.emoji) == "4️⃣":
            while(tf):
                await ctx.send("Sally: Welcome to Sally's 'Murican Vehicles, pipsqueak! I'm Sally, and here, we only sell them 'Murican motors.")
                Dealermessage = await ctx.send(ctx.author.mention + " Sally's 'Murican Vehicles Inventory 🇺🇸 (Refreshes in " + str(convert(datetime.timedelta.total_seconds(refreshDealers.next_iteration - datetime.datetime.now(datetime.timezone.utc))) + ") : \n" + carDealerPrint(Sdealercars, Sdealernum)))
                allowedresponses = []
                await Dealermessage.add_reaction('1️⃣')
                allowedresponses.append("1️⃣")
                await Dealermessage.add_reaction('2️⃣')
                allowedresponses.append("2️⃣")
                await Dealermessage.add_reaction('3️⃣')
                allowedresponses.append("3️⃣")
                await Dealermessage.add_reaction('4️⃣')
                allowedresponses.append("4️⃣")
                await Dealermessage.add_reaction('5️⃣')
                allowedresponses.append("5️⃣")
                await Dealermessage.add_reaction('6️⃣')
                allowedresponses.append("6️⃣")
                await Dealermessage.add_reaction('7️⃣')
                allowedresponses.append("7️⃣")
                await Dealermessage.add_reaction('8️⃣')
                allowedresponses.append("8️⃣")
                await Dealermessage.add_reaction('9️⃣')
                allowedresponses.append("9️⃣")
                await Dealermessage.add_reaction('🔟')
                allowedresponses.append("🔟")
                await Dealermessage.add_reaction('🔙')
                allowedresponses.append("🔙")
                carnum = None
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                else:
                    if str(reaction.emoji) not in allowedresponses:
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    if str(reaction.emoji) == "🔙":
                            await ctx.send(ctx.author.mention + " Leaving dealership...")
                            break
                    emojinum = emojitonum(str(reaction.emoji))
                    car = Sdealercars[emojinum]
                    await ctx.send(embed = DealerCarCard(car, Sdealernum[emojitonum(str(reaction.emoji))] ))
                               
                    Dealermessage = await ctx.send(Dealersubject.mention + (" Will you buy this " + car + " for $" + str(Car_Price[car]) + "?"))
                    await Dealermessage.add_reaction('✅')
                    await Dealermessage.add_reaction('❌')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                         if str(reaction.emoji) == "✅":
                            if Odealernum[emojinum] == 0:
                                await ctx.send(ctx.author.mention + " Sally: There is no inventory left of this car. You cannot buy it.")
                            elif money[users.index(Dealersubject)] < Car_Price[car]:
                                await ctx.send(ctx.author.mention + " Sally: You reek. You don't have the money, do ya now?")
                            else:
                                if house_slot[houses[users.index(Dealersubject)]] < len(garages[users.index(Dealersubject)]) + 1:
                                    await ctx.send(ctx.author.mention + " You don't have enough space in your garage for a new car!")
                                else:
                                    money[users.index(Dealersubject)] -= Car_Price[car]
                                    await ctx.send(ctx.author.mention + " Sally: You have bought a " + car + " for $" + str(Car_Price[car]) + ". You now have $" + str(money[users.index(Dealersubject)]) + " left.")                                    
                                    garages[users.index(Dealersubject)].append(car)
                                    conditions[users.index(Dealersubject)].append(10)
                                    mods[users.index(Dealersubject)].append("Stock")
                                    Sdealernum[emojinum] -= 1
                                    carTotalAdd(car)
                                    carNumbers[users.index(Dealersubject)].append(carTotal[car])
                                    
        elif str(reaction.emoji) == "5️⃣":
            await ctx.send("Auction sites will go live when online auctions are added.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        elif str(reaction.emoji) == "6️⃣":
            await ctx.send("Auction sites will go live when online auctions are added.")
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        else:
            await ctx.send(ctx.author.mention + " Don't try to break me.")
    UsersInCommand.pop(UsersInCommand.index(ctx.author))

@client.command()
@commands.check(allowedCommand)
async def race(ctx):
    def check1(reaction, user):
        return user == ctx.author
    if ctx.author not in users:
        await setup(ctx, True)
    onlineMessage = await ctx.send(ctx.author.mention + " 1. PvE or 2. PvP?")
    allowedresponses = []
    await onlineMessage.add_reaction('1️⃣')
    allowedresponses.append("1️⃣")
    await onlineMessage.add_reaction('2️⃣')
    allowedresponses.append("2️⃣")
    try:
        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
    except asyncio.TimeoutError:
        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
        return
    else:
        if str(reaction.emoji) not in allowedresponses:
            UsersInCommand.pop(UsersInCommand.index(ctx.author))
            return
        if str(reaction.emoji) == "1️⃣":
            await ctx.send(ctx.author.mention + " You have selected PvE. Select a car. (If you don't have one, sorry lol, can't race)")
            page = 1
            num = 0
            while(True):
                embed = discord.Embed(title = ctx.author.name + "'s Garage", description = houses[users.index(ctx.author)] + ": Available garage slots " + str(house_slot[houses[users.index(ctx.author)]] - len(garages[users.index(ctx.author)])) + "/" + str(house_slot[houses[users.index(ctx.author)]]), colour = discord.Colour.blurple())
                templist = Return10(garages[users.index(ctx.author)], page)
                tempthing = carGaragePrint(ctx, templist)
                embed.add_field(name = "Garage", value = tempthing, inline = True)
                if math.ceil(len(garages[users.index(ctx.author)])) != 0:
                    embed.set_footer(text = "Page " + str(page) + " of " + str(math.ceil(len(garages[users.index(ctx.author)]) / 10)))
                garagemsg = await ctx.send(embed = embed)
                allowedResponses = []
                if templist == None:
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                if len(templist) > 0:
                    await garagemsg.add_reaction('1️⃣')
                    allowedResponses.append("1️⃣")
                if len(templist) > 1:
                    await garagemsg.add_reaction('2️⃣')
                    allowedResponses.append("2️⃣")
                if len(templist) > 2:
                    await garagemsg.add_reaction('3️⃣')
                    allowedResponses.append("3️⃣")
                if len(templist) > 3:
                    await garagemsg.add_reaction('4️⃣')
                    allowedResponses.append("4️⃣")
                if len(templist) > 4:
                    await garagemsg.add_reaction('5️⃣')
                    allowedResponses.append("5️⃣")
                if len(templist) > 5:
                    await garagemsg.add_reaction('6️⃣')
                    allowedResponses.append("6️⃣")
                if len(templist) > 6:
                    await garagemsg.add_reaction('7️⃣')
                    allowedResponses.append("7️⃣")
                if len(templist) > 7:
                    await garagemsg.add_reaction('8️⃣')
                    allowedResponses.append("8️⃣")
                if len(templist) > 8:
                    await garagemsg.add_reaction('9️⃣')
                    allowedResponses.append("9️⃣")
                if len(templist) > 9:
                    await garagemsg.add_reaction('🔟')
                    allowedResponses.append("🔟")
                if(10*page < len(garages[users.index(ctx.author)])):
                    await garagemsg.add_reaction('➡️')
                    allowedResponses.append("➡️")
                if(page != 1):
                    await garagemsg.add_reaction('⬅️')
                    allowedResponses.append("⬅️")
                await garagemsg.add_reaction('🔙')
                allowedResponses.append("🔙")
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                else:
                    if str(reaction.emoji) in allowedResponses:
                        if str(reaction) == "🔙":
                            await ctx.send("Leaving race...")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        elif str(reaction) == "➡️":
                            page+=1
                        elif str(reaction) == "⬅️":
                            page-=1
                        else:
                            allowedResponses.clear()
                            num = emojitonum(str(reaction.emoji))
                            break
            car = garages[users.index(ctx.author)][num]
            mod = mods[users.index(ctx.author)][num]
            garagecard = await ctx.send(embed = GarageCarCard(ctx, num))
            yesnomsg = await ctx.send("Use this car?")
            await yesnomsg.add_reaction('✅')
            allowedResponses.append("✅")
            await yesnomsg.add_reaction('❌')
            allowedResponses.append("❌")
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            
            else:
                if str(reaction.emoji) not in allowedResponses:
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                elif str(reaction.emoji) == "✅":
                    if conditions[users.index(ctx.author)][num] <= 0:
                        await ctx.send("This car is broken. You cannot race with this.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    EnemyFirstName=random.choice(list(First_Names))
                    EnemyLastName=random.choice(list(Last_Names))
                    HandlingSkill = skills[users.index(ctx.author)][1]
                    AccelSkill = skills[users.index(ctx.author)][0]
                    enemycar = ""
                    enemyupgrade = "Stock"
                    winning = 0
                    while(1==1):
                        while(1==1):
                            enemycar = random.choice(list(Car_HP))
                            if abs(Car_HP[enemycar]- CalcHP(ctx, garages[users.index(ctx.author)], num)) < 1000:
                                break
                        while(1==1):
                            if CalcPRFromData(enemycar, "Stock")==CalcPR(ctx, garages[users.index(ctx.author)], num):
                                 enemyupgrade = "Stock"
                                 break
                            if Car_Upgradable[enemycar]== 5:
                                enemyupgrade = "Race Stage 5"
                                if CalcPRFromData(enemycar, enemyupgrade)==CalcPR(ctx, garages[users.index(ctx.author)], num):
                                    break    
                            if Car_Upgradable[enemycar]== 4:
                                enemyupgrade = "Race Stage 4"
                                if CalcPRFromData(enemycar, enemyupgrade)==CalcPR(ctx, garages[users.index(ctx.author)], num):
                                    break                                
                            if Car_Upgradable[enemycar]>= 3:
                                enemyupgrade = "Race Stage 3"
                                if CalcPRFromData(enemycar, enemyupgrade)==CalcPR(ctx, garages[users.index(ctx.author)], num):
                                    break
                                
                            if Car_Upgradable[enemycar] >= 2:
                                enemyupgrade = "Race Stage 2"
                                if CalcPRFromData(enemycar, enemyupgrade)==CalcPR(ctx, garages[users.index(ctx.author)], num):
                                    break                                    
                            if Car_Upgradable[enemycar] >= 1:
                                enemyupgrade = "Race Stage 1"
                                if CalcPRFromData(enemycar, enemyupgrade)==CalcPR(ctx, garages[users.index(ctx.author)], num):
                                    break
                            if Car_Upgradable[enemycar] >= 0:
                                enemyupgrade = "Stock"
                                if CalcPRFromData(enemycar, enemyupgrade)==CalcPR(ctx, garages[users.index(ctx.author)], num):
                                    break
                            break
                        if CalcPRFromData(enemycar, enemyupgrade)==CalcPR(ctx, garages[users.index(ctx.author)], num):
                            break
                    xpmult = 1
                    presnumh = 10
                    presnuma = 10
                    randlength = random.randint(-3, 7)
                    PRGroup = CalcPR(ctx, garages[users.index(ctx.author)], num)
                    if(PRGroup == "X"):
                        winning = 10000 + random.randint(0, 10000)
                        enemyAccelSkill = random.randint(9, 12)
                        enemyHandleSkill = random.randint(9, 12)
                        if enemyAccelSkill > 10:
                            presnuma = enemyAccelSkill
                        if enemyHandleSkill > 10:
                            presnumh = enemyHandleSkill
                        xpmult = 2.5
                    if(PRGroup == "R"):
                        winning = 7500 + random.randint(0, 5000)
                        enemyAccelSkill = random.randint(7, 11)
                        enemyHandleSkill = random.randint(7, 11)
                        if enemyAccelSkill > 10:
                            presnuma = enemyAccelSkill
                        if enemyHandleSkill > 10:
                            presnumh = enemyHandleSkill
                        xpmult = 2.25
                    if(PRGroup == "S"):
                        winning = 5000 + random.randint(0, 5000)
                        enemyAccelSkill = random.randint(5, 10)
                        enemyHandleSkill = random.randint(5, 10)
                        xpmult = 2
                    if(PRGroup == "A"):
                        winning = 3000 + random.randint(0, 4000)
                        enemyAccelSkill = random.randint(4, 8)
                        enemyHandleSkill = random.randint(4, 8)
                        xpmult = 1.75
                    if(PRGroup == "B"):
                        winning = 2000 + random.randint(0, 2000)
                        enemyAccelSkill = random.randint(4, 6)
                        enemyHandleSkill = random.randint(4, 6)
                        xpmult = 1.5
                    if(PRGroup == "C"):
                        winning = 1000 + random.randint(0, 1500)
                        enemyAccelSkill = random.randint(2, 5)
                        enemyHandleSkill = random.randint(2, 5)
                        xpmult = 1.25
                    if(PRGroup == "D"):
                        winning = 500 + random.randint(0, 500)
                        enemyAccelSkill = random.randint(1, 3)
                        enemyHandleSkill = random.randint(1, 3)
                        xpmult = 1
                    if(PRGroup == "F"):
                        winning = 250 + random.randint(0, 250)
                        enemyAccelSkill = random.randint(1, 2)
                        enemyHandleSkill = random.randint(1, 2)
                        xpmult = 0.75
                    winning = math.ceil(winning*10)/10
                    playerenergy = 100
                    enemyenergy = 100
                    playerzone = 10
                    enemyzone = 10
                    enemypoint = 0
                    yourpoint = 0
                    tightbonus = 0
                    shallowbonus = 0
                    straightbonus = 0
                    if Car_Drive[car] == 0:
                        tightbonus = 2
                        shallowbonus = 3
                        straightbonus = 0
                    if Car_Drive[car] == 1:
                        tightbonus = 0
                        shallowbonus = 2
                        straightbonus = 3
                    if Car_Drive[car] == 2:
                        tightbonus = 2
                        shallowbonus = 1
                        straightbonus = 2
                    await ctx.send("Welcome everybody! Today, we have a Class " + PRGroup + " touge duel!")
                    await ctx.send("It's " + ctx.author.mention + " in their " + mod + " " + car + " with a Handling Skill of " + str(HandlingSkill) + "/" + str(prestiges[users.index(ctx.author)][1] + 10) + ", and an Acceleration Skill of " + str(AccelSkill) + "/" + str(prestiges[users.index(ctx.author)][0] + 10) + ", \n versus " + EnemyFirstName + " " + EnemyLastName + " in their " + enemyupgrade + " " + enemycar + " with a Handling Skill of " + str(enemyHandleSkill) + "/" + str(presnumh) + ", and an Acceleration Skill of " + str(enemyAccelSkill) + "/" + str(presnuma) + ", for a $" + str(winning) + " prize!")
                    await ctx.send(embed = EnemyCarCard(EnemyFirstName + " " + EnemyLastName, enemycar, enemyupgrade))
                    await asyncio.sleep(2)
                    await ctx.send("They've lined up at the start...")
                    await asyncio.sleep(2)
                    await ctx.send("3, 2, 1...")
                    await asyncio.sleep(3)
                    if CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num) > CalcHPFromData(enemycar, enemyupgrade) * CalcHandlingFromData(enemycar, enemyupgrade):
                            enemypoint=0.01 * CalcHPFromData(enemycar, enemyupgrade) * CalcHandlingFromData(enemycar, enemyupgrade)
                            yourpoint=0.01 * CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num)
                            await ctx.send("GO! And " + ctx.author.mention + "'s " + car + " starts with a lead!")
                    if CalcHPFromData(enemycar, enemyupgrade) * CalcHandlingFromData(enemycar, enemyupgrade) > CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num):
                            enemypoint=0.01 * CalcHPFromData(enemycar, enemyupgrade)*CalcHandlingFromData(enemycar, enemyupgrade)
                            yourpoint=0.01 * CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num)
                            await ctx.send("GO! And " + EnemyFirstName + " " + EnemyLastName + "'s " + enemycar + " starts with a lead!")
                    if CalcHP(ctx, garages[users.index(ctx.author)], num)*CalcHandling(ctx, garages[users.index(ctx.author)], num) == CalcHPFromData(enemycar, enemyupgrade)*CalcHandlingFromData(enemycar, enemyupgrade):
                            enemypoint=0.01 * CalcHPFromData(enemycar, enemyupgrade)*CalcHandlingFromData(enemycar, enemyupgrade)
                            yourpoint=0.01 * CalcHP(ctx, garages[users.index(ctx.author)], num)*CalcHandling(ctx, garages[users.index(ctx.author)], num)
                            await ctx.send("OOOOOOH BOTH CARS ARE NECK AND NECK!")
                    x = 0
                    
                    while(x < 7+randlength):
                        roadtype = random.randint(0, 2)
                        speed = 1
                        perfmult = 0.8
                        enemyperfmult = 0.8
                        yourscore = 0
                        enemyscore = 0
                        await ctx.send(embed = pveRaceCard(ctx, yourpoint, enemypoint, playerenergy, playerzone, car, mod, PRGroup, conditions[users.index(ctx.author)][num], roadtype, x+1, 7+randlength))
                        racemsg = await ctx.send(ctx.author.mention + " 1. Drive Slow (+30 Energy, +2 Focus) 2. Drive Normal (-10 Energy, -1 Focus) 3. Drive Fast (-25 Energy, -2 Focus)")
                        allowedResponses = []
                        await racemsg.add_reaction('1️⃣')
                        allowedResponses.append("1️⃣")
                        await racemsg.add_reaction('2️⃣')
                        allowedResponses.append("2️⃣")
                        await racemsg.add_reaction('3️⃣')
                        allowedResponses.append("3️⃣")
                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                        except asyncio.TimeoutError:
                            await ctx.send(ctx.author.mention+ " you didn't give me a response in time. Drive Slow has been automatically selected.")
                            speed = 1
                        else:
                            if str(reaction.emoji) not in allowedResponses:
                                await ctx.send(ctx.author.mention + " you get confused and spin out. You retire from the race.")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                return
                            elif str(reaction.emoji) == "1️⃣":
                                speed = 1
                            elif str(reaction.emoji) == "2️⃣":
                                speed = 2
                            elif str(reaction.emoji) == "3️⃣":
                                speed = 3

                        if speed == 2:
                            if playerenergy < 10:
                                    await ctx.send(ctx.author.mention + " You do not have enough energy to do that. Drive Slow has been automatically selected.")
                                    speed = 1
                            else:
                                    await ctx.send("-10 Energy")
                                    playerenergy=playerenergy-10
                                    
                            if speed == 2:
                                if playerzone != 0:
                                        playerzone=playerzone-1
                                        await ctx.send("-1 Focus")
                                        
                                if playerzone==0:
                                        await ctx.send("You have no focus.")
                        if speed == 3:
                            if playerenergy < 25:
                                    await ctx.send(ctx.author.mention + " You do not have enough energy to do that. Drive Slow has been automatically selected.")
                                    speed = 1
                            else:
                                    await ctx.send("-25 Energy")
                                    playerenergy=playerenergy-25
                                    
                            if speed == 3:
                                if playerzone - 2 <= 0:
                                    if playerzone-1==0:
                                            await ctx.send("-1 Focus")
                                    elif playerzone-2==0:
                                            await ctx.send("-2 Focus")
                                    await ctx.send("You have no focus.")
                                    playerzone=0
                                        
                                else:
                                   await ctx.send("-2 Focus")
                                   playerzone = playerzone - 2
                        if speed == 1:
                            if playerzone + 2 >= 10:
                                if playerzone + 2 == 10:
                                    await ctx.send("+2 Focus")
                                elif playerzone + 1 == 10:
                                    await ctx.send("+1 Focus")
                                playerzone = 10
                                await ctx.send("You have maximum Focus.")
                                    
                            else:
                                    await ctx.send("+2 Focus")
                                    playerzone=playerzone+2
                            if playerenergy >= 70:
                                    await ctx.send("+" + str(100-playerenergy) + " Energy")
                                    playerenergy=100
                                    
                            else:
                                    await ctx.send("+30 Energy")
                                    playerenergy=playerenergy+30
                        def check(m):
                            return ctx.author == m.author and m.channel == ctx.channel
                        if(speed != 1):
                            wordList = []
                            extratime = 0
                            basetime = 0
                            if roadtype == 0:
                                wordList = Straight_Words
                                extratime = straightbonus
                            elif roadtype == 1:
                                wordList = Shallow_Corner_Words
                                extratime = shallowbonus
                            elif roadtype == 2:
                                wordList = Tight_Corner_Words
                                extratime = tightbonus
                            if speed == 2:
                                basetime = 7
                            if speed == 3:
                                basetime = 5
                            timelimit = basetime + (playerzone - 5)
                            word = random.choice(wordList)
                            typeMsg = await ctx.send(ctx.author.mention + " Type the word '" + word + "' in chat! You get " + str(timelimit + extratime) + " seconds! (+" + str(extratime) + " Drivetrain bonus)")
                            try:
                                msg = await client.wait_for('message', timeout = timelimit + extratime, check = check)
                            except asyncio.TimeoutError:
                                await ctx.send(ctx.author.mention + " Too late! You mess up, damaging your car slightly. \n-1 Car Condition")
                                conditions[users.index(ctx.author)][num] -= 1
                                perfmult = 0.8
                            else:
                                if str(msg.content) != word:
                                    await ctx.send(ctx.author.mention + " You mess up, damaging your car slightly. \n-1 Car Condition")
                                    conditions[users.index(ctx.author)][num] -= 1
                                    perfmult = 0.8

                                else:
                                    await ctx.send(ctx.author.mention + ", nice job.")
                                    if speed == 2:
                                        perfmult = 1
                                    if speed == 3:
                                        perfmult = 1.2
                        else:
                            perfmult = 0.8
                            enemyperfmult = 0.8
                        if conditions[users.index(ctx.author)][num] == 0:
                            await ctx.send(ctx.author.mention + " Your car has broken down. You have retired from the race.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        if enemyenergy > 50 and enemyzone > 7 and enemypoint <= yourpoint:
                            enemyperfmult = 1.2
                            enemyenergy -= 25
                            enemyzone -= 2
                            if enemyzone < 10:
                                enemyzone = 0
                        elif enemyenergy > 30 and enemyzone >= 3:
                            enemyperfmult = 1
                            enemyenergy -= 10
                            enemyzone -= 1
                        elif enemyenergy <= 30 or enemyzone < 3:
                            enemyperfmult = 0.8
                            enemyenergy += 30
                            enemyzone += 2
                        
                        if roadtype == 0:
                            yourscore = .03*(perfmult*0.3*(CalcHP(ctx, garages[users.index(ctx.author)], num)+ (100* CalcHandling(ctx, garages[users.index(ctx.author)], num)) + 20*AccelSkill))
                            enemyscore = .03*(enemyperfmult*0.3*(CalcHPFromData(enemycar, enemyupgrade)+(100*CalcHandlingFromData(enemycar, enemyupgrade)) + 20*enemyAccelSkill))
                        elif roadtype == 1:
                            yourscore = 0.2 * (perfmult*(10*(CalcHandling(ctx, garages[users.index(ctx.author)], num))+0.5*AccelSkill + 0.5*HandlingSkill)+ .05*perfmult*(CalcHP(ctx, garages[users.index(ctx.author)], num))/50)
                            enemyscore = 0.2 * (enemyperfmult*(10*(CalcHandlingFromData(enemycar, enemyupgrade)) + 0.5*enemyAccelSkill + 0.5*enemyHandleSkill)+ .05*perfmult*(CalcHPFromData(enemycar, enemyupgrade))/50)
                        elif roadtype == 2:
                            yourscore =  0.6 * (perfmult*(10*(CalcHandling(ctx, garages[users.index(ctx.author)], num)) + HandlingSkill))
                            enemyscore = 0.6 * (enemyperfmult*(10*((CalcHandlingFromData(enemycar, enemyupgrade))) + enemyHandleSkill))
                        if yourscore > enemyscore:
                            if yourpoint > enemypoint:
                                await ctx.send(ctx.author.mention + " keeps their lead on " + EnemyFirstName + " " + EnemyLastName + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            elif yourpoint < enemypoint:
                                await ctx.send(ctx.author.mention + " gains on " + EnemyFirstName + " " + EnemyLastName + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                if yourpoint > enemypoint:
                                    await ctx.send(ctx.author.mention + " pulls ahead!")
                                if yourpoint == enemypoint:
                                    await ctx.send(ctx.author.mention + " is now neck and neck with " + EnemyFirstName + " " + EnemyLastName + "!")
                            else:
                                await ctx.send(ctx.author.mention + "'s position does not change with " + EnemyFirstName + " " + EnemyLastName + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                
                        elif yourscore < enemyscore:
                            if enemypoint > yourpoint:
                                await ctx.send(EnemyFirstName + " " + EnemyLastName + " keeps their lead on " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            elif enemypoint < yourpoint:
                                await ctx.send(EnemyFirstName + " " + EnemyLastName +  " gains on " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                if enemypoint > yourpoint:
                                    await ctx.send(EnemyFirstName + " " + EnemyLastName + " pulls ahead!")
                                if yourpoint == enemypoint:
                                    await ctx.send(EnemyFirstName + " " + EnemyLastName + + " is now neck and neck with " + ctx.author.mention + "!")
                            else:
                                await ctx.send(EnemyFirstName + " " + EnemyLastName + "'s position does not change with " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                
                        else:
                            if enemypoint > yourpoint:
                                await ctx.send(EnemyFirstName + " " + EnemyLastName + " pulls ahead from " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            elif enemypoint < yourpoint:
                                await ctx.send(ctx.author.mention + " pulls ahead from " + EnemyFirstName + " " + EnemyLastName + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            else:
                                await ctx.send(EnemyFirstName + " " + EnemyLastName + "'s position does not change with " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                        x += 1    
                    if(yourpoint > enemypoint):
                        await ctx.send(ctx.author.mention + " wins the race, and earns their $" + str(winning) + " prize!")
                        money[users.index(ctx.author)] += winning
                        await ctx.send(ctx.author.mention + " now has $" + str(money[users.index(ctx.author)]) + ".")
                        await levelup(ctx, 1000*xpmult)
                    if(yourpoint < enemypoint):
                        await ctx.send(EnemyFirstName + " " + EnemyLastName + " wins the race, and earns their $" + str(winning) + " prize!")
                        await levelup(ctx, 250*xpmult)
                    if(yourpoint == enemypoint):
                        await ctx.send("A TIE??? THE HELL???")
                    await ctx.send("Race Ends.")

        elif str(reaction.emoji) == "2️⃣":
            Dealermessage = await ctx.send(ctx.author.mention + " You have selected PvP. Select a class. 1. X  2. R  3. S  4. A  5. B  6. C  7. D  8. F  9. Unrestricted")
            allowedresponses = []
            await Dealermessage.add_reaction('1️⃣')
            allowedresponses.append("1️⃣")
            await Dealermessage.add_reaction('2️⃣')
            allowedresponses.append("2️⃣")
            await Dealermessage.add_reaction('3️⃣')
            allowedresponses.append("3️⃣")
            await Dealermessage.add_reaction('4️⃣')
            allowedresponses.append("4️⃣")
            await Dealermessage.add_reaction('5️⃣')
            allowedresponses.append("5️⃣")
            await Dealermessage.add_reaction('6️⃣')
            allowedresponses.append("6️⃣")
            await Dealermessage.add_reaction('7️⃣')
            allowedresponses.append("7️⃣")
            await Dealermessage.add_reaction('8️⃣')
            allowedresponses.append("8️⃣")
            await Dealermessage.add_reaction('9️⃣')
            allowedresponses.append("9️⃣")
            await Dealermessage.add_reaction('🔙')
            allowedresponses.append("🔙")
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            else:
                if str(reaction.emoji) in allowedresponses:
                    if str(reaction.emoji) == "🔙":
                        await ctx.send("Leaving race...")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                        if str(reaction.emoji) != "9️⃣":
                            classletter = classlist[emojitonum(str(reaction.emoji))]
                        else:
                            classletter = "Unrestricted"
            await ctx.send("Choose a car. The class requirement is " + classletter + ".")
            page = 1
            num = 0
            while(True):
                embed = discord.Embed(title = ctx.author.name + "'s Garage", description = houses[users.index(ctx.author)] + ": Available garage slots " + str(house_slot[houses[users.index(ctx.author)]] - len(garages[users.index(ctx.author)])) + "/" + str(house_slot[houses[users.index(ctx.author)]]), colour = discord.Colour.blurple())
                templist = Return10(garages[users.index(ctx.author)], page)
                tempthing = carGaragePrint(ctx, templist)
                embed.add_field(name = "Garage", value = tempthing, inline = True)
                if math.ceil(len(garages[users.index(ctx.author)])) != 0:
                    embed.set_footer(text = "Page " + str(page) + " of " + str(math.ceil(len(garages[users.index(ctx.author)]) / 10)))
                garagemsg = await ctx.send(embed = embed)
                allowedResponses = []
                if templist == None:
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                if len(templist) > 0:
                    await garagemsg.add_reaction('1️⃣')
                    allowedResponses.append("1️⃣")
                if len(templist) > 1:
                    await garagemsg.add_reaction('2️⃣')
                    allowedResponses.append("2️⃣")
                if len(templist) > 2:
                    await garagemsg.add_reaction('3️⃣')
                    allowedResponses.append("3️⃣")
                if len(templist) > 3:
                    await garagemsg.add_reaction('4️⃣')
                    allowedResponses.append("4️⃣")
                if len(templist) > 4:
                    await garagemsg.add_reaction('5️⃣')
                    allowedResponses.append("5️⃣")
                if len(templist) > 5:
                    await garagemsg.add_reaction('6️⃣')
                    allowedResponses.append("6️⃣")
                if len(templist) > 6:
                    await garagemsg.add_reaction('7️⃣')
                    allowedResponses.append("7️⃣")
                if len(templist) > 7:
                    await garagemsg.add_reaction('8️⃣')
                    allowedResponses.append("8️⃣")
                if len(templist) > 8:
                    await garagemsg.add_reaction('9️⃣')
                    allowedResponses.append("9️⃣")
                if len(templist) > 9:
                    await garagemsg.add_reaction('🔟')
                    allowedResponses.append("🔟")
                if(10*page < len(garages[users.index(ctx.author)])):
                    await garagemsg.add_reaction('➡️')
                    allowedResponses.append("➡️")
                if(page != 1):
                    await garagemsg.add_reaction('⬅️')
                    allowedResponses.append("⬅️")
                await garagemsg.add_reaction('🔙')
                allowedResponses.append("🔙")
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                except asyncio.TimeoutError:
                    await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return
                else:
                    if str(reaction.emoji) in allowedResponses:
                        if str(reaction) == "🔙":
                            await ctx.send("Leaving race...")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        elif str(reaction.emoji) == "➡️":
                            page+=1
                        elif str(reaction.emoji) == "⬅️":
                            page-=1
                        else:
                            num = emojitonum(str(reaction.emoji))
                            break
            car = garages[users.index(ctx.author)][num]
            mod = mods[users.index(ctx.author)][num]
            garagecard = await ctx.send(embed = GarageCarCard(ctx, num))
            yesnomsg = await ctx.send("Use this car?")
            await yesnomsg.add_reaction('✅')
            allowedResponses.append("✅")
            await yesnomsg.add_reaction('❌')
            allowedResponses.append("❌")
            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
            except asyncio.TimeoutError:
                await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                return
            
            else:
                winning = 0
                def check(m):
                                return ctx.author == m.author and m.channel == ctx.channel
                if str(reaction.emoji) not in allowedResponses:
                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                    return

                elif str(reaction.emoji) == "✅":
                    if CalcPR(ctx, garages[users.index(ctx.author)], num) != classletter and classletter != "Unrestricted":
                        await ctx.send("You can't use this car for a class " + classletter + " race!")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    if conditions[users.index(ctx.author)][num] <= 0:
                        await ctx.send("This car is broken. You cannot race with this.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    await ctx.send("How much will you bet? Enter a number below:")
                    try:
                        msg = await client.wait_for('message', timeout = 30, check = check)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                        if not str(msg.content).isnumeric():
                            await ctx.send("That's not a number.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        winning = int(msg.content)
                        if winning > money[users.index(ctx.author)]:
                            await ctx.send(ctx.author.mention + "You don't have that much money to bet. The race has been canceled.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                    await ctx.send("Mention the user that you want to PvP below.")
                    try:
                        msg = await client.wait_for('message', timeout = 30, check = check)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return
                    else:
                        mentionlist = msg.mentions
                        if len(mentionlist) != 1:
                            if len(mentionlist) == 0:
                                await ctx.send(ctx.author.mention+ " Please actually mention someone.")
                            else:
                                await ctx.send(ctx.author.mention+ " don't mention multiple users.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return

                        else:
                            enemy = client.get_user(mentionlist[0].id)
                            if enemy not in users:
                                await ctx.send(ctx.author.mention+ " you have to pick somebody who's used the bot before.")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                return
                            if enemy == ctx.author:
                                await ctx.send(ctx.author.mention + ", don't mention yourself, idiot.")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                return
                    yesnomsg = await ctx.send(enemy.mention + ", " + ctx.author.mention + " has requested a duel with you! The bet is $" + str(winning) + ", and the class restriction is " + classletter + ". Do you accept? Answer within the next 30 seconds:")
                    allowedResponses.clear()
                    await yesnomsg.add_reaction('✅')
                    allowedResponses.append("✅")
                    await yesnomsg.add_reaction('❌')
                    allowedResponses.append("❌")
                    def check3(reaction, user):
                        return user == enemy
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check3)
                    except asyncio.TimeoutError:
                        await ctx.send(ctx.author.mention + ", " + enemy.mention + " did not give me a response in time. The race has been cancelled.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        return     
                    else:
                        if str(reaction.emoji) == "✅":
                            if enemy in UsersInCommand:
                                await ctx.send(enemy.mention + " Cancel your running command first. The race has been cancelled.")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                return
                            if money[users.index(enemy)] < winning:
                                await ctx.send(enemy.mention + " You don't have that much money to bet. The race has been canceled.")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                return
                            elif len(garages[users.index(enemy)]) == 0:
                                await ctx.send(enemy.mention + " You don't have any cars! The race has been canceled.")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                return
                        else:
                            await ctx.send(ctx.author.mention + " The opponent declined your invitation. The race has been canceled.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return     
                    await ctx.send(enemy.mention + " Choose a car. The class requirement is " + classletter + ".")
                    UsersInCommand.append(enemy)
                    page = 1
                    enemynum = 0
                    while(True):
                        embed = discord.Embed(title = enemy.name + "'s Garage", description = houses[users.index(enemy)] + ": Available garage slots " + str(house_slot[houses[users.index(enemy)]] - len(garages[users.index(enemy)])) + "/" + str(house_slot[houses[users.index(enemy)]]), colour = discord.Colour.blurple())
                        templist = Return10(garages[users.index(enemy)], page)
                        tempthing = carGaragePrintEnemy(enemy, templist)
                        embed.add_field(name = "Garage", value = tempthing, inline = True)
                        if math.ceil(len(garages[users.index(ctx.author)])) != 0:
                            embed.set_footer(text = "Page " + str(page) + " of " + str(math.ceil(len(garages[users.index(ctx.author)]) / 10)))
                        garagemsg = await ctx.send(embed = embed)
                        allowedResponses = []
                        if templist == None:
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            return
                        if len(templist) > 0:
                            await garagemsg.add_reaction('1️⃣')
                            allowedResponses.append("1️⃣")
                        if len(templist) > 1:
                            await garagemsg.add_reaction('2️⃣')
                            allowedResponses.append("2️⃣")
                        if len(templist) > 2:
                            await garagemsg.add_reaction('3️⃣')
                            allowedResponses.append("3️⃣")
                        if len(templist) > 3:
                            await garagemsg.add_reaction('4️⃣')
                            allowedResponses.append("4️⃣")
                        if len(templist) > 4:
                            await garagemsg.add_reaction('5️⃣')
                            allowedResponses.append("5️⃣")
                        if len(templist) > 5:
                            await garagemsg.add_reaction('6️⃣')
                            allowedResponses.append("6️⃣")
                        if len(templist) > 6:
                            await garagemsg.add_reaction('7️⃣')
                            allowedResponses.append("7️⃣")
                        if len(templist) > 7:
                            await garagemsg.add_reaction('8️⃣')
                            allowedResponses.append("8️⃣")
                        if len(templist) > 8:
                            await garagemsg.add_reaction('9️⃣')
                            allowedResponses.append("9️⃣")
                        if len(templist) > 9:
                            await garagemsg.add_reaction('🔟')
                            allowedResponses.append("🔟")
                        if(10*page < len(garages[users.index(ctx.author)])):
                            await garagemsg.add_reaction('➡️')
                            allowedResponses.append("➡️")
                        if(page != 1):
                            await garagemsg.add_reaction('⬅️')
                            allowedResponses.append("⬅️")
                        await garagemsg.add_reaction('🔙')
                        allowedResponses.append("🔙")
                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check3)
                        except asyncio.TimeoutError:
                            await ctx.send(ctx.author.mention+ " you didn't give me a response in time.")
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            UsersInCommand.pop(UsersInCommand.index(enemy))
                            return
                        else:
                            if str(reaction.emoji) in allowedResponses:
                                if str(reaction) == "🔙":
                                    await ctx.send("Leaving race...")
                                    UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                    UsersInCommand.pop(UsersInCommand.index(enemy))
                                    return
                                elif str(reaction.emoji) == "➡️":
                                    page+=1
                                elif str(reaction.emoji) == "⬅️":
                                    page-=1
                                else:
                                    allowedResponses.clear()
                                    enemynum = emojitonum(str(reaction.emoji))
                                    break
                                

                    enemycar = garages[users.index(enemy)][enemynum]
                    enemyupgrade = mods[users.index(enemy)][enemynum]
                    garagecard = await ctx.send(embed = UserCarCard(enemy, enemycar, enemyupgrade))
                    yesnomsg = await ctx.send("Use this car?")
                    await yesnomsg.add_reaction('✅')
                    allowedResponses.append("✅")
                    await yesnomsg.add_reaction('❌')
                    allowedResponses.append("❌")
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check3)
                    except asyncio.TimeoutError:
                        await ctx.send(enemy.mention+ " you didn't give me a response in time.")
                        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                        UsersInCommand.pop(UsersInCommand.index(enemy))
                        return
                    
                    else:
                        if str(reaction.emoji) not in allowedResponses:
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            UsersInCommand.pop(UsersInCommand.index(enemy))
                            return
                        elif str(reaction.emoji) == "✅":
                            if CalcPRFromData(enemycar, enemyupgrade) != classletter and classletter != "Unrestricted":
                                await ctx.send("You can't use this car for a class " + classletter + " race!")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                UsersInCommand.pop(UsersInCommand.index(enemy))
                                return
                            if conditions[users.index(enemy)][enemynum] <= 0:
                                await ctx.send("This car is broken. You cannot race with this.")
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                UsersInCommand.pop(UsersInCommand.index(enemy))
                                return

                    HandlingSkill = skills[users.index(ctx.author)][1]
                    AccelSkill = skills[users.index(ctx.author)][0]
                    enemyHandleSkill = skills[users.index(enemy)][1]
                    enemyAccelSkill = skills[users.index(enemy)][0]
                    
                    
                    xpmult = 1
                    randlength = random.randint(-3, 7)
                    PRGroup = classletter
                    if(PRGroup == "PP"):
                        
                        xpmult = 6
                    if(PRGroup == "X"):
                        
                        xpmult = 6
                    if(PRGroup == "R"):
                      
                        xpmult = 4.5
                    if(PRGroup == "S"):
                        
                        xpmult = 3
                    if(PRGroup == "A"):
                        
                        xpmult = 2.5
                    if(PRGroup == "B"):
                        
                        xpmult = 2
                    if(PRGroup == "C"):
                        
                        xpmult = 1.5
                    if(PRGroup == "D"):
                        
                        xpmult = 1
                    if(PRGroup == "F"):
                        
                        xpmult = 0.5
                    winning = math.ceil(winning*10)/10
                    playerenergy = 100
                    enemyenergy = 100
                    playerzone = 10
                    enemyzone = 10
                    enemypoint = 0
                    yourpoint = 0
                    tightbonus = 0
                    shallowbonus = 0
                    straightbonus = 0
                    enemytightbonus = 0
                    enemyshallowbonus = 0
                    enemystraightbonus = 0
                    if Car_Drive[car] == 0:
                        tightbonus = 2
                        shallowbonus = 3
                        straightbonus = 0
                    if Car_Drive[car] == 1:
                        tightbonus = 0
                        shallowbonus = 2
                        straightbonus = 3
                    if Car_Drive[car] == 2:
                        tightbonus = 2
                        shallowbonus = 1
                        straightbonus = 2
                    if Car_Drive[enemycar] == 0:
                        enemytightbonus = 2
                        enemyshallowbonus = 3
                        enemystraightbonus = 0
                    if Car_Drive[enemycar] == 1:
                        enemytightbonus = 0
                        enemyshallowbonus = 2
                        enemystraightbonus = 3
                    if Car_Drive[enemycar] == 2:
                        enemytightbonus = 2
                        enemyshallowbonus = 1
                        enemystraightbonus = 2
                    await ctx.send("Welcome everybody! Today, we have a Class " + PRGroup + " touge duel!")
                    await ctx.send("It's " + ctx.author.mention + " in their " + mod + " " + car + " with a Handling Skill of " + str(HandlingSkill) + ", and an Acceleration Skill of " + str(AccelSkill) + ", \n versus " + enemy.mention + " in their " + enemyupgrade + " " + enemycar + " with a Handling Skill of " + str(enemyHandleSkill) + ", and an Acceleration Skill of " + str(enemyAccelSkill) + ", for a $" + str(winning) + " prize!")
                    await ctx.send(embed = UserCarCard(ctx.author, car, mod))
                    await ctx.send(embed = UserCarCard(enemy, enemycar, enemyupgrade))
                    await asyncio.sleep(2)
                    await ctx.send("They've lined up at the start...")
                    await asyncio.sleep(2)
                    await ctx.send("3, 2, 1...")
                    await asyncio.sleep(3)
                    if CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num) > CalcHPFromData(enemycar, enemyupgrade) * CalcHandlingFromData(enemycar, enemyupgrade):
                            enemypoint=0.01 * CalcHPFromData(enemycar, enemyupgrade) * CalcHandlingFromData(enemycar, enemyupgrade)
                            yourpoint=0.01 * CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num)
                            await ctx.send("GO! And " + ctx.author.mention + "'s " + car + " starts with a lead!")
                    if CalcHPFromData(enemycar, enemyupgrade) * CalcHandlingFromData(enemycar, enemyupgrade) > CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num):
                            enemypoint=0.01 * CalcHPFromData(enemycar, enemyupgrade)*CalcHandlingFromData(enemycar, enemyupgrade)
                            yourpoint=0.01 * CalcHP(ctx, garages[users.index(ctx.author)], num) * CalcHandling(ctx, garages[users.index(ctx.author)], num)
                            await ctx.send("GO! And " + enemy.mention + "'s " + enemycar + " starts with a lead!")
                    if CalcHP(ctx, garages[users.index(ctx.author)], num)*CalcHandling(ctx, garages[users.index(ctx.author)], num) == CalcHPFromData(enemycar, enemyupgrade)*CalcHandlingFromData(enemycar, enemyupgrade):
                            enemypoint=0.01 * CalcHPFromData(enemycar, enemyupgrade)*CalcHandlingFromData(enemycar, enemyupgrade)
                            yourpoint=0.01 * CalcHP(ctx, garages[users.index(ctx.author)], num)*CalcHandling(ctx, garages[users.index(ctx.author)], num)
                            await ctx.send("OOOOOOH BOTH CARS ARE NECK AND NECK!")
                    x = 0
                    
                    while(x < 7+randlength):
                        roadtype = random.randint(0, 2)
                        speed = 1
                        perfmult = 0.8
                        enemyperfmult = 0.8
                        yourscore = 0
                        enemyscore = 0
                        await ctx.send(embed = pvpRaceCard(ctx.author, enemy, yourpoint, enemypoint, playerenergy, playerzone, car, mod, PRGroup, conditions[users.index(ctx.author)][num], roadtype, x+1, 7+randlength))
                        racemsg = await ctx.send(ctx.author.mention + " 1. Drive Slow (+30 Energy, +2 Focus) 2. Drive Normal (-10 Energy, -1 Focus) 3. Drive Fast (-25 Energy, -2 Focus)")
                        allowedResponses = []
                        await racemsg.add_reaction('1️⃣')
                        allowedResponses.append("1️⃣")
                        await racemsg.add_reaction('2️⃣')
                        allowedResponses.append("2️⃣")
                        await racemsg.add_reaction('3️⃣')
                        allowedResponses.append("3️⃣")
                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check1)
                        except asyncio.TimeoutError:
                            await ctx.send(ctx.author.mention+ " you didn't give me a response in time. Drive Slow has been automatically selected.")
                            speed = 1
                        else:
                            if str(reaction.emoji) not in allowedResponses:
                                await ctx.send(ctx.author.mention + " you get confused and spin out. You retire from the race.")
                                await ctx.send(enemy.mention + " wins $" + winning + "!")
                                await ctx.send(ctx.author.mention + " loses $" + winning + "!")
                                money[users.index(ctx.author)] -= winning
                                money[users.index(enemy)] += winning
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                UsersInCommand.pop(UsersInCommand.index(enemy))
                                return
                            elif str(reaction.emoji) == "1️⃣":
                                speed = 1
                            elif str(reaction.emoji) == "2️⃣":
                                speed = 2
                            elif str(reaction.emoji) == "3️⃣":
                                speed = 3
                    
                        if speed == 2:
                            if playerenergy < 10:
                                    await ctx.send(ctx.author.mention + " You do not have enough energy to do that. Drive Slow has been automatically selected.")
                                    speed = 1
                            else:
                                    await ctx.send("-10 Energy")
                                    playerenergy=playerenergy-10
                                    
                            if speed == 2:
                                if playerzone != 0:
                                        playerzone=playerzone-1
                                        await ctx.send("-1 Focus")
                                        
                                if playerzone==0:
                                        await ctx.send("You have no focus.")
                        if speed == 3:
                            if playerenergy < 25:
                                    await ctx.send(ctx.author.mention + " You do not have enough energy to do that. Drive Slow has been automatically selected.")
                                    speed = 1
                            else:
                                    await ctx.send("-25 Energy")
                                    playerenergy=playerenergy-25
                                    
                            if speed == 3:
                                if playerzone - 2 <= 0:
                                    if playerzone-1==0:
                                            await ctx.send("-1 Focus")
                                    elif playerzone-2==0:
                                            await ctx.send("-2 Focus")
                                    await ctx.send("You have no focus.")
                                    playerzone=0
                                        
                                else:
                                   await ctx.send("-2 Focus")
                                   playerzone = playerzone - 2
                        if speed == 1:
                            if playerzone + 2 >= 10:
                                if playerzone + 2 == 10:
                                    await ctx.send("+2 Focus")
                                elif playerzone + 1 == 10:
                                    await ctx.send("+1 Focus")
                                playerzone = 10
                                await ctx.send("You have maximum Focus.")
                                    
                            else:
                                    await ctx.send("+2 Focus")
                                    playerzone=playerzone+2
                            if playerenergy >= 70:
                                    await ctx.send("+" + str(100-playerenergy) + " Energy")
                                    playerenergy=100
                                    
                            else:
                                    await ctx.send("+30 Energy")
                                    playerenergy=playerenergy+30
                        def check(m):
                            return ctx.author == m.author and m.channel == ctx.channel
                        if(speed != 1):
                            wordList = []
                            extratime = 0
                            basetime = 0
                            if roadtype == 0:
                                wordList = Straight_Words
                                extratime = straightbonus
                            elif roadtype == 1:
                                wordList = Shallow_Corner_Words
                                extratime = shallowbonus
                            elif roadtype == 2:
                                wordList = Tight_Corner_Words
                                extratime = tightbonus
                            if speed == 2:
                                basetime = 7
                            if speed == 3:
                                basetime = 5
                            timelimit = basetime + (playerzone - 5)
                            word = random.choice(wordList)
                            typeMsg = await ctx.send(ctx.author.mention + " Type the word '" + word + "' in chat! You get " + str(timelimit + extratime) + " seconds! (+" + str(extratime) + " Drivetrain bonus)")
                            try:
                                msg = await client.wait_for('message', timeout = timelimit + extratime, check = check)
                            except asyncio.TimeoutError:
                                await ctx.send(ctx.author.mention + " Too late! You mess up, damaging your car slightly. \n-1 Car Condition")
                                conditions[users.index(ctx.author)][num] -= 1
                                perfmult = 0.8
                            else:
                                if str(msg.content) != word:
                                    await ctx.send(ctx.author.mention + " You mess up, damaging your car slightly. \n-1 Car Condition")
                                    conditions[users.index(ctx.author)][num] -= 1
                                    perfmult = 0.8
                    
                                else:
                                    await ctx.send(ctx.author.mention + ", nice job.")
                                    if speed == 2:
                                        perfmult = 1
                                    if speed == 3:
                                        perfmult = 1.2
                        else:
                            perfmult = 0.8
                        if conditions[users.index(ctx.author)][num] == 0:
                            await ctx.send(ctx.author.mention + " Your car has broken down. You have retired from the race.")
                            await ctx.send(enemy.mention + " wins $" + winning + "!")
                            await ctx.send(ctx.author.mention + " loses $" + winning + "!")
                            money[users.index(ctx.author)] -= winning
                            money[users.index(enemy)] += winning
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            UsersInCommand.pop(UsersInCommand.index(enemy))
                            return
                        
                        enemyspeed = 1
                        await ctx.send(embed = pvpRaceCard(enemy, ctx.author, enemypoint, yourpoint, enemyenergy, enemyzone, enemycar, enemyupgrade, PRGroup, conditions[users.index(enemy)][enemynum], roadtype, x+1, 7+randlength))
                        racemsg = await ctx.send(enemy.mention + " 1. Drive Slow (+30 Energy, +2 Focus) 2. Drive Normal (-10 Energy, -1 Focus) 3. Drive Fast (-25 Energy, -2 Focus)")
                        allowedResponses = []
                        await racemsg.add_reaction('1️⃣')
                        allowedResponses.append("1️⃣")
                        await racemsg.add_reaction('2️⃣')
                        allowedResponses.append("2️⃣")
                        await racemsg.add_reaction('3️⃣')
                        allowedResponses.append("3️⃣")
                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=30.0, check = check3)
                        except asyncio.TimeoutError:
                            await ctx.send(enemy.mention + " you didn't give me a response in time. Drive Slow has been automatically selected.")
                            enemyspeed = 1
                        else:
                            if str(reaction.emoji) not in allowedResponses:
                                await ctx.send(enemy.mention + " you get confused and spin out. You retire from the race.")
                                await ctx.send(ctx.author.mention + " wins $" + str(winning) + "!")
                                await ctx.send(enemy.mention + " loses $" + str(winning) + "!")
                                money[users.index(ctx.author)] += winning
                                money[users.index(enemy)] -= winning
                                UsersInCommand.pop(UsersInCommand.index(ctx.author))
                                UsersInCommand.pop(UsersInCommand.index(enemy))
                                return
                            elif str(reaction.emoji) == "1️⃣":
                                enemyspeed = 1
                            elif str(reaction.emoji) == "2️⃣":
                                enemyspeed = 2
                            elif str(reaction.emoji) == "3️⃣":
                                enemyspeed = 3
                    
                        if enemyspeed == 2:
                            if enemyenergy < 10:
                                    await ctx.send(enemy.mention + " You do not have enough energy to do that. Drive Slow has been automatically selected.")
                                    enemyspeed = 1
                            else:
                                    await ctx.send("-10 Energy")
                                    enemyenergy=enemyenergy-10
                                    
                            if enemyspeed == 2:
                                if enemyzone != 0:
                                        enemyzone=enemyzone-1
                                        await ctx.send("-1 Focus")
                                        
                                if enemyzone==0:
                                        await ctx.send("You have no focus.")
                        if enemyspeed == 3:
                            if enemyenergy < 25:
                                    await ctx.send(ctx.author.mention + " You do not have enough energy to do that. Drive Slow has been automatically selected.")
                                    enemyspeed = 1
                            else:
                                    await ctx.send("-25 Energy")
                                    enemyenergy=enemyenergy-25
                                    
                            if enemyspeed == 3:
                                if enemyzone - 2 <= 0:
                                    if enemyzone-1==0:
                                            await ctx.send("-1 Focus")
                                    elif enemyzone-2==0:
                                            await ctx.send("-2 Focus")
                                    await ctx.send("You have no focus.")
                                    enemyzone=0
                                        
                                else:
                                   await ctx.send("-2 Focus")
                                   enemyzone = enemyzone - 2
                        if enemyspeed == 1:
                            if enemyzone + 2 >= 10:
                                if enemyzone + 2 == 10:
                                    await ctx.send("+2 Focus")
                                elif enemyzone + 1 == 10:
                                    await ctx.send("+1 Focus")
                                enemyzone = 10
                                await ctx.send("You have maximum Focus.")
                                    
                            else:
                                    await ctx.send("+2 Focus")
                                    enemyzone=enemyzone+2
                            if enemyenergy >= 70:
                                    await ctx.send("+" + str(100-enemyenergy) + " Energy")
                                    enemyenergy=100
                                    
                            else:
                                    await ctx.send("+30 Energy")
                                    enemyenergy=enemyenergy+30
                        def check4(m):
                            return enemy == m.author and m.channel == ctx.channel
                        if(enemyspeed != 1):
                            wordList = []
                            extratime = 0
                            basetime = 0
                            if roadtype == 0:
                                wordList = Straight_Words
                                extratime = enemystraightbonus
                            elif roadtype == 1:
                                wordList = Shallow_Corner_Words
                                extratime = enemyshallowbonus
                            elif roadtype == 2:
                                wordList = Tight_Corner_Words
                                extratime = enemytightbonus
                            if enemyspeed == 2:
                                basetime = 7
                            if enemyspeed == 3:
                                basetime = 5
                            timelimit = basetime + (enemyzone - 5)
                            word = random.choice(wordList)
                            typeMsg = await ctx.send(enemy.mention + " Type the word '" + word + "' in chat! You get " + str(timelimit + extratime) + " seconds! (+" + str(extratime) + " Drivetrain bonus)")
                            try:
                                msg = await client.wait_for('message', timeout = timelimit + extratime, check = check4)
                            except asyncio.TimeoutError:
                                await ctx.send(enemy.mention + " Too late! You mess up, damaging your car slightly. \n-1 Car Condition")
                                conditions[users.index(enemy)][enemynum] -= 1
                                enemyperfmult = 0.8
                            else:
                                if str(msg.content) != word:
                                    await ctx.send(enemy.mention + " You mess up, damaging your car slightly. \n-1 Car Condition")
                                    conditions[users.index(enemy)][enemynum] -= 1
                                    enemyperfmult = 0.8
                    
                                else:
                                    await ctx.send(enemy.mention + ", nice job.")
                                    if enemyspeed == 2:
                                        enemyperfmult = 1
                                    if enemyspeed == 3:
                                        enemyperfmult = 1.2
                        else:
                            enemyperfmult = 0.8
                        if conditions[users.index(enemy)][enemynum] == 0:
                            await ctx.send(enemy.mention + " Your car has broken down. You have retired from the race.")
                            await ctx.send(enemy.mention + " wins $" + str(winning) + "!")
                            await ctx.send(ctx.author.mention + " loses $" + str(winning) + "!")
                            money[users.index(ctx.author)] += winning
                            money[users.index(enemy)] -= winning
                            UsersInCommand.pop(UsersInCommand.index(ctx.author))
                            UsersInCommand.pop(UsersInCommand.index(enemy))
                            return
                        
                        if roadtype == 0:
                            yourscore = .03*(perfmult*0.3*(CalcHP(ctx, garages[users.index(ctx.author)], num)+ (100* CalcHandling(ctx, garages[users.index(ctx.author)], num)) + 20*AccelSkill))
                            enemyscore = .03*(enemyperfmult*0.3*(CalcHPFromData(enemycar, enemyupgrade)+(100*CalcHandlingFromData(enemycar, enemyupgrade)) + 20*enemyAccelSkill))
                        elif roadtype == 1:
                            yourscore = 0.2 * (perfmult*(10*(CalcHandling(ctx, garages[users.index(ctx.author)], num))+0.5*AccelSkill + 0.5*HandlingSkill)+ .05*perfmult*(CalcHP(ctx, garages[users.index(ctx.author)], num))/50)
                            enemyscore = 0.2 * (enemyperfmult*(10*(CalcHandlingFromData(enemycar, enemyupgrade)) + 0.5*enemyAccelSkill + 0.5*enemyHandleSkill)+ .05*perfmult*(CalcHPFromData(enemycar, enemyupgrade))/50)
                        elif roadtype == 2:
                            yourscore =  0.6 * (perfmult*(10*(CalcHandling(ctx, garages[users.index(ctx.author)], num)) + HandlingSkill))
                            enemyscore = 0.6 * (enemyperfmult*(10*((CalcHandlingFromData(enemycar, enemyupgrade))) + enemyHandleSkill))
                        print(str(yourscore))
                        print(str(enemyscore))
                        if yourscore > enemyscore:
                            if yourpoint > enemypoint:
                                await ctx.send(ctx.author.mention + " keeps their lead on " + enemy.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            elif yourpoint < enemypoint:
                                await ctx.send(ctx.author.mention + " gains on " + enemy.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                if yourpoint > enemypoint:
                                    await ctx.send(ctx.author.mention + " pulls ahead!")
                                if yourpoint == enemypoint:
                                    await ctx.send(ctx.author.mention + " is now neck and neck with " + enemy.mention + "!")
                            else:
                                await ctx.send(ctx.author.mention + "'s position does not change with " + enemy.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                
                        elif yourscore < enemyscore:
                            if enemypoint > yourpoint:
                                await ctx.send(enemy.mention + " keeps their lead on " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            elif enemypoint < yourpoint:
                                await ctx.send(enemy.mention +  " gains on " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                if enemypoint > yourpoint:
                                    await ctx.send(enemy.mention + " pulls ahead!")
                                if yourpoint == enemypoint:
                                    await ctx.send(enemy.mention + " is now neck and neck with " + ctx.author.mention + "!")
                            else:
                                await ctx.send(enemy.mention + "'s position does not change with " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                                
                        else:
                            if enemypoint > yourpoint:
                                await ctx.send(enemy.mention + " pulls ahead from " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            elif enemypoint < yourpoint:
                                await ctx.send(enemy.mention + " pulls ahead from " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                            else:
                                await ctx.send(enemy.mention + "'s position does not change with " + ctx.author.mention + "!")
                                yourpoint += yourscore
                                enemypoint += enemyscore
                        x += 1    
                    if(yourpoint > enemypoint):
                        await ctx.send(ctx.author.mention + " wins the race, and earns their $" + str(winning) + " prize!")
                        await ctx.send(enemy.mention + " loses $" + str(winning) + "!")
                        money[users.index(ctx.author)] += winning
                        money[users.index(enemy)] -= winning
                        await ctx.send(ctx.author.mention + " now has $" + str(money[users.index(ctx.author)]) + ".")
                        await ctx.send(enemy.mention + " now has $" + str(money[users.index(enemy)]) + ".")
                        await levelup(ctx, 1000*xpmult)
                        await levelupuser(ctx, enemy, 250*xpmult)
                    if(yourpoint < enemypoint):
                        await ctx.send(enemy.mention + " wins the race, and earns their $" + str(winning) + " prize!")
                        await ctx.send(ctx.author.mention + " loses $" + str(winning) + "!")
                        money[users.index(ctx.author)] -= winning
                        money[users.index(enemy)] += winning
                        await ctx.send(ctx.author.mention + " now has $" + str(money[users.index(ctx.author)]) + ".")
                        await ctx.send(enemy.mention + " now has $" + str(money[users.index(enemy)]) + ".")
                        await levelup(ctx, 250*xpmult)
                        await levelupuser(ctx, enemy, 1000*xpmult)
                    if(yourpoint == enemypoint):
                        await ctx.send("A TIE??? THE HELL???")
                    await ctx.send("Race Ends.")
                    UsersInCommand.pop(UsersInCommand.index(enemy))
        UsersInCommand.pop(UsersInCommand.index(ctx.author))
                

client.run(key.key)


