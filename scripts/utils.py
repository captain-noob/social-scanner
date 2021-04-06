

def list_contains(List1, List2):
    set1 = set(List1) 
    set2 = set(List2) 
    if set1.intersection(set2): 
        return True 
    else: 
        return False