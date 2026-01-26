def map_resource_type_to_bibtex(resource_type):
    csl_to_bibtex = {
    "report": "techreport",
    "article": "article",
    "book": "book",
    "chapter": "inbook",
    "map": "misc",
    "paper-conference": "inproceedings",
    "graphic": "misc",
    "pamphlet": "misc",
    "legislation": "misc",
    "manuscript": "unpublished",
    "webpage": "misc",
    "article-newspaper": "misc",
    "review": "article"
}
    
    return csl_to_bibtex.get(resource_type, "misc")


def valid_int_or_none(v, lo, hi):
    if v is None:
        return None
    try:
        v = int(v)
    except (ValueError, TypeError):
        return None
    return v if lo <= v <= hi else None


def create_bibtex_entry(csl_data, id_):
    entry_type = map_resource_type_to_bibtex(csl_data['type'])
    authors = csl_data.get('author', [])
    title = csl_data.get('title')
    year, month, day = None, None, None
    if 'issued' in csl_data:
        date_parts = csl_data['issued'].get('date-parts')
        if date_parts and len(date_parts) > 0:
            year, month, day = (date_parts[0] + [None, None, None])[:3]
            year = valid_int_or_none(year, 1, 9999)
            month = valid_int_or_none(month, 1, 12)
            day = valid_int_or_none(day, 1, 31)
            
    doi = csl_data.get('DOI')
    publisher = csl_data.get('publisher','')    

    
    author_list = []
    for author in authors:
        family = author.get('family', '')
        given = author.get('given', '')
        if family and given:
            author_str = f"{family}, {given}"
        elif family:
            author_str = family
        else:
            author_str = given
        author_list.append(author_str)
    authors_str = " and ".join(author_list)
    
    bibtex_fields = []
    if authors_str:
        bibtex_fields.append(f'author = {{{authors_str}}}')
    if title:
        bibtex_fields.append(f'title = {{{title}}}')
    if year:
        bibtex_fields.append(f'year = {{{year}}}')
    if month:
        bibtex_fields.append(f'month = {{{month}}}')
    if day:
        bibtex_fields.append(f'day = {{{day}}}')
    if publisher:
        bibtex_fields.append(f'publisher = "{publisher}"')   
    if doi:
        bibtex_fields.append(f'doi = {{{doi}}}') 
        
    bibtex_entry = f"@{entry_type}{{{id_},\n"
    bibtex_entry += ",\n".join(bibtex_fields)
    bibtex_entry += "\n}\n"
 
    return bibtex_entry       

        
                  
def get_bibtex_type(csl_type):
    return 'dataset'


    
    
    