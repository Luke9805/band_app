class ValidazioneCampoError(Exception):
    """Eccezione lanciata quando un campo obbligatorio non è valido."""
    pass

class CanzoneGiaPresenteException(Exception):
    """Eccezione lanciata quando la canzone è già presente in una lista"""
    pass

class CanzoneNonTrovataException(Exception):
    """Eccezione lanciata quando la canzone non è presente in una lista"""
    pass