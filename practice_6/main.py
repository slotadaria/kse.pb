import geometry
print ("1:",geometry.rectangle_area(4,6))
import converter
print ("2:",converter.uah_to_usd(1000,39.5))
print(converter.usd_to_uah(converter.uah_to_usd(1000,39.5), 39.5))
import taxes
print("3:",taxes.calculate_income_tax(15000))