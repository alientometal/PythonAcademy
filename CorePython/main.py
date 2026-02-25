import argparse

parser = argparse.ArgumentParser(description="Run extraction pipeline.")

parser.add_argument("--source-id", required=True) # Required argument
parser.add_argument("--full-load", action="store_true")

args = parser.parse_args()
print(args.source_id, args.full_load)
