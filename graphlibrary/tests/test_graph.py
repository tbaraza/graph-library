from unittest import TestCase
from graphlibrary import graph


class GraphTest(TestCase):

    def test_uninitialized_graph_object(self):
        empty_graph = graph.Graph()
        self.assertEquals(empty_graph._Graph__graph, {})

    def test_bad_initialization_graph_object(self):
        graph_values = ['A', 'B', 'C']
        wrong_init_graph = graph.Graph(graph_values)
        self.assertEqual(wrong_init_graph._Graph__graph, None)

    def test_initialized_graph_object(self):
        graph_values = {'A': ['B', 'C'], 'B': ['A', 'E', 'D'], 'C': ['B', 'C']}
        initialized_graph = graph.Graph(graph_values)
        self.assertEquals(initialized_graph._Graph__graph, graph_values)
        initialized_graph._Graph__graph.clear()

    def test_add_node(self):
        graph_add = graph.Graph()
        node = "A"
        graph_add.add_vertex(node)
        self.assertTrue(graph_add._Graph__graph)
        graph_add._Graph__graph.clear()

    def test_remove_node(self):
        graph_remove = graph.Graph(
            {'A': ['B', 'C'], 'B': ['A', 'E', 'D'], 'C': ['B', 'C']})
        node = "B"
        graph_remove.remove_vertex(node)
        self.assertTrue(graph_remove._Graph__graph)
        graph_remove._Graph__graph.clear()

    def test_add_edge_correct_spec(self):
        graph_edge = graph.Graph({'A': [], 'B': [], 'C': []})
        edge = ['A', 'B']
        self.assertTrue(graph_edge.add_edge(edge))
        graph_edge._Graph__graph.clear()

    def test_add_edge_bad_spec(self):
        graph_edge = graph.Graph({'A': [], 'B': [], 'C': []})
        edge = ['A']
        self.assertFalse(graph_edge.add_edge(edge))
        graph_edge._Graph__graph.clear()