import datetime
user_bd = input("ВВедіть вашу дату народження")
bd_date = datetime.datetime.strptime(user_bd, "%Y-%m-%d")
now = datetime.date.today()
lived = (now - bd_date.date()).days
print(lived)