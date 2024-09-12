import random
from lead_service import LeadService
from database import db
from models import Lead

# Função para gerar leads fictícios
def generate_leads():
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    dominios = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlock.com']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']

    # Cria uma instância de LeadService com o db
    lead_service = LeadService(db)

    generated_emails = set()  # Conjunto para armazenar e-mails já gerados
    generated_telefones = set() # Conjunto para armazenar telefones já gerados

    for _ in range(100):
        name = random.choice(names)

        email = f"{name.lower().replace(' ', '')}{random.randint(1, 100)}{random.choice(dominios)}"  # Gera e-mails únicos
        # Garante que o e-mail seja único, tanto na memória quanto no banco de dados
        while email in generated_emails or Lead.query.filter_by(email=email).first() is not None:
            email = f"{name.lower().replace(' ', '')}{random.randint(1, 100)}{random.choice(dominios)}"
        
        generated_emails.add(email)  # Adiciona o e-mail ao conjunto

        telefone = f"({random.randint(10, 99)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        while telefone in generated_telefones or Lead.query.filter_by(telefone=telefone).first() is not None:
            telefone = f"({random.randint(10, 99)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

        generated_telefones.add(telefone)  # Adiciona o telefone ao conjunto
        
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(10, 40)
        interest = random.choice(interests)
        
        # Usa a instância de LeadService para criar o lead
        lead_service.create_lead(name, email, telefone, latitude, longitude, temperature, interest)
