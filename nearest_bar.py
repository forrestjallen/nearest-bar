#  _  _                     _     ___           
# | \| |___ __ _ _ _ ___ __| |_  | _ ) __ _ _ _ 
# | .` / -_) _` | '_/ -_|_-<  _| | _ \/ _` | '_|
# |_|\_\___\__,_|_| \___/__/\__| |___/\__,_|_|  
#                                               
#                                                                                    #
# By Forrest Allen                                                                   #
######################################################################################                                                                                    

# To execute script "python3 nearest_bar.py"

import xlrd 
import googlemaps
import os 
import xlwt 
from xlwt import Workbook 

#Google API key goes here:
api_key='MY_API_KEY'

#User Prompt to get input xlsx file name
print('Please make sure that the xlsx input file is in the same directory as this script!!!')
print('EXAMPLE USER INPUT: address_list.xlsx')
print('IMPORTANT: script will not run correctly if input file does not have columns labeled in the following order:')
print('    Number, Street, City, Zip Code, Miles To Nearest Bar')
file_name = input("Enter xlsx file name : ")
print('EXAMPLE USER INPUT: output-address_list.xls')
print('IMPORTANT: file must end with .xls')
output_name = input("Enter xls output name : ")

path_to_xlsx=os.getcwd()+'/'+file_name


# Requires API key and creates google connection
gmaps = googlemaps.Client(key=api_key) 

# Give the location of the input file 
loc = (path_to_xlsx) 
  
# Opens the input Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

#Creates the Output Workbook 
wb_out = Workbook()
sheet_out = wb_out.add_sheet('Output Sheet') 

#write column headers to the output sheet
sheet_out.write(0, 0, 'Number')
sheet_out.write(0, 1, 'Street') 
sheet_out.write(0, 2, 'Zip Code') 
sheet_out.write(0, 3, 'Miles To Nearest Bar') 
sheet_out.write(0, 4, 'Note')  
print('Number, Street, Zip Code, Miles To Nearest Bar, Note')

#Iterate through the input sheet 
for i in range(1, sheet.nrows):
	#Gets sheet values from imput xlsx file
	number = str(sheet.cell_value(i, 0))[:-2]
	street =str(sheet.cell_value(i, 1))
	zip_code=str(sheet.cell_value(i, 2))[:-2]
	note='' 

	#if no address then skip distance search
	if street=='':
		dist_value=''
		note='Warning: empty address'
		#writes values into output sheet, where distance is skipped
		sheet_out.write(i, 0, number)
		sheet_out.write(i, 1, street) 
		sheet_out.write(i, 2, zip_code) 
		sheet_out.write(i, 3, dist_value) 
		sheet_out.write(i, 4, note) 
		print('%s, %s, %s, %s, %s'%(number, street, zip_code, dist_value, note))
	
	#Run a distance search using distance_matrix function using google API
	else:
		whole_address=number+' '+street+' '+zip_code+'San Francisco CA'
		dist_dict = gmaps.distance_matrix(whole_address,'Bar near %s' % whole_address)['rows'][0]['elements'][0] 
		try:
			dist_value=str(round(dist_dict['distance']['value']*0.000621,2))
		except:
			dist_value=''
			note='Warning: Address invalid, Google could not process'
			sheet_out.write(i, 4, note) 
		#writes values into output sheet 
		sheet_out.write(i, 0, number)
		sheet_out.write(i, 1, street) 
		sheet_out.write(i, 2, zip_code) 
		sheet_out.write(i, 3, dist_value) 
		sheet_out.write(i, 4, note) 
		print('%s, %s, %s, %s, %s'%(number, street, zip_code, dist_value, note))

#save xlsx file!
wb_out.save(output_name) 

#User prompts, letting user know that script is complete
print('.                                          ')
print('.                                          ')
print('.                                          ')
print('Output saved to: '+os.getcwd()+'/'+output_name)
print('*******************************************')
print('************     DONE    ******************')
print('*******************************************')		
		
