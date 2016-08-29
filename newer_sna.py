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
	target_char_lst=["-", "*", "/", "."]
	replacer=" "
	for each_target_char in target_char_lst:
		kwd=kwd.replace(each_target_char, replacer)
	while "  " in kwd:
		kwd=kwd.replace("  ", " ").strip().lower()
	# how to make plural noun to singular
	# are there any library can be used?
	return kwd
class paper:
        def __init__(self, csv_df_elem):
                self.authors = [ processed_kwd(elem) for elem in csv_df_elem["Authors"].split(".,") ]
                self.title = csv_df_elem["Title"]
                self.abstract = csv_df_elem["Abstract"]
        def __str__(self):
                return self.title
#######
#############
#### main ######
#print( processed_kwd("dd-d* *  /dDDdfd ") )

scopus_csv_name="risk_bpm_raw.csv"
csv_df = pd.read_csv(scopus_csv_name)
csv_df.columns = csv_df.columns.str.replace("\ufeff", "")#encoding
print( "Headers in csv DataFrame\n", csv_df.columns.values )


temp=paper(csv_df.iloc[0])
print(temp.authors)
print(temp)

##Data preprocessing


#print( csv_df.iloc[2]["Authors"])
#print( csv_df["Year"] )

#csv_df_lst=csv_df.values.tolist()
#print( csv_df.columns )

#design paper class
#save all related information about each paper

#read rule file(from: a to: b)



