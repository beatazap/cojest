import json


class AddableMixin:
    def __add__(self, other):
        cls = type(self)
        return cls(self.value + other.value)

      
class FromJSONMixin:
    def from_json(self, value):
        data = json.loads(value)
        self.value = data['value']
      
      
class ToJsonMixin:
    def to_json(self):
        return json.dumps({'value': self.value})  # bardzo duże uproszczenie jak to powinno działać

    
    
class NumberValue(AddableMixin, FromJSONMixin, ToJsonMixin):
    def __init__(self, value):
        self.value = value

        
class StringValue(AddableMixin, FromJSONMixin, ToJsonMixin):
    def __init__(self, value):
        self.value = value
        
        
n = NumberValue(5)
s = StringValue('Hello World')

# Przetestowanie domieszki ToJsonMixin

print(n.to_json())
print(s.to_json())

# Przetestowanie domieszki AddableMixin
s2 = s + s
n2 = n + n

print(n2.value)
print(s2.value)


n1 = NumberValue(1)

print(n1.value)

# Przetestowanie domieszki FromJsonMixin
n1.from_json('{"value": [1,2,3,4]}')

print(n1.value)
