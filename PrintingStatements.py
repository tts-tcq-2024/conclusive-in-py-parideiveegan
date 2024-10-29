Mock_breachType = ''
Mock_header = ''
Mock_recepient = ''
class PrintingStatement():
  def printStatement_to_controller(self, header,breachType):
    header = 0xfeed
    print(f'{header}, {breachType}')
  def printStatement_to_email(self, recepient, breachType):
    recepient = "a.b@c.com"
    if breachType == 'TOO_LOW':
      print(f'To: {recepient}')
      print('Hi, the temperature is too low')
    elif breachType == 'TOO_HIGH':
      print(f'To: {recepient}')
      print('Hi, the temperature is too high')
  def MockprintStatement_to_controller(self, header,breachType):
    Mock_breachType = breachType
    Mock_header = header
    print(f'{header}, {breachType}')
  def MockprintStatement_to_email(self, recepient,breachType):
    print(breachType)
    Mock_breachType = breachType
    Mock_recepient = recepient
