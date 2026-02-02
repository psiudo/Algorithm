tree = {}
N = int(input())
for _ in range(N) :
    parent, child1, child2 = map(str, input().split())
    tree[parent] = [child1, child2]

###########################################################
# print(tree)
# {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'] ...
###########################################################
ans1 = []
def preorder(node) : # node에는 str 타입
    ans1.append(node)
    if tree[node][0] != '.':
        preorder(tree[node][0])
    if tree[node][1] != '.' :
        preorder(tree[node][1])

ans2 = []
def inorder(node) : # node에는 str 타입
    if tree[node][0] != '.':
        inorder(tree[node][0])
    ans2.append(node)
    if tree[node][1] != '.' :
        inorder(tree[node][1])

ans3 = []
def postorder(node) : # node에는 str 타입
    if tree[node][0] != '.':
        postorder(tree[node][0])
    if tree[node][1] != '.' :
        postorder(tree[node][1])
    ans3.append(node)

preorder('A')
inorder('A')
postorder('A')
###########################################################
print(''.join(ans1))
print(''.join(ans2))
print(''.join(ans3))
