def test_function( name_user = ''):

    def inner_function():
        print(f"Дорогая, {name_user}, должен сказать, что я в области видимости функции test_function.")

    inner_function()

    return 0

person = 'Frosya'
test_function( person)
# inner_function( person)
# Вызов inner_function( person) вызывает ошибку конфликт имён 'NameError: name 'inner_function' is not defined'
