import random
from lead_service import LeadService
from database import db

# Função para gerar leads fictícios
def generate_leads():
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']

    # Cria uma instância de LeadService com o db
    lead_service = LeadService(db)

    for _ in range(100):
        name = random.choice(names)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(10, 40)
        interest = random.choice(interests)
        
        # Usa a instância de LeadService para criar o lead
        lead_service.create_lead(name, latitude, longitude, temperature, interest)
