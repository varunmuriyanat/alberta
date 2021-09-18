with open("property_search5.md", "w") as fw:
    with open("property_search5.txt", "r") as fp:
        line = fp.readline()
        cnt = 1
        address = None
        postal = None
        mls = None
        price = None
        description = None
        beds = None
        baths = None
        flrArea = None
        daysOnMarket = None
        residential = None
        status_change = None

        fw.write("|Status".ljust(16))
        fw.write("|Price".ljust(9))
        fw.write("|B".ljust(1))
        fw.write("|Bat".ljust(3))
        fw.write("|Postal".ljust(8))
        fw.write("|FlrA".ljust(9))
        fw.write("|Address".ljust(50))
        fw.write("|Day".ljust(4))
        fw.write("|Residential".ljust(61))
        fw.write("|mls".ljust(9))
        fw.write("|Description".ljust(1021))
        fw.write("|")
        fw.write("\n")

        while line:
            if(cnt > 11):
                cnt = cnt - 11

                fw.write("|")
                fw.write(status_change + "|")
                fw.write(price + "|")
                fw.write(beds  + "|")
                fw.write(baths  + "|")
                fw.write(postal  + "|")
                fw.write(flrArea  + "|")
                fw.write(address  + "|")
                fw.write(daysOnMarket  + "|")
                fw.write(residential  + "|")
                fw.write(mls  + "|")
                fw.write(description  + "|")
                fw.write("\n")

            if(cnt == 1):
                address = line.strip()     
                address = address.ljust(49)
            elif(cnt == 2):
                postal= line.strip().replace("Postal Code: ", "")
            elif(cnt == 3):
                mls = line.strip()
            elif(cnt == 4):
                residential = line.strip().ljust(60)
            elif(cnt == 5):
                price = line.strip().replace("Price: ", "")
            elif(cnt == 6):
                description = line.strip().ljust(1020)
            elif(cnt == 7):
                beds = line.strip().replace("BEDS: ", "")
            elif(cnt == 8):
                baths = line.strip().replace("BATHS: ", "")
            elif(cnt == 9):
                flrArea = line.strip().replace("FlrArea SF : ", "").strip().ljust(8)
            elif(cnt == 10):
                daysOnMarket = line.strip().replace("Days on Market: ", "").strip().ljust(3)
            elif(cnt == 11):
                status_change = line.strip().ljust(15)

            line = fp.readline() 
            cnt += 1

