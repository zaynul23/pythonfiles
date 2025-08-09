std={"rollno":1,"dept":"CSM","Section":"A","marks":{"math":92,"phy":45,"chem":12}}
std2={"rollno":2,"dept":"CSM","Section":"B","marks":{"math":12,"phy":100,"chem":56}}
std3={"rollno":3,"dept":"CSM","Section":"C","marks":{"math":23,"phy":74,"chem":78}}
dat=[std,std2,std3]
top_marks=[(i["rollno"],sum(i["marks"].values())) for i in dat]
top=max([b for a,b in top_marks])
for a,b in top_marks:
    if b==top:
        maxscorer=a
for a,b in top_marks:
    if b<0.4*300:
        print(f"{a} failed")        
for i in dat:
    if i["math"]>90:
        print(i["marks"]["rollno"])

for i in dat:
    if i["phy"]>75:
        print(i["marks"]["rollno"])

for i in range(len(top_marks)):
    if b>0.75*300 and:
        pass   
    