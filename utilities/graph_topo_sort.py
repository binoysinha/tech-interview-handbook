def graph_topo_sort(num_nodes, edges):
    nodes, order, queue = {}, [], []
    for node_id in range(num_nodes):
        nodes[node_id] = { 'in': 0, 'out': set() }
    for node_id, pre_id in edges:
        nodes[node_id]['in'] += 1
        nodes[pre_id]['out'].add(node_id)
    for node_id in nodes.keys():
        if nodes[node_id]['in'] == 0:
            queue.append(node_id)
    while len(queue) > 0:
        node_id = queue.pop(0)
        for outgoing_id in nodes[node_id]['out']:
            nodes[outgoing_id]['in'] -= 1
            if nodes[outgoing_id]['in'] == 0:
                queue.append(outgoing_id)
        order.append(node_id)
    return order if len(order) == num_nodes else []
