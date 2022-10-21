
from datetime import datetime

def logger_file(result: str):
    path = 'log.cvs'
    time_sign = datetime.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign}--> {result}\n')