from flask import Flask, jsonify, request, Response
from google.cloud.logging import DESCENDING
from src.lib.gcl_config import gcl_client
from src.lib.response import ApiResponse


app = Flask(__name__)

@app.route('/', methods=["GET"])
def write_log():
    return ApiResponse().success("you are in write-log.", 200)

@app.route('/test', methods=['GET'])
def test():
    print("you are in test.")
    return ApiResponse().success("You are calling test.", 200)


@app.route('/write_logs', methods=['POST'])
def write_logs():
    try:
        log_type = request.args.get('log-type', '')
        try:
            rbody = request.json
        except Exception as e:
            return ApiResponse().error("Invalid JSON format", 400)
            
        logger_name = rbody['logger']
        logging_client, logger = gcl_client(logger_name)
        if log_type == 'user':
            # print("\n" + log_type * 3)
            # print(logging_client, logger)
            # print("\n" + log_type * 3)
            logger.log_struct(rbody)
        elif log_type == 'application':
            print(logging_client, logger)
            # print("\n" + log_type * 3)
            logger.log_struct(rbody)
        else:
            return ApiResponse().error("Please provide valid log-type.", 404)
            
        return ApiResponse().success("log inserted successfully.", 200)       
    except Exception as err:
        return ApiResponse().error("Somthing went wrong.", 404)
    
@app.route('/get_logs', methods=['POST', 'GET'])
def get_logs():
    try:
        rbody = request.json
    except Exception as e:
        ApiResponse().error("Invalid JSON format", 400)
    logger_name = rbody.get('logger', '')
    if not logger_name:
        return ApiResponse().error("Please provide logger name.", 400)
    logger_name = rbody['logger']
    logging_client, logger = gcl_client(logger_name)
    # FILTER = 'timestamp > "2022-06-01T01:00:00Z" timestamp < "2022-07-30T22:00:00Z"'
    # print("\nF111: ", FILTER)
    
    from_date, to_date = rbody["from_date"], rbody["to_date"]
    print(from_date, to_date)
    
    if from_date == "":
        return ApiResponse().error("Please provide start data.", 404)
    
    if to_date == "":
        return ApiResponse().error("Please provide end data.", 404)
        
    FILTER1 = 'timestamp > "{}" timestamp < "{}"'.format(from_date, to_date)
    print("F222: ", FILTER1)
    logs = []
    # ent = logger.list_entries(order_by=DESCENDING, filter_=FILTER1)
    # print("eeee: ", ent)
    # ll = []
    # for ee in ent:
    #     print(ee.payload)
    #     if type(ee.payload) != dict:
    #         continue
    #     ll.append(ee.payload)
    # print(ll)
    # print(len(ll))

    try:
        entries = logging_client.list_entries(order_by=DESCENDING, filter_=FILTER1)
        for ind, entry in enumerate(entries):
            if type(entry.payload) != dict:
                continue
            # print("{0}: , {1}\n".format(ind, entry.payload))
            logs.append(entry.payload)
        return ApiResponse().paginationSuccess(logs, 200, len(logs))
    except Exception as err:
        print("get_logs: ", err)
        return ApiResponse().error("Something went wrong.", 404)



@app.route('/delete-gcplogs', methods=['GET', 'POST'])
def delete_googglecloudlogs():
    try:
        rbody = request.json
    except Exception as e:
        ApiResponse().error("Invalid JSON format", 400)

    logger_name = rbody['logger']
    logging_client, logger = gcl_client(logger_name)
    logger.delete()
    return {'logger': 'HW_testing', 'status': 'success', 'message': 'logs deleted successfully.'}