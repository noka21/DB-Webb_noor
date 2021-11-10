"""
i den ska skrivas funktionerna som har med utsläppen att göra. 
I kraven när det står att skapa en specifik funktion ska du skapa den i filen emission_functions.py
"""

import emission_data


def get_country_id(country_search):
    """
    This method
    """
    for country in emission_data.country_data:
        if country == country_search:
            return emission_data.country_data[country_search]["id"]
    raise ValueError("Country does not exist!")


def get_country_pop_1990(country_search):
    """
    This method
    """
    for _ in emission_data.country_data[country_search]:
        if len(emission_data.country_data[country_search]["population"]) == 0 :
            return None
    for country in emission_data.country_data:
        if country == country_search:
            return emission_data.country_data[country_search]["population"][0]
    raise ValueError("Country does not exist!")


def get_country_pop_2005(country_search):
    """
    This method
    """
    for _ in emission_data.country_data[country_search]:
        if len(emission_data.country_data[country_search]["population"]) == 0:
            return None
    for country in emission_data.country_data:
        if country == country_search:
            return emission_data.country_data[country_search]["population"][1]
    raise ValueError("Country does not exist!")


def get_country_pop_2017(country_search):
    """
    This method
    """
    for _ in emission_data.country_data[country_search]:
        if len(emission_data.country_data[country_search]["population"]) == 0:
            return None
    for country in emission_data.country_data:
        if country == country_search:
            return emission_data.country_data[country_search]["population"][2]
    raise ValueError("Country does not exist!")


def get_country_popul(country, year):
    """
    This method
    """
    if year == '1990':
        return get_country_pop_1990(country)
    if year == '2005':
        return get_country_pop_2005(country)
    if year == '2017':
        return get_country_pop_2017(country)

    raise ValueError(" Wrong year!")


def get_country_emission_1990(emission_search):
    """
    This method
    """
    for country in emission_data.emission_1990:
        if country == emission_search:
            return (float(emission_data.emission_1990[emission_search])*1000000)
    raise ValueError("Country does not exist!")


def get_country_emission_2005(emission_search):
    """
    This method
    """
    for country in emission_data.emission_2005:
        if country == emission_search:
            return (float(emission_data.emission_2005[emission_search])*1000000)
    raise ValueError("Country does not exist!")


def get_country_emission_2017(emission_search):
    """
    This method
    """
    for country in emission_data.emission_2017:
        if country == emission_search:
            return (float(emission_data.emission_2017[emission_search])*1000000)
    raise ValueError("Country does not exist!")


def get_country_year_data_megaton(country, year):
    """
    This method
    """
    em = get_country_id(country)
    if year == '1990':
        return get_country_emission_1990(em)
    if year == '2005':
        return get_country_emission_2005(em)
    if year == '2017':
        return get_country_emission_2017(em)

    raise ValueError(" Wrong year!")


def get_country_change_for_years(country, year1, year2):
    """
    This method
    """
    result_year1 = get_country_year_data_megaton(country, year1)
    result_year2 = get_country_year_data_megaton(country, year2)
    if result_year1 == " Wrong year!" or result_year2 == " Wrong year!":
        raise ValueError(" Wrong year!")
    Decrease = result_year2-result_year1
    result = round(((Decrease / result_year1) * 100), 2)
    return result


def get_country_data(country_name):
    """
    This method
    """
    dic_data = {}
    dic_data['name'] = country_name
    dic_data['1990'] = {'emission': get_country_year_data_megaton(
        country_name, '1990'), 'population': get_country_pop_1990(country_name)}
    dic_data['2005'] = {'emission': get_country_year_data_megaton(
        country_name, '2005'), 'population': get_country_pop_2005(country_name)}
    dic_data['2017'] = {'emission': get_country_year_data_megaton(
        country_name, '2017'), 'population': get_country_pop_2017(country_name)}
    dic_data['emission_change'] = (get_country_change_for_years(
        country_name, '1990', '2005'), get_country_change_for_years(country_name, '2005', '2017'))

    return dic_data


def print_country_data(data):
    """
    This method
    """
    if data['1990']['population'] is None or data['2005']['population'] is None or data['2017']['population']is None :
        print(f"{data['name']}\nEmission\
                      - 1990: {data['1990']['emission']}    2005: {data['2005']['emission']}\
                2017: {data['2017']['emission']}\nEmission change   -   1990-2005: {data['emission_change'][0]}%\
                            2005-2017: {data['emission_change'][1]}%\nPopulation\
                                        Missing population data!")



    print(f"{data['name']}\nEmission          - 1990: {data['1990']['emission']}    2005: {data['2005']['emission']}\
                2017: {data['2017']['emission']}\nEmission change   -   1990-2005: {data['emission_change'][0]}%\
                            2005-2017: {data['emission_change'][1]}%\nPopulation\
                                        - 1990: {data['1990']['population']}       2005: {data['2005']['population']}\
                                               2017: {data['2017']['population']}")
    


def get_country(country_search):
    """
    This method
    """
    for country in emission_data.country_data:
        if country.lower() == country_search.lower():
            return True
    raise ValueError("Country does not exist!")


def search_country(search_word):
    """
    This
    """
    list_c = []
    for country in emission_data.country_data:
        if search_word.lower() == country.lower() or search_word.lower() in country.lower() :
            list_c.append(country)
    if len(list_c) == 0:
        raise ValueError("Country does not exist!")
		
    return list_c
