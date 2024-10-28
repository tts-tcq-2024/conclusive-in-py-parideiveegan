from PrintingStatements import *
call_print = PrintingStatement()
CoolingTypeLimits = {'PASSIVE_COOLING':[0,35], 'HI_ACTIVE_COOLING':[0,45], 'MED_ACTIVE_COOLING':[0,40] } 

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  Limits = CoolingTypeLimits[coolingType]
  lowerLimit = Limits[0] 
  upperLimit = Limits[1]
  return infer_breach(temperatureInC, lowerLimit, upperLimit)


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)
  return breachType

def send_to_controller(breachType):
  header = 0xfeed
  if __name__ != "__main__":
    call_print.MockprintStatement_to_controller(header,breachType)
  else:
    call_print.printStatement_to_controller(header,breachTtype)

def send_to_email(breachType):
  recepient = "a.b@c.com"
  if __name__ != "__main__":
    call_print.MockprintStatement_to_email(recepient,breachType)
  else:
    call_print.printStatement_to_email(recepient, breachType)

print (check_and_alert('TO_CONTROLLER',batteryChar,34))
print (Mock_breachType)
