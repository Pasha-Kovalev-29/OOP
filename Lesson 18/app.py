import models as mod
import logging
import datetime

logging.basicConfig(filename="logs.py", datefmt=datetime.datetime.today(), level = logging.INFO)

def main():
    try:
        ivan = mod.Recruiter("Ivan", 'ivan@gmail.com', 100, 23)
        print(ivan)
        alex = mod.Programmer("Alex", 'alex@gmail.com', 200, 23, {'knowledge of English ', 'Python', 'JS', 'Git', 'html&css'})
        print(alex)
        alesha = mod.Programmer("Alesha", 'alexsei@gmail.com', 200, 23, {'knowledge of English ', 'Python', 'Flask', 'Django'})
        print(alesha)
        vitalik = mod.Candidate('Vitalik', 'vitos@gmail.com', {'Python', 'Git', 'Postgresql'}, 'Python', 'Middle')
        petr = mod.Candidate('Petr', 'petos@gmail.com', {'Java', 'Git', 'Postgresql'}, 'Java', 'Senior')
        python_vacancy = mod.Vacancy('Vacancy Python', 'Python', 'Middle')
        java_vacancy = mod.Vacancy('Vacancy Java', 'Java', 'Senior')
        alfa=alex+alesha
        print(alfa)

    except Exception as e:
        with open('logs.py', 'a+') as fh:
            fh.write(str(datetime.datetime.today()) + ' ')
        logging.exception(e)


if __name__ == '__main__':
    main()
