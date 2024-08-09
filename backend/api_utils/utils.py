def get_separate_location_parts(name: str):
    clean_str = lambda x: x.strip()
    if ',' in name:
        return list(filter(clean_str, name.split(',')))
    else:
        list(filter(clean_str, name.split(' ')))