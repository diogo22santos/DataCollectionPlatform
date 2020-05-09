from package.crawler.crawler.support_functions.functions import request, save_dataframe, worten_scrapping
from package.crawler.config import config


def request_data(pages=config.PAGES):
    """Request data from individual URL link obtained from baseline_request.list_extraction"""
    for page in range(1, pages):
        worten_soup = request(baseline_url=config.build_worten_url(page=str(page)))
        worten_data = worten_scrapping(soup=worten_soup)
        return worten_data


if __name__ == '__main__':
    save_dataframe(
        data=request_data(),
        columns=config.worten_columns,
        path_to_save=config.FILES_DIR,
        file_name=config.worten_file_name
    )
