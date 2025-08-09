import json
d={"name":"zaymukl","age":18}
with open(r"D:\zaynu\Documents\pythonfiles\Python file prtactise folder\jsonhandling\somefile.json","r+") as f:
    # json.dump(d,f,indent=4)
    dat = json.load(f)
    print(dat)
    print(type(dat))
    print("\n\n")
    ns=input("name to search:  ")
    for i in dat["faculty"]:
        if i["name"]==ns:
            print("person found")
            i["salary"]+=3000
            print(i)


# create a: product id ,brand name ,catrgory,price
# create 5 such products
#put them under a store :name ,location, products (its a list of prods)
#three stores of this kind
#city :name longitude latitude
#4 metero cities
# each city will have 3 stores
# cities{
#     city{
#         store{
#             Name
#             loc
#             prod{
#                 id
#                 brandname 
#                 category
#                 price
#             }
#         }
#     }
# }   