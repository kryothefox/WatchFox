def validateURL(url):
    import validators
    if(validators.url(url)):
        return True
    else: 
        return False