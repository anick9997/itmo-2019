from datetime import datetime


def is_adult(
    input_function=input,
    today_function=datetime.now,
):
    users_birthday = datetime.strptime(
        input_function('Your birthday:'),
        '%Y.%m.%d',
    )
    delta = today_function() - users_birthday
    return delta.days / 365 >= 18
