import pytest
from main import BooksCollector
class TestBooksCollector:
    # 1.Проверка метода add_new_book - добавление книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Проверка метода get_book_genre - устанавливаем для книги жанр 
    @pytest.mark.parametrize('name, genre', [('Кладбище домашних животных', 'Ужасы')])
    def test_set_book_genre_add_one_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get(name) == 'Ужасы'

     #3. Проверим, что если мы добавляем жанр, которого нет в списке genre, то данный жанр не добавляется
    @pytest.mark.parametrize('name, genre', [('Сумерки', 'Фентези')])
    def test_set_book_genre_not_in_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''   

    #4. Проверим, что у добавленной книги нет жанра 
    @pytest.mark.parametrize('name',['Кот в сапогах'])
    def test_add_new_book_not_book_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_book_genre(name)) == 0

    #5. Книги с возрастным рейтингом отсутствуют в списке книг для детей.
    @pytest.mark.parametrize('name, genre', [('Достать ножи', 'Детективы'), ('Сияние', 'Ужасы')])
    def test_get_books_for_children_not_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == []

    #6. Книги без возрастного рейтинга есть в списке книг для детей
    @pytest.mark.parametrize('name, genre',[('Кот в сапогах', 'Мультфильмы')])
    def test_get_books_for_children_one_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert len(collector.get_books_for_children()) == 1    

    #7. Вывод  списка книг с определённым жанром - метод get_books_with_specific_genre
    @pytest.mark.parametrize('name, genre', [('Худеющий', 'Ужасы'), ('Сияние', 'Ужасы')])
    def test_get_books_with_specific_genre_horror_two_genres(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        add_books = []
        add_books.append(name)
        assert collector.get_books_with_specific_genre(genre) == add_books

    # 8.Проверка метода get_books_with_specific_genre - если добавим книгу с жанром которого нет в списке genre, то данные книги не будут выведены
    @pytest.mark.parametrize('name, genre', [('К центру земли', 'Фентези'), ('Сумерки', 'Фентези')])
    def test_get_books_with_specific_genre_horror_two_genres(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        add_books = []
        add_books.append(name)
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    #9. Проверка метода add_book_in_favorites - добавление книги в избранное
    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 10. Проверка метода delete_book_from_favorites - удаление книги из избранного
    def test_delete_book_from_favorites_add_two_books_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1
