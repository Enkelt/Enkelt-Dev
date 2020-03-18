# This module is used in unit testing
# Manages sample code generated by the generate_test_resources.py script.


# ###################### #
#  NON REAL SAMPLE CODE  #
# ###################### #
def get_non_real_sample_code():
    return [
        '"text"',
        '"text text"',
        '"text \"text\""',
        '"text \\ text"',
        '23',
        '10 + 5',
        '10 - 1',
        '10 * 5',
        '10 / 5',
        '10 % 5',
        'Sant',
        'Falskt',
        '["text", 1, Sant]',
        '["text", 1, Sant, ["text", 1, Sant]]',
        '$var',
        '"text" + "text"',
        '$var + "text"',
        'funktion()',
        'funktion("text", Falskt, 1, ["text", 1])',
    ]


# Lexer
def get_non_real_sample_code_in_all_functions_expected_lexer_output():
    lines = []
    with open('TestResources/non_real_sample_code/expected_lexer_output/in_all_functions.txt') as f:
        for line in f.readlines():
            lines.append(list(eval(line.strip())))

    return lines


def set_non_real_sample_code_in_all_functions_expected_lexer_output(expected_lexer_output):
    with open('TestResources/non_real_sample_code/expected_lexer_output/in_all_functions.txt', 'w') as f:
        f.writelines(expected_lexer_output)


# Parser
def get_non_real_sample_code_in_all_functions_expected_parser_output():
    lines = []
    with open('TestResources/non_real_sample_code/expected_parser_output/in_all_functions.txt') as f:
        for line in f.readlines():
            if line:
                lines.append(line.strip())

    return lines


def set_non_real_sample_code_in_all_functions_expected_parser_output(expected_parser_output):
    with open('TestResources/non_real_sample_code/expected_parser_output/in_all_functions.txt', 'w') as f:
        f.writelines(expected_parser_output)


# ################## #
#  REAL SAMPLE CODE  #
# ################## #

def get_real_sample_code():
    return [
        '$var = "hej"',
        '$matematik = 1+ 2 * -3 /4',
        'om ("test" == $var) {}',
        'anom (1 > 4) {}',
        'annars {}',
        'för ($i; inom området(0,11) {}',
        'medan ($var <= längd($var_a)) {}',
        'def minFunktion() {}',
        'def en_funktion ($param) {}',
        'def minAndra_Funktion($param_1, $param_2)',
        'klass minKlass2 {}',
        'försök {}',
        'fånga $error {}',
        '$lista_1 = [1, 2, 3]',
        '$lista.till(4)',
        '$lexikon = {"a": "alpha", "b": Sant}',
        '$lexikon["c"] = 4'
    ]


# Lexer
def get_real_sample_code_in_all_functions_expected_lexer_output():
    lines = []
    with open('TestResources/real_sample_code/expected_lexer_output/in_all_functions.txt') as f:
        for line in f.readlines():
            lines.append(list(eval(line.strip())))

    return lines


def set_real_sample_code_in_all_functions_expected_lexer_output(expected_lexer_output):
    with open('TestResources/real_sample_code/expected_lexer_output/in_all_functions.txt', 'w') as f:
        f.writelines(expected_lexer_output)


# Parser
def get_real_sample_code_in_all_functions_expected_parser_output():
    lines = []
    with open('TestResources/real_sample_code/expected_parser_output/in_all_functions.txt') as f:
        for line in f.readlines():
            if line:
                lines.append(line.strip())

    return lines


def set_real_sample_code_in_all_functions_expected_parser_output(expected_parser_output):
    with open('TestResources/real_sample_code/expected_parser_output/in_all_functions.txt', 'w') as f:
        f.writelines(expected_parser_output)

