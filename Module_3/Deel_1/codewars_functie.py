def solution(text: str, last_letters: str) -> bool:
    last_letters = text
    if text == last_letters:
        return True
    else:
        return False

print(solution('Felicia', 'ja'))  