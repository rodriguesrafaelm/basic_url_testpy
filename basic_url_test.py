import urllib.error
import urllib.request
while True:
    lang = str(input("PT or ENG: ").upper())
    if lang == 'PT':
        break
    elif lang == 'ENG':
        break
    else:
        "Try again."
if lang == 'PT':
    while True:
        link = str(input("Digite a URL desejada: "))
        if ".com" in link:
            if link.startswith('http://') or link.startswith('https://'):
                break
            else:
                link = "http://" + link
                break
        else:
            print("Digite um link válido: (ex: http://google.com)")
    try:
        site = urllib.request.urlopen(link)
    except urllib.error.URLError:
        print(f"\"{link}\" está indisponível.")
    else:
        print(f"\"{link}\" está disponível.")
elif lang == 'ENG':
    while True:
        link = str(input("Insert URL: "))
        if ".com" in link:
            if link.startswith('http://') or link.startswith('https://'):
                break
            else:
                link = "http://" + link
                break
        else:
            print("Please, insert a valid link: (ex: http://google.com)")
    try:
        site = urllib.request.urlopen(link)
    except urllib.error.URLError:
        print(f"\"{link}\" website is unavaible")
    else:
        print(f"\"{link}\" website is avaible")