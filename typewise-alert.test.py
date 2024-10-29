import unittest
from typewise_alert import *

batteryChar = {'coolingType':'PASSIVE_COOLING'}
class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(infer_breach(20, 50, 100) == 'TOO_LOW')
  def test_controller_msg(self):
    print(check_and_alert('TO_CONTROLLER',batteryChar,34))
    print(Mock_breachType)
    self.assertTrue(check_and_alert('TO_CONTROLLER',batteryChar,34)=='NORMAL' )
    self.assertTrue(Mock_breachType == 'NORMAL')
  def test_email_msg(self):
    self.assertTrue(check_and_alert('TO_EMAIL',batteryChar,34)=='NORMAL')
    self.assertTrue (Mock_breachType == 'NORMAL')
if __name__ == '__main__':
  print(Mock_breachType,"test")
  unittest.main()
