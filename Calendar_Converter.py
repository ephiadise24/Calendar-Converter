x = input("Please choose your calendar type GC for Gregorian calendar or EC for Ethiopian calendar...").upper()
if x == "GC":
   D = input("Choose your date according to DD-MM-YYYY for Gregorian calendar...")
elif x == "EC":
   D = input("Choose your date according to DD-MM-YYYY for Ethiopian calendar...")
else:
   D = "NONE"
if not D == "NONE" and len(D) == 10:
   try:
    int(D[0:2])
    int(D[3:5])
    int(D[6:10])

    print(f"Processing {D[0:2]}/{D[3:5]}/{D[6:10]} {x}...")
    D2 = int(D[0:2])
    M2 = int(D[3:5])
    Y2 = int(D[6:10])

    if x == "EC":

        DD = int(D2) - 9
        MM = int(M2) - 2
        YY = int(Y2) + 7

        if int(DD) <= 29 and int(MM) in (1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12):
           print(f"Converted to Gregorian calendar {DD}/{MM}/{YY} GC")

        elif int(DD) < 1 and int(MM) <= int("12") and int(MM) >= 1:
           DD2 = int(DD) + 30
           MM2 = int(MM) - 1
           YY2 = YY
           print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) < 1 and int(MM) < int("1"):
           DD2 = int(DD) + 30
           MM2 = int(MM) + 12
           YY2 = YY - 1
           print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) <= 29 and int(MM) > 12:
           DD2 = int(DD)
           MM2 = int(MM) - 12
           YY2 = YY + 1
           print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) > 31 and int(MM) in (1, 3, 5, 7, 8, 10):
           DD2 = int(DD) - 31
           MM2 = int(MM) + 1
           YY2 = YY
           print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) > 31 and int(MM) > 12:
           DD2 = int(DD) - 31
           MM2 = int(MM) - 12
           YY2 = YY + 1
           print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) > 30 and int(MM) in (4, 6, 9, 11):
            DD2 = int(DD) - 30
            MM2 = int(MM) + 1
            YY2 = YY
            print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) > 30 and int(MM) > 12:
            DD2 = int(DD) - 30
            MM2 = int(MM) - 12
            YY2 = YY + 1
            print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) > 29 and int(MM) == int("02"):
            DD2 = int(DD) - 29
            MM2 = int(MM) + 1
            YY2 = YY
            print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")

        elif int(DD) > 31 and int(MM) == int("12"):
            DD2 = int(DD) - 31
            MM2 = int(MM) - 11
            YY2 = YY + 1
            print(f"Converted to Gregorian calendar {DD2}/{MM2}/{YY2} GC")
        else:
            print(f"{D2}/{M2}/{Y2} EC is invalid date! please enter your date correctly")



    else:
        DD = int(D[0:2]) + 9
        MM = int(D[3:5]) + 2
        YY = int(D[6:10]) - 7

        if int(DD) <= 30 and int(MM) in (1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12):
           print(f"Converted to Ethiopian calendar {DD}/{MM}/{YY} EC")

        elif int(DD) <= 30 and int(MM) > 12:
           DD2 = int(DD)
           MM2 = int(MM) - 12
           YY2 = YY + 1
           print(f"Converted to Ethiopian calendar {DD2}/{MM2}/{YY2} EC")

        elif int(DD) > 30 and int(MM) > 12:
           DD2 = int(DD) - 30
           MM2 = int(MM) - 12
           YY2 = YY + 1
           print(f"Converted to Ethiopian calendar {DD2}/{MM2}/{YY2} EC")
        elif int(DD) > 30 and int(MM) < 12:
           DD2 = int(DD) - 30
           MM2 = int(MM) + 1
           YY2 = YY
           print(f"Converted to Ethiopian calendar {DD2}/{MM2}/{YY2} EC")
        elif int(DD) > 30 and int(MM) == 12:
           DD2 = int(DD) - 30
           MM2 = int(MM) - 11
           YY2 = YY + 1
           print(f"Converted to Ethiopian calendar {DD2}/{MM2}/{YY2} EC")
        else:
            print(f"{D2}/{M2}/{Y2} GC is invalid date! please enter your date correctly")

   except ValueError:
    print("Please enter date only in DD-MM-YYYY format")
elif not D == "NONE" and len(D) != 10:
    print("Please enter date only in DD-MM-YYYY format")
else:
    print("Please choose from GC or EC")

