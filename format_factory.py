from formats import Json, Xml


class FormatFactory:
    def __init__(self):
        self.formats = {
            'json': Json(),
            'xml': Xml(),
        }

    def set_format(self, name, value):
        self.formats.setdefault(name, value)

    def get_format(self, name):
        format = self.formats.get(name)
        if not format:
            raise ValueError()
        else:
            return format
