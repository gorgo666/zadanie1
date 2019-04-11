import datetime

born = input("spisz swoją datę urodzenia w formacie 'dd-mm-yyyy': ")
date_format = '%d-%m-%Y'

try:
    date_obj = datetime.datetime.strptime(born, date_format)
    born = born.split("-")
    bornD = int(born[0])
    bornM = int(born[1])
    bornY = int(born[2])
    actualYear = datetime.datetime.now()
    age = actualYear.year - bornY
    thisYearBirstday = datetime.datetime(actualYear.year, bornM, bornD)
    thisYearBirstday = thisYearBirstday.strftime("%A")
    futureYearBirstday = datetime.datetime(actualYear.year + 15, bornM, bornD)
    futureYearBirstday = futureYearBirstday.strftime("%A")
    print("W tym roku będziasz miał urodziny w: " + thisYearBirstday)
    print("Za 15 lat będziesz miał urodziny w: " + futureYearBirstday)
except:
    print("zły format daty, powinien być DD-MM-YYYY")