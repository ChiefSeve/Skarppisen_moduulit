# Module 11

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, writer, page_count, name):
        self.page_count = page_count
        self.writer = writer
        super().__init__(name)

    def print_info(self):
        print(self.writer, self.page_count, self.name)


class Magazine(Publication):
    def __init__(self, editor_in_chief, name):
        self.editor_in_chief = editor_in_chief
        super().__init__(name)

    def print_info(self):
        print(self.editor_in_chief, self.name)


def main_app():
    new_book = Book('Rosa Liksom', 200, 'Hytti n:o 6')
    new_magazine = Magazine('Aki Hyyppä', 'Aku Ankka')
    new_book.print_info()
    new_magazine.print_info()


main_app()
