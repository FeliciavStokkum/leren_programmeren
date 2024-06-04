import functions_name_age

lijst = functions_name_age.questions()
for dict in lijst:
    print(f"{dict['name']}, die in {dict['city']} woont, is {dict['age']} jaar")