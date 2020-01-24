stu=["John","Angel","Anna","Krishna","Jacob","Anita","Alina","Anjali","Stan","Kookie"]
name=set(stu)
pas=["Angel","Johnny","Krishna","Anjali"]
ok=set(pas)
fail=name.difference(ok)
print("Students that failed are",fail)