import random

def funny_number_guessing_game():
    target = random.randint(1, 100)
    max_attempts = 7  # Fixed inconsistency and made it reasonable for kids
    attempts = 0
    
    print("🎪 Welcome to Captain Giggles' SUPER SILLY Number Guessing Game! 🎪")
    print("=" * 60)
    print("🤡 Captain Giggles says: 'I'm thinking of a number between 1 and 100!'")
    print("🎯 You have 7 chances to guess it!")
    print("🎈 I'll give you silly hints to help you out!")
    print("Let the giggles begin! 🎉\n")
    
    funny_responses_too_low = [
        "🐸 Ribbit! That's too low! My number is doing jumping jacks higher up!",
        "🚀 Whoosh! Your guess needs to blast off higher!",
        "🦒 Even a giraffe would say that's too low!",
        "🏔️ Climb higher, mountain climber!",
        "🎈 Your guess needs more helium to float up!",
        "🚁 Helicopter up, up, and away!"
    ]
    
    funny_responses_too_high = [
        "🐢 Slow down there, speedy turtle! That's too high!",
        "🪂 Parachute down! Your guess is flying too high!",
        "🦘 Hop down a bit, bouncy kangaroo!",
        "⛰️ Come down from that mountain peak!",
        "🎢 Wheee! Slide down the roller coaster!",
        "🕳️ Dig down like a happy mole!"
    ]
    
    while attempts < max_attempts:
        try:  # Added proper error handling
            print(f"🎯 Attempt {attempts + 1} of {max_attempts}")
            guess = input("🤔 What's your guess, genius? (1-100): ")
            guess = int(guess)
            
            if guess >= 1 and guess <= 100:
                attempts += 1
                
                if guess == target:
                    print(f"🎉 HOORAY! 🎉 You found my secret number {target}!")
                    print(f"🏆 You did it in {attempts} attempts! You're a SUPER GUESSER!")
                    print("🎪 Captain Giggles is doing a happy dance! 💃🕺")
                    if attempts <= 3:
                        print("🧠 WOW! You must be a mind reader!")
                    elif attempts <= 5:
                        print("👏 Fantastic job, number detective!")
                    else:
                        print("🎯 Great persistence, never-give-up champion!")
                    break
                elif guess < target:
                    print(random.choice(funny_responses_too_low))
                else:
                    print(random.choice(funny_responses_too_high))
                    
                remaining = max_attempts - attempts
                if remaining == 1:
                    print("⚡ Last chance! You can do this, superstar!")
                elif remaining == 2:
                    print("🔥 Only 2 left! You're getting warmer!")
                elif remaining <= 3:
                    print(f"💪 {remaining} attempts left! Don't give up!")
                    
            else:
                print("🤪 Oopsie! Captain Giggles only knows numbers between 1 and 100!")
                print("🎭 Try again with a number in the magic range!")
                
        except ValueError:  # Handle non-number inputs gracefully
            print("🙃 Silly goose! That's not a number!")
            print("🔢 Captain Giggles needs actual numbers like 42 or 73!")
            print("🎪 Try typing just numbers, no letters or symbols!")
            
    else:
        print(f"🎪 Game Over! The secret number was {target}!")
        print("🤡 Captain Giggles says: 'Good try, brave adventurer!'")
        print("🎈 Want to play again? I have LOTS more silly numbers!")
        print("🌟 Remember: Every guess makes you smarter!")

if __name__ == "__main__":
    print("🎮 Starting the Giggle Game Engine...")
    print("🎪 Loading Captain Giggles...")
    print("✨ Sprinkling magic number dust...")
    print()
    funny_number_guessing_game()
    print("\n🎪 Thanks for playing with Captain Giggles! 🎪")
