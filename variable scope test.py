max_attempts=5

def test_scope2(attempts):
   
    while attempts !=0 :
        attempts-=1
        print(attempts)
    return True
    
test_scope2(max_attempts)
