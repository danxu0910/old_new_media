# https://github.com/aparrish/rwet/blob/master/ngrams-and-markov-chains.ipynb

from collections import Counter
import random 

# text = open("the_nameless_city.txt").read()
# words = text.split()

#create a list of tuples < consecutive word pairs
# pairs = [(words[i], words[i+1]) for i in range(len(words) - 1)]

# char_pairs = [(text[i], text[i+1]) for i in range(len(text) - 1)]

# five_grams = [tuple(words[i:i+5]) for i in range(len(words) - 4)]
#print(pairs[:5])

# pair_counts = Counter(pairs)
# char_pair_counts = Counter(char_pairs)
# five_grams_counts = Counter(five_grams)
# print(five_grams_counts.most_common(10))


def ngrams_for_sequence(n, seq):
    return [tuple(seq[i:i+n]) for i in range(len(seq) - n+1)]

# nameless_8grams = ngrams_for_sequence(8, text)

# alice_word_5grams = ngrams_for_sequence(5, open("/Users/dxu/Desktop/Py_texts/alice.txt").read().split())

# print(Counter(ngrams_for_sequence(5, text)).most_common(10))

def add_to_model(model, n, seq):
    seq = list(seq[:]) + [None]
    for i in range(len(seq) - n):
        gram = tuple(seq[i:i+n])
        next_item = seq[i+n]
        if gram not in model:
            model[gram] = []
        model[gram].append(next_item)

def markov_model(n, seq):
    model = {}
    add_to_model(model, n, seq)
    return model

def gen_from_model(n, model, start=None, max_gen=100):
    if start is None:
        start = random.choice(list(model.keys()))
    output = list(start)
    for _ in range(max_gen):
        start = tuple(output[-n:])
        next_item = random.choice(model[start])
        if next_item is None:
            break
        else:
            output.append(next_item)
    return output

# nameless_markov = markov_model(2, words)
# generated_nameless = gen_from_model(2, nameless_markov, ("THE", "NAMELESS"), 200)

# print(" ".join(generated_nameless))

def markov_model_from_sequences(n, sequences):
    model = {}
    for item in sequences:
        add_to_model(model, n, item)
    return model

# button_line = open("/Users/dxu/Desktop/tender_buttons.txt").readlines()

# button_line_words = [line.strip().split() for line in button_line]
# button_line_starts = [item[:2] for item in button_line_words if len(item) >= 2]

# button_line_model = markov_model_from_sequences(2, button_line_words)

# for i in range(10):
#     start = random.choice(button_line_starts)
#     generated = gen_from_model(2, button_line_model, start)
#     print(" ".join(generated))

def markov_generate_from_sequences(n, sequences, count, max_gen = 100):
    starts = [item[:n] for item in sequences if len(item) >= n]
    model = markov_model_from_sequences(n, sequences)
    return [gen_from_model(n, model, random.choice(starts), max_gen)
            for i in range(count)]

# tempers_lines = [line.strip() for line in open("/Users/dxu/Desktop/the_tempers.txt").readlines()]
# button_lines = [line.strip() for line in open("/Users/dxu/Desktop/tender_buttons.txt").readlines()]
# both_lines = tempers_lines + button_lines
# for item in markov_generate_from_sequences(5, both_lines, 20):
#     print("".join(item))

def markov_generate_from_lines_in_file(n, filename, count, level = "char", max_gen=200):
    if level == "char":
        glue = ""
        sequences = [line.strip() for line in open(filename).readlines()]
    elif level == "word":
        glue = " "
        sequences = [line.strip().split() for line in open(filename).readlines()]
    generated = markov_generate_from_sequences(n, sequences, count, max_gen)
    return [glue.join(item) for item in generated]


if __name__ == "__main__":
    # for item in markov_generate_from_lines_in_file(2, "/Users/dxu/Desktop/Py_texts/crash-new.txt", 10, "word"):
    for item in markov_generate_from_lines_in_file(3, "/Users/dxu/Desktop/nmnt-title.txt", 10, "char"):
        print(item)
        print("\n")