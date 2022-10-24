def zapis(contact: str):
    path = 'DZ\\dz8\\spravochnik.csv'
    f = open(path, 'a')
    f.write(f'{contact}\n')