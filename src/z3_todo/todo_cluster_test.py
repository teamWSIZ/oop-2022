import unittest

from src.z3_todo.repo_server import RepoServer


def create_cluster(nodes=3) -> list[RepoServer]:
    """
    Create a list of 'node' servers, form a cluster from these.
    :param nodes: number of nodes in cluster
    :return: list of servers which are joined together in cluster
    """
    servers = [RepoServer() for _ in range(nodes)]
    for c in servers:
        for ca in servers:
            c.add_other(ca)
    return servers


def create_cluster_easy(nodes=3) -> list[RepoServer]:
    node0 = RepoServer()
    node0.elect_leader()
    for _ in range(nodes - 1):
        node0.extend_cluster(RepoServer())

    return list(node0.cluster)


class TodoServerTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_simple_3_node_cluster(self):
        cluster = create_cluster(3)
        nodes = cluster

        node0 = nodes[0]  # first node from cluster
        for n in nodes:
            assert node0 in n.cluster  # must be preset in all other nodes

    def test_can_add_extra_node(self):
        # arrange
        cluster = create_cluster()
        extra_server = RepoServer()
        cluster[0].elect_leader()  # to be tested
        previous_leader = cluster[0].leader
        previous_leader.write('abra kadabra')

        # act
        cluster[0].extend_cluster(extra_server)

        # assert
        # 1.  ref to extra_server is in all nodes of the cluster
        # 2.  ref to all previous nodes of cluster are in extra_server
        # 3.  leader of the cluster is unchanged
        # 4.  all data from the cluster is copied to the extra node

        # 1
        for node in cluster[0].cluster:
            assert extra_server in node.cluster

        # 2
        for node in cluster[0].cluster:
            assert node in extra_server.cluster

        # 3
        for node in cluster[0].cluster:
            assert node.leader == previous_leader

        # 4
        for (leader_msg, extra_node_msg) in zip(cluster[0].leader.data, extra_server.data):
            assert leader_msg == extra_node_msg

    def test_simple_cluster_creation(self):
        cluster = create_cluster_easy(1)

        assert len(cluster[0].cluster) == 1
        assert cluster[0].is_leader == True
        assert cluster[0].leader == cluster[0]

    def test_write_replicates(self):
        # arrange
        cluster = create_cluster_easy(3)

        # act
        cluster[1].write('kadabra')

        assert cluster[1].data[0] == 'kadabra'  # fixme: this shall not pass --> add .read() method

        # assert
        for node in cluster:
            self.assertEqual(len(node.data), 1)
            assert node.data[0] == 'kadabra'
