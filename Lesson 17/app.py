import models as mod

if __name__ == '__main__':
    ivan = mod.Recruiter("Ivan", 100, 23)
    print(ivan)
    alex = mod.Programmer("Alex", 200, 23, {'knowledge of English ', 'Python', 'JS', 'Git', 'html&css'})
    print(alex)
    alesha = mod.Programmer("Alesha", 200, 23, {'knowledge of English ', 'Python', 'Flask', 'Django'})
    print(alesha)
    vitalik= mod.Candidate('Vitalik', 'vitos@gmail.com', 'Python', 'Python', 'Python')
    petr=mod.Candidate('Petr', 'petos@gmail.com', 'Java', 'Java', 'Java')
    python_vacancy=mod.Vacancy('Python', 'Python', 'Python')
    java_vacancy= mod.Vacancy('Java', 'Java', 'Java')
