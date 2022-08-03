import argparse
import json
import jsonschema
import pprint


def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_description',
                        type=str,
                        help='File dataset_description.json with metadata.')
    args = parser.parse_args()
    return args


def validate_metadata(metadata):
    json_scheme = json.loads(open("scheme_mafil.json", "r").read())
    validator = jsonschema.Draft202012Validator(json_scheme)
    errors = sorted(validator.iter_errors(metadata))
    if not errors:
        pprint.pprint(metadata)
        return True
    else:
        print("Error! Dataset_description.json file is not valid!\n\nErrors:")
        for error in errors:
            print(error.message)
        print("\n")


if __name__ == "__main__":
    args = load_arguments()
    metadata = json.loads(open(args.dataset_description, "r").read())
    validate_metadata(metadata, json_scheme)
