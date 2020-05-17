d={"G":"C","C":"G","T":"A","A":"U"}
n=input()
for i in range(len(n)):
  if "X" in n:
    print("Invalid Input")
    break
  elif "G"in n  or"C"in n or"T"in n or"A"in n:
    if n[i] in d:
      print(d[n[i]],end="")
