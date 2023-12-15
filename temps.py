from datetime import date
FORMAT_FR_DATE = '%d/%m/%Y'
d = date.today()
# wrong call
print(f"date = {d:FORMAT_FR_DATE}")
# good calls
print(f"date = {d:{FORMAT_FR_DATE}}")
print(f"date = {{:{FORMAT_FR_DATE}}}".format(d))
print("date = {{:{}}}".format(FORMAT_FR_DATE).format(d))