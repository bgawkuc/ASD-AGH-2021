#dostaje na wejściu dwa zbiory reprezentowane jako drzewa BST
#znajdz ile jest w nich elementów wspólnyvh
#przechodze oba drzewa inorder zpaisuje to w tablicach
#inorder daje mi kolejność rosnącą
#wiec teraz wysatrczy przechodzic po dwoch tablicach(nie dwie pętle a jedna!)
#patrzac czy gdzies znajde taką samą wartość

class BST_Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def insert(root,key,value):
    prev = None
    while root is not None:
        if key > root.key:
            prev = root
            root = root.right
        else:
            prev = root
            root = root.left

    if key < prev.key:
        prev.left = BST_Node(key,value)
        prev.left.parent = prev
    else:
        prev.right = BST_Node(key,value)
        prev.right.parent = prev


#zapisuje klucze z drzewa rosnąco
def inorderToArray(root,A):
    if root is not None:
        inorderToArray(root.left,A)
        A.append(root.key)
        inorderToArray(root.right,A)
    return A


def intersection(root1,root2):
    A1 = inorderToArray(root1,[])
    A2 = inorderToArray(root2,[])
    print(A1,A2)
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

r1 = BST_Node(5,1)
insert(r1,3,1)
insert(r1,8,1)
insert(r1,4,1)
insert(r1,9,1)
insert(r1,6,1)
insert(r1,2,1)

r2 = BST_Node(7,1)
insert(r2,2,1)
insert(r2,8,1)
insert(r2,4,1)
insert(r2,10,1)

print(intersection(r1,r2))