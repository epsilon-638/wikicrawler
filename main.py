import scrape_wiki


class Lock:


    def __init__(self):
        self.__lock = False


    def await_unlock(self):
        while not self.__lock: 
            pass
        self.__lock = True


    def acquire(self):
        self.await_unlock()
        self.__lock = True


    def release(self):
        self.__lock = False



class Node:


    def __init__(self, source, edges):

        self._source = source
        self._edges = edges
        self.__lock = Lock() 


    def get_source(self):
        return self._source


    def get_children(self):
        return self._edges


    def number_of_links(self):
        return len(self._edges)

    def append_edge(self, edge):
        self.__lock.acquire()
        self._edges.append(edge)
        self.__lock.release()
    


class WikiGraph:


    def __init__(self, v, max_depth=100000):
        self.v = v
        self.depth = 0
        self.max_depth = max_depth
        self.queue = []
        self.edges = []
        self.__lock = Lock()


    def release(self):
        self.__lock = False


    def depth_check(self):
        if self.max_depth == None:
            return True
        if self.max_depth > 0:
            return True
        return False


    def increase_depth(self):
        self.__lock.acquire()
        self.depth += 1
        self.__lock.release()


    def check_queue_duplicate(self, url):
        if url in self.queue:
            return True
        return False


    def push_to_queue(self, url):
        self.__lock.acquire()
        if not self.check_queue_duplicate(url):
            self.queue.append(url)
        self.__lock.release()


    def pop_queue(self):
        self.__lock.acquire()
        url = self.queue.pop(0)
        self.__lock.release()
        return url


    def append_edge(self, node):
        self.__lock.acquire()
        self.edges.append(node)
        self.__lock.release()


    def scrape_edge(self, url):
        pass
