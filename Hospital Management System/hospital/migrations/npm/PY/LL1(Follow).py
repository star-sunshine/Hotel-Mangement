def first(productions, non_terminal):
    first_set = set()

    if non_terminal not in productions:
        return first_set

    for expression in productions[non_terminal]:
        if expression[0].islower() or expression[0] == '':
            first_set.add(expression[0])
        elif expression[0].isupper():
            first_set.update(first(productions, expression[0]))

    return first_set

def follow(productions, start_symbol, non_terminal):
    follow_set = set()

    if non_terminal == start_symbol:
        follow_set.add('$')

    for key, value in productions.items():
        for expression in value:
            for index, symbol in enumerate(expression):
                if symbol == non_terminal and index < len(expression) - 1:
                    follow_set.update(first(productions, expression[index + 1]))
                elif symbol == non_terminal and key != non_terminal:
                    follow_set.update(follow(productions, start_symbol, key))

    return follow_set

# Example usage:
productions = {
    'S': ['AB'],
    'A': ['a'], 
    'B': ['b']
}
start_symbol = 'S'
non_terminal = 'A'
follow_set = follow(productions, start_symbol, non_terminal)
print(f'Follow({non_terminal}): {follow_set}')
