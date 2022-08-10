import argparse
import datetime
import json
import pprint
import jsonschema


def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_description',
                        type=str,
                        help='File dataset_description.json with metadata.')
    args = parser.parse_args()
    return args


def validate_metadata():
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


def add_additional_info():
    metadata["_version"] = "1.0.0"
    metadata["_created"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


if __name__ == "__main__":
    args = load_arguments()
    metadata = json.loads(open(args.dataset_description, "r").read())
    validate_metadata()
    add_additional_info()
