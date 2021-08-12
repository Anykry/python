class Date:

    @classmethod
    def retrieve(cls, input_date):
        day = int(input_date[:2])
        month = int(input_date[3:5])
        year = int(input_date[6:])

    @staticmethod
    def check_date_format(check_date):
        is_error = False
        day = int(check_date[:2])
        month = int(check_date[3:5])
        year = int(check_date[6:])
        if day < 1 or day > 31:
            error = 'incorrect day'
            is_error = True
        if month < 1 or month > 12:
            error = 'incorrect month'
            is_error = True
        if not is_error and month == 2:
            if day > 29:
                is_error = True
                error = 'incorrect day'
        if is_error:
            return error
        else:
            return 'The date is correct!'


print(Date.check_date_format('28-02-1980'))

Date.retrieve('31-02-1980')
