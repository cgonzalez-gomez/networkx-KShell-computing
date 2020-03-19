import networkx as nx

def check_degree(G,deg):
	""" Checks if all the nodes of a graph have a degree greater than the threshold.

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


def draw_kshell(DG,k_shell,target,TF):
	#green: TF #blue:target genes #orange:both
    """ Draw the kshell of a gene regulatory network with NetworkX draw.
        See draw(G, pos=None, ax=None, hold=None, **kwds) for more details.
        
        Parameters
        ----------
        DG: NetworkX Digraph
            A directed graph.
        k_shell: list
            A set of nodes in the k-core but not in the (k+1)-core.
        target: list
            A list of the target genes of the regulatory network.
        TF: list
            A list of the transcription factors of the regulatory network.
    """
	for node in kshell:
    if node in target and node not in TF :
        color_map3.append('blue')
    if node in TF and node not in target: 
        color_map3.append('green')
    if node in set(TF.intersection(target)):
        color_map3.append('orange')
    nx.draw(DG.subgraph(kshell[6]),with_labels=False,node_size=50,node_color=color_map3) 
