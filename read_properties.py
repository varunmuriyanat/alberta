with open("property_search4.md", "w") as fw:
    with open("property_search4.txt", "r") as fp:
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

        fw.write("|Price".ljust(9))
        fw.write("|B".ljust(1))
        fw.write("|Bat".ljust(3))
        fw.write("|Postal".ljust(8))
        fw.write("|FlrA".ljust(9))
        fw.write("|Address".ljust(36))
        fw.write("|Day".ljust(4))
        fw.write("|Residential".ljust(61))
        fw.write("|mls".ljust(9))
        fw.write("|Description".ljust(1021))
        fw.write("|")
        fw.write("\n")

        while line:
            if(cnt > 10):
                cnt = cnt - 10

                # include only postal codes starting with T6
                if(postal.startswith("T6")):
                    fw.write("|")
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
                address = address.replace(", Edmonton, AB", "")
                address = address.ljust(35)
            elif(cnt == 2):
                postal= line.strip() 
                postal = postal.replace("Postal Code: ", "")
            elif(cnt == 3):
                mls = line.strip()
            elif(cnt == 4):
                residential = line.strip()
                residential = residential.ljust(60)
            elif(cnt == 5):
                price = line.strip()
                price = price.replace("Price: ", "")
            elif(cnt == 6):
                description = line.strip()
                description = description.ljust(1020)
            elif(cnt == 7):
                beds = line.strip()
                beds = beds.replace("BEDS: ", "")
            elif(cnt == 8):
                baths = line.strip()
                baths = baths.replace("BATHS: ", "")
            elif(cnt == 9):
                flrArea = line.strip()
                flrArea = flrArea.replace("FlrArea SF : ", "").strip()
            elif(cnt == 10):
                daysOnMarket = line.strip()
                daysOnMarket = daysOnMarket.replace("Days on Market: ", "").strip()
                daysOnMarket = daysOnMarket.ljust(3)

            line = fp.readline()

            cnt += 1

