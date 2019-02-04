## Time Blocks 

Program działa pod wersją Python 3.6.
Skrypt pozwalający na szybkie, zautomatyzowane tworzenie zadań w kalendarzu google.
Tworzone są eventy w kolejności tak jak w pliku wejściowym. Dodawane do agendy 
w wybranym dniu -> informacja podana wraz z danymi wejściowymi. 

### Wprowadzanie danych:
    1. plik podawany do funkcji main *python timeBlocks.py input_data_as_text*
    2. format zapisu danych: nazwa zadania ;[czas w minutach] np.:
		+ instalacja oprogramowania ;20
		+ medytacja;15
		+ drzemka;25
	3. możliwość zdefiniowania przerw czasowych (nie jako wydarzenie, a odstęp pomiędzy eventami):
		- " --- ; 30 "

### Settings:
    * Możliwość wyboru czy wydarzenia wpisywane będą na dzień obecny, czy jutrzejszy. Klucz "day" może przyjmować wartości: "today" lub "tommorow"
### Futures:
	1. Main future - GUI
    2. Możliwość skonfigurowania zmiennych globalnych (czas przerwy pomiędzy zadaniami itp.) - przechowywane w osobnym pliku ustawień.
		- oddzielna zakładka z wszystkimi zmiennymi defaultowymi do skonfigurowania
	3. Użytkownik wprowadza dane w trybie wizualnym -> konwersja wprowadzonych danych na format dictionary
	4. Sprawdzanie poprawności wprowadzonych danych przed przeniesieniem do kalendarza
	5. Opcja wprowadzenia zadań na wybrany dzień tygodnia z wyświetlaniem mini kalendarza umożliwiającego wskazanie konkretnego dnia.
