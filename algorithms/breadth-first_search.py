from collections import deque

graph = {}
graph['me'] = ['john', 'alice', 'pavel']
graph['john'] = ['rafael', 'julie']
graph['alice'] = ['julie']
graph['pavel'] = ['ben', 'harold']
graph['rafael'] = []
graph['julie'] = []
graph['ben'] = []
graph['harold'] = []


def person_is_seller(person):
    return person[-1] == 'e'


def search():
    """
    Example implementation of breadth-first search algorithm looking for seller in the graph of friends.

    :param name:
    :return:
    """
    search_queue = deque()
    search_queue += graph['me']
    searched = []  # already searched people
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} sells mango')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('Seller not found')
    return False


search()
