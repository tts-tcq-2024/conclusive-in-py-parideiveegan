import unittest
import typewise_alert

batteryChar = {'coolingType':'PASSIVE_COOLING'}
class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
  def test_controller_msg(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',batteryChar,34)=='NORMAL' && Mock_breachType == 'NORMAL')
  def test_email_msg(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',batteryChar,34)=='NORMAL' && Mock_breachType == 'NORMAL')
if __name__ == '__main__':
  unittest.main()
