TEST_URL = "http://172.19.0.2:5000/test"
WRITE_LOG_URL = "http://172.19.0.2:5000/write_logs"


application_logs = {
    "logger": "test_logs",
    "ModelID": "3M_PH_HTS_2021_V1",
    "ProductID": "GTS-25-04",
    "RequestID": "3f1dcb34",
    "SystemID": "GTDCLNT9010",
    "TZ": "CST",
    "Timestamp": "2022-07-04, 15:20:14",
    "Type": "Avyay",
    "UserID": "TBHUVANA-04-07"
}

expected_log_resp = {
    "data": {
        "message": "log inserted successfully.",
        "responseCode": 200,
        "result": []
    }
}