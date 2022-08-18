#Listat
List1 = ['Probit', 0.0, 'Academy', 616, 12.5] #616
List2 = ['Python', 0.5, 'Language', 1008, 15.5] #1008
List3 = ['Computer', 1.0, 'Architecture', 1011, 10.5] #1011
List4 = ['Javascript', 1.9, 'Language', 601, 11.5] #601
List5 = ['jQuery', 7.2, 'Language', 4031, 16.5] #4031

#Përmbledhja e gjitha Listave.
Listat = (List1, List2, List3, List4, List5,)
print ('Listat:', (Listat))

#Aksesimi i termeve dhe indeksimi negativ
vlera = (List1 [-2], List2 [-2], List3 [-2], List4 [-2], List5 [-2])
print ('Vlerat mesatare:', vlera)

# Mbledhja e shumës së përgjithëshme të vlerave mesatare ne lista
print('Shuma totale e elmenteve:', sum(vlera))


#Aksesimi i shumës totale
shuma = (sum(vlera))

#definimi i funksionit te numrimit te elementeve në listen "vlera"
def numri_elementeve(listA):
    count = 0
    for element in listA:
        count += 1
    return count

print("Numri i elementeve ne liste: ", numri_elementeve(vlera))

# Pjestimi i shumës me numrin e elementeve që na nxjerr vleren mesatare
mbetje = (shuma/numri_elementeve(vlera))
print ('Vlera mesatare e gjitha vlerave:', mbetje)