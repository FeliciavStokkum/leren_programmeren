# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

# The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

# If the score < 0, return 0.

arr1 = ["a", "a", "b", "b"]
arr2 = ["a", "c", "b", "d"]


def check_exam(arr1,arr2):
    score = 0

    controle = zip(arr1, arr2)
    controle = tuple(controle)
    # print(controle[0])
    # print(controle[0][0])
    # print(controle[0][1])

    for index in range(len(controle)):
        if controle[index][0] == controle[index][1]:
            score += 4 
        elif controle == '':
            score += 0
        else:
            score -= 1
        


    return score

print(check_exam(arr1, arr2))