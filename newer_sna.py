from frhyme_kwd_analysis import *
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
print("Author kwd")
all_author_kwd_count_lst = return_elem_count_lst( [kwd for paper_elem in papers for kwd in paper_elem.author_kwds ] )
all_author_kwd_arc_count_lst = return_elem_count_lst( [(paper_elem.author_kwds[i], paper_elem.author_kwds[j]) for paper_elem in papers for i in range(0, len(paper_elem.author_kwds)-1) for j in range(i+1, len(paper_elem.author_kwds))])
print( all_author_kwd_count_lst[0:10] )
print( all_author_kwd_arc_count_lst[0:10] )

print("Index kwd")
all_index_kwd_count_lst = return_elem_count_lst( [kwd for paper_elem in papers for kwd in paper_elem.index_kwds ] )
all_index_kwd_arc_count_lst = return_elem_count_lst( [(paper_elem.index_kwds[i], paper_elem.index_kwds[j]) for paper_elem in papers for i in range(0, len(paper_elem.index_kwds)-1) for j in range(i+1, len(paper_elem.index_kwds))])
print( all_index_kwd_count_lst[0:10] )
print( all_index_kwd_arc_count_lst[0:10] )
"""
all_author_count_lst = return_elem_count_lst( [author for paper_elem in papers for author in paper_elem.authors ] )
print( all_author_count_lst[0:10] )

all_affiliation_count_lst = return_elem_count_lst( [affiliation for paper_elem in papers for affiliation in paper_elem.affiliations ] )
print( all_affiliation_count_lst[0:10] )

all_reference_count_lst = return_elem_count_lst( [reference for paper_elem in papers for reference in paper_elem.references ] )
print( all_reference_count_lst[0:10] )
"""
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



