#!/usr/bin/python3
"""
Convert text to sentences
"""


def text_indentation(text):
    """
    text_indentation: converts a text into sentneces
    """
    if isinstance(text, str):
        check = 0
        for i in text:
            if i in ['.', '?', ':']:
                print(i,'\n', sep='')
                check = 0
            else:
                if i == ' ' and check == 0:
                    continue
                print(i, sep='', end='')
                check = 1
    else:
        raise TypeError("text must be a string")


if __name__ == "__main__":
    #import doctest
    #doctest.testfile("tests/5-text_indentation.txt")
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere?\
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud:\
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere.\
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum\
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo\
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum\
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio\
    beatiorem! Iam ruinas videres""")
