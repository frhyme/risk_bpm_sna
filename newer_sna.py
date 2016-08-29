import networkx as nx
import pandas as pd
#read excel file(scopus)
#class paper_information()

def return_excel_n_th_sheet_as_dataframe(excel_name, n):
	xl=pd.ExcelFile(excel_name)
	return xl.parse(xl.sheet_names[n])

def return_kwds_from_str(paper_str):	
	return [elem.strip().lower() for elem in paper_str.split(";")]
def processed_kwd(kwd):
	target_char_lst=["-", "*", "/"]
	replacer=" "
	for each_target_char in target_char_lst:
		kwd=kwd.replace(each_target_char, replacer)
	while "  " in kwd:
		kwd=kwd.replace("  ", " ").strip().lower()
	# how to make plural noun to singular
	# are there any library can be used?
	return kwd
                
#######
#############
#### main ######
print( processed_kwd("dd-d* *  /dDDdfd ") )

scopus_csv_name="risk_bpm_raw.csv"
csv_df = pd.read_csv(scopus_csv_name)
csv_df_lst=csv_df.values.tolist()

print( csv_df.columns )
#print( csv_df_lst[0] )
#print( csv_df.columns )

#design paper class
#save all related information about each paper

#read rule file(from: a to: b)



