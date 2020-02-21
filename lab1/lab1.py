from lab1_utilities import *
import math


def get_installations_from_file(file_name):
    answer = []
    with open(file_name, 'r') as f:
        f.readline()
        for line in f:
            r = line.strip().split('\t')
            fool = r[-1].find('INDOORS') >= 0
            answer.append(Installation(r[0], int(r[2]), (float(r[7]), float(r[8])), fool))
    return answer
            
    


def euclidean_distance(position1, position2):
    return math.sqrt((position2[0]-position1[0])**2+(position2[1]-position1[1])**2)


def get_adjacency_mtx(installations):
    answer = []
    x= len(installations)
    for j in installations:
        values = []
        for i in installations:
            z = int(abs(i.ward - j.ward)< 2)
            k = 1.5 if (i.indoor or j.indoor) else 1.0
            values.append(z*k*euclidean_distance(i.position, j.position))
        answer.append(values)
    return answer

def make_graph(installations):
    lirst= []
    for i in installations:
        lirst.append(i.name)
    return Graph(lirst, get_adjacency_mtx(installations))
def minimum(dic):
    min = 18423487345495238
    key = ''
    for i in dic:
        if dic[i] < min:
            min = dic[i]
            key = i
    return key
def find_shortest_path(installation_A, installation_B, graph):
    dist_queue= {installation_A:0}
    queue = [installation_A]
    prev_node = {}
    answer=[installation_B]
    visited = []
    visiting_node = installation_A
    done = False
    while not done:
        #print(queue)
        if installation_B == visiting_node:
            break;
        for i in range(len(graph.adjacency_mtx[graph.artwork_to_index[visiting_node]])):
            if graph.adjacency_mtx[graph.artwork_to_index[visiting_node]][i]>0 and (graph.installations[i] not in visited) and (graph.installations[i] not in queue):
                queue.append(graph.installations[i])
        
        for i in queue:
            if i not in dist_queue.keys():
                dist_queue[i] = dist_queue[visiting_node] + graph.adjacency_mtx[graph.artwork_to_index[visiting_node]][graph.artwork_to_index[i]]
                prev_node[i] = visiting_node
            else:
                if graph.adjacency_mtx[graph.artwork_to_index[visiting_node]][graph.artwork_to_index[i]]>0 and dist_queue[visiting_node] + graph.adjacency_mtx[graph.artwork_to_index[visiting_node]][graph.artwork_to_index[i]] < dist_queue[i]:
                    dist_queue[i] = dist_queue[visiting_node] + graph.adjacency_mtx[graph.artwork_to_index[visiting_node]][graph.artwork_to_index[i]]
                    prev_node[i] = visiting_node
                    
        del queue[queue.index(visiting_node)]
        del dist_queue[visiting_node]
        visited.append(visiting_node)
       
        if len(queue) == 0:
            done = True
        visiting_node = minimum(dist_queue)
    if installation_B in dist_queue:
        s = installation_B
        while(s != installation_A):
            answer.append(prev_node[s])
            s = prev_node[s]
        return dist_queue[installation_B], list(reversed(answer))
    else:
        return 4
