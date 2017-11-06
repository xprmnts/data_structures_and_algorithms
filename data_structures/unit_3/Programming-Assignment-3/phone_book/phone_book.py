# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if phonebook[cur_query.number] is not None:
                phonebook[cur_query.number] = cur_query.name
            else: # otherwise, just add it
                phonebook[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if phonebook[cur_query.number] is not None:
                phonebook[cur_query.number] = None
        else:
            response = 'not found'
            if phonebook[cur_query.number] is None:
                result.append(response)
            else:
                result.append(phonebook[cur_query.number])
    return result

if __name__ == '__main__':
    phonebook = [None]*10000000
    write_responses(process_queries(read_queries()))

