import os


class FileHelper:

    def __init__(self, path):
        self.path = path

    def create_directory(self):

        if os.path.exists(self.path):
            return True

        try:
            os.mkdir(self.path)
        except OSError:
            return False

        return True

    def create_put_file(self, file_name, data):
        f = open('%s/%s.txt' % (self.path, file_name), 'w')
        f.write(data)
