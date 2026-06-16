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
    # Expanded easy word pool with 15 words and direct hints
    easy_word_pool = [
        # Fruits & Food
        {"word": "apple", "hint": "A crisp, sweet fruit that keeps the doctor away"},
        {"word": "banana", "hint": "A long, yellow fruit that monkeys love to peel"},
        {"word": "pizza", "hint": "A popular cheesy Italian food delivered in a square box"},
        {"word": "burger", "hint": "A fast-food favorite with a patty inside a round bun"},
        {"word": "orange", "hint": "A citrus fruit named after its own vibrant color"},
        
        # Animals
        {"word": "monkey", "hint": "A playful, tree-climbing animal that loves bananas"},
        {"word": "kitten", "hint": "A small, adorable, and furry baby cat"},
        {"word": "dolphin", "hint": "An intelligent, friendly marine mammal known for jumping out of the ocean"},
        
        # Objects & Clothing
        {"word": "guitar", "hint": "A musical instrument with six strings you can strum"},
        {"word": "jacket", "hint": "An item of clothing you wear to stay warm outside"},
        {"word": "pencil", "hint": "A wooden tool with graphite used for writing or sketching"},
        {"word": "camera", "hint": "A device used to capture pictures and record videos"},
        {"word": "watch", "hint": "A small device worn on your wrist to keep track of time"},
        
        # Places & Nature
        {"word": "school", "hint": "A place where students go to learn from teachers"},
        {"word": "desert", "hint": "A vast, hot, and sandy region with very little water"}
    ]
    
    # Randomly select a word mapping
    selected_pair = random.choice(easy_word_pool)
    target_word = selected_pair["word"]
    category_hint = selected_pair["hint"]
    
    guessed_letters = set()
    incorrect_count = 0
    max_incorrect = 6
    
    print("==================================================")
    print("🎯  WELCOME TO THE CODEALPHA HANGMAN GAME  🎯")
    print("==================================================")
    typing_effect("Loading expanded word banks...\nConfiguring user interface parameters...\nGame Ready!\n", speed=0.01)
    
    # Display the hint explicitly right at the start
    print(f"💡 HINT FOR THIS ROUND ➜  {category_hint}\n")
    print("==================================================")
    
    while incorrect_count < max_incorrect:
        # Print the visual hangman bracket structure
        print(display_hangman(incorrect_count))
        
        # Display the hidden word compilation dynamically
        display_word = [char if char in guessed_letters else "_" for char in target_word]
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
        guess = input("🔤 Guess a letter ➜ ").strip().lower()
        print() 
        
        # Data integrity checks
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Input Execution Error: Please enter exactly one alphabetical character.")
            continue
            
        if guess in guessed_letters:
            print(f"⚠️ Notice: You've already tested the letter '{guess}'. Pick another target.")
            continue
            
        guessed_letters.add(guess)
        
        # Evaluation conditional loop
        if guess in target_word:
            print(f"✅ Success! The letter '{guess}' exists in the sequence.")
        else:
            print(f"💥 Miss! The letter '{guess}' is not part of the sequence.")
            incorrect_count += 1
            
    # Lose-state termination sequence
    print(display_hangman(incorrect_count))
    print("==================================================")
    typing_effect(f"💥 GAME OVER! You ran out of operational attempts. The word was: '{target_word.upper()}'.")
    print("==================================================")

if __name__ == "__main__":
    play_game()
