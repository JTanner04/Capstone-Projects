print("Welcome to the tip calculator!")

bill_total = float(input("How much was the bill: $ "))

tip_percent = int(input("What percentage of tip would you like to give? 10, 12, or 15: "))

split = int(input("How many people will split the bill? "))

conve_tip = (float(tip_percent) / 100)
convert_tip = float(bill_total * conve_tip)
converte_tip = float(bill_total + convert_tip)
converted_tip = (float(converte_tip / split))

print("%.2f" % converted_tip)