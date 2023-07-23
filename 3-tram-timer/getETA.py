def extract(json_result: str) -> int:
    """
    This function will extract the ETA value from the JSON
    result body returned from the server. This function
    attempts to do this without using the JSON package for
    Python as the task can be acconmplished by simple string
    processing due to the predictable nature of the result.

    Parameters:
        json_result:
            This is a string type object that contains the
            ETA value for the next tram.
    """

    # Find the location of the keyword eta
    eta_loc = json_result.find("eta")

    # Add the predictable number of characters to skip to
    # get the location of the eta value
    eta_num_start = eta_loc + 7

    rest_string = json_result[eta_num_start:]

    # Extract the value until the comma appears, this is
    # where the eta value will end
    result = int(rest_string.split(",")[0])

    return result