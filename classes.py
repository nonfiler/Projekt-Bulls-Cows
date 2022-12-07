import random

class Dictionary:
    def get_isogram(difficulty_level):
        try:
            if(difficulty_level==1):
                with open("python_projekt_zal/dictionary_easy.txt", 'r') as file:
                    get_word = file.read()
            elif(difficulty_level==2):
                with open("python_projekt_zal/dictionary_medium.txt", 'r') as file:
                    get_word = file.read()
            else:
                with open("python_projekt_zal/dictionary_hard.txt", 'r') as file:
                    get_word = file.read()
        except FileNotFoundError:
            print("Couldn't locate file!")   
            return FileNotFoundError 
        to_guess_word = get_word.split(" ")
        to_guess_word = random.choice(to_guess_word)
        return to_guess_word
        
#************************************************************************#
class Validator:
    @staticmethod
    def only_letters(word):
        if word.isalpha():
            # print('Slowo ok')
            return True
        else:
            print('Pamietaj, slowo moze zawierac tylko litery!')
            return False
    #?-----------------------------------------------------------
    def is_isogram(word):
        clean_word = word.lower()
        letter_list = []
        for letter in clean_word:
            if letter in letter_list:
                return False
            letter_list.append(letter)
        return True
    #?---------------------------------------------------
    # @staticmethod
    def check_words_lenght(word, to_guess_word):
        if(len(word) == len(to_guess_word)) == True:
            return True
        else:
            print("Slowa maja rozna dlugosc!")
            return False
    def final_check(word, to_guess_word):
        if(Validator.only_letters(word) and Validator.check_words_lenght(word, to_guess_word) and Validator.is_isogram(word)):
            return True
        else:
            return False
#*************************************************************************#
class Stats:
    def __init__(self, word, cows, bulls):
        self.word = word
        self.cows = cows
        self.bulls = bulls
    def change_stats(word, cows, bulls):
        word.cows += cows
        word.bulls += bulls
    def show_score(obj):
        print(f"Cows: {obj.cows}\tBulls: {obj.bulls}")
#*************************************************************************#   
class Engine(Stats):
    def __init__(self):
        self.difficulty_level = 1
        self.trials = 10
        self.changes = 1
        self.game_work = 1
        self.settings = 2
        self.player_score = []
    #?
    def game_engine(self, player_word, to_guess_word):
        stats = player_word
        stats = Stats(player_word, 0, 0)
        for char in range(len(player_word)):
            if(player_word[char] == to_guess_word[char]): 
                Stats.change_stats(stats,1,0)
            if(player_word[char] in to_guess_word) and (player_word[char] != to_guess_word[char]): #warunek na cow
                Stats.change_stats(stats,0,1)
        return stats
    def choose_difficulty(self):
        print("---------------------------------------------------------")
        self.difficulty_level = int(input("Do wyboru sa trzy poziomy trudnosci:\n- latwy(1), slowa maja po 4 litery\n- sredni(2), slowa maja po 6 liter\n- trudny(3), slowa maja po 8 liter\nCo wybierasz? "))
    #?
    def ile_prob(self):
        self.trials = int(input("Podaj nowa ilosc prob: "))
    #?
    def print_info(self):
        print("---------------------------------------------------------")
        print(f"Aktualne ustawienia gry:\n-trudnosc rozgrywki: {self.difficulty_level}\n-ilosc prob: {self.trials}")
        print("---------------------------------------------------------")
    #?
    def rules(self):
        print("Witaj w grze Cows & Bulls!\nGra bedzie polegac na zgadnieciu slowa ktore jest izogramem, czyli takiego, ktore nie ma powtarzajacych sie liter.\nTwoim zadniem bedzie proba zgadniecia wylosowanego slowa. Jezeli podasz slowo w ktorym jakas litera znajduje sie w wylosowanym\nslowie, ale nie jest na dobrym miejscu, zostanie dodany punkt do pola \"cows\", a jezeli dana litera bedzie w wylosowanym slowie\ni na tym samym miejscu, dostaniesz punkt w kategorii bulls.\nPowodzenia!\n")    
    #?
    def main_menu(self):
        print("---------------------------------------------------------")
        choice = int(input("Witaj! Oto twoje opcje do wyboru:\n1) Pokaz zasady gry\n2) Pokaz akutalne ustawienia\n3) Zmien ustawienia gry\n4) Nowa gra\nCo wybierasz?: "))
        if(choice == 1):
            self.rules()
        elif(choice == 2):
            self.print_info()
        elif(choice == 3):
            settings = int(input("Zmiana ilosci prob - 1\tZmiana poziomu trudnosci - 2: "))
            if(settings == 1):
                self.ile_prob()
            elif(settings == 2):
                self.choose_difficulty()
        elif(choice == 4):
            self.new_game()
    def new_game(self):
        to_guess_word = Dictionary.get_isogram(self.difficulty_level)
        print(f"Ilosc liter w wylosowanym slowie: {len(to_guess_word)}")
        
        while(self.trials>0):
            print("---------------------------------------------------------")
            player_word = str(input("Wprowadz slowo: "))
            Validator.final_check(player_word, to_guess_word)
            self.player_score.append(self.game_engine(player_word, to_guess_word))
            if(to_guess_word == player_word):
                print(f"Zgadles! Twoje slowo: {player_word}, wylosowane slowo: {to_guess_word}")
                self.player_score.pop(0)
                break
            for print_score in self.player_score:
                print(f"{print_score.word} bulls: {print_score.bulls} cows: {print_score.cows}")
            self.trials -= 1
            
            print(f"Pozostala liczba prob: {self.trials}\n*")
            
            if(self.trials<1):
                print(f"Koniec prob! Wylosowane haslo to: {to_guess_word}") 
                self.player_score.pop(0)
            self.player_score.pop(0)
        self.trials = 10
  