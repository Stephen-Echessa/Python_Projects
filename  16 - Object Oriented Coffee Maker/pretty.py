from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City name",["Nairobi","Nakuru","Kisumu","Mombasa","Eldoret","Thika"])
table.add_column("Population",[100,35,76,90,48,20])
print(table)