

def translate(value):
    if value=="Homme":
        return "Male"
    elif value=="Femme":
        return "Female"
    elif value=="Autre":
        return "Other"
    elif value=="Oui":
        return "Yes"
    elif value=="Non":
        return "No"
    elif value=="Souvent":
        return "Often"
    elif value=="Parfois":
        return "Sometimes"
    elif value=="Rarement":
        return "Rarely"
    elif value=="Jamais":
        return "Never"
    elif value=="Non concerné":
        return "Not concerned"
    elif value=="Plus de 1000":
        return "More than 1000"
    elif value=="Je ne sais pas":
        return "Don't know"
    elif value=="Je ne suis pas sûr":
        return "Not sure"
    elif value=="Très facilement":
        return "Very easy"
    elif value=="Assez facilement":
        return "Somewhat easy"
    elif value=="Assez difficilement":
        return "Somewhat difficult"
    elif value=="Très difficilement":
        return "Very difficult"
    elif value=="Peut-être":
        return "Maybe"
    elif value=="Certains d'entre eux":
        return "Some of them"
    else:
        return value