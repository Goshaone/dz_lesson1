
def thesaurus(*names):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))