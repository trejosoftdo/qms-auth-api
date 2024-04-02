"""Database seed script
"""

import os
from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder
from . import main


def run():
    """
    Run the seed script
    """

    dir_name = os.path.dirname(os.path.abspath(__file__))
    session = next(main.get_session())
    seeder = Seeder(session)
    entities = load_entities_from_json(f"{dir_name}/data/data.json")
    seeder.seed(entities)
    session.commit()
