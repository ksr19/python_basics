type_list = [1, 2.0, "str", True, None, [1, 3, 9], (1, 2), {400, True, None}, {1: 17, "key": 6.0, False: "some"},
             b'text', bytearray(b'some text')]
for element in type_list:
    print(f"Элемент списка {element} принадлежит типу {type(element)}.")
