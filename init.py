import time
import datetime
import os
import pickle


class Patient:
    """
    A single patient.
    """

    def __init__(self, name, sex, age, id_):
        self.name = name
        self.sex = sex
        self.id_ = id_
        self.phone = set()
        self.history = []
        self.age = age

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
        return self.name == other.name and self.id_ == other.id_


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
        self.num = 0
        if "saved.p" not in os.listdir(path):
            self.PatientList = []
            save = open(os.path.join(path, 'saved.p'), 'wb')
            pickle.dump(self.PatientList, save)
            save.close()
        else:
            save = open(os.path.join(path, 'saved.p'), 'rb')
            self.PatientList = pickle.load(save)
            save.close()

    def add(self, patient):
        """
        add a patient
        :param patient:
        :type patient:
        :return:
        :rtype:
        """
        self.PatientList.append(patient)
        print(self.PatientList)
        self.num += 1
        self.save()

    def save(self):
        """
        save file.
        :return:
        :rtype:
        """
        save = open(os.path.join(r"D:\\", 'saved.p'), 'wb')
        pickle.dump(self.PatientList, save)
        save.close()
