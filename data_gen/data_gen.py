import sys
import json
from data_gen.dataset import Dataset
# read command line arguments
# validate command line arguments
# validate input file
# process input file


def main(input_file):
    # first we are going to load the file and validate it
    with open(input_file) as f:
        json_input = json.load(f)
        errors = validate(json_input)
        if len(errors) > 0:
            # TODO: output errors
            return
        errors = generate(json_input)
        if len(errors) > 0:
            return


def validate(json):
    # accumulate a list of errors
    # if the list is empty continue
    # otherwise print the list of errors
    return []


def generate(json):
    dataset = Dataset(json)
    return dataset.generate()


if __name__ == '__main__':
    main(sys.argv[1])
