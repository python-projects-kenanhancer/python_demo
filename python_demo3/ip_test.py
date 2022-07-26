import unittest
from ipAddress import getIpAddressWithIpinfo, getIpAddressWithHttpbin

class TestIpAddress(unittest.TestCase):
    
    def test_ipInfo(self):
        self.assertEqual(getIpAddressWithIpinfo(), '152.37.86.31', '')
        
    def test_httpBin(self):
        self.assertEqual(getIpAddressWithHttpbin(), '152.37.86.31', '')

if __name__ == '__main__':
    unittest.main()