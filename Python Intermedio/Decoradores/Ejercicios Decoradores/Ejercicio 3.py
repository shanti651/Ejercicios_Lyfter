from datetime import date

class User():
    def __init__(self, name, date_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year - self._date_of_birth.year
            - ((today.month, today.day) < (self._date_of_birth.month, self._date_of_birth.day))
        )


def mayor_edad(funcion_original):
    def funcion_decorada(user):
        if user.age < 18:
            raise ValueError(f"{user._name} NO es mayor de edad")
        return funcion_original(user)
    return funcion_decorada


@mayor_edad
def validar(user):
    print(f"{user._name} es mayor")


adulto = User("Carlos", date(1995, 3, 15))
menor = User("Andrea", date(2015, 6, 1))

validar(adulto)   
validar(menor)   