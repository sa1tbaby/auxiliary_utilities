import os

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