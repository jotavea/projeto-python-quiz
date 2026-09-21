print("Seja bem-vindo ao Quiz do João!")
answer_user =input("Quer começar? (S/N) ")

if answer_user!= "S":
    quit()

score = 0

print("começando...")
print("Quem desenvolveu o jogo Grand Theft Auto? \n (A) Rockstar Games \n (B) EA \n (C) Ubisoft \n (D) Activision")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Parabéns! Você acertou!")
    score = score + 1
else: 
    print("Você errou!")

print("Qual o nome do personagem do jogo GTA: San Andreas? \n (A) Carl Johnson \n (B) Tommy Vercetti \n (C) Niko Bellic \n (D) Trevor Philips")
answer_2 = input("Resposta: ")

if answer_2 == "A":
    print("Parabéns! Você acertou!")
    score = score + 1
else: 
    print("Você errou!")

print(f"Quiz acabou! Sua pontuação final é: {score}/2")
