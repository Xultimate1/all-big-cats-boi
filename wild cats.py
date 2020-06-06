wild_cats={'Tiger':['Panthera Tigris','Asia, Southeast Asia, Russia, Indonesia','forest, Jungle, woodland, Swamp, grassland, Savanna','13 feet','120 cm'],
'Lion':['Panthera leo','Africa, India','Grasslands, Savanna, Open Woodland, Dense Scrub','10 feet','120 cm'],
'Jaguar':['Panthera Onca','North America, Central America, South America','Swamp, grassland, Arid Scrubland, Tropical Forest','6.25 feet','76 cm'],
'Cheetah':['Acynonix Jubatus','Northern Africa, Southern Africa, Eastern Africa, The Sahel','Open Plains, Desert, Dry Forests, Grasslands','7.5 feet','90 cm'],
'Leopard':['Panthera Pardus','Southeast Asia, South Asia, Africa, India, Middle East','Rainforest, Desert, Woodland, Grassland, Savanna','7.2 feet','70 cm'],
'Lynx':['Lynx Canadensis','North America, Russia, Europe, Central Asia, Himalayas, Iberia','Tundra, Forests, Semi-Deserts','4.25 feet','70 cm'],
'Margay':['Leopardus Wiedii','South America, Central America','Forest, Tropical Evergreen, Humid Forests','3.5 feet','60.96 cm'],
'Cougar':['Puma Concolor','Western North America, Florida, South America','Tropical Forest, Swamp, Grassland, Desert Scrub','9 feet','90 cm'],
'Bobcat':['Lynx Rufus','North America','Mountain, Woodland, desert, Forest, Swampland','4.16667 feet','53.34 cm'],
'Snow Lepoard':['Panthera Uncia','Central Asia, Himalayas, Russia','Mountain','6.88976 feet','1524 cm'],
'Clouded Lepoard':['Neofelis Nebulosa','Southeast Asia, Himalayas','Mountain, Rainforest, Swamp, Dry Forest','2.95276 feet','55 cm'],
'Siberian Tiger':['Panthera Tigris Altaica','Korea, China, South Siberia','Birch Forest','11 feet','106.68 cm'],
'Ocelot':['Leopardus Pardalis','Texas, Mexico, Central America, South America','Forest, Grassland, Marsh','2.91667 feet','50.8 cm']
}

print('''1. Tiger
2. Lion
3. Jaguar
4. Cheetah
5. Leopard
6. Lynx
7. Margay
8. Cougar
9. Bobcat
10. snow Leopard
11. Clouded Leopard
12. Siberian Tiger
13. Ocelot

''')

cat = input('please enter the wild cat you want to find out about: ').title()

if cat in wild_cats:
    print('-'*70)
    print(f'''{cat} = scientific name: {wild_cats[cat][0]}
regions found: {wild_cats[cat][1]}
natural habitat: {wild_cats[cat][2]}
max length: {wild_cats[cat][3]}
max height: {wild_cats[cat][4]}''')

    print('-'*70)


#1. scientific name
#2. regions found
#3. natural habitat
#4. max length
#5. max height
