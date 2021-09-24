with open("property_search6.csv", "w") as fw:
    with open("collaboration_center_2021_09_23.txt", "r") as fp:
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

        fw.write("Status")
        fw.write("|Price")
        fw.write("|B")
        fw.write("|Bat")
        fw.write("|Postal")
        fw.write("|FlrA")
        fw.write("|Address")
        fw.write("|Day")
        fw.write("|Residential")
        fw.write("|mls")
        fw.write("|Description")
        fw.write("\n")

        while line:
            if(cnt > 12):
                cnt = cnt - 12

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
                address = address
            elif(cnt == 2):
                address = address + ", " + line.strip()     
            elif(cnt == 3):
                postal= line.strip().replace("Postal Code: ", "").strip()
            elif(cnt == 4):
                mls = line.strip()
            elif(cnt == 5):
                residential = line.strip()
            elif(cnt == 6):
                price = line.strip().replace("Price: ", "").strip()
            elif(cnt == 7):
                description = line.strip()
            elif(cnt == 8):
                beds = line.strip().replace("BEDS: ", "").strip()
            elif(cnt == 9):
                baths = line.strip().replace("BATHS: ", "").strip()
            elif(cnt == 10):
                flrArea = line.strip().replace("FlrArea SF : ", "").strip()
            elif(cnt == 11):
                daysOnMarket = line.strip().replace("Days on Market: ", "").strip()
            elif(cnt == 12):
                status_change = line.replace("Status: ","").strip()

            line = fp.readline() 
            cnt += 1

