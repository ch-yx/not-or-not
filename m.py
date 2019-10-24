def and2non(c1):
    assert c1["condition"]=="and"
    terms=c1["terms"]
    c1.clear()
    c1.update(inv(alt(inv(i) for i in terms)))

def inv(c1):
    return {"condition":"inverted","term":c1}

def alt(c1):
    return {"condition":"alternative","terms":list(c1)}


def se(c1):
    marker=[c1]
    if c1["condition"]in["and","alternative"]:
        for i in c1["terms"]:
            marker.extend(se(i)) 
    elif c1["condition"]=="inverted":
        marker.extend(se(c1["term"]))
    #else atom
    return marker

def modif(c1):
    
    for i in (se(c1)):
        if i["condition"]=="and":
            and2non(i)


import json
from pathlib import Path
filelist=[*Path("").rglob("*.json")]
print("发现了一些json文件\n"+"\n".join(map(str,filelist))+"\n==========")
for x in filelist:
    print(f"尝试读取{x}...",end="")
    try:        
        with x.open("r") as file:
                jsonobj=(json.load(file))
    except:
        print(f"?!?!没读出来{x},跳过")
    else:
        print("读好了。",end="")
        try:
            modif(jsonobj)
        except:
            print("但没改成")
            continue
        with x.open("w") as file:
            json.dump(jsonobj,file,ensure_ascii=False,indent=4)
        print("改好了。")
            
