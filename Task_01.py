# names = [] names of student
# markes =[] student markes


def list_to_dic(names, markes):
    return dict(zip(names, markes))


print(list_to_dic(['AdamSmith', 'John Doe'], [4.5, 3.5]))
