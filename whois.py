import whois
def site_check(site_address):
    return whois.whois(site_address)


def get_input_address():
    site_address = input('Please enter the site address: ')
    return site_address


def main_program():
    print(site_check(get_input_address()))
    
    
main_program()