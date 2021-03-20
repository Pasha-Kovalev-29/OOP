import models as mod


def main():
    ivan = mod.Recruiter("Ivan", 'ivan@gmail.com', 100, 23)
    print(ivan)
    alex = mod.Programmer("Alex", 'alex@gmail.com', 200, 23, {'knowledge of English ', 'Python', 'JS', 'Git', 'html&css'})
    print(alex)
    alesha = mod.Programmer("Alesha", 'alesha@gmail.com', 200, 23, {'knowledge of English ', 'Python', 'Flask', 'Django'})
    print(alesha)
    vitalik = mod.Candidate('Vitalik', 'vitos@gmail.com', {'Python', 'Git', 'Postgresql'}, 'Python', 'Middle')
    petr = mod.Candidate('Petr', 'petos@gmail.com', {'Java', 'Git', 'Postgresql'}, 'Java', 'Senior')
    python_vacancy = mod.Vacancy('Vacancy Python', 'Python', 'Middle')
    java_vacancy = mod.Vacancy('Vacancy Java', 'Java', 'Senior')


if __name__ == '__main__':
    main()
