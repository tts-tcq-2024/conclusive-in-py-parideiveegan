class PrintingStatement:
  Mock_breachtype = ''
  def printStatement_to_controller(self,breachtype):
    header = 0xfeed
    print(f'{header}, {breachType}')
  def printStatement_to_email(self, breachtype):
    recepient = "a.b@c.com"
    if breachType == 'TOO_LOW':
      print(f'To: {recepient}')
      print('Hi, the temperature is too low')
    elif breachType == 'TOO_HIGH':
      print(f'To: {recepient}')
      print('Hi, the temperature is too high')
  def MockprintStatement_to_controller(self, breachtype):
    Mock_brechtype = breachtype
  def printStatement_to_email(self, breachtype):
    Mock_brechtype = breachtype
