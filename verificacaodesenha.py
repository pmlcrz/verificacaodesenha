def verificar_senha(senha):
  
    if len(senha) < 8:
        return False
    
    
    if not any(c.isupper() for c in senha) or not any(c.islower() for c in senha):
        return False
    
    
    if not any(c.isdigit() for c in senha):
        return False
    
  
    caracteres_especiais = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    if not any(c in caracteres_especiais for c in senha):
        return False
    
    
    return True


senha = input("Digite senha forte: ")
if verificar_senha(senha):
    print("A senha é forte.")
else:
    print("A senha é fraca.")
