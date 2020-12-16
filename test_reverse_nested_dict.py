def test_reverse_nested_dict():
    from reverse_nested_dict import reverse_nested_dict
    assert reverse_nested_dict(input_dict={'hired': {'be': {'to': {'deserve': 'I'}}}}) == {
        'I': {'deserve': {'to': {'be': 'hired'}}}}
    assert reverse_nested_dict(input_dict={"a": "b"}) == {"b": "a"}
    assert reverse_nested_dict(input_dict={"a": {"b": "c"}}) == {'c': {'b': 'a'}}