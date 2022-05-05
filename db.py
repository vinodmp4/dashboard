
import csv

DEFAULT_SETTINGS = """[APPLICATION]
DATABASE=db.csv

[THEME]
BACKGROUND='#BADDAD'
"""


def loadsettings():
    DATA = {}
    SETTINGS = './config'
    try:
        config_file = open(SETTINGS,'r')
    except FileNotFoundError as e:
        config_file = open(SETTINGS,'w')
        config_file.write(DEFAULT_SETTINGS)
        config_file.close()
        config_file = open(SETTINGS,'r')
    appsection = False;appdata = {}
    themesection = False;themedata = {}
    for line in config_file:
        if '[APPLICATION]' in line.upper():
            appsection = True
            themesection = False
        elif '[THEME]' in line.upper():
            appsection = False
            themesection = True
        else:
            if (line.rstrip()==''):pass
            elif appsection:
                d = line.rstrip().split(sep='=')
                appdata[d[0]]=d[1]
            elif themesection:
                d = line.rstrip().split(sep='=')
                themedata[d[0]]=d[1]
            else:pass
    DATA['APPLICATION'] = appdata
    DATA['THEME'] = themedata
    config_file.close()
    return DATA
        

class reader:
    def __init__(self):
        databasefile = loadsettings()['APPLICATION']['DATABASE']
        data = {'ENQUIRY':0,
                'HOURS':0}
        if not(databasefile.startswith('http')):
            try:
                with open(databasefile,'r') as csvfile:
                    dbdata = csv.reader(csvfile)
                    for row in dbdata:
                        print(row)
                        if row[0].lower() == 'enquiry':data['ENQUIRY'] = int(row[1])
                        else:pass
            except FileNotFoundError as e:
                pass
        else:
            pass
        print(data)

class writer:
    def __init__(self):
        pass

data = loadsettings()
print(data)

x = reader()
