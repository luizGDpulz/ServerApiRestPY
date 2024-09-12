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

    for _ in range(100):
        name = random.choice(names)

        email = f"{name.lower().replace(' ', '')}{random.randint(1, 100)}{random.choice(dominios)}"  # Gera e-mails únicos

        telefone = f"({random.randint(10, 99)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(10, 40)
        interest = random.choice(interests)
        
        # Usa a instância de LeadService para criar o lead
        lead_service.create_lead(name, email, telefone, latitude, longitude, temperature, interest)
