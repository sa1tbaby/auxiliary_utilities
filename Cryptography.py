from cryptography.fernet import Fernet

class Encrypt:
    key_path = 'filekey.key'

    def __init__(self, key_path = None):

        if key_path == None:
            key_path = Encrypt.key_path

        try:
            self.__key = self.open_file(key_path)
            self.__fernet_key = Fernet(self.__key)
        except FileNotFoundError:
            pass

        self.__file_name = None
        print(self.__file_name)
        self.__exc = None


    def open_file(self, path):
        with open(f'{path}', 'rb') as file:
            text = file.read()
            file.close()

        self.__exc = path[path.find('.'):]
        self.__file_name = path[:path.find('.')]

        return text

    def save_file(self, path, text):
        with open(f'{path}', 'wb') as file:
            file.write(text)
            file.close()

        return True

    def encrypting_file(self, path_from, new_path = None):
        text = self.open_file(path_from)
        encrypted = self.__fernet_key.encrypt(text)

        if new_path == None:
            new_path = self.__file_name + '_encrypted' + self.__exc

        self.save_file(new_path, encrypted)

        return True

    def decrypting_file(self, path_from, new_path = None):
        text = self.open_file(path_from)
        decrypted = self.__fernet_key.decrypt(text)

        if new_path == None:
            new_path = self.__file_name + '_decrypted' + self.__exc

        self.save_file(new_path, decrypted)

        return True

    def generate_key(self, path = 'filekey.key'):
        key = Fernet.generate_key()
        self.save_file(path, key)

    @property
    def key(self):
        return self.__key

    @property
    def exc(self):
        return self.__exc

    @property
    def file_name(self):
        return self.__file_name

if __name__ == "__main__":

    prog_status = False
    launch_obj = Encrypt()

    while prog_status == False:

        print('Which method your want?'
              '\n1.Encrypt'
              '\n2.Decrypt'
              '\n3.Generate key')

        method = int(input('\nPlz enter number of method: '))

        if method == 1 or method == 2 or method == 3:
            path = input('\nPlz enter path:')

            if method == 1:
                launch_obj.encrypting_file(path)
            elif method == 2:
                launch_obj.decrypting_file(path)
            elif method == 3:
                launch_obj.generate_key(path)

            prog_status = True

        else:
            print('\nInvalid number of method!\n')