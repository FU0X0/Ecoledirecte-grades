from underline import underline
from average import Avg
def print_grades(grades, average):
    moyenneG = Avg()
    for matiere in grades:
        print('\n' + underline(grades[matiere]['name'] + ':'))
        for i in grades[matiere]['notes']:
            if i:
                print(f'{i}: {grades[matiere]['notes'][i]}')
        try:
            moyenneG.add(average[matiere], 20)
            print(f'\n{underline('Moyenne', f' = {average[matiere]:.2f}/20')}\n')
        except:
            print('\n')
    if moyenneG.get():
        print(f'\n{underline(f'Moyenne générale : {moyenneG.get():.2f}/20')}')