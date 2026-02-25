#n, m = [int(x) for x in input().split()]
#W = [[] for _ in range(n)]
#for _ in range(m):
#    i, j = [int(x) - 1 for x  in input().split()]
#    W[i].append(j)
#
#start = 0
#dist = [-1] * n
#dist[start] = 0
#queue = [start]
#while queue:
#    u = queue.pop(0)
#    for v in W[u]:
#        if dist[v] == -1:
#            dist[v] = dist[u] + 1
#        queue = [v] + queue
#
#print(dist)

from collections import deque

graph = {
    "you": ["alice", "ЬоЬ", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def bfs():
    search_queue = deque()
    search_queue = graph["you"]

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is mango seller!")
            return True
        else:
            search_queue += graph[person]
    return False

def person_is_seller(person):
    return person[-1] == 'm'