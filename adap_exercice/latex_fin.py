import os.path
from sympy import Rational
from .latex_q1 import question_1
from .latex_q2 import question_2
from .latex_q3 import question_3
from .latex_q4 import question_4
from .latex_q5 import question_5
from .latex_q6 import question_6

def preambule(*packages):
    p = ""
    for i in packages:
        p = p +"\\usepackage{"+i+"}\n"
    return p


def document(h: int = 4, l: int = 2, gh: Rational = Rational(1,4), gl: Rational = Rational(1,2)):
    start = "\\documentclass[11pt,a4paper,french]{article}\n\\usepackage[utf8]{inputenc}\n"
    start = start + preambule('amsmath','lmodern','babel', 'graphicx') + "\n\\graphicspath{{resolution_modele/resolution_modele/}}\n" +"\\usepackage[T1]{fontenc}\n\\usepackage[super]{nth}\n\\title{\\textbf{Exercice adaptatif}}\n\\author{VERON \\& NEPVEUX}\n"
    start = start + "\\usepackage{geometry}\n\\geometry{a4paper, total={210mm,297mm}, left=25mm, right=25mm, bottom=20mm, top=20mm}\n"
    start = start+"\\begin{document}\n\\maketitle\n"
    end = "\n\\end{document}"
    body = ""

    body = question_1(h, l, gh, gl) + question_2(h, l, gh, gl) +question_3(h, l, gh, gl)+question_4(h, l, gh, gl)+question_5(h, l, gh, gl)+question_6(h, l, gh, gl)

    container = start+body+end

    file = "exercice.tex"

    if os.path.exists(file):
        os.remove(file)

    with open("exercice.tex","x") as fichier: # "x" pour la création et l'écriture
        fichier.write(container)
    
    instructions = "pdflatex "+file
    os.system(instructions)
    readpdf = "START "+file[:-4]+".pdf"
    os.system(readpdf)