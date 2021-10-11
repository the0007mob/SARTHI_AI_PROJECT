def transform_response(status_code, status, data, message):
    """
    Response for API calls.
    :param status_code:
    :param status:
    :param data:
    :param message:
    :return: response
    """
    response = {
        "status": status,
        "status_code": status_code,
        "data": data
    }
    if message:
        response["message"] = message
    return response
