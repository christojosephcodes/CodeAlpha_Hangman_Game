import random
import time
import sys

def typing_effect(text, speed=0.015):
    """Prints text to the screen with a clean typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def display_hangman(wrong_guesses):
    """Returns a visual text-based representation of the hangman state."""
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]
    return stages[wrong_guesses]

def play_game():
    # Predefined list of exactly 5 words as per simplified scope constraints
    word_pool = ["python", "coding", "script", "program", "backend"] [cite: 5, 29]
    target_word = random.choice(word_pool) [cite: 32]
    guessed_letters = set()
    incorrect_count = 0
    max_incorrect = 6 [cite: 30]
    
    print("==================================================")
    print("🎯  WELCOME TO THE CODEALPHA HANGMAN GAME  🎯")
    print("==================================================")
    typing_effect("Loading dictionary arrays...\nSetting up execution parameters...\nGame Interface Ready!\n", speed=0.01)
    
    while incorrect_count < max_incorrect: [cite: 32]
        # Print the visual hangman bracket structure
        print(display_hangman(incorrect_count))
        
        # Display the hidden word compilation dynamically (e.g., p y _ h o n)
        display_word = [char if char in guessed_letters else "_" for char in target_word] [cite: 32]
        print(f"📖 Word Progress ➜  {' '.join(display_word)}")
        print(f"🚫 Already Guessed ➜  {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"❤️ Guesses Remaining ➜  {max_incorrect - incorrect_count}\n")
        
        # Win-state validation block
        if "_" not in display_word:
            print("==================================================")
            typing_effect(f"🎉 CONGRATULATIONS! You perfectly deciphered the word: '{target_word.upper()}'!")
            print("==================================================")
            return

        # Core input processing stream
        guess = input("🔤 Guess a letter ➜ ").strip().lower() [cite: 31, 32]
        print() # Line spacing
        
        # Data integrity checks
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Input Execution Error: Please enter exactly one alphabetical character.")
            continue
            
        if guess in guessed_letters:
            print(f"⚠️ Notice: You've already tested the letter '{guess}'. Pick another target.")
            continue
            
        guessed_letters.add(guess) [cite: 32]
        
        # Evaluation conditional loop
        if guess in target_word: [cite: 32]
            print(f"✅ Success! The letter '{guess}' exists in the sequence.")
        else:
            print(f"💥 Miss! The letter '{guess}' is not part of the sequence.")
            incorrect_count += 1 [cite: 30, 32]
            
    # Lose-state termination sequence
    print(display_hangman(incorrect_count))
    print("==================================================")
    typing_effect(f"💥 GAME OVER! You ran out of operational attempts. The word was: '{target_word.upper()}'.")
    print("==================================================")

if __name__ == "__main__":
    play_game()
