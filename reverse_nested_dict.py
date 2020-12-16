def reverse_nested_dict(input_dict):
    output_dict = None
    while True:
        key_, value_ = input_dict.popitem()
        output_dict = key_ if output_dict is None else {key_: output_dict}
        if not isinstance(value_, dict):
            return {value_: output_dict}
        else:
            input_dict = value_