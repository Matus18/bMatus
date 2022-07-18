import wikipedia as wiki

#Article of Wikipedia
print(wiki.search("Enter the article"))

#Set languaje and Summary of the search
wiki.set_lang("set languaje")
print(wiki.summary("Enter the search article"))

#Suggest search in Wikipedia
print(wiki.suggest("Enter the suggest article"))
