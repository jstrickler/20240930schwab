from datetime import date

def mkdate(raw_date):
    if raw_date != "NONE":
        raw_year, raw_month, raw_day = raw_date.split('-')
        d = date(int(raw_year), int(raw_month), int(raw_day))
    else:
        d = None

    return d

def get_info(index):
    pres_data = {}
    with open("../DATA/presidents.txt") as pres_in:
        for line in pres_in:
            flds = line[:-1].split(":")
            if int(flds[0]) == index:
                pres_data["lastname"] = flds[1]
                pres_data["firstname"] = flds[2]

                pres_data["birthdate"] = mkdate(flds[3])
                pres_data["deathdate"] = mkdate(flds[4])

                pres_data["birthplace"] = flds[5]
                pres_data["birthstate"] = flds[6]

                pres_data["termstart"] = mkdate(flds[7])
                pres_data["termend"] = mkdate(flds[8])

                pres_data["party"] = flds[9]

                break
        else:
            raise ValueError("Term not found")

    return pres_data

def get_all_data():
    all_data = []
    for i in range(1, 47):
        all_data.append(get_info(i))
    return all_data

if __name__ == "__main__":
    print(get_all_data()[-1])
    # i = 1
    # while True:
    #     try:
    #         p = get_info(i)
    #     except ValueError as err:
    #         curr_term = i - 1
    #         pres = get_info(curr_term)
    #         print("Current president:")
    #         print(pres)
    #         break
    #     i += 1