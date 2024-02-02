"""Database seed script
"""

import os
from sqlalchemyseed import Seeder
from . import main
from . import models

def run():
    """
    Run the seed script
    """
  
    dir_name = os.path.dirname(os.path.abspath(__file__))
    seeder = Seeder(main.session)
    seeder.add_entity(models.Status, f"{dir_name}/data/statuses.json")
    seeder.seed()
    main.session.commit()
