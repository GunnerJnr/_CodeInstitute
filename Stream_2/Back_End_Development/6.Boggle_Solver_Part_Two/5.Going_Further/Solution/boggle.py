from string import ascii_uppercase
from random import choice


def check():
    return 1


def make_grid(width, height):
    return {(row, col): choice(ascii_uppercase)
            for row in range(height)
            for col in range(width)}


def neighbours_of_position((row, col)):
    return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]


def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours


def path_to_word(grid, path):
    return ''.join([grid[p] for p in path])


def is_a_real_word(word, dictionary):
    return word in dictionary


def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary

    def do_search(word_path):
        word = path_to_word(grid, word_path)
        if is_a_real_word(word, full_words):
            paths.append(word_path)
        if word not in stems:
            return
        for next_pos in neighbours[word_path[-1]]:
            if next_pos not in word_path:
                do_search(word_path + [next_pos])

    for position in grid:
        do_search([position])

    words = []
    for word_path in paths:
        words.append(path_to_word(grid, word_path))
    return set(words)


def get_dictionary(dictionary_file):
    full_words, stems = set(), set()

    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)

            for i in range(1, len(word)):
                stems.add(word[:i])
    return full_words, stems


def main():
    grid = make_grid(3, 3)
    dictionary = get_dictionary('Words_two.txt')
    words = search(grid, dictionary)
    for word in words:
        print word
    print "Found {0} words".format(len(words))


main()


