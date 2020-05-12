import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'

# Check if command line arguments were passed

if len(sys.argv) > 1:
   address = ' '.join(sys.argv[1:])
else:
    address=pyperclip.paste


headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',

    }

    
webbrowser.open('https://google.com/maps/place/' + address)
