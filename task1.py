IPneeded = "10.1.192.38"
sids = []

logfile = open("log.txt", "r")
logs = logfile.read().split('\n')

for log in logs:
    if log != '':
        userIP = log.split()[0]
        query = log.split()[6]
        sid = query.split('sid=/')[1].split('/&type')[0]
        if userIP == IPneeded:
            sids.append(sid)

result = sorted(sids)

for sid in result: print(sid)
