## Sprint_4
Несколько автотестов для приложения BookCollector.

### Автотесты
- пример автотеста для метода add_new_book(self,name)
- автотесты для метода __init__
- автотест для метода add_new_book(self, name): проверка случая, когда книга уже была добавлена в словарь books_genre
- позитивный автотест для метода set_book_genre(self,name,genre) с использованием параметризации: книга есть в словаре books_genre, а жанр в списке genre
- позитивный автотест для метода get_book_genre(self,name)
- позитивный автотест для метода get_books_with_specific_genre(self,genre) с использованием параметризации
- автотест для метода get_books_genre(self): проверка случая, когда словарь books_genre пустой
- автотест для метода get_books_genre(self): проверка случая, когда словарь books_genre заполнен
- негативный автотест для метода get_books_for_children(self): проверка случая, когда у книги есть возрастной рейтинг
- автотест для метода add_book_in_favorites(self, name) с использованием параметризации
- автотест для метода delete_book_from_favorites(self, name) с использованием параметризации
- автотест для метода get_list_of_favorites(self)