email: str = input("Digite seu email:")
senha: str = input("Digite sua senha:")

email_novamente: str = input("Digite seu email denovo:")
senha_novamente: str = input("Digite sua senha denovo:")

emails_iguais: bool = email == email_novamente
senhas_iguais: bool = senha == senha_novamente

print("Dados iguais?", emails_iguais and senhas_iguais)
