from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "admin"

    def has_permission(self, permission):
        return True  


class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "regular"

    def has_permission(self, permission):
        permisos_permitidos = ["read"]
        return permission in permisos_permitidos

user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))  
print(user2.has_permission("delete"))  
print(user2.has_permission("read"))    