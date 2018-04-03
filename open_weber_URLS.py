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
    elif command=='F':
        url='https://www.weber.com/FR/fr'
    elif command=='f':
        url='http://staging.weber.com/on/demandware.store/Sites-FR-Site'
    elif command=='U':
        url='https://www.weber.com/FI/fi'
    elif command=='K':
        url='https://www.weber.com/DK/da'
    elif command=='k':
        url='http://staging.weber.com/DK/da/home/'
    elif command=='S':
        url='https://www.weber.com/SE/sv'
    elif command=='S':
            url='http://staging.weber.com/SE/sv/home/'
    elif command=='G':
        url='https://www.weber.com/GB/en'
    elif command=='I':
        url='https://www.weber.com/IE/en'
    elif command=='N':
        url='https://www.weber.com/NL/nl'
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
#end
print('end')







#webbrowser.open('',new=2)
