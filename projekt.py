import random

def generate_lorem_ipsum():
    odstavce = int(input("Zadejte počet odstavců: "))
    slova_na_odstavec = int(input("Zadejte počet slov na odstavec: "))

    lorem_sluvka = ["morem", "kipsum", "dvere", "sitě", "samet,", "consikulovat", "adipisciovat", "elita",
                   "sedleh", "do", "eiusmod", "temporarne", "incididuntit", "tutat", "laborete", "eta", "doloreice", "kockopes", "katzehunde", "kous", "špíluser", "komanditista", "tichykamos", "smegrus",
                   "mononukleousus", "hladus", "potisse", "rychlous", "morus", "modius", "morbius", "stolus", "negrus", "venizitiri"]
    
    lorem_ipsum_text = ""

    lorem_ipsum_text += "Lorem ipsum "
    for _ in range(slova_na_odstavec - 2):
        slovo = random.choice(lorem_sluvka)
        lorem_ipsum_text += slovo + " "
    lorem_ipsum_text += ".\n"

    for _ in range(odstavce - 1):  
        for _ in range(slova_na_odstavec):
            slovo = random.choice(lorem_sluvka)
            lorem_ipsum_text += slovo + " "
        lorem_ipsum_text += ".\n"

    return lorem_ipsum_text

generated_text = generate_lorem_ipsum()
print(generated_text)
