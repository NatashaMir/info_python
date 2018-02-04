class Character:
    def __init__(self, char):
        self.char = char

def create_list_from_string(str):
    list = []
    for s in str:
        for character in list:
            if s == character.char:
                list.append(character)
                break
        else:
            list.append(Character(s))
    return list


list = create_list_from_string('asdfgsd')
