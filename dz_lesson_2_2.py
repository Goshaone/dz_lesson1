my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

new_list = []
for idx, elements in enumerate(my_list):
    if elements.isdigit():
        new_list.extend(['"', f'{int(elements):02}', '"'])
    elif (elements.startswith('+') or elements.startswith('-')) and elements[1:].isdigit():
        new_list.extend(['"', f'{elements[0]}{int(elements):02}', '"'])
    else:
        new_list.append(elements)

out_info = ' '.join(new_list)
print(out_info)
