import json
def validate_response(json_string):
    try:
        data = json.loads(json_string)
        req_keys = {"status","data","message"}
        return req_keys.issubset(data)
    except json.JSONDecodeError:
        return False
response = '{"status": 200, "data": {"user": "Alex"}, "message": "Success"}'
print(validate_response(response))