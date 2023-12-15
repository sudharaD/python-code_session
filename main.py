from frontend.validators import is_valid_age
from backend.models import Person

age = 28

p = Person("SD")

if is_valid_age(age):
    p.set_age(age)

print(p.get_age())
