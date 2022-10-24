
from datetime import datetime

def logger_file(result: str):
    path = 'DZ\\dz7_v2\\calk2\\log.csv'
    time_sign = datetime.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign}--> {result}\n')