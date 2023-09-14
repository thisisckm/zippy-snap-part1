
def sort_dict_list(dict_list, key, ascending=True):
    """
    Sort a list of dictionaries based on a specified key.

    Returns:
    list: A sorted list of dictionaries.
    """
    if not dict_list:
        return []
    
    if key not in dict_list[0]:
        raise KeyError(f"'{key}' not found in dictionary keys")
    
    return sorted(dict_list, key=lambda x: x[key], reverse=not ascending)
