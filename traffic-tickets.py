def readData():
  f = open("traffic-tickets.txt", "r")
  data = f.readlines()
  return data

def getFine(totalSpeed):
  if totalSpeed >= 1 and totalSpeed < 5:
    fine = 65

  elif totalSpeed < 10: 
    fine = 85

  elif totalSpeed < 15:
    fine = 120

  elif totalSpeed < 25:
    fine = 150

  else:
     fine = 200   

  return (fine)  

def main():
   rates = []
  

   dataList = readData()
   print("Name      MPH over  Fine")
   for record in dataList:
     name, speed, speedLimit = record.split()

     totalSpeed = int(speed) - int(speedLimit)

     fine = getFine(totalSpeed)

     rates.append(rate)

     print("%-9s  %4d  %6d" % (name, totalSpeed, fine))

main()

