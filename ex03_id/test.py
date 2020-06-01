isikukood = "3-12162710"

year_number = isikukood[1:3]

if (0 < int(year_number) < 100):
    print("Õige")
else:
    print("Vale")
