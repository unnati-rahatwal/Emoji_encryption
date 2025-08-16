emoji_dict = {
    'A': '🍎', 'B': '🐝', 'C': '🌊', 'D': '🍩', 'E': '🐘',
    'F': '🌻', 'G': '🍇', 'H': '🏠', 'I': '🍦', 'J': '🕹',
    'K': '🔑', 'L': '🦁', 'M': '🌝', 'N': '🥜', 'O': '🍊',
    'P': '🥞', 'Q': '👸', 'R': '🤖', 'S': '🌠', 'T': '🌴',
    'U': '🦄', 'V': '🌋', 'W': '🍉', 'X': '❌', 'Y': '🍋',
    'Z': '⚡',
    ' ': '⬜',
    '.': '🔵', ',': '🟡', '!': '❗', '?': '❓'
}
print(emoji_dict)

chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ .!?"
chars_key=list(chars)
print(chars_key)

print("Emoji Encryption System")
print("1. Encrypt Text -> Emoji")
print("2. Decrypt Emoji -> Text")
choice = int(input("Enter choice (1/2): "))

if choice==1:
#encrypt
   plain_text=input("Enter message to encrypt:")
   emoji_text=""

   for letter in plain_text:
          emoji_text+=emoji_dict[letter.upper()]

   print(f"original msg: {plain_text}")
   print(f"encrypted msg: {emoji_text}")

elif choice==2:
#decrypt
   emoji_text=input("Enter message to decrypt:")
   plain_text=""

   for emoji in emoji_text:
          values=list(emoji_dict.values())
          index=values.index(emoji)
          plain_text+=chars_key[index]

   print(f"original msg: {emoji_text}")
   print(f"encrypted msg: {plain_text}")

else:
    print("Invalid choice. Please enter 1 or 2.")



