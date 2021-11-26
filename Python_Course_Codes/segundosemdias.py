totalseg = input("Por favor, entre com o número de segundos que deseja converter: ")
totalintseg = int(totalseg)

dias = (totalintseg // 86400)
horas = ((totalintseg % 86400) // 3600)
minutos = (((totalintseg % 86400) % 3600) // 60)
segrestantes = ((((totalintseg % 86400) % 3600) % 60))

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segrestantes,"segundos.")