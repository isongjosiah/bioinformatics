import os.path
import sys
import matplotlib.pyplot as plt


def plot_skew(index_list: list, skew_list: list):
    plt.plot(index_list, skew_list)
    plt.show()


def minimum_skews(genome: str) -> list:
    """
    minimum_skews functions finds out the position in the genome with the minimum skew in an attempt to identify the
    ori region by taking into account the skew value of the genome Params: genome(str): The genome on which the
    computation is to be performed on Returns minimum_index(list): The indexes relative to the starting point where
    the minimum skew ws observed.
    """
    skew_value: int = 0
    index_list: list = []
    skew_list: list = []
    skew_dict: dict = {}
    for index, base in enumerate(genome):
        if base == "G":
            skew_dict[index + 1] = skew_value + 1
            skew_list.append(skew_value + 1)
            skew_value += 1
            index_list.append(index + 1)
        if base == "C":
            skew_dict[index + 1] = skew_value - 1
            skew_list.append(skew_value - 1)
            skew_value -= 1
            index_list.append(index + 1)
    minimum = min(skew_dict.values())
    min_index = [index for index, skew in skew_dict.items() if skew == minimum]
    print("minimum index: ", min_index)
    plot_skew(index_list, skew_list)
    return min_index


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python minimum_skew.py genome")
        sys.exit()
    sequence = sys.argv[1]

    # if entry is a file, read content of file
    if os.path.isfile(sequence):
        if os.path.exists(sequence):
            with open(sequence) as f:
                sequence = f.read().replace('\n', '')
        else:
            print(f"File {sequence} does not exist")
            sys.exit()

    mi = minimum_skews(sequence)
    print(f"minimum index of genome is {mi}")
