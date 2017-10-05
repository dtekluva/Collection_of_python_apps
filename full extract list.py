the_list = ["jammes",75,["first","boy",["hiden guy","woooow"]],("football","orange",),{"pointed":"second"},["third","boy"],("soccer","mango",),{"stuble":"logistics"}]

def extractlist(itemlist):
    
    for item in itemlist:
        
        if type(item)==list or type(item)==tuple or type(item)==dict:
                
                print (extractlist(item))
                
        if type(item)==dict:
                for key in item:
                    print (item[key])
        else:
            print(item)

extractlist(the_list)
input()
