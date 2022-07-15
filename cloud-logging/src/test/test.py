import json
import unittest
import requests
from request_data import TEST_URL, WRITE_LOG_URL
from request_data import application_logs, expected_log_resp


class TestApi(unittest.TestCase):
    
    def test_1_test(self):
        resp = requests.get(TEST_URL)
        self.assertEqual(resp.status_code, 200)
        print("Test 1 is completed.")
    
    def test_2_write_logs(self):
        params={'log-type': 'application'}
        resp = requests.post(WRITE_LOG_URL, params=params, json=application_logs)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["data"]["responseCode"], 
                         expected_log_resp["data"]["responseCode"])
        print("Test 2 write logs is completed.")
        
        
if __name__ == "__main__":
    tester = TestApi()
    tester.test_1_test()
    tester.test_2_write_logs()