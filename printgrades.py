from underline import underline
def print_grades(grades, average):
    moyenneG = 0
    coefG = 0
    for matiere in grades:
        print('\n' + underline(grades[matiere]['name'] + ':'))
        for i in grades[matiere]['notes']:
            if i:
                print(i + ': ' + str(grades[matiere]['notes'][i]))
        try:
            moyenneG += average[matiere]
            coefG += 1
            print(f'\nMoyenne = {average[matiere]:.2f}/20\n')
        except:
            print('\n')
    if coefG != 0:
        toPrint = f'Moyenne générale : {moyenneG/coefG:.2f}/20'
        print(underline(toPrint))