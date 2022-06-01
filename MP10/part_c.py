from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_shortest_distances(graphframe, dst_id):
    # TODO
    # Find shortest distances in the given graphframe to the vertex which has id `dst_id`
    # The result is a dictionary where key is a vertex id and the corresponding value is
    # the distance of this node to vertex `dst_id`.
    graph_result = graphframe.shortestPaths(landmarks=[dst_id,dst_id])
    # graph_result.show()
    ret = {}
    distances=0
    sources = ''
    for i in range(graph_result.count()):
        if graph_result.collect()[i][1]:
            distances=graph_result.collect()[i][1][dst_id]
        else:
            distances = -1
        # print(distances)
        sources=graph_result.collect()[i][0]
        # print(sources)
        ret[f'{sources}']=distances   
    # print(ret) 
    return ret


if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:
        for line in f:
            # TODO: Parse line to get vertex id
            src = line.split(" ",1)[0]
            # TODO: Parse line to get ids of vertices that src is connected to
            dst_str = line.split(" ",1)[1]
            dst_list = []
            for dest in dst_str.split():
                dst_list.append(dest)
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list, ["id"])  # TODO: Create dataframe for vertices
    edges = spark.createDataFrame(edge_list, ["src","dst"])  # TODO: Create dataframe for edges

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/shortest-paths")
    # get_shortest_distances(g,'1')
    # We want the shortest distance from every vertex to vertex 1
    for k, v in get_shortest_distances(g, '1').items():
        print(k, v)