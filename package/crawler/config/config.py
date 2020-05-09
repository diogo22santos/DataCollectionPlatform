import pathlib

# directories for storing data
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES_DIR = PACKAGE_ROOT / 'files'

# information for http request
HEADERS = {'User-Agent': 'Mozilla/5.0'}
WORTEN_URL = 'https://www.worten.pt'
WORTEN_URL = WORTEN_URL + '/promocoes?per_page=48&page='
WORTEN_URL_SORT = '&sort_by=name'


def build_worten_url(*, page):
    """Defines the page for the URL Extraction"""
    if page:
        url = f'{WORTEN_URL}{page}{WORTEN_URL_SORT}'
    else:
        url = f'{WORTEN_URL}1{WORTEN_URL_SORT}'
    return url


# Number of pages to be extracted
PAGES = 2

# Configurations of worten data file
worten_columns = ['produto', 'promocao', 'preco', 'preco_antigo', 'descricao']
worten_file_name = 'worten_extraction.csv'
