from abc import ABC, abstractmethod
from dicttoxml import dicttoxml
import json


class UploadFormat(ABC):
    def dump(self, obj, fp):
        with open(fp, "w") as fp:
            fp.write(self.dumps(obj))

    @abstractmethod
    def dumps(self, obj):
        pass


class LoadFormat(ABC):
    @abstractmethod
    def load(self, fp):
        pass


class JsonSerializer(UploadFormat, LoadFormat):
    def dumps(self, obj):
        return json.dumps(obj)

    def load(self, fp):
        with open(fp, 'r') as fp:
            return json.load(fp)


class XmlSerializer(UploadFormat):
    def dumps(self, obj):
        xml = dicttoxml(obj, custom_root='rooms', attr_type=False, item_func=lambda x: x[:-1])
        xml_decode = xml.decode()
        return xml_decode
