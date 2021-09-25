#Na wejściu znajdują się dwa drzewa BST.
#Znajduje ilość kluczy, które występują w obu drzewach.

#Zapisuje klucze 1 i 2 drzewa w kolejności inorder.
#Przechodzę po wartościach kluczy i szukam elementów wspólnych.

class BST_Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


#zapisuje klucze z drzewa w tablicy A
def inorderToArray(root,A):
    if root is not None:
        inorderToArray(root.left,A)
        A.append(root.key)
        inorderToArray(root.right,A)
    return A


#znajduje ilość takich samych kluczy
def intersection(root1,root2):
    A1 = inorderToArray(root1,[])
    A2 = inorderToArray(root2,[])
    
    i = j = 0
    cnt = 0

    while i < len(A1) and j < len(A2):
        if A1[i] == A2[j]:
            cnt += 1
            i += 1
            j += 1
        
        elif A1[i] < A2[j]:
            i += 1
        
        else:
            j += 1
    
    return cnt
