from datalib.import_xlsx import Data


if __name__ == '__main__':

    print(F'Список файлов {Data.get_files()}')
    print(F'Список данных {Data.get_data()}')


