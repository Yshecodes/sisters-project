
print("Olá Diretor! Seja bem vindo!")

alunos = {}

while True:
  nome = input("Digite o nome do aluno:")
  CPF = input("Digite o CPF do aluno:")
  email = input("Digite o email do aluno:")
  matricula = input("Digite o número da matricula:")
  
  notas = []
  
  for nota in range(3):
    notas.append(int(input(f"Digite a nota {nota + 1: }")))
  
  
  media = sum(notas) / len(notas)
  print(f"Média: {media:.2f}")
  
  while True:
    if media > 6:
      print(f"{nome} foi aprovada. \
      O diploma terá os seguintes dados:\
      Nome: {nome}\
      CPF: {CPF}\
      Email: {email}\
      Matricula: {matricula}")
      break
    else:
      notas.append(int(input(f"Digite a nota de recuperacao: ")))
      media = sum(notas) / len(notas)
      print(f"Nova média: {media:.2f}")
      if media < 6:
        print(f"Aluno {nome} foi reprovado.")
        break
      
  alunos[matricula] = {
    "nome":nome,
    "CPF": CPF,
    "email": email,
    "notas": notas,
    "media": media
  }
  
  continuar_cadastros = input("Continuar cadastros S/N").lower()
  if continuar_cadastros == "s":
    continue
  else:
    print("Tenha um bom dia Diretor!")
    break

print("Dados dos alunos cadastrados:")
print(alunos)
for matricula, dados in alunos.items():
  print(f"Matrícula: {matricula}, Nome: {dados['nome']}, Média: {dados['media']:.2f}")