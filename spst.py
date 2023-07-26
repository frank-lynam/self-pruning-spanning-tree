import random, json

def create_random_graph(n, connectivity=5):
  # Creates a random potentially disjoint directed graph of 
  #  a defined number of nodes (n) and connectivity
  
  graph = {x:[] for x in range(n)}
  for _ in range(n*connectivity):
    graph[random.randint(0,n-1)].append(random.randint(0,n-1))
  return graph

def spst(graph, sources=[0], sinks=[1]):
  # Creates a spanning tree from the source nodes then reverses it
  #  and creates a spanning tree from the sink nodes to find
  #  *only* the connected subgraph
  
  big_tree = span(graph, sources)
  pruned_tree = span(big_tree, sinks)
  return pruned_tree

def span(graph, sources):
  # Basic spanning tree that returns a reversed subgraph

  stack = [x for x in sources if x in graph.keys()]
  tree = {x:[] for x in stack}
  index = 0
  while index < len(stack):
    for next_node in graph[stack[index]]:
      if next_node not in stack:
        stack.append(next_node)
      if next_node not in tree.keys():
        tree[next_node] = [stack[index]]
      else:
        tree[next_node].append(stack[index])
    index = index + 1
  return tree

def list_paths(graph, sources=[0], sinks=[1]):
  # Runs a simple recursive spanning process to list all 
  #  paths in a graph between two subgraphs

  [recurse_path(graph, [x], sinks) for x in sources if x in graph.keys()]

def recurse_path(graph, path, sinks):
  # Simple recursion to output all forking paths

  for next_node in graph[path[-1]]:
    if next_node not in path:
      path.append(next_node)
      if next_node in sinks:
        print(" -> ".join([f"{x}" for x in path]))
      recurse_path(graph, path, sinks)

if __name__=="__main__":
  # A demo of the spanning tree that creates a random graph and 
  #  lists all the paths from sources to sinks
 
  graph = create_random_graph(100)
  sources = [0,1,2]
  sinks = [3,4,5]
  
  list_paths(spst(graph, sources, sinks), sources, sinks)
