from mainAssignment.customeExceptions.invalidCredential import InvalidInput


class InputCheck(InvalidInput, Exception):

    def int_input_check(param):
        valid = False

        while not valid:

            user_input = input(param)

            try:
                converted = int(user_input)
                valid = True
                return converted

            except InvalidInput as e:
                e.print_msg("Invalid input !! `int` required ")

            except Exception as e:
                print(e)

    def float_input_check(param):
        user_input = input(param)

        try:
            converted = float(user_input)
            return converted
        except InvalidInput as e:
            e.print_msg("Invalid input !! `float` required ")
        except Exception as e:
            print(e)

    def str_input_check(param):
        user_input = input(param)

        try:
            converted = str(user_input)

            return converted

        except InvalidInput as e:
            e.print_msg("Invalid input !! `str` required ")
        except Exception as e:
            print(e)

