def is_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False

"""Pentru inceput verificam cazul de baza respectiv daca cuvantul nostru are mai mult de o litera
Apoi verificam daca prima litera din cuvand == cu ultima litera din cuvant si daca aceasta conditie este True
Apelam recursiv literele din cuvant exceptand prima si ultima litera. Repetam recursiv acest proces pana cand cazul de baza == True
"""
print(is_palindrome("radar"))