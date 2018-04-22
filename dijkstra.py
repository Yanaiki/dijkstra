#Author: Yanai Lipshitz


def dijkstra(graph,weights,source):
    inf = "infinity"
    A = [inf] * len(graph)
    queue = []
    B = graph.keys()
     
    queue = [(0, source)]
    while queue:
        (path_len, v) = heapq.heappop(queue)
        
        t = ord(v)-97        
        if A[t] is inf: 
            A[t] = path_len
            for w in graph[v]:
                if (v,w) in weights:
                    edge_len = weights.get((v,w))
                r = ord(w)-97
                if A[r] is inf:
                    heapq.heappush(queue, (path_len + edge_len, w))
    dictionary = dict(zip(B, A))

    return dictionary
