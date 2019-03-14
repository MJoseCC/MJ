Cinco = ["Alejandro","Ana","Edu","Carlos","Felix"]
Selected = []

for i in range(len(Cinco)):
            Nom=Cinco[i]
            for j in range(len(Nom)):
                if Nom[j] == "a":
                    Selected.append(Cinco[i])
                    break
print(Selected)