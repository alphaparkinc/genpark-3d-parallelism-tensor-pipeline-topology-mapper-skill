from client import ThreeDParallelismTensorPipelineTopologyMapperClient

def main():
    client = ThreeDParallelismTensorPipelineTopologyMapperClient()
    res = client.map_cluster_parallelism_topology(128, 671, 30)
    print('3D Parallelism Plan: ' + res['topology_plan_id'] + ' (' + str(res['total_nodes']) + ' nodes)')
    print('TP=' + str(res['tensor_parallel_size']) + ', PP=' + str(res['pipeline_parallel_size']) + ', SP=' + str(res['context_sequence_parallel_size']))
    print('Overlap Efficiency: ' + str(res['communication_overlap_efficiency_pct']) + '% | Microbatch: ' + str(res['optimal_microbatch_size']))
    print('Topology URL: ' + res['nccl_topology_graph_url'])

if __name__ == '__main__':
    main()
