# This script is used for generating sample code used in unit-testing
# This file is auto run before tests.

import enkelt
import sample_code_manager


def generate():
    generate_non_real_sample_code_all_functions_expected_lexer_output()
    generate_non_real_sample_code_all_functions_expected_parser_output()
    generate_real_sample_code_all_functions_expected_lexer_output()
    generate_real_sample_code_all_functions_expected_parser_output()


functions = enkelt.functions_keywords_and_obj_notations()['functions'].keys()

# ###################### #
#  NON REAL SAMPLE CODE  #
# ###################### #

non_real_sample_code = sample_code_manager.get_non_real_sample_code()


def generate_non_real_sample_code_all_functions_expected_lexer_output():
    non_real_sample_code_all_functions_expected_lexer_output = ''

    for function in functions:
        for sample in non_real_sample_code:
            non_real_sample_code_all_functions_expected_lexer_output += str(
                enkelt.lex(
                    enkelt.fix_up_code_line(
                        function + '(' + sample + ')'
                    )
                )
            ) + '\n'

    sample_code_manager.set_non_real_sample_code_in_all_functions_expected_lexer_output(
        non_real_sample_code_all_functions_expected_lexer_output
    )


def generate_non_real_sample_code_all_functions_expected_parser_output():
    non_real_sample_code_all_functions_expected_parser_output = ''

    for function in functions:
        for sample in non_real_sample_code:
            enkelt.parse(enkelt.lex(enkelt.fix_up_code_line(function + '(' + sample + ')')), 0)
            non_real_sample_code_all_functions_expected_parser_output += ''.join(enkelt.source_code) + '\n'
            enkelt.source_code = []

    sample_code_manager.set_non_real_sample_code_in_all_functions_expected_parser_output(
        non_real_sample_code_all_functions_expected_parser_output
    )


# ################## #
#  REAL SAMPLE CODE  #
# ################## #

real_sample_code = sample_code_manager.get_real_sample_code()


# Lexer

def generate_real_sample_code_all_functions_expected_lexer_output():
    real_sample_code_all_functions_expected_lexer_output = ''

    for sample in real_sample_code:
        real_sample_code_all_functions_expected_lexer_output += str(
            enkelt.lex(
                enkelt.fix_up_code_line(
                    sample
                )
            )
        ) + '\n'

    sample_code_manager.set_real_sample_code_in_all_functions_expected_lexer_output(
        real_sample_code_all_functions_expected_lexer_output
    )


# Parser

def generate_real_sample_code_all_functions_expected_parser_output():
    real_sample_code_all_functions_expected_parser_output = ''

    for sample in real_sample_code:
        enkelt.parse(
            enkelt.lex(
                enkelt.fix_up_code_line(
                    sample
                )
            ), 0
        )
        real_sample_code_all_functions_expected_parser_output += ''.join(enkelt.source_code).replace('\n', '') + '\n'
        enkelt.source_code = []

    sample_code_manager.set_real_sample_code_in_all_functions_expected_parser_output(
        real_sample_code_all_functions_expected_parser_output
    )


def clear_files():
    sample_code_manager.set_non_real_sample_code_in_all_functions_expected_lexer_output([])
    sample_code_manager.set_non_real_sample_code_in_all_functions_expected_parser_output([])
    sample_code_manager.set_real_sample_code_in_all_functions_expected_lexer_output([])
    sample_code_manager.set_real_sample_code_in_all_functions_expected_parser_output([])
