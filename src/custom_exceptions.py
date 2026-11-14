class ValidazioneCampoError(Exception):
    """Eccezione lanciata quando un campo obbligatorio non è valido."""
    pass

class CanzoneGiaPresenteException(Exception):
    """Eccezione lanciata quando la canzone è già presente in una lista"""
    pass

class CanzoneNonTrovataException(Exception):
    """Eccezione lanciata quando la canzone non è presente in una lista"""
    pass

class MessaggioNonPresente(Exception):
    """Eccezione lanciata quando un messaggio non è presente nella chat"""
    pass

class UtenteNonRegistrato(Exception):
    """Eccezione lanciata quando un l'utente non risulta nel database"""
    pass

class BandNonRegistrata(Exception):
    """Eccezione lanciata quando un la band non risulta nel database"""
    pass