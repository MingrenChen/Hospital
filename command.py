import init

if __name__ == "__main__":
    lst = init.PatientsList()
    lst.add(init.Patient("MingrenChen", "male", 20))
    print(lst.PatientList[0].id_)
