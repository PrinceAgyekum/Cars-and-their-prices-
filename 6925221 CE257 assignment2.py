#Agyekum Agyapong Prince
#6925221
#List of cars and their prices
cars={
      "Mazda 6":58000,
      "Maclaren":63000,
      "Land Cruiser":75000,
      "Mercedes Benz C63":58500, 
      "Toyota Rush":61000,
      "BMW M5":78000,
      "Prado V8":52000,
      "Kia Rio":17450,
      "Tesla Model 4":62000,
      "Ford 150":75600,
      "Chevrolet Camaro":25950,
      "Audi Q7":85800,
      "Kia Sportage":70000,
      "Honda Accord":85600,
      "Honda Civic":79900,
      "Honda CR-V":58700,
      "Lincoln":39000,
      "Jeep Wrangler":69800,
      "Jeep Rubicon":55900,
      "Hyundai Sonata":86000,
      "Honda Pilot":85000,
      "BMW M4":60975,
      "Highlander":55600,
      "Porche":82200,
      "Rolls Royce":100250,
      "Bugatti Chiron":95000,
      "Lamboghini":84000,
      "Rexton":44000, 
      "Pajero":45500,
      "VW Jetta":35600,
      "Toyota Hilux":55000,
      "Range Rover Velar":63600,
      "Camry":75000,
      "Santafe":57200,
      "Tundra":45220,
      "G Wagon":89632,
      "Benz S550":85500,
      "Vitz":36500,
      "Golf 2022":42500
      }
car_name=input("Enter a car_name:")
if car_name in cars:
    print("Yes")
    car_price=cars[car_name]
    print(f"Tthe price of {car_name}is${car_price}")
else:
    print(f"Sorry,{car_name}is not available")

    