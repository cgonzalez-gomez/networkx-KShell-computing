import networkx as nx

def check_degree(G,deg):
    """ Checks if at least one node of a graph has a degree below the threshold

	Parameters
	----------
    G : NetworkX graph
        A graph or directed graph.
	deg: int
		Threshold for the nodes degree.
		
    Returns
    -------
    low_degree: bool
        True if the graph has at least one node with a degree below the threshold.
        
    
    Example
    -------
    >>> G=nx.Graph()
    >>> G.add_edges_from([(1, 2),(1,3),(1,4),(2,3),(3,4)])
    >>> check_degree(G,1)
    False
    >>> check_degree(G,2)
    True
    """
    low_degree=False
    for n in G.nodes():
        if G.degree(n)<=deg:
            low_degree=True
            break
    return low_degree

def find_nodes(G,deg):
    """ Return the nodes with a degree below the threshold.
        
    Parameters
    ----------
    G : NetworkX graph
        A graph or directed graph.
    deg: int
        Threshold for the nodes degree.
        
    Returns
    -------
    nodes: list
        A list of nodes with a degree below the threshold.
    
    Example
    -------
    >>> G=nx.Graph()
    >>> G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(3,4)])
    >>> find_nodes(G,2)
    [2,4]
    >>> find_nodes(G,5)
    [1,2,3,4]
    
    """
    nodes=[]
    for n in G.nodes():
        if G.degree(n)<=deg:
            nodes.append(n)
    return nodes

def k_shell(Graph):
    """ Return the nodes in each kshell of the graph.
    
    The k-shell is the set of nodes in the k-core but not in the (k+1)-core.
    
    Parameters
    ----------
    Graph : NetworkX graph
        A graph or directed graph.
        
    Returns
    -------
    cores: list
        A list of lists of the nodes in each kshell of th graph.
        
    Example
    -------
    >>> G=nx.Graph()
    >>> G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(3,4),(1,5)])
    >>> k_shell(G)
    [[5], [2, 4, 1, 3]]
    
    """
    G=Graph.copy()
    deg=1
    cores=[]
    tmp=[]
    while(len(G.nodes())>0):
        check=check_degree(G,deg)
        if(not check):
            deg+=1
            cores.append(tmp)
            tmp=[]
        if(check):
            node_set=find_nodes(G,deg)
            for n in node_set:
                G.remove_node(n)
                tmp.append(n)
        if(len(G.nodes())==0):
            cores.append(tmp)
    return cores


def draw_kshell(G,kshell,target=None,TF=None,color_target='blue', color_TF='red', color_intersection='magenta',nodesize=300,labels=True):
    """ Draw the kshell of a directed graph or the kshell of a gene regulatory network with NetworkX draw.
    See draw(G, pos=None, ax=None, hold=None, **kwds) for more details.
    
    Parameters
    ----------
    G: NetworkX Graph
        A graph or directed graph.
    k_shell: list
        A set of nodes in the k-core but not in the (k+1)-core.
    target: set, optional (default = None)
        A set of the target genes of the regulatory network.
    TF: set, optional (default = None)
        A set of the transcription factors of the regulatory network.
    color_target: string, optional (default = 'blue')
        Color of the target genes.
    color_TF: string, optional (default = 'red')
        Color of the transcription fractors.
    color_intersection: string (default = 'magenta')
        Color of the genes that are both transcription factors and target genes.
    nodesize: scalar or array, optional (default=300)
        Size of nodes.  If an array is specified it must be the
        same length as nodelist.
    labels: boolean,optional (default=True)
        Set to True to draw labels on the nodes.
        
    """
    if (target and TF):
        color_map=[]
        subgraph=G.subgraph(kshell)
        for node in subgraph.nodes():
            if node in target and node not in TF :
                color_map.append(color_target)
            if node in TF and node not in target:
                color_map.append(color_TF)
            if node in set(TF.intersection(target)):
                color_map.append(color_intersection)

        nx.draw(subgraph,with_labels=labels,node_size=nodesize,node_color=color_map)
    
    else:
        nx.draw(G.subgraph(kshell),with_labels=labels,node_size=nodesize)
