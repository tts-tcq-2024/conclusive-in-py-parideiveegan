Mock_breachtype = ''
Mock_header = ''
Mock_recepient = ''
class PrintingStatement:
  def printStatement_to_controller(self, header,breachtype):
    header = 0xfeed
    print(f'{header}, {breachType}')
  def printStatement_to_email(self, recepient, breachtype):
    recepient = "a.b@c.com"
    if breachType == 'TOO_LOW':
      print(f'To: {recepient}')
      print('Hi, the temperature is too low')
    elif breachType == 'TOO_HIGH':
      print(f'To: {recepient}')
      print('Hi, the temperature is too high')
  def MockprintStatement_to_controller(self, header,breachtype):
    Mock_brechtype = breachtype
    Mock_header = header
  def MockprintStatement_to_email(self, recepient,breachtype):
    Mock_brechtype = breachtype
    Mock_recepient = recepient
