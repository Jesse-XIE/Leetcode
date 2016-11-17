
# coding: utf-8


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import os


site = "https://leetcode.com"
result_dir = './scrapped_code'
username = 'Jesse-XIE'
passwork = '*********'
PhantomJS_executable_path = '/home/jin/Documents/apprendre/'
    'Informatique/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'


def log_in(driver):
    # Log in
    driver.get('https://leetcode.com/accounts/login/')
    print 'Login in...'
    username = driver.find_element_by_id("id_login")
    username.clear()
    username.send_keys(username)
    password = driver.find_element_by_id("id_password")
    password.clear()
    password.send_keys(password)
    password.send_keys(Keys.RETURN)
    assert 'Problems' in driver.title
    print 'Logged in successfully!\n'


def get_scrapped_problems():
    prob_nums = []
    pattern = re.compile(r'(\d*)-.*')
    for fname in os.listdir(result_dir):
        match = pattern.match(fname)
        if match:
            prob_nums.append(int(match.group(1)))
    prob_nums.sort()
    return prob_nums


def get_accepted_problems(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    rows = soup.find_all('tr')
    hrefs = []
    scrapped = get_scrapped_problems()
    print 'Problem scrapped: '
    print scrapped
    prob_nums = []
    for row in rows:
        tds = row.find_all('td')
        if tds and tds[0].get('value') == 'ac':
            prob_num = int(tds[1].string)
            if prob_num not in scrapped:
                prob_nums.append(prob_num)
                href = site + row.find('a').get('href')
                hrefs.append(href)
    print 'Problems to scrap: ({} in tatal)'.format(len(prob_nums))
    print prob_nums
    return hrefs


def parse_submission_list(href, driver):
    driver.get(href)
    # parse submission page
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    rows1 = soup.find_all('tr')
    for row1 in rows1:
        temp = row1.find('strong')
        if temp and temp.get_text() == 'Accepted':
            tds = row1.find_all('td')
            href1 = site + tds[2].find('a').get('href')
            return href1


def parse_submission(href, driver):
    driver.get(href)
    code = driver.find_element_by_xpath("//div[@class='ace_content']").text
    code = code.split('\n')
    language = driver.find_element_by_id("result_language").text
    return [code, language]


def parse_problem_description(href, driver):
    driver.get(href)
    description = driver.find_element_by_class_name('question-content').text
    description = description.split('\n')
    to_remove = ['Subscribe to see which companies asked this question',
                 'Show Tags',
                 'Show Similar Problems',
                 'Show Hint']
    for item in to_remove:
        if item in description:
            description.remove(item)
    description = [d for d in description]

    title = driver.find_element_by_tag_name('h3')
    pattern = re.compile(r'(\d*)\.\s(.*)')
    match = pattern.match(title.text)
    pb_num = int(match.group(1))
    pb_str = match.group(2)
    return [pb_num, pb_str, description]


def save_code(pb_num, pb_str, description, code, language):
    # file name generation
    suffix = {'python': 'py', 'cpp': 'cpp'}
    comment = {'python': "# ", 'cpp': '//'}

    fname = '{:03}-{}.{}'.format(pb_num,
                                 pb_str.replace(' ', '_'),
                                 suffix[language])
    lines = ['Description: ']
    lines += ['---------------\n']
    lines += ['' + d for d in description]
    lines += ['\n']
    lines = [comment[language] + ' ' + l for l in lines if l != '\n']
    lines += ['\n\n']
    lines += code
    with open(os.path.join(result_dir, fname), 'w+') as f:
        f.write('\n'.join(lines).encode('utf-8'))

if __name__ = '__main__':

    driver = webdriver.PhantomJS(executable_path=PhantomJS_executable_path)
    driver.set_window_position(0, 0)
    driver.set_window_size(1600, 900)
    # Poll the DOM for a certain amount of time when trying to find an
    # element or elements if they are not immediately available
    driver.implicitly_wait(10)

    log_in(driver)

    option = driver.find_element_by_xpath(
        "//span[@class='row-selector']/select[@class='form-control']/option[4]")
    option.click()

    accepted_hrefs = get_accepted_problems(driver)

    for i, href in enumerate(accepted_hrefs):
        print 'Getting problem description:'
        pb_num, pb_str, description = parse_problem_description(href, driver)
        print 'Problem: {}. {}'.format(pb_num, pb_str)
        submission_href = parse_submission_list(href + '/submissions', driver)
        print 'Got latest submission href: {}'.format(submission_href)
        code, language = parse_submission(submission_href, driver)
        print 'Got code'
        save_code(pb_num, pb_str, description, code, language)
        print 'Saved code to file\n'
    print '\nFinished'
