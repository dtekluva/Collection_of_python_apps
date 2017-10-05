the_list = ["jammes",75,["first","boy",["hiden guy","woooow"]],("football","orange",),{"pointed":"second"},["third","boy"],("soccer","mango",),{"stuble":"logistics"}]

def extractlist(itemlist):
    
    for item in itemlist:
        
        if type(item)==list or type(item)==tuple:
                
                print (extractlist(item))
                
        
        elif type(item)==dict:
            for key in item:
                print (item[key])
        else:
            print(item)

extractlist(the_list)


def return_multiple():
    return "james ", " nigeria", " male"

name,country,gender=return_multiple()
detail=return_multiple()
print(type(detail))

print (name,country,gender)
input()
