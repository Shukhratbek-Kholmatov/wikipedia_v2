import wikipedia
def search_info(text):
    wikipedia.set_lang("uz")
    try:
        response=wikipedia.summary(text)
    except:
        response="Ma'lumot topilmadi"
    return response