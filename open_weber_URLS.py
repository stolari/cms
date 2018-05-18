#start
##call method
import webbrowser
##explaining command
print ('the following commands will open a weber URL ')
print ('D=DE,A=AT,N=NL,G=GB,F=FR,I=IE,S=SV,K=DK,U=FI')
##while loop
while True:
###ask url to open
    command=raw_input('digit the command ')
    ###ceck url
    print('you have digited ')
    print(command)
    ###transforming command in url
    if command=='D':
        url='https://www.weber.com/DE/de'
    elif command=='d':
        url='http://staging.weber.com/DE/de/start/'
    elif command=='A':
        url='https://www.weber.com/AT/de'
    elif command=='a':
        url='http://staging.weber.com/AT/de/start/'
    elif command=='BD':
        url='https://www.weber.com/BE/nl'
    elif command=='bd':
        url='https://staging.weber.com/BE/nl/home/'
    elif command=='BF':
            url='https://www.weber.com/BE/fr'
    elif command=='bf':
            url='https://staging.weber.com/BE/fr/home/'
    elif command=='F':
        url='https://www.weber.com/FR/fr'
    elif command=='f':
        url='http://staging.weber.com/on/demandware.store/Sites-FR-Site'
    elif command=='U':
        url='https://www.weber.com/FI/fi'
    elif command=='u':
        url='http://staging.weber.com/FI/fi/home/'
    elif command=='K':
        url='https://www.weber.com/DK/da'
    elif command=='k':
        url='http://staging.weber.com/DK/da/home/'
    elif command=='S':
        url='https://www.weber.com/SE/sv'
    elif command=='s':
            url='http://staging.weber.com/SE/sv/home/'
    elif command=='G':
        url='https://www.weber.com/GB/en'
    elif command=='g':
        url='http://staging.weber.com/on/demandware.store/Sites-UK-Site'
    elif command=='I':
        url='https://www.weber.com/IE/en'
    elif command=='i':
        url='http://staging.weber.com/IE/en/home/'
    elif command=='n':
        url='http://staging.weber.com/NL/nl/home/'
    elif command=='N':
        url='https://www.weber.com/NL/nl'
    elif command=='n':
            url='http://staging.weber.com/on/demandware.store/Sites-NL-Site'
    elif command=='CD':
        url='https://www.weber.com/CH/de'
    elif command=='cd':
        url='http://staging.weber.com/CH/de/'
    elif command=='cf':
        url='http://staging.weber.com/CH/fr/'
    elif command=='CF':
        url='https://www.weber.com/CH/fr/home/'
    elif command=='0':
        print('Exit the program')
        break
    else :
        print('your command is not valid if you need to exit digit 0 ')
        continue
    ###check url
    print(url)
    ###open url
    webbrowser.open(url,new=2)
#endx
print('end')




#webbrowser.open('',new=2)
