def abbrevName(name):
    #code away!
    h=''
    l=name.split()
    for i in l:
        i.capitalize()
        h+=(i[0]+'.')
    h=h.strip(".")
    h=h.upper()
    print(h)
name=input()
abbrevName(name)
