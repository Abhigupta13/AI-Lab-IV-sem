from queue import Queue
ad_list={
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}

# DFS CODE
visited={ }
level={}
parent={}
bfs_traversal_output=[]
queue=Queue()


for node in ad_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
# print(visited)
# print(level)
# print(parent)

s="A"
visited[s]=True
level[s]=0
queue.put(s)
while not queue.empty():
    u=queue.get()
    bfs_traversal_output.append(u)
    for v in ad_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
print(bfs_traversal_output)
    