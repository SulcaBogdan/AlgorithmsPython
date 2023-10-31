graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 6

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}


infinity = float("inf")


costs = {}
costs["a"] = 6
costs["b"] = 2
costs["inf"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

#Exemplul A

graph1 = {}
graph1["start"] = {}
graph1["start"]["a"] = 5
graph1["start"]["b"] = 2

graph1["a"] = {}
graph1["a"]["c"] = 4
graph1["a"]["d"] = 2

graph1["b"] = {}
graph1["b"]["a"] = 8
graph1["b"]["d"] = 7

graph1["c"] = {}
graph1["c"]["d"] = 6
graph1["fin"] = 2

graph1["d"] = {}
graph1["d"]["fin"] = 1
graph1["fin"] = {}

costs1 = {}
costs1["a"] = 5
costs1["b"] = 2
costs1["c"] = 4
costs1["d"] = 7
costs1["inf"] = infinity

parents1 = {}
parents1["a"] = "start"
parents1["b"] = "start"
parents1["c"] = "a"
parents1["d"] = "b"
parents["fin"] = None

infinity1 = float("inf")

print(graph1)



def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

print(find_lowest_cost_node(costs1))