def post_order(tree: list, current_space: int, total_length: int, current_value: list) -> list:
    if current_space>total_length:
        return
    post_order(tree,current_space*2,total_length,current_value)
    post_order(tree,current_space*2+1,total_length,current_value)
    tree[current_space-1]= current_value[0]
    current_value[0]+=1
    
def solution(h: int, labels: list) -> list:
    total = sum([pow(2,x) for x in range(0,h)])
    tree = [-1]*total
    post_order(tree,1,total,[1])
    ans = []
    for label in labels:
        index = tree.index(label)
        if index==0:
            ans.append(-1)
            continue
        if index%2==0:
            ans.append(tree[int(index/2)-1])
        else:
            ans.append(tree[int(index/2)])
    return ans