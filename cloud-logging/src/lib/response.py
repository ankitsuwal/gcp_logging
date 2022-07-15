from flask import jsonify

class ApiResponse:
    def success(self, response, code, token=None):
        msg = response if isinstance(response, str) else "Successfully"
        result = [] if isinstance(response, str) else response
        res = {
            "data": {
                "message": msg,
                "responseCode": code,
                "result": result,
            }
        }
        return jsonify(res)

    def paginationSuccess(self, response, code, count):
        res = {
            "data": {
                "message": "Successfully",
                "responseCode": code,
                "result": response,
                "total_records": count
            }
        }

        return jsonify(res)

    def error(self, response, code):
        return jsonify({
            "data": {
                "message": "error",
                "responseCode": code,
                "error": response
            }
        })









# {'data': {'message': 'Successfully', 'responseCode': 200, 
#           'result': [{'SystemID': 'GTDCLNT9010', 'Type': 'Avyay', 'Timestamp': 
#               '2022-06-08, 15:58:14', 'RequestID': '3f1dcb34', 'UserID': 
#                   'TBHUVANA-05', 'TZ': 'CST', 'ModelID': '3M_PH_HTS_2021_V1', 'ProductID': 'GTS-25-04'}, 
#                      {'Text': 'Test comment.', 'logger': 'test_logs', 'Request': 'POST', 
#                       'URL': 'https://gcloud.readthedocs.io/en/latest/logging-usage.html'}, 
#                      {'Request': 'POST', 'URL': 'https://gcloud.readthedocs.io/en/latest/logging-usage.html', 'logger': 'test_logs', 
#                       'Text': 'Test comment.'}, 
#                      {'TZ': 'CST', 'ModelID': '3M_PH_HTS_2021_V1', 'Type': 'Avyay', 'SystemID': 'GTDCLNT9010', 'ProductID': 'GTS-25-04',
#                       'UserID': 'TBHUVANA-04', 'Timestamp': '2022-06-07, 16:43:14', 'RequestID': '3f1dcb34'}, 
#                      {'Timestamp': '2022-06-07, 16:43:14', 'SystemID': 'GTDCLNT9010', 'TZ': 'CST', 'ModelID': '3M_PH_HTS_2021_V1', 
#                       'RequestID': '3f1dcb34', 'Type': 'Avyay', 'ProductID': 'GTS-25-04', 'UserID': 'TBHUVANA-03'}, 
#                      {'SystemID': 'GTDCLNT9010', 'TZ': 'CST', 'UserID': 'TBHUVANA-02', 'Type': 'Avyay', 'RequestID': '3f1dcb34', 
#                       'ModelID': '3M_PH_HTS_2021_V1', 'Timestamp': '2022-06-07, 16:43:14', 'ProductID': 'GTS-25-04'},
#                      {'Timestamp': '2022-06-07, 16:43:14', 'Type': 'Avyay', 'ProductID': 'GTS-25-04', 'SystemID': 'GTDCLNT9010',
#                       'ModelID': '3M_PH_HTS_2021_V1', 'TZ': 'CST', 'UserID': 'TBHUVANA-01', 'RequestID': '3f1dcb34'}, 
#                      {'logger': 'test_logs', 'URL': 'https://gcloud.readthedocs.io/en/latest/logging-usage.html', 'Text': 'Test comment.', 
#                       'Request': 'POST'}]}}