import random

class Reservoir(object):
    """
    if you have to select data randomly from a big data set which you don't know its exact count, 
    reservior sampling algorithm may be your best choice, you deserve a try.
    """
    def __init__(self):
        pass

    def do_sampling(self, input_stream,  size):
        """
        sampling from a data stream
        para:
            input_stream -- stdin or file stream
            size -- sampling count

        return:
            list selected randomly
            """

        selected_lines = []
        current_index = 0
        for line in input_stream:
            current_index += 1
            if len(selected_lines) < size:
                selected_lines.append(line.strip())
                continue
            random_index = int(random.uniform(0, current_index))
            if random_index < size:
                selected_lines[random_index] = line.strip()

        return selected_lines


if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser(description='reservoir_sampler')
    parser.add_argument('--size', type=int,
                        help='sampling size from stream')
    args = vars(parser.parse_args())
    reservoir_sampler = Reservoir()
    selected_lines = reservoir_sampler.do_sampling(sys.stdin, args['size'])
    for line in selected_lines:
        print(line)
