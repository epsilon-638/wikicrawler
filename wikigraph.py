import proxy
import scrape_wiki
import json
import redis
from redisgraph import Node, Edge, Graph, Path


def get_redisgraph_client(host='localhost', port=6379):
    return redis.Redis(host=host, port=port)

def get_wikigraph(client):
    return Graph('wikigraph', r)

def internal_link_node(graph, wiki_content):
    graph.add_node(Node(
        label=wiki_content.content_type,
        properties={
            'name': wiki_content.name,
            'internal_links': wiki_content.internal_links,
            'external_links': wiki_content.external_links,
            'internal_media': wiki_content.internal_media,
        }))

def internal_media_node(graph, wiki_content):
    graph.add_node(Node(
        label='media',
        properties={
            'name': wiki_content.name,
        }))

def internal_link_edge(graph, url, link_from, link_to, link_index):
    graph.add_edge(Edge(
        link_from, 
        'links-to', 
        link_to, 
        properties={
            'link_index':link_index
        }))
