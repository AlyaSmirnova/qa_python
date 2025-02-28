import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_books_genre_empty_dictionary_is_true(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_favorites_empty_list_is_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_genre_list_with_data_is_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_with_data_is_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_already_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        collector.add_new_book('Убить пересмешника')
        assert len(collector.books_genre) == 1
        
    @pytest.mark.parametrize('book_name, book_genre, expected_genre', [['Дюна: часть 1', 'Фантастика', 'Фантастика'], ['Дневник Бриджит Джонс', 'Комедии', 'Комедии']])

    def test_set_book_genre_with_correct_name_and_valid_genre_is_success(self, book_name, book_genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == expected_genre

    def test_get_book_genre_with_correct_name_return_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна: часть 1')
        collector.set_book_genre('Дюна: часть 1', 'Фантастика')
        assert collector.get_book_genre('Дюна: часть 1') == 'Фантастика'

    @pytest.mark.parametrize('genre, expected_books', [['Фантастика', ['Дюна: часть 1']], ['Комедии', ['Дневник Бриджит Джонс']]])

    def test_get_books_with_specific_genre_valid_names_and_genres_return_existing_genres(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Дюна: часть 1')
        collector.set_book_genre('Дюна: часть 1', 'Фантастика')
        collector.add_new_book('Дневник Бриджит Джонс')
        collector.set_book_genre('Дневник Бриджит Джонс', 'Комедии')

        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_empty_dictionary_is_true(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_genre_not_empty_dictionary_is_true(self):
        collector= BooksCollector()
        collector.add_new_book('Голубые таблетки')
        collector.set_book_genre('Голубые таблетки', 'Комедии')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        books_in_dictionary = {'Голубые таблетки': 'Комедии', 'Оно': 'Ужасы'}
        assert collector.get_books_genre() == books_in_dictionary

    def get_books_for_children_with_not_for_children_genres_is_restricted(self):
        collector = BooksCollector()
        collector.add_new_book('Мизери')
        collector.set_book_genre('Мизери', 'Ужасы')
        assert collector.get_books_for_children() == []

    @pytest.mark.parametrize('book_name', ['Острые предметы', 'Безмолвный пациент', 'Каштановый человечек'])

    def test_add_book_in_favorites_book_in_books_genre_is_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    @pytest.mark.parametrize('book_name', ['Острые предметы', 'Безмолвный пациент', 'Каштановый человечек'])
    def test_delete_book_from_favorites_three_books_in_favorites_one_book_is_deleted(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites('Каштановый человечек')
        assert 'Каштановый человечек' not in collector.favorites

    def test_get_list_of_favorites_books_with_three_books_in_favorites_is_true(self):
        collector = BooksCollector()
        collector.add_new_book('Острые предметы')
        collector.add_new_book('Оно')
        collector.add_new_book('Голубые таблетки')
        collector.add_book_in_favorites('Острые предметы')
        collector.add_book_in_favorites('Голубые таблетки')

        assert collector.get_list_of_favorites_books() == ['Острые предметы', 'Голубые таблетки']
