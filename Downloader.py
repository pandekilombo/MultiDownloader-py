from src.Youtube_D import *
import os
from src.ascis import *
from src.Instagram import *
import time

def borrarPantalla():
    if os.name == "posix":  # Para sistemas Unix/Linux/Mac
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":  # Para Windows
        os.system("cls")


def switch(case):
    borrarPantalla()
    match case:

        case "1":
            Shrek()
            print(" ")
            print(" ")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿  Descargardor de video para Youtube    ⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("  \n\n\n")       
            print("Ingrese Link: ")     
            link=input("")
            
            if link != "":
                Youtube_Video_Resolution(link,"1080p")
                print("\nHecho!\n")
            print("")
        case "2":
            Teemo()
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿  Descargardor de video para Youtube en 240p  ⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("  \n\n\n")       
            print("Ingrese Link: ")     
            link=input("")
            
            if link != "":
                Youtube_Video_Resolution(link,"240p")
                print("\nHecho!\n")
            print("")

        case "3":
            LeBlanc()
            print(" ")
            print(" ")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿         Descargardor de Videos para Youtube Custom         ⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("  \n\n\n")       
     
            link=input("Ingrese Link: ")

            res=input("Ingrese resolucion( 240 - 360 - 720 - 1080): \n")
            if link != "": #and res!= "":
                Youtube_Video_Resolution(link,res)
                print("\nHecho!\n")
            print("")
        case "4":
            Viktor()
            print(" ")
            print(" ")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿  Descargardor de Audio para Youtube  ⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("  \n\n\n")       
            print("Ingrese Link: ")   
            link=input("")
            if link != "":
                Youtube_Audio(link)
                print("\nHecho!\n")
            print("")
            

        case "5":
            NagaSuS()
            print(" ")
            print(" ")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿  Descargardor de Videos para Instagram  ⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("  \n\n\n")       
            print("Ingrese Link: ")   
            link=input("")
            if link != "":
                Instagram_Video(link)
                print("\nHecho!\n")
            print("")


        case "6":
            NagaSuS()
            print(" ")
            print(" ")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿                 Saliendo              ⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("  \n\n\n")    
            time.sleep(2)
            borrarPantalla()
            os._exit(0)  # 0 indica que el proceso terminó correctamente

        case _:
            print("")





    pass

def main ():
    #while(True):
        borrarPantalla()
        #AmonGas
        sus()


        print(" ")
        print(" ")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿              Descargador de videos             ⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("  ")

        print("Opciones: \n1) Youtube Video 1080p\n2) Youtube Video 240p \n3) Youtube Video Custom \n4) Youtube Audio \n5) Instagram \n6) Salir")
        
        option=input("")
        switch(option)
        main()

main()