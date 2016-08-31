import networkx as nx
import pandas as pd
import numpy as np
#read excel file(scopus)
#class paper_information()
class paper:
	def __init__(self, csv_df_elem):
		self.authors = [ processed_kwd(elem) for elem in csv_df_elem["Authors"].split(".,") ]
		self.title = csv_df_elem["Title"]
		self.year = csv_df_elem["Year"]
		self.abstract = csv_df_elem["Abstract"] if not pd.isnull( csv_df_elem["Abstract"] ) else ""
		self.author_kwds = sorted( [ processed_kwd(elem) for elem in csv_df_elem["Author Keywords"].split(";") ] if not pd.isnull( csv_df_elem["Author Keywords"] ) else [] )
		self.index_kwds = sorted( [ processed_kwd(elem) for elem in csv_df_elem["Index Keywords"].split(";") ] if not pd.isnull( csv_df_elem["Index Keywords"] ) else [] )
		self.document_type = csv_df_elem["Document Type"]
		self.references = sorted( [ elem.strip() for elem in csv_df_elem["References"].split(";")] if not pd.isnull( csv_df_elem["References"] ) else [] )
		self.affiliations = sorted( [ elem.strip() for elem in csv_df_elem["Affiliations"].split(";")] if not pd.isnull( csv_df_elem["Affiliations"] ) else [] )
	def __str__(self):
		return self.title
 
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
               
def return_elem_count_lst(all_lst):
	elem_count_dict={ elem:all_lst.count(elem) for elem in list(set(all_lst)) }
	return sorted( [[key, elem_count_dict[key] ]for key in elem_count_dict], key=lambda x: x[1], reverse=True)
#designing papers class needed?
#######
#############
