alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(plain_text, shift_amount, direction_move):
  new_message = ''
  if direction == 'decode':
    shift_amount * -1

  for char in plain_text:
    if char in alphabet:
      index = alphabet.index(char)
      new_message += alphabet[(index + shift_amount) % 26]
    else:
      new_message += char
  
  print(f'The {direction_move}d text is {new_message}.')
    # print(index, let)


from art import logo
print(logo)

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(plain_text=text, shift_amount=shift, direction_move=direction)
  
  result = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.  ").lower()
  if result == 'no':
    should_continue = False
    print("Goodbye")
  




