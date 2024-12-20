from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:
    # Тесты на инит класса - для полноты можно было сделать на каждую self переменную класса, но я решил это опустить
    def test_initialization_default_genre_true(self):
        collector = BooksCollector()
        assert collector.genre == [
            "Фантастика",
            "Ужасы",
            "Детективы",
            "Мультфильмы",
            "Комедии",
        ]
        assert isinstance(collector.favorites, list)

    def test_initialization_default_genre_age_rating_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ["Ужасы", "Детективы"]

    # Тест на добавление новой книги с допустимым именем
    def test_add_new_book_valid_name_true(self):
        book_name = "Book1"
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre and collector.books_genre[book_name] == ""

    # Тест на добавление новой книги с недопустимым именем
    @pytest.mark.parametrize(
        "name",
        [
            "",
            "А тут ровно 41 символ-граничное значение!",
            "Имя этой книги слиииииииииииииииииииииииииииииииииииишком",
        ],
    )
    def test_new_book_invalid_name_true(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # Тест на добавление жанра книге по имени книги
    @pytest.mark.parametrize(
        "name, genre", [("Book1", "Фантастика"), ("Book2", "Комедии")]
    )
    def test_set_book_genre_true(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    # Тест на получение жанра книги по имени
    def test_get_book_genre_true(self):
        collector = BooksCollector()
        book_name = "Book1"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест на получение списка книг с определенным жанром
    @pytest.mark.parametrize("genre", ["Фантастика", "Несуществующий"])
    def test_get_books_with_specific_genre_true(self, genre):
        collector = BooksCollector()
        book_name = "Book1"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        if genre in collector.genre:
            assert collector.get_books_with_specific_genre(genre) == ["Book1"]
        else:
            assert collector.get_books_with_specific_genre(genre) == []

    # Тест на получение словаря books_genre
    def test_get_books_genre_true(self):
        collector = BooksCollector()
        book_name = "Book1"
        collector.add_new_book(book_name)
        assert collector.get_books_genre() == {book_name: ""}

    # Тест на получение списка книг для детей
    def test_books_for_children_true(self):
        collector = BooksCollector()
        book_name = ["Book1", "Book2"]
        for name in book_name:
            collector.add_new_book(name)
        # Set genres to only some books
        collector.set_book_genre("Book1", "Ужасы")  # Not for children
        collector.set_book_genre("Book2", "Фантастика")  # For children
        assert collector.get_books_for_children() == ["Book2"]

    # Test adding a book to favorites
    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        book_name = "Book1"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    # Test deleting book from favorites
    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        book_name = "Book1"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites

    # Test getting list of favorite books
    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        book_name = ["Book1", "Book2"]
        for name in book_name:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == book_name
