import unittest
from typewise_alert import *
call_print = PrintingStatement()
batteryChar = {'coolingType':'PASSIVE_COOLING'}
class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(infer_breach(20, 50, 100) == 'TOO_LOW')
  def test_controller_msg(self):  
    
    self.assertTrue(check_and_alert('TO_CONTROLLER',batteryChar,34)=='NORMAL' )
    # Check if the mocked values were set correctly
    self.assertEqual(call_print.Mock_breachType, 'NORMAL')
    self.assertEqual(call_print.Mock_header, 0xfeed)
    
  def test_email_msg(self):
    self.assertTrue(check_and_alert('TO_EMAIL',batteryChar,34)=='NORMAL')
    # Check if the mocked values were set correctly
    self.assertEqual(call_print.Mock_breachType, 'NORMAL')
    self.assertEqual(call_print.Mock_recepient, "a.b@c.com")
    
if __name__ == '__main__':
  
  unittest.main()
