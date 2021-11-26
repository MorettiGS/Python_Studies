totalseg = input("Digite o número de segundos que deseja converter: ")
totalintseg = int(totalseg)

anos = (totalintseg // 31536000)
dias = ((totalintseg % 31536000) // 86400)
horas = (((totalintseg % 31536000) % 86400) // 3600)
minutos = ((((totalintseg % 31536000) % 86400) % 3600) // 60)
segrestantes = int(((((totalintseg % 31536000) % 86400) % 3600) % 60))

print(anos, "anos, ", dias, "dias, ", horas, "horas, ", minutos, "minutos e", segrestantes, "segundos estão contidos nisto. :)") 