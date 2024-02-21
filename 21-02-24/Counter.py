# ************************************************
# klasa: 3E
# opis: klasa liczy liczbę samogłosek w tekście i usuwa powtorzenia
# metody:
#            count - zwraca liczbę samogłosek w tekście
#            remove_repeated - zwraca tekst bez powtórzeń
#   autor:  Łukasz Stępień
# ************************************************
class Counter:
    numb = 0
    letters = "aąeęiouóyAĄEĘIOUÓY"

    @staticmethod
    def count(text):
        for char in text:
            if char in Counter.letters:
                Counter.numb += 1
        if Counter.numb == 0:
            return 0
        else:
            return Counter.numb

    @staticmethod
    def remove_repeated(text):
        new_text = ""
        for char in text:
            if char not in new_text:
                new_text += char
        return new_text
