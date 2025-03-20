

class Solution:
    def minimumCost(self, n, edges, queries):
        # Initialize the parent array with -1 as initially each node belongs to its own component
        self.parent = [-1] * n
        self.depth = [0] * n

        # All values are initially set to the number with only 1s in its binary representation
        component_cost = [-1] * n

        # Construct the connected components of the graph
        for edge in edges:
            self._union(edge[0], edge[1])

        # Calculate the cost of each component by performing bitwise AND of all edge weights in it
        for edge in edges:
            root = self._find(edge[0])
            component_cost[root] &= edge[2]

        answer = []
        for query in queries:
            start, end = query

            # If the two nodes are in different connected components, return -1
            if self._find(start) != self._find(end):
                answer.append(-1)
            else:
                # Find the root of the edge's component
                root = self._find(start)
                # Return the precomputed cost of the component
                answer.append(component_cost[root])

        return answer

    # Find function to return the root (representative) of a node's component
    def _find(self, node):
        # If the node is its own parent, it is the root of the component
        if self.parent[node] == -1:
            return node
        # Otherwise, recursively find the root and apply path compression
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]

    # Union function to merge the components of two nodes
    def _union(self, node1, node2):
        root1 = self._find(node1)
        root2 = self._find(node2)

        # If the two nodes are already in the same component, do nothing
        if root1 == root2:
            return

        # Union by depth: ensure the root of the deeper tree becomes the parent
        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1

        # Merge the two components by making root1 the parent of root2
        self.parent[root2] = root1

        # If both components had the same depth, increase the depth of the new root
        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += 1
            
            
            
"""
There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]

Explanation:


To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).

In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

Example 2:

Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]

Output: [0]

Explanation:


To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

"""            

