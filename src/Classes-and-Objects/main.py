class Student:
    """This Is a student class"""


    def __init__(self, name:str, age: int, score: float, tracks:list ) -> None:
        self.__name = name
        self.__age = age
        self.__score = score
        self.__tracks = tracks


    def __str__(self):
        return self.__name

    
    def change_name(self, new_name: str) -> str:
        self.__name = new_name
        return 'Name Changed!!'


    def change_age(self, new_age: str)-> str:

        assert new_age.isdigit, f'new age ({new_age}) cannot be {type(new_age)}'
        
        self.__age = new_age
        return 'Age Changed!!'


    def add_track(self, new_track: list) -> str:
        self.__tracks += new_track
        return 'New track added!!'


    def get_score(self) -> str:
        return self.__score


if __name__ == '__main__':
    Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
n = Bob.change_name("Peter")
a = Bob.change_age('hello')
t = Bob.add_track("UI/UX")