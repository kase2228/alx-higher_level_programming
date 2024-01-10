def best_score(a_dictionary):
    max_score = None
    max_key = None

    for key in a_dictionary:
        if a_dictionary[key] > int(max_score):
            max_score = a_dictionary[key]
            max_key = key

    if max_key:
        return max_key
    else:
        return None
