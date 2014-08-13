import argparse
from arnold import main
from fish import db

MIGRATION_PATH = "fish/migrations"
parser = argparse.ArgumentParser(
    description="down up"
)
parser.add_argument('direction', help='migration direction')


args = parser.parse_args()
main(
    direction=args.direction,
    database=db,
    directory=MIGRATION_PATH,
    migration_module="fish.migrations"
)
