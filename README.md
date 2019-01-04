## Time Blocks 

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

### Futures:
    1. Skrypt działa w trybie interaktywnym, tzn. po odpaleniu jest możliwość wpisywania zadanie po zadaniu (wraz, z przedziałem czasowym)
        * akceptacja przez wciśniecie klawisza enter
        * skrypt na bieżąco dodaje zadania do kalendarza
    2. możliwość skonfigurowania zmiennych globalnych (czas przerwy pomiędzy zadaniami itp.) - przechowywane w osobnym pliku ustawień.
