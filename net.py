import subprocess
def NetLP():
    m = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    d = m.decode('utf-8', errors="backslashreplace")
    d = d.split('\n')
    p = []
    for i in d:
        if 'All User Profiles' in i:
            i = i.split(":")
            i = i[1]
            i = i[1:-1]
            p.append(i)
    o = "{:<30}| {:<}".format('Wi-Fi Name', "Password") + " \n ----------------------------------------------\n"
    for i in p:
        try:
            r = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
            r = r.decode('utf-8', errors="backslashreplace")
            r = r.split('\n')
            r = [b.split(":")[1][1:-1] for b in r if "Key Content" in b]
            try:
                o += "{:<30}| {:<}\n".format(i, r[0])
            except IndexError:
                o += "{:<30}| {:<}\n".format(i, "")
        except subprocess.CalledProcessError:
            o += "Encoding error occurred\n"
    return o

