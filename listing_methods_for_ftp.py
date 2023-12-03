import os

def lisint_method_boring():
    def listing():
        path_ = '/FILES_FOR_FTP'
        validators_list = list()
        zip_list = list()

        for item_ in os.listdir('/FILES_FOR_FTP'):
            tmp = item_[-4:]

            if 'zip' in tmp:
                zip_list.append(item_)
            elif 'done' in tmp:
                validators_list.append(item_[:-5])

        return zip_list, validators_list

    def validate(zip_list: list, validators_list: list):

        print(len(zip_list))

        for index1, item1 in enumerate(zip_list):
            if not item1 in validators_list:
                zip_list.pop(index1)


        print(len(zip_list))

        return zip_list

    zip_list, validators_list = listing()
    zip_list = validate(zip_list, validators_list)

    return zip_list

def listing_method_1():
    def listing():
        path_ = '/FILES_FOR_FTP'
        validators_set = set()
        zip_list = dict()

        for item_ in os.listdir('/FILES_FOR_FTP'):
            tmp = item_[-4:]

            if 'zip' in tmp:
                zip_list[item_] = False
            elif 'done' in tmp:
                validators_set.add(item_[:-5])

        return zip_list, validators_set

    def validate(zip_list_: dict, validators_set):
        zip_list_ = zip_list_
        for item in zip_list_.keys():
            if item in validators_set:
                zip_list_[item] = True

        return zip_list_

    zip_list_, validators_set = listing()
    zip_list_ = validate(zip_list_, validators_set)

    return zip_list_