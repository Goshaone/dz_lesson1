list_for_home_work = []
for number in range(1, 1001, 2):
    list_for_home_work.append(number ** 3)
final_answer = 0
for number in list_for_home_work:
    number += 17
    check_sum = 0
    for check_number in str(number):
        check_sum += int(check_number)
    if check_sum % 7 == 0:
        final_answer += number
print(final_answer)
