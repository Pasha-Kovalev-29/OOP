import datetime
import math


class Employee:
    def __init__(self, name, email, zp_day, days):
        self.name = name
        self.email = email
        self.validation()
        self.zp_day = zp_day
        self.days = days
        self.save_email()

    def save_email(self):
        with open('email.txt', 'a+') as fp:
            fp.write(self.email + '\n')

    def validation(self):
        with open('email.txt') as fp:
            if self.email in fp.read():
                raise ValueError('Email is already in use.')

    @property
    def full_info(self):
        return f"Class name: {self.__class__.__name__}, Name: {self.name}, Number of days worked: {self.working_days()} "

    def work(self):
        return "I come to the office"

    @staticmethod
    def working_days():
        first_data = datetime.date.today() - datetime.timedelta(days=datetime.date.today().day)
        data_now = datetime.date.today()
        delta = datetime.timedelta(1)

        days = 0
        while first_data != data_now:
            if data_now.isoweekday() not in (6, 7):
                days += 1
            data_now -= delta
        return days

    def cheak_salary(self):
        zp_now = self.working_days() * self.zp_day
        zp_month = Employee.zp_month_calc(self)
        return f"Зарплата за месяц: {zp_month}. Зарплата на текущий рабочий день: {zp_now}"

    def zp_month_calc(self):
        return self.zp_day * self.days

    def __gt__(self, other):
        return self.zp_month_calc() > other.zp_month_calc()

    def __ge__(self, other):
        return self.zp_month_calc() >= other.zp_month_calc()

    def __lt__(self, other):
        return self.zp_month_calc() < other.zp_month_calc()

    def __le__(self, other):
        return self.zp_month_calc() <= other.zp_month_calc()

    def __eq__(self, other):
        return self.zp_month_calc() == other.zp_month_calc()

    def __ne__(self, other):
        return self.cheak_salary() != other.cheak_salary()


class Recruiter(Employee):

    def work(self):
        return 'I come to the office and start to hiring.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"


class Programmer(Employee):

    def __init__(self, name, email, zp_day, days, tech_stack):
        """added skills"""
        super().__init__(name, email, zp_day, days)
        self.tech_stack = tech_stack

    def work(self):
        return 'I come to the office and start to coding.'

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"

    """comparison by skills """

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __add__(self, other):
        """combining two programmers """
        tech_stack = self.tech_stack | other.tech_stack
        name = self.name + other.name
        email = self.name + other.name + '@gmail.com'
        zp_day = self.zp_day + other.zp_day
        day = math.ceil((self.days + other.days) / 2)
        return Programmer(name, email, zp_day, day, tech_stack)


class Candidate():

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException("I'm not hired yet,lol")

    @classmethod
    def create_candidates(cls, file):
        with open(file) as cand:
            lines = cand.readlines()[1:]
            for i in lines:
                candidat = i.split(',')
                name = candidat[0]
                email = candidat[1]
                technologies = set(candidat[2].split('|'))
                main_skill = candidat[3]
                main_skill_grade = candidat[4]
                a = Candidate(name, email, technologies, main_skill, main_skill_grade)
                print(a.__dict__)


class Vacancy():

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


print(Candidate.create_candidates)


class UnableToWorkException(Exception):
    pass
