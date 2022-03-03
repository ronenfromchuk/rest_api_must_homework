from logger import Logger

class DbRepo:
    def __init__(self, local_session):
        self.local_session = local_session
        self.logger = Logger.get_instance()

    def get_all(self, table_class):
        return self.local_session.query(table_class).all()

    def add(self, one_row):
        self.local_session.add(one_row)
        self.local_session.commit()
        print('row has been added!')

    def update_by_id(self, table_class, id_column_name, id, data):
        self.local_session.query(table_class).filter(id_column_name == id).update(data)
        self.local_session.commit()
        print(f'updated by id={id}')

    def delete_by_id(self, table_class, id_column_name, id):
        self.local_session.query(table_class).filter(id_column_name == id).delete(synchronize_session=False)
        self.local_session.commit()
        self.logger.logger.warning(f'deleting from table {table_class}.')
        print(f'deleted by id={id}')

    def get_by_id(self, table_class, id):
        return self.local_session.get(table_class,id)