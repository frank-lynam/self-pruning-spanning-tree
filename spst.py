import random, json

def create_random_graph(n, connectivity=2):
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
  print(f"The first spanning tree has {len(big_tree)} nodes.")
  pruned_tree = span(big_tree, sinks)
  print(f"The pruned spanning tree has {len(pruned_tree)} nodes.")
  return pruned_tree

def span(graph, sources):
  # Basic spanning tree that returns a reversed subgraph

  # Use a stack to list the places we want to go
  stack = [x for x in sources if x in graph.keys()]

  # Use a tree to build a map of where we've been
  tree = {x:[] for x in stack}

  # Keep track of where we are in the stack
  index = 0

  # Build the stack until you stop adding to it
  while index < len(stack):
    # Check every edge from this node
    for next_node in graph[stack[index]]:
      # If we haven't been there, add it to the stack
      if next_node not in stack:
        stack.append(next_node)
      # If we haven't mapped it, add it to the tree
      if next_node not in tree.keys():
        tree[next_node] = [stack[index]]
      else:
        # If we have, at least add the edge
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
      if next_node in sinks:
        print(" -> ".join([f"{x}" for x in (path + [next_node])]))
      recurse_path(graph, path+[next_node], sinks)

if __name__=="__main__":
  # A demo of the spanning tree that creates a random graph and 
  #  lists all the paths from sources to sinks
 
  # Create the reference data
  graph = create_random_graph(10)
  sources = [0,1]
  sinks = [3,4]
  print(f"I have created a random graph with {len(graph.keys())} nodes.")
  print(f"Now I will find the subgraph describing all paths from nodes {sources} to {sinks}.")
  
  # Get the subgraph
  result = spst(graph, sources, sinks)

  # List the outputs
  if len(result.keys()) == 0:
    print("That graph had no connectivity.")
  else:
    print(f"Here is a list of all the paths:")
    list_paths(result, sources, sinks)
