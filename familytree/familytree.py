class Familytree:
    def __init__(self, first, last, age, gender, birth_month, birth_day, birth_year, mother_first, mother_last, father_first, father_last, is_grandkid):
        self.first = first
        self.last = last
        self.name = 'Name: ' + first + ' ' + last
        self.age = age
        self.gender = 'Gender: ' + gender
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.birth_year = birth_year
        self.mother_first = mother_first
        self.mother_last = mother_last
        self.father_first = father_first
        self.father_last = father_last
        self.is_grandkid = 'Grand kid: ' + ' ' + is_grandkid

    def name(self):
        return 'Name: {} {}'.format(self.first, self.last)

    def birthday(self):
        return 'Birthday: {} {}, {}'.format(self.birth_month, self.birth_day, self.birth_year)

    def mother_name(self):
        return 'Mother\'s Name: {} {}'.format(self.mother_first, self.mother_last)

    def father_name(self):
        return 'Father\'s Name: {} {}'.format(self.father_first, self.father_last)

    def child_info(self):
        print("chelsea")