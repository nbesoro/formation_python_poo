# Section 2 : Heritage

# Etudiant
# Professeur


# class Professeur:
#     def __init__(self, first_name, last_name, email, matiere_enseigner):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.matiere_enseigner = matiere_enseigner


class Personne:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
    def se_presenter(self):
        print("Name: ", self.first_name)
        print("Last Name: ", self.last_name)
        print("Email: ", self.email)

class Etudiant(Personne):
    def __init__(self, first_name, last_name, email, niveau_etude):
        super().__init__(first_name, last_name, email)
        self.niveau_etude = niveau_etude

    def se_presenter(self):
        super().se_presenter()
        print("Niveau: ", self.niveau_etude)
        
class Professeur(Personne):
    def __init__(self, first_name, last_name, email, matiere_enseigner):
        super().__init__(first_name, last_name, email)
        self.matiere_enseigner = matiere_enseigner

    def se_presenter(self):
        super().se_presenter()
        print("Matière: ", self.matiere_enseigner)
        
    

e1 = Etudiant("Soro", "Nbe", "bonjour@nbesoro.com", "6 eme")
prof1 = Professeur("Samake", "Mohamed", "bonjour@samake.com", "Python")

e1.se_presenter()

print("-"*20)

prof1.se_presenter()