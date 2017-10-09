from random import randint

BATCH_SIZE = 100


def generate_batch():
    batch = []
    for i in range(0, BATCH_SIZE):
        r = randint(0, 100000000)
        batch.append(r)

    return set(batch)


def main():
    batches = [generate_batch() for i in range(0, 10)]
    unique_in_all_count = 0
    unique_elements = batches[0]
    for i in range(1, len(batches)):
        unique_elements = unique_elements.symmetric_difference(batches[i])

    unique_elements = len(unique_elements)
    print("Total unique count in all batches: {}".format(unique_in_all_count))

if __name__ == "__main__":
    main()
