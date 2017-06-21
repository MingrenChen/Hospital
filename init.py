import time
import datetime
import os
import pickle


class Patient:
    """
    A single patient.
    """
    __hash__ = object.__hash__

    def __init__(self, name, sex, age, id_):
        self.name = name
        self.sex = sex
        self.id_ = id_
        self.phone = set()
        self.history = []
        self.age = age

    def __repr__(self):
        return "{}: {}, age {}".format(self.name, self.sex, self.age)

    def set_phone(self, phone):
        """
        set a patient's phone number.
        :param phone: phone number
        :type phone: int
        :return: None
        :rtype: None
        """
        self.phone.add(phone)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and\
               self.sex == other.sex and self.id_ == other.id_


class Histroy:
    """
    A Patient's history.
    """
    def __init__(self, num):
        self.num = num
        self.diagnose = ""
        self.time = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')

    def diagnosed(self, d):
        """
        diagnose a patient.
        :param d: disease
        :type d: str
        :return: None
        :rtype: None
        """
        self.diagnose = d


class PatientsList:
    """
    A collections contains all the patient.
    """

    def __init__(self):
        path = r"D:\\"
        if "saved.p" not in os.listdir(path):
            self.PatientList = []
            save = open(os.path.join(path, 'saved.p'), 'wb')
            pickle.dump(self.PatientList, save)
            save.close()
        else:
            save = open(os.path.join(path, 'saved.p'), 'rb')
            self.PatientList = pickle.load(save)
            save.close()

    def new(self, name, sex, age):
        """

        :param name:
        :type name:
        :param sex:
        :type sex:
        :param age:
        :type age:
        :return:
        :rtype:
        """
        length = len(self.PatientList)
        self.PatientList.append(Patient(name, sex, age, length + 1))
        self.save()

    def remove(self, patient):
        """
        remove a patient
        :param patient:
        :type patient:
        :return:
        :rtype:
        """
        self.PatientList.remove(patient)


    def save(self):
        """
        save file.
        :return:
        :rtype:
        """
        save = open(os.path.join(r"D:\\", 'saved.p'), 'wb')
        pickle.dump(self.PatientList, save)
        save.close()

    def __repr__(self):
        return str(self.PatientList)

    def __str__(self):
        return str(self.PatientList)
