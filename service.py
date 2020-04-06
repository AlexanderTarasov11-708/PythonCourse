from model import ToDoDb


class ToDoService:
    def __init__(self):
        self.db = ToDoDb()

    def create(self, params):
        result = self.db.create(params['title'])
        return result

    def done(self, to_do_id):
        return self.db.is_done(to_do_id)

    def get_undone(self):
        to_dos = self.db.get_undone()
        string = "{"
        for index in range(0, len(to_dos) - 1):
            string += to_dos[index].to_json + ','
        string += '}'
        return string
