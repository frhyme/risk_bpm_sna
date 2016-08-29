import networkx as nx
import pandas as pd
import numpy as np
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
		kwd=kwd.replace("  ", " ")
	# how to make plural noun to singular
	# are there any library can be used?
	return kwd.strip().lower()
class paper:
        def __init__(self, csv_df_elem):
                self.authors = [ processed_kwd(elem) for elem in csv_df_elem["Authors"].split(".,") ]
                self.title = csv_df_elem["Title"]
                self.year = csv_df_elem["Year"]
                self.abstract = csv_df_elem["Abstract"] if  not pd.isnull( csv_df_elem["Abstract"] ) else ""
                self.author_kwds = [ processed_kwd(elem) for elem in csv_df_elem["Author Keywords"].split(";") ] if not pd.isnull( csv_df_elem["Author Keywords"] ) else []
                self.index_kwds = [ processed_kwd(elem) for elem in csv_df_elem["Index Keywords"].split(";") ] if not pd.isnull( csv_df_elem["Index Keywords"] ) else []
                self.document_type = csv_df_elem["Document Type"]
                self.references = [ elem.strip() for elem in csv_df_elem["References"].split(";")] if not pd.isnull( csv_df_elem["References"] ) else []
                self.affiliations = [ elem.strip() for elem in csv_df_elem["Affiliations"].split(";")] if not pd.isnull( csv_df_elem["Affiliations"] ) else []
        def __str__(self):
                return self.title
def return_elem_count_lst(all_lst):
        elem_count_dict={ elem:all_lst.count(elem) for elem in list(set(all_lst)) }
        return sorted( [[key, elem_count_dict[key] ]for key in elem_count_dict], key=lambda x: x[1], reverse=True)
#designing papers class needed?
#######
#############
#### main ######
#print( processed_kwd("dd-d* *  /dDDdfd ") )

scopus_csv_name="risk_bpm_raw.csv"
csv_df = pd.read_csv(scopus_csv_name)
csv_df.columns = csv_df.columns.str.replace("\ufeff", "")#encoding
print( "Headers in csv DataFrame:\n", csv_df.columns.values )

#csv_df = csv_df[ csv_df["Year"]<=2015].merge( csv_df[ csv_df["Year"]>=2014 ] )
papers=[paper( csv_df.iloc[i] ) for i in range(0, len( csv_df.index ) ) if csv_df.iloc[i].isnull ]

#####kwd will be changed in this part#####
print("Paper count", len(papers))

#all_author_kwds=[kwd for paper_elem in papers for kwd in paper_elem.author_kwds ]
#all_author_kwds_dict={ kwd:all_author_kwds.count(kwd) for kwd in list(set(all_author_kwds)) }
#all_author_kwds_count_lst= sorted( [[key, all_author_kwds_dict[key] ]for key in all_author_kwds_dict], key=lambda x: x[1], reverse=True)
all_author_kwd_count_lst = return_elem_count_lst( [kwd for paper_elem in papers for kwd in paper_elem.author_kwds ] )
print( all_author_kwd_count_lst[0:10] )

all_index_kwd_count_lst = return_elem_count_lst( [kwd for paper_elem in papers for kwd in paper_elem.index_kwds ] )
print( all_index_kwd_count_lst[0:10] )

all_author_count_lst = return_elem_count_lst( [author for paper_elem in papers for author in paper_elem.authors ] )
print( all_author_count_lst[0:10] )

all_affiliation_count_lst = return_elem_count_lst( [affiliation for paper_elem in papers for affiliation in paper_elem.affiliations ] )
print( all_affiliation_count_lst[0:10] )

all_reference_count_lst = return_elem_count_lst( [reference for paper_elem in papers for reference in paper_elem.references ] )
print( all_reference_count_lst[0:10] )



#print( "\n".join( temp.references ) )
#print(temp)

##Data preprocessing


#print( csv_df.iloc[2]["Authors"])
#print( csv_df["Year"] )

#csv_df_lst=csv_df.values.tolist()
#print( csv_df.columns )

#design paper class
#save all related information about each paper

#read rule file(from: a to: b)



