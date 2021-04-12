s=input() b = s.count ("B") s=s.replace("B", "")+" " s=s+" " n="L" while
True:
    if n=="L":
        if s.startswith("LL"):
            b+=1
            n="R"
            s=s[2:]
 
        elif s.startswith("LR"):
            b+=1
            s=s[1:]
 
        elif s.startswith("R"):
            s=s[1:]
 
        elif s.startswith("L ") or s.startswith(" "):
            b+=1
            break
       
    if n=="R":
        if s.startswith("RR"):
            b+=1
            n="L"
            s=s[2:]
 
        elif s.startswith("RL") or s.startswith("R"):
            b+=1
            s=s[1:]
 
        elif s.startswith("L"):
            s=s[1:]
 
        elif s.startswith("R ") or s.startswith(" "):
            break
 
print (b)
