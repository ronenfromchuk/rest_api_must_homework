from Customers import Customers
from DbRepo import DbRepo
from db_config import local_session, create_all_entities

repo = DbRepo(local_session)

create_all_entities()