class ToDoModel:
    def __init__(self, title, to_do_id, is_done):
        self.title = title
        self.to_do_id = to_do_id
        self.is_done = is_done

    def to_json(self):
        return {'title': + self.title,
                'id': + self.to_do_id,
                'is_done': self.is_done}


class ToDoDb:
    def __init__(self):
        self.to_dos = []

    def create(self, title):
        new_to_do = ToDoModel(title)
        self.to_dos.append(new_to_do)
        return new_to_do

    def is_done(self, to_do_id):
        to_do = self.to_dos[to_do_id]
        self.to_dos[to_do_id] = ToDoModel(to_do.title)
        return self.to_dos[to_do_id]

    def get_undone(self):
        to_dos = []
        for index in range(0, len(self.to_dos) - 1):
            if not self.to_dos[index].is_done:
                to_dos.append(self.to_dos[index].is_done)
            return to_dos



