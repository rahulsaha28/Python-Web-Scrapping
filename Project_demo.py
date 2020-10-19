# --------------------------------import all important library ------------------------
import requests
import time
from bs4 import BeautifulSoup
import csv

# -----------------------------------------------------------------

class GraphData:
    def __init__(self, url):
        self.url = url
        self.data = []

    def get_Beautiful_html_from_url(self):

        try:
            request_file = requests.get(self.url)
            b_html = BeautifulSoup(request_file.text, 'html.parser')
            return b_html
        except:
            print("Invalid url")
            return None

    # ---------------------------------------------------get all versity link ----------------------------------------
    def gel_all_link(self):
        self.all_link = []
        all_html = self.get_Beautiful_html_from_url()
        all_versity_link = all_html.select('a[class=link-container__link]')

        for a in all_versity_link:
            self.all_link.append('https://digital.ucas.com'+a.get('href'))


    def get_all_fee(self, link_html):
        try:
            fee_array = link_html.find_all('div', {
                    'class': 'table-responsive table-responsive--list table-borderless table-col1-bold'})[1]
            t_fee_array = BeautifulSoup(f'<html>{fee_array}</html>', 'html.parser')
            t_fee = t_fee_array.find_all('td', {'class':'column-width--30pc'})
            t_fee_val = t_fee_array.find_all('td', {"class": 'column-width--20pc'})
        except:
            t_fee = []

        t_fee_v = {}
        if 0 < len(t_fee):
            for a in t_fee:

                if a.text == 'England':
                    t_fee_v.update({
                        'England': t_fee_val[t_fee.index(a)].text
                    })
                elif a.text == 'Northern Ireland':
                    t_fee_v.update({
                        'Northern Ireland': t_fee_val[t_fee.index(a)].text
                    })
                elif a.text == 'Scotland':
                    t_fee_v.update({
                        'Scotland': t_fee_val[t_fee.index(a)].text
                    })
                elif a.text == 'Wales':
                    t_fee_v.update({
                        'Wales': t_fee_val[t_fee.index(a)].text
                    })

        return t_fee_v



    def made_data(self):
        for a in self.all_link:
            self.url = a
            versity_data = self.get_Beautiful_html_from_url()
            time.sleep(2)
            v_name = versity_data.find(id = 'provider-name')
            v_course = versity_data.find(id='course-title')
            degree_level = versity_data.find('div', {'class': 'heading-with-meta'}).findChild('h5')

            # ------------------------------------different----------------------------
            cd = versity_data.find_all('label', {'class':'v5-form-item__label'})
            course_duration = BeautifulSoup(f'<html>{cd[4]}</html>', 'html.parser').label
            study_mode = BeautifulSoup(f'<html>{cd[3]}</html>', 'html.parser').label
            start_date = BeautifulSoup(f'<html>{cd[2]}</html>', 'html.parser').label
            # ---------------------------------------------

            course_code = versity_data.find('td',{'id':'application-code'})
            institution_code = versity_data.find('td',{'id':'institution-code'})

            # -----------------------different-----------------------------
            try:
                campous_name_1= versity_data.find_all('td', {'class':'column-width--70pc'})
                campous_name = BeautifulSoup(f'<html>{campous_name_1[2]}</html>', 'html.parser').td
                campous_code = BeautifulSoup(f'<html>{campous_name_1[3]}</html>', 'html.parser').td
            # -------------------------------------------

                a_level_descript = versity_data.find('td', {'class':'column-width--50pc'})

                fees = self.get_all_fee(versity_data)

                #-------------------- collect data ---------------------------
                self.data.append({

                    'Versity Name':v_name.text,
                    'Course':v_course.text,
                    'Degree':degree_level.text,
                    'Course Duration':course_duration['data-options-bar-item-value'],
                    'Study mode':study_mode['data-options-bar-item-value'],
                    'Start Date':start_date['data-options-bar-item-value'],
                    'Course Code':course_code.text,
                    'Institution Code':institution_code.text,
                    'Campous Name':campous_name.text,
                    'Campous Code':campous_code.text,
                    'A level Description':a_level_descript.text,
                    'England':fees.get('England', ''),
                    'Northern Ireland':fees.get('Northern Ireland', ''),
                    'Wales':fees.get('Wales', ''),
                    'Scotland':fees.get('Scotland', '')


                })

            except:
                print('Some thing went wrong')


    def save_as_csv_file(self):
        with open('new_data.csv', 'w') as csv_file:
            csv_writter = csv.DictWriter(csv_file, fieldnames=[
                'Versity Name',
                'Course',
                'Location',
                'Degree',
                'Course Duration',
                'Study mode',
                'Start Date',
                'Course Code',
                'Institution Code',
                'Campous Name',
                'Campous Code',
                'A level Description',
                'England',
                'Northern Ireland',
                'Wales',
                'Scotland'

                ])
            csv_writter.writeheader()
            for a in self.data:
                csv_writter.writerow(a)



