from sys import maxsize


class Contact:

    def __init__(self,
                 id=None,
                 first_name=None,
                 middle_name=None,
                 last_name=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 all_emails_from_home_page=None,
                 all_phones_from_home_page=None,
                 home_phone=None,
                 mobile_phone=None,
                 work_phone=None,
                 fax=None,
                 email_1=None,
                 email_2=None,
                 email_3=None,
                 homepage=None,
                 day_of_birth=None,
                 month_of_birth=None,
                 year_of_birth=None,
                 anniversary_day=None,
                 anniversary_month=None,
                 anniversary_year=None,
                 address_2=None,
                 phone_2=None,
                 notes=None):

        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.notes = notes

    def __repr__(self):
        return f"id: {self.id}; last name: {self.last_name}; first name: {self.first_name}; home phone: {self.home_phone}; " \
               f"mobile phone: {self.mobile_phone}; work phone: {self.work_phone}; phone 2: {self.phone_2}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
