def merhaba(isim, yas):
    if isim == "ali" and yas > 20:
      print("Merhaba " + isim.upper() + ", senin yasin " + str(yas))
    else:
        print("Seni tanimiyorum" )  

def main():
    merhaba() 

def kimsin(isim, yas):
    return ("Merhaba ben %s, %d yasindayim" % (isim, yas))     

if __name__ == '__main__':
    main() 