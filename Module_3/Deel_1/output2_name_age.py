import functions_name_age

lijst = functions_name_age.questions()
for dict in lijst:
    print(f"In {dict['city']} woont de {dict['age']} jarige {dict['name']}")