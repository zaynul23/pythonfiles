import json
with open(r"jsonhandling\recieve.json","w+") as f:
    inp={
            "id":"n1",
            "name":43.0,
            "dept":"csm"
        }
    sinp=json.dumps(inp)
    json.dump(inp,f,indent=4,separators=( " , "," : "))
    f.seek(0)
    dat=json.load(f)
    print(dat)
    
    