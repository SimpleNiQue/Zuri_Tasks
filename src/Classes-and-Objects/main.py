class Student:
    """This Is a student class"""


    def __init__(self, name:str, age: int, score: float, tracks:list ) -> None:
        self.__name = name
        self.__age = age
        self.__score = score
        self.__tracks = tracks


    def __repr__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nScore: {self.__score}\nTracks: {self.__tracks}"

    
    def change_name(self, new_name: str) -> str:
        self.__name = new_name
        return self.__name


    def change_age(self, new_age: int)-> int:
        assert int(new_age), 'new age '+new_age+'cannot be '+type(new_age)
        
        self.__age = new_age
        return self.__age


    def add_track(self, new_track: list) -> str:
        self.__tracks.append(new_track)
        return self.__tracks


    def get_score(self) -> str:
        return self.__score


if __name__ == '__main__':
    Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
n = Bob.change_name("Peter")
a = Bob.change_age('hello')
t = Bob.add_track("UI/UX")