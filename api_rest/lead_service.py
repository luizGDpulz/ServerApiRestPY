from models import Lead

class LeadService:
    def __init__(self, db):
        self.db = db

    def create_lead(self, name, email, telefone, latitude, longitude, temperature, interest):

        existing_lead = Lead.query.filter_by(email=email).first()
        if existing_lead:
            print(f"O e-mail '{email}' já existe no banco de dados. Ignorando a inserção.")
            return  # Ignora a inserção se o e-mail já existe
        
        existing_lead = Lead.query.filter_by(telefone=telefone).first()
        if existing_lead:
            print(f"O Telefone '{telefone}' já existe no banco de dados. Ignorando a inserção.")
            return  # Ignora a inserção se o telefone já existe
        
        lead = Lead(name=name, email=email, telefone=telefone, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest)
        self.db.session.add(lead)
        self.db.session.commit()

    def get_all_leads(self):
        return Lead.query.all()

    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)

    def update_lead(self, lead_id, name, email, telefone, latitude, longitude, temperature, interest):
        lead = self.get_lead_by_id(lead_id)
        lead.name = name
        lead.email = email
        lead.telefone = telefone 
        lead.latitude = latitude
        lead.longitude = longitude
        lead.temperature = temperature
        lead.interest = interest
        self.db.session.commit()

    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self.db.session.commit()
