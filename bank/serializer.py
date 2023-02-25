import abc
from bank.structure import Personal, Development, Bank

class Serializer(abc.ABC):

    @abc.abstractmethod
    def serialize(self, obj):
        pass

    @abc.abstractmethod
    def deserialize(self, obj):
        pass

class PersonalSerializer(Serializer):
    def serialize(self, obj):
        return{
            "last_name": obj.last_name,
            "position": obj.position
        }

    def deserialize(self, obj):
        return Personal(obj["last_name"], obj["position"])

class DevelopmentSerializer(Serializer):
    def serialize(self, obj):
        personal_serializer = PersonalSerializer()
        result = {
            "development_name": obj.development_number,
            "employee_data": []
        }
        for el in obj:
            result["employee_data"].append(personal_serializer.serialize(el))
        return result

    def deserialize(self, obj):
        personal_serializer = PersonalSerializer()
        result = Development(obj["development_name"])
        for el in obj["development_name"]:
            result.add(personal_serializer.deserialize(el))
        return result

class BankSerializer(Serializer):
    def serialize(self, obj):
        development_serializer = DevelopmentSerializer()
        result = {
            "bank_name": obj.bank_name,
            "developments": []
        }
        new_bank = Bank(obj.bank_name)
        while not obj.is_empty():
            development = obj.pop()
            result["developments"].append(development_serializer.serialize(development))
            new_bank.push(development)
        while not new_bank.is_empty():
            obj.push(new_bank.pop())
        return result

    def deserialize(self, obj):
        development_serializer = DevelopmentSerializer()
        result = Bank(obj["bank_name"])
        obj["developments"].reverse()
        for development in obj["developments"]:
            result.push(development_serializer.deserialize(development))
        return result

class BankListSeralizer(Serializer):
    def serialize(self, obj):
        bank_serializer = BankSerializer()
        result = []
        for element in obj:
            result.append(bank_serializer.serialize(element))
        return result

    def deserialize(self, obj):
        bank_serializer = BankSerializer()
        result = []
        for element in obj:
            result.append(bank_serializer.deserialize(element))
        return result
