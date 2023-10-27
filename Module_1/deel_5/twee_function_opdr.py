from test_lib import test,report

# def get_value(data: str, separator: str, position: int) -> str:
#     # toets_data has name:score combinations separated by a komma
#     splitted_strings = data.split(separator) # string splits itself into collection of strings
#     if 0 <= position< len(splitted_strings):
#         value = splitted_strings[position] # read value at position of split_values
#     else:
#         value = None
    
#     return value # prints: Bram:6
# data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
# separator = ','
# position= 1

# print(get_value(data, separator, position))

# expected_content = 'Emma:7'
# calculated_content = get_value(data, separator, position)
# name = f'test toets data: {data} separator: {separator}, position{position}'
# test(name, expected_content, calculated_content)
     
# report()

import re

# replace alle separators "." , ",", " en ", "omdat ", "zodat ", "want ", " wanneer " en "dat ”by a marker "|"
def sub_sentences(text):
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|") # split de text on marker "|"
    return sub_sentences

def ego(sub_sentences):

    ego_score = 0
    for sentence in sub_sentences: # repeat for every sentence in a list sentences
        sentence = sentence.strip() # remove leading and trailing spaces
        sentence = sentence.lower() # convert uppercase characters to lowercase
        if len(sentence) > 0:
            words = sentence.split(' ') # split sentence into words
    # first words of sentence equal to ik?
        if len(words) >= 2 and (words[0] in ('ik','mijn') or words[1] in ('ik','mijn')):
            ego_score += 1

    return ego_score

text = """ 
“Geachte heer/mevrouw,
Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team.
Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie.”
"""

expected_content = 16
calculated_content = ego(sub_sentences(text))
name = f''
test(name, expected_content, calculated_content)

report()