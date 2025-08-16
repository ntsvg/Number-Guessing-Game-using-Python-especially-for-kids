import random

def funny_number_guessing_game():
    target = random.randint(1, 100)
    max_attempts = 7  
    attempts = 0
    
    print("⚓ Welcome to Captain NTSVG's Fun Number Game! ⚓")
    print("=" * 50)
    print("🏴‍☠️ Captain NTSVG says: 'Hi there! I'm thinking of a number from 1 to 100!'")
    print("🎯 You get 7 tries to guess it!")
    print("🗺️ I'll help you with hints!")
    print("Let's play! ⛵\n")
    
    funny_responses_too_low = [
        "🐙 Too small! My number is bigger!",
        "⚓ Go higher! Try a bigger number!",
        "🦜 My bird says that's too low!",
        "🏔️ Think bigger! Go up!",
        "⛵ Try a higher number!",
        "🌊 Go up like a big wave!"
    ]
    
    funny_responses_too_high = [
        "🐢 Too big! My number is smaller!",
        "🪂 Come down! That's too high!",
        "🦘 Hop down! Try a smaller number!",
        "⛰️ Come down from up there!",
        "🎢 Go down like a slide!",
        "🕳️ Dive down! Try lower!"
    ]
    
    while attempts < max_attempts:
        try:
            print(f"🎯 Try number {attempts + 1} of {max_attempts}")
            guess = input("🤔 What number do you think it is? (1-100): ")
            guess = int(guess)
            
            if guess >= 1 and guess <= 100:
                attempts += 1
                
                if guess == target:
                    print(f"🎉 YES! You got it! The number was {target}!")
                    print(f"🏆 You did it in {attempts} tries! You're awesome!")
                    print("⚓ Captain NTSVG is so happy! 💃🕺")
                    if attempts <= 3:
                        print("🧠 Wow! You're really smart!")
                    elif attempts <= 5:
                        print("👏 Great job! You did amazing!")
                    else:
                        print("🎯 Good work! You never gave up!")
                    break
                elif guess < target:
                    print(random.choice(funny_responses_too_low))
                else:
                    print(random.choice(funny_responses_too_high))
                    
                remaining = max_attempts - attempts
                if remaining == 1:
                    print("⚡ Last try! You can do it!")
                elif remaining == 2:
                    print("🔥 Only 2 left! You're getting close!")
                elif remaining <= 3:
                    print(f"💪 {remaining} tries left! Keep going!")
                    
            else:
                print("🤪 Oops! Pick a number between 1 and 100!")
                print("🎭 Try again!")
                
        except ValueError:
            print("🙃 That's not a number!")
            print("🔢 Try typing numbers like 25 or 50!")
            print("⚓ Just numbers, please!")
            
    else:
        print(f"⚓ Game Over! The number was {target}!")
        print("🏴‍☠️ Captain NTSVG says: 'Good try! You did great!'")
        print("🗺️ Want to play again? I have more numbers!")
        print("🌟 Every guess helps you get better!")

if __name__ == "__main__":
    print("🎮 Starting the fun game...")
    print("⚓ Getting Captain NTSVG ready...")
    print("✨ Picking a secret number...")
    print()
    funny_number_guessing_game()
    print("\n⚓ Thanks for playing with Captain NTSVG! See you next time! ⚓")
