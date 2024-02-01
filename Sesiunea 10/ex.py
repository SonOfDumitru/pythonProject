class Sorin:
    name = "So'"
    age = 35
    wife = 'Sisi'
    year = 1988

    def __init__(self, job , foot):
        self.job = job
        self.foot = foot


s = Sorin(job= "QA",foot=42)
s2 = Sorin(foot=43333, job="MK")

print(s.age,s.wife,s.job, s.foot)
print(s2.foot,s2.wife)

s3 =Sorin
s3.name = "Puffy"
print(s3.name, s.job)
