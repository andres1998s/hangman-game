def intentos(errores):
    
    if errores == 0:
        return """
                    ||=================
                    ||        
                    ||        O
                    ||        
                    ||        
                    ||
                    =======@==== ======
                    ||               ||        
                    Puedes equivocarte solamente 4 veces"""
    
    if errores == 1:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||        
                    ||        
                    ||
                    =======@==== ======
                    ||               ||           
"""
    
    if errores == 2:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||        | 
                    ||         
                    ||
                    =======@==== ======
                    ||               ||        
        """
    
    if errores == 3:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||       /| 
                    ||         
                    ||
                    =======@==== ======
                    ||               ||        
        """

    if errores == 4:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||       /|\ 
                    ||         
                    ||
                    =======@==== ======
                    ||               ||        
        """
    if errores == 5:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||       /|\ 
                    ||       /  
                    ||
                    =======@==== ======
                    ||               ||
                    Juego terminado      
        """