from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
import threading






class Recipies:
    def __init__(self,root):
        self.root=root
        self.root.title("Recepies")
        self.root.geometry("800x600")
        self.root.iconbitmap("logo1029.ico")
        self.root.resizable(0,0)


        

        cources=StringVar()
        cuisines=StringVar()
        desserts=StringVar()
        health=StringVar()
        recip=StringVar()
        web_url=StringVar()
        down_url=StringVar()
        filename=StringVar()








        def on_enter1(e):
            but_select_courses['background']="black"
            but_select_courses['foreground']="cyan"  
        def on_leave1(e):
            but_select_courses['background']="SystemButtonFace"
            but_select_courses['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_select_desserts['background']="black"
            but_select_desserts['foreground']="cyan"  
        def on_leave2(e):
            but_select_desserts['background']="SystemButtonFace"
            but_select_desserts['foreground']="SystemButtonText"
            


        def on_enter3(e):
            but_select_cuisines['background']="black"
            but_select_cuisines['foreground']="cyan"  
        def on_leave3(e):
            but_select_cuisines['background']="SystemButtonFace"
            but_select_cuisines['foreground']="SystemButtonText"



        def on_enter4(e):
            but_select_health['background']="black"
            but_select_health['foreground']="cyan"  
        def on_leave4(e):
            but_select_health['background']="SystemButtonFace"
            but_select_health['foreground']="SystemButtonText"

            

        def on_enter5(e):
            but_select_recipes['background']="black"
            but_select_recipes['foreground']="cyan"  
        def on_leave5(e):
            but_select_recipes['background']="SystemButtonFace"
            but_select_recipes['foreground']="SystemButtonText"
            


        def on_enter6(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave6(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter7(e):
            but_select_search['background']="black"
            but_select_search['foreground']="cyan"  
        def on_leave7(e):
            but_select_search['background']="SystemButtonFace"
            but_select_search['foreground']="SystemButtonText"


        def on_enter8(e):
            but_download['background']="black"
            but_download['foreground']="cyan"  
        def on_leave8(e):
            but_download['background']="SystemButtonFace"
            but_download['foreground']="SystemButtonText"

        
        def on_enter9(e):
            but_clears['background']="black"
            but_clears['foreground']="cyan"  
        def on_leave9(e):
            but_clears['background']="SystemButtonFace"
            but_clears['foreground']="SystemButtonText"


        def on_enter10(e):
            but_clears_box['background']="black"
            but_clears_box['foreground']="cyan"  
        def on_leave10(e):
            but_clears_box['background']="SystemButtonFace"
            but_clears_box['foreground']="SystemButtonText"















        def cou():
            try:
                web_url.set("")
                if cources.get()!="select Courses":
                    with open("C:/TEMP/recipes.txt","w") as f:
                        if cources.get()=="Soups":
                                web_url.set("https://recipes.timesofindia.com/recipes/soup-recipes/52974844?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Snacks":
                                web_url.set("https://recipes.timesofindia.com/recipes/snack-recipes/52518623?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Salads":
                                web_url.set("https://recipes.timesofindia.com/recipes/salad-recipes/52975040?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Appetizer":
                                web_url.set("https://recipes.timesofindia.com/recipes/appetizers-recipes/67380588?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Finger Food":
                                web_url.set("https://recipes.timesofindia.com/recipes/finger-food-recipes/57201519?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Veg Snacks":
                                web_url.set("https://recipes.timesofindia.com/recipes/veg-snacks/61361110?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="BreakFast":
                                web_url.set("https://recipes.timesofindia.com/recipes/breakfast-recipes/61642536?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Lunch":
                                web_url.set("https://recipes.timesofindia.com/recipes/lunch-recipes/52518261?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Veg Dinners":
                                web_url.set("https://recipes.timesofindia.com/recipes/veg-dinners/61361358?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Dinners":
                                web_url.set("https://recipes.timesofindia.com/recipes/dinner-recipes/52518344?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Biryani":
                                web_url.set("https://recipes.timesofindia.com/recipes/biryani-recipes/57201646?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Paratha":
                                web_url.set("https://recipes.timesofindia.com/recipes/paratha-recipes/57201611?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Kabab":
                                web_url.set("https://recipes.timesofindia.com/recipes/kebab-recipes/57202004?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Sandwiches":
                                web_url.set("https://recipes.timesofindia.com/recipes/sandwich-recipes/52974891?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Desserts":
                                web_url.set("https://recipes.timesofindia.com/recipes/desserts-sweets/52975006?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Party Snacks":
                                web_url.set("https://recipes.timesofindia.com/recipes/birthday-kitty-party-anniversary-snacks/56588993?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Dips":
                                web_url.set("https://recipes.timesofindia.com/recipes/dip-recipes/56331683?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                        if cources.get()=="Kids":
                                web_url.set("https://recipes.timesofindia.com/recipes/kids-recipes/62053272?curpg=1")
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                    with open("C:/TEMP/recipes.txt","r") as f:
                            text.insert("end",f.read())
                        
                else:
                    tkinter.messagebox.showerror("Error","Please Select Courses ")
            except:
                tkinter.messagebox.showerror("Error","Network Error")        
                               

                        
        def  thread_cou():
            t1=threading.Thread(target=cou)
            t1.start()









                        


        def des():
            try:
                if desserts.get()!="select Desserts":
                    with open("C:/TEMP/recipes.txt","w") as f:
                        web_url.set("")
                        if desserts.get()=="No Bakes Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/no-bake-desserts/67380552?curpg=1')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                               
                        if desserts.get()=="Cookies":
                                web_url.set('https://recipes.timesofindia.com/recipes/cookies/67380566?curpg=1')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")

                                                
                        if desserts.get()=="Cakes":
                                web_url.set('https://recipes.timesofindia.com/recipes/cake-recipes/61544220?curpg=1')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                                                        
                        if desserts.get()=="Birthday Cakes":
                                web_url.set('https://recipes.timesofindia.com/recipes/birthday-cakes/67380584?curpg=1')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                                                        
                        if desserts.get()=="North Indian Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/north-indian-dessert-recipes/67383261?curpg=1')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                                                        
                        if desserts.get()=="South Indian Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/south-indian-dessert-recipes/67380575?curpg=1')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                
                                                        
                        if desserts.get()=="Punjabi Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/punjabi-dessert-recipes/67383445')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                        
                        if desserts.get()=="Goan Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/goan-dessert-recipes/67383482')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                        
                        if desserts.get()=="Gujrati Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/gujarati-dessert-recipes/67383636')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                        
                        if desserts.get()=="Rajasthani Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/rajasthani-dessert-recipes/67383666')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                        
                        if desserts.get()=="Bengali Desserts":
                                web_url.set('https://recipes.timesofindia.com/recipes/bengali-dessert-recipes/67383707?curpg=1')
                                url=web_url.get()
                                response= requests.get(url)
                                Soup=BeautifulSoup(response.text,"html.parser")
                                gather=Soup.findAll("div",class_="caption clearfix")
                                for link in gather:
                                        child=link.findChildren("a")
                                        for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                        
            
                    with open("C:/TEMP/recipes.txt","r") as f:
                                text.insert("end",f.read())        
                                        
                else:
                    tkinter.messagebox.showerror("Error","Please Select Desserts")
                      
            except:
                tkinter.messagebox.showerror("Error","Network Error")
             


        def  thread_des():
            t1=threading.Thread(target=des)
            t1.start()
















        def rec():
            try:
                if recip.get()!="select Recipes":
                        with open("C:/TEMP/recipes.txt","w") as f:

                                if recip.get()=="Paneer Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/paneer-recipes/52983771?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Chicken Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/chicken-recipes/61545604?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Biryani Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/biryani-recipes/57201646?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Potato Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/potato-recipes/52983801?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Mutton Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/mutton-recipes/67380510?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")

                                if recip.get()=="Egg Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/egg-recipes/52983786?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")

                                if recip.get()=="Street Food":
                                        web_url.set("https://recipes.timesofindia.com/recipes/street-food-recipes/56331164?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Seafood Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/seafood-recipes/67380450?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Rice Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/rice-recipes/52983789?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")

                                if recip.get()=="Tandoor Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/tandoor-recipes/56589209?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Microwave Recipes":
                                        web_url.set("https://recipes.timesofindia.com/recipes/microwave-recipes/56589174?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="One-Pot Meals":
                                        web_url.set("https://recipes.timesofindia.com/recipes/one-pot-meal-recipes/65054668?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")



                                if recip.get()=="Comfort food":
                                        web_url.set("https://recipes.timesofindia.com/recipes/comfort-food/67380487?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Sunday Brunch":
                                        web_url.set("https://recipes.timesofindia.com/recipes/sunday-brunch/52974860?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="High Tea":
                                        web_url.set("https://recipes.timesofindia.com/recipes/high-tea-recipes/56330868?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Weekend Breakfasts":
                                        web_url.set("https://recipes.timesofindia.com/recipes/weekend-breakfasts/52519882?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")


                                if recip.get()=="Beverages":
                                        web_url.set("https://recipes.timesofindia.com/beverages?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                                child=link.findChildren("a")
                                                for childs in child:
                                                        f.write("\n")
                                                        f.write(childs.get("href"))
                                                        f.write("\n")

                        with open("C:/TEMP/recipes.txt","r") as f:
                            text.insert("end",f.read())

                else:
                   tkinter.messagebox.showerror("Error","Please Select Recipies")
            
            except:
                tkinter.messagebox.showerror("Error","Network Error")


                    
        def  thread_rec():
            t1=threading.Thread(target=rec)
            t1.start()











            

        def hel():
            try:
                    web_url.set("")
                    if health.get()!="select Health":
                        with open("C:/TEMP/recipes.txt","w") as f:
                                if health.get()=="Diabetic":
                                        web_url.set("https://recipes.timesofindia.com/recipes/diabetic-recipes/52975024?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="Low-Crab":
                                        web_url.set("https://recipes.timesofindia.com/recipes/low-carbohydrates-recipes/67380520?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="Vegan":
                                        web_url.set("https://recipes.timesofindia.com/recipes/vegan-recipes/52974938?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="Keto":
                                        web_url.set("https://recipes.timesofindia.com/recipes/keto-recipes/67721254")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")



                                if health.get()=="Gluteen Free":
                                        web_url.set("https://recipes.timesofindia.com/recipes/gluten-free-recipes/52519944?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="Low Cholesterol":
                                        web_url.set("https://recipes.timesofindia.com/recipes/low-cholesterol-recipes/56590366?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="High Fiber":
                                        web_url.set("https://recipes.timesofindia.com/recipes/high-fibre-recipes/67380528?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="Low Calorie":
                                        web_url.set("https://recipes.timesofindia.com/recipes/low-calorie-dinners/52520179?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="Dairy Free":
                                        web_url.set("https://recipes.timesofindia.com/recipes/dairy-free-recipes/67380537?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if health.get()=="High Protien":
                                        web_url.set("https://recipes.timesofindia.com/recipes/high-protein-diet/52974994?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                            child=link.findChildren("a")
                                            for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                        with open("C:/TEMP/recipes.txt","r") as f:
                               text.insert("end",f.read())   


                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Health Recipies")

            except:
                tkinter.messagebox.showerror("Error","Network error")
                

        

        def thread_hel():
                t1=threading.Thread(target=hel)
                t1.start()
                
        














        def cui():
            try:
                web_url.set("")                       
                if cuisines.get()!="select Cuisines":
                        with open("C:/TEMP/recipes.txt","w") as f:
                                if cuisines.get()=="Chinese":
                                        web_url.set("https://recipes.timesofindia.com/recipes/chinese/52974773?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                
                                if cuisines.get()=="Punjabi":
                                        web_url.set("https://recipes.timesofindia.com/recipes/punjabi/53597550?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")



                                if cuisines.get()=="Continental":
                                        web_url.set("https://recipes.timesofindia.com/recipes/continental/53597178?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="South Indian":
                                        web_url.set("https://recipes.timesofindia.com/recipes/south-indian/52974693?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")



                                if cuisines.get()=="Italian":
                                        web_url.set("https://recipes.timesofindia.com/recipes/italian/52984460?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Rajasthani":
                                        web_url.set("https://recipes.timesofindia.com/recipes/rajasthani/53597052?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")



                                if cuisines.get()=="North Indian":
                                        web_url.set("https://recipes.timesofindia.com/recipes/north-indian/52518822?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")



                                if cuisines.get()=="Mexican":
                                        web_url.set("https://recipes.timesofindia.com/recipes/mexican/52983973?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                

                                if cuisines.get()=="Mughlai":
                                        web_url.set("https://recipes.timesofindia.com/recipes/mughlai/59032115?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Jain":
                                        web_url.set("https://recipes.timesofindia.com/recipes/jain/61101557?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")



                                if cuisines.get()=="Bengali":
                                        web_url.set("https://recipes.timesofindia.com/recipes/bengali/53597068?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Gujrati":
                                        web_url.set("https://recipes.timesofindia.com/recipes/gujarati/52516836?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")



                                if cuisines.get()=="American":
                                        web_url.set("https://recipes.timesofindia.com/recipes/american/52517752?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Goan":
                                        web_url.set("https://recipes.timesofindia.com/recipes/goan/63731801?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Mediterranean":
                                        web_url.set("https://recipes.timesofindia.com/recipes/mediterranean/53597518?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="French":
                                        web_url.set("https://recipes.timesofindia.com/recipes/french/52517664?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Satvik":
                                        web_url.set("https://recipes.timesofindia.com/recipes/satvik/61101505?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Asian":
                                        web_url.set("https://recipes.timesofindia.com/recipes/asian/53597161?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Kashmiri":
                                        web_url.set("https://recipes.timesofindia.com/recipes/kashmiri/53597350?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                

                                if cuisines.get()=="Maharashtrain":
                                        web_url.set("https://recipes.timesofindia.com/recipes/maharashtrian/53597502?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="Fusion":
                                        web_url.set("https://recipes.timesofindia.com/recipes/fusion/53597227?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="East Indian":
                                        web_url.set("https://recipes.timesofindia.com/recipes/east-indian/67721222")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")


                                if cuisines.get()=="west Indian":
                                        web_url.set("https://recipes.timesofindia.com/recipes/west-indian/67721178")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")
                                                

                                if cuisines.get()=="Thai":
                                        web_url.set("https://recipes.timesofindia.com/recipes/thai/52974717?curpg=1")
                                        url=web_url.get()
                                        response= requests.get(url)
                                        Soup=BeautifulSoup(response.text,"html.parser")
                                        gather=Soup.findAll("div",class_="caption clearfix")
                                        for link in gather:
                                           child=link.findChildren("a")
                                           for childs in child:
                                                f.write("\n")
                                                f.write(childs.get("href"))
                                                f.write("\n")

                        with open("C:/TEMP/recipes.txt","r") as f:
                                text.insert("end",f.read())       

                else:
                    tkinter.messagebox.showerror('Error',"Please Select Cuisines")
            except:
                tkinter.messagebox.showerror("Error","Network Error")
                

        def thread_cui():
                t1=threading.Thread(target=cui)
                t1.start()

                










        def clear_all():
            web_url.set("")
            recip.set("select Recipes")
            health.set("select Health")
            desserts.set("select Desserts")
            cuisines.set("select Cuisines")
            cources.set("select Courses")




            


            

        def clears():
            down_url.set("")
            filename.set("")
            lab_sucessfully.config(text="")





            

        def clear_box():
            text.delete("1.0","end")









            

        def search():
            try: 
                if web_url.get()!="":
                    with open("C:/TEMP/recipes.txt","w") as f:
                        url=web_url.get()
                        response= requests.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        gather=Soup.findAll("div",class_="caption clearfix")
                        for link in gather:
                           child=link.findChildren("a")
                           for childs in child:
                                f.write("\n")
                                f.write(childs.get("href"))
                                f.write("\n")
                    with open("C:/TEMP/recipes.txt","r") as f:
                                text.insert("end",f.read())                                 
                else:
                    tkinter.messagebox.showerror("Error","Please Enter Url")
            except:
                tkinter.messagebox.showerror("Error","Network error")


        def thread_search():
            t1=threading.Thread(target=search)
            t1.start()







        def download():
            try:
                if down_url.get()!="":
                    if filename.get()!="":
                        url=down_url.get()
                        response= requests.get(url)
                        Soup=BeautifulSoup(response.text,"html.parser")
                        heading=Soup.findAll("h1",class_="nheadingrs")
                        prg.start(10)
                        for name in heading:
                            with open("{}.txt".format(filename.get()),"w") as f:
                                f.write("*"+name.get_text()+"*\n")
                                f.write("------------------------------"+"\n\n")
                            
                           
                        ingredient_heading=Soup.findAll("span",class_="spanul")
                        for ing in ingredient_heading:
                            with open("{}.txt".format(filename.get()),"a") as f:
                                f.write("***"+ing.get_text()+"***\n")
                                f.write("------------------------------"+"\n\n")


                        ingredient=Soup.findAll("div",class_="recipetabsdata ingredients_lilsting clearfix")
                        for ins in ingredient:
                              a=ins.get_text(separator=',\n')
                              with open("{}.txt".format(filename.get()),"a") as f:
                                f.write(a+"\n\n")
                                f.write("------------------------------"+"\n\n")
                                f.write("=================Steps==========="+"\n\n")
                        

                        steps=Soup.findAll("div",class_="steps_listings clearfix")
                        for step in steps:
                            with open("{}.txt".format(filename.get()),"a") as f:
                                f.write(step.get_text(separator='\n=======\n')+"\n")
                                prg.stop()
                                lab_sucessfully.config(text="Recipies Successfully Downloaded")
                        
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Filename")
                else:
                    tkinter.messagebox.showerror("Error","Please Enter Url")
            except:
                tkinter.messagebox.showerror("Error","Network Error")





        def thread_download():
            t1=threading.Thread(target=download)
            t1.start()
        



#==================frame=========================================#
        mainframe=Frame(self.root,width=800,height=600,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=794,height=320,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=794,height=245,relief="ridge",bd=3)
        secondframe.place(x=0,y=320)

        thirdframe=Frame(mainframe,width=794,height=28,relief="ridge",bd=3)
        thirdframe.place(x=0,y=565)


#===============================firstframe===============================================================#
        tabControl = Notebook(firstframe,width=783,height=288) 
  
        recipies = Frame(tabControl,background="grey57") 
        download_recipies = Frame(tabControl,background="grey87") 
        about = Frame(tabControl,background="grey77") 
        
        tabControl.add(recipies, text ='Recipies') 
        tabControl.add(download_recipies, text ='Download Recipies')
        tabControl.add(about, text ='About') 
        tabControl.place(x=0,y=0)

#==============================firstframe/recipies===========================================================================#

        list_courses=["Soups","Snacks","Salads","Appetizer","Finger Food",\
                      "Veg Snacks","BreakFast","Lunch","Veg Dinners","Dinners",\
                      "Biryani","Paratha","Kabab","Sandwiches","Desserts","Party Snacks",\
                      "Dips","Kids"]
        list_courses_combo=Combobox(recipies,values=list_courses,font=('arial',12),width=14,state="readonly",textvariable=cources)
        list_courses_combo.set("select Courses")
        list_courses_combo.place(x=10,y=15)

        but_select_courses=Button(recipies,width=10,text="Select Courses",font=('times new roman',12),cursor="hand2",command=thread_cou)
        but_select_courses.place(x=180,y=10)
        but_select_courses.bind("<Enter>",on_enter1)
        but_select_courses.bind("<Leave>",on_leave1)






        list_Desserts=["No Bakes Desserts","Cookies","Cakes","Birthday Cakes",\
                       "North Indian Desserts","South Indian Desserts","Punjabi Desserts",\
                        "Goan Desserts","Gujrati Desserts","Rajasthani Desserts","Bengali Desserts"]
        list_Desserts_combo=Combobox(recipies,values=list_Desserts,font=('arial',12),width=14,state="readonly",textvariable=desserts)
        list_Desserts_combo.set("select Desserts")
        list_Desserts_combo.place(x=500,y=15)

        but_select_desserts=Button(recipies,width=10,text="Select Desserts",font=('times new roman',12),cursor="hand2",command=thread_des)
        but_select_desserts.place(x=670,y=10)
        but_select_desserts.bind("<Enter>",on_enter2)
        but_select_desserts.bind("<Leave>",on_leave2)








        list_cuisines=["Chinese","Punjabi","Continental","South Indian","Italian","Rajasthani",\
                       "North Indian","Mexican","Mughlai","Jain","Bengali","Gujrati","American",\
                        "Goan","Mediterranean","French","Satvik","Asian","Kashmiri","Maharashtrain",\
                        "Fusion","East Indian","west Indian","Thai"]
        list_cuisines_combo=Combobox(recipies,values=list_cuisines,font=('arial',12),width=14,state="readonly",textvariable=cuisines)
        list_cuisines_combo.set("select Cuisines")
        list_cuisines_combo.place(x=10,y=95)

        but_select_cuisines=Button(recipies,width=10,text="Select Cuisines",font=('times new roman',12),cursor="hand2",command=thread_cui)
        but_select_cuisines.place(x=180,y=90)
        but_select_cuisines.bind("<Enter>",on_enter3)
        but_select_cuisines.bind("<Leave>",on_leave3)







        list_health=["Diabetic","Low-Crab","Vegan","Keto","Gluteen Free",\
                     "Low Cholesterol","High Fiber","Low Calorie",\
                     "Dairy Free","High Protien"]
        list_health_combo=Combobox(recipies,values=list_health,font=('arial',12),width=14,state="readonly",textvariable=health)
        list_health_combo.set("select Health")
        list_health_combo.place(x=500,y=95)

        but_select_health=Button(recipies,width=10,text="Select Health",font=('times new roman',12),cursor="hand2",command=thread_hel)
        but_select_health.place(x=670,y=90)
        but_select_health.bind("<Enter>",on_enter4)
        but_select_health.bind("<Leave>",on_leave4)





        list_recipes=["Paneer Recipes","Chicken Recipes","Biryani Recipes","Potato Recipes",\
                      "Mutton Recipes","Egg Recipes","Street Food","Rice Recipes","Seafood Recipes",\
                      "Tandoor Recipes","Microwave Recipes","One-Pot Meals","Comfort food",\
                      "Sunday Brunch","High Tea","Weekend Breakfasts","Beverages"]
        list_recipes_combo=Combobox(recipies,values=list_recipes,font=('arial',12),width=14,state="readonly",textvariable=recip)
        list_recipes_combo.set("select Recipes")
        list_recipes_combo.place(x=10,y=175)

        but_select_recipes=Button(recipies,width=10,text="Select Recipes",font=('times new roman',12),cursor="hand2",command=thread_rec)
        but_select_recipes.place(x=180,y=170)
        but_select_recipes.bind("<Enter>",on_enter5)
        but_select_recipes.bind("<Leave>",on_leave5)



        but_clear=Button(recipies,width=10,text="Clear",font=('times new roman',12),cursor="hand2",command=clear_all)
        but_clear.place(x=500,y=165)
        but_clear.bind("<Enter>",on_enter6)
        but_clear.bind("<Leave>",on_leave6)

        


        lab_url=Label(recipies,text="Paste Url",font=('times new roman',12),bg="grey57",fg="white")
        lab_url.place(x=20,y=230)

        ent_url=Entry(recipies,width=65,relief="ridge",bd=3,font=('times new roman',12),textvariable=web_url)
        ent_url.place(x=120,y=230)

        but_select_search=Button(recipies,width=10,text="Search",font=('times new roman',12),cursor="hand2",command=thread_search)
        but_select_search.place(x=670,y=225)
        but_select_search.bind("<Enter>",on_enter7)
        
        but_select_search.bind("<Leave>",on_leave7)


#======================================download recipies=========================================#

        lab_url=Label(download_recipies,text="Paste Url",font=('times new roman',12),background="grey87",fg="black")
        lab_url.place(x=20,y=20)

        ent_url=Entry(download_recipies,width=70,relief="ridge",bd=3,font=('times new roman',12),textvariable=down_url)
        ent_url.place(x=120,y=20)


        lab_filename=Label(download_recipies,text="File Name",font=('times new roman',12),background="grey87",fg="black")
        lab_filename.place(x=20,y=90)

        ent_filename=Entry(download_recipies,width=27,relief="ridge",bd=3,font=('times new roman',12),textvariable=filename)
        ent_filename.place(x=120,y=90)


        but_download=Button(download_recipies,text="Download Recipies",width=15,bd=3,font=('times new roman',12),cursor="hand2",command=thread_download)
        but_download.place(x=90,y=180)
        but_download.bind("<Enter>",on_enter8)
        but_download.bind("<Leave>",on_leave8)



        but_clears=Button(download_recipies,text="Clear",width=15,bd=3,font=('times new roman',12),cursor="hand2",command=clears)
        but_clears.place(x=540,y=180)
        but_clears.bind("<Enter>",on_enter9)
        but_clears.bind("<Leave>",on_leave9)

        but_clears_box=Button(download_recipies,text="Clear Box",width=15,bd=3,font=('times new roman',12),cursor="hand2",command=clear_box)
        but_clears_box.place(x=310,y=200)
        but_clears_box.bind("<Enter>",on_enter10)
        but_clears_box.bind("<Leave>",on_leave10)

        lab_sucessfully=Label(download_recipies,text="",font=('times new roman',12),background="grey87",fg="black")
        lab_sucessfully.place(x=280,y=250)
        




#============================secondframe===================================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=95,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)




#==============================thirdframe===========================================#
        prg=Progressbar(thirdframe,length=788,orient=HORIZONTAL,mode='indeterminate')
        prg.place(x=0,y=0)

    


if __name__ == "__main__":
    root=Tk()
    app=Recipies(root)
    root.mainloop()
