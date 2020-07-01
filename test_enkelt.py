import unittest
import enkelt


def get_all_functions_sample_code_file_name(prefix, is_parser):
    return ''.join(
        [
            'TestResources/',
            prefix,
            '_sample_code/expected_',
            'parser' if is_parser else 'lexer',
            '_output/in_all_functions.txt'
        ]
    )


def default_get_sample_code(prefix, is_parser):
    lines = []
    with open(get_all_functions_sample_code_file_name(prefix, is_parser), encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                if is_parser is False:
                    import ast
                    line = list(ast.literal_eval(line))

                lines.append(line)

    return lines


def default_set_sample_code(prefix, is_parser, output):
    with open(get_all_functions_sample_code_file_name(prefix, is_parser), 'w') as f:
        f.writelines(output)


def get_enkelt_lex(code):
    return enkelt.lex(enkelt.fix_up_code_line(code))


def standard_get_expected_output(is_parser, to_lex):
    lexed_code = get_enkelt_lex(to_lex)

    if is_parser is False:
        expected = str(lexed_code)
    else:
        enkelt.parse(lexed_code, 0)
        expected = ''.join(enkelt.source_code).replace('\n', '')
        enkelt.source_code = []

    return expected + '\n'


def standard_non_real_generator(is_parser):
    sample_code_all_functions_expected_output = ''

    for function in functions:
        if function != 'töm':
            for sample in non_real_sample_code:
                sample_code_all_functions_expected_output += standard_get_expected_output(
                    is_parser, function + '(' + sample + ')'
                )

    default_set_sample_code(
        'non_real',
        is_parser,
        sample_code_all_functions_expected_output
    )


def standard_real_generator(is_parser):
    sample_code_all_functions_lexer_output = ''

    for sample in real_sample_code:
        sample_code_all_functions_lexer_output += standard_get_expected_output(
            is_parser,
            sample
        )

    default_set_sample_code(
        'real',
        is_parser,
        sample_code_all_functions_lexer_output
    )


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
        '$lexikon["c"] = 4',
        '$var => ($a, $b) {$a + $b}',
        '$var("hej", "text")',
    ]


def generator():
    standard_non_real_generator(False)
    standard_non_real_generator(True)
    standard_real_generator(False)
    standard_real_generator(True)


functions = enkelt.functions_keywords_and_obj_notations()['functions'].keys()
non_real_sample_code = get_non_real_sample_code()
real_sample_code = get_real_sample_code()


class TestEnkelt(unittest.TestCase):
    functions = enkelt.functions_keywords_and_obj_notations()['functions'].keys()
    keywords = enkelt.functions_keywords_and_obj_notations()['keywords'].keys()
    obj_notations = enkelt.functions_keywords_and_obj_notations()['obj_notations'].keys()
    operators = enkelt.operator_symbols()

    def index_calculator(self, loop_counter):
        return ((len(self.non_real_sample_code) - 1) * loop_counter) + loop_counter

    def expected_output_index_calculator(self, loop_counter, x):
        index = 0

        if loop_counter > 0:
            index = self.index_calculator(loop_counter)
        index += x

        return index

    # ###################### #
    #  NON REAL SAMPLE CODE  #
    # ###################### #

    non_real_sample_code = get_non_real_sample_code()

    # Lexer output
    non_real_sample_code_in_all_functions_expected_lexer_output = default_get_sample_code('non_real', False)

    # Parser output
    non_real_sample_code_in_all_functions_expected_parser_output = default_get_sample_code('non_real', True)

    # ################## #
    #  REAL SAMPLE CODE  #
    # ################## #

    real_sample_code = get_real_sample_code()

    # Lexer output
    real_sample_code_in_all_functions_expected_lexer_output = default_get_sample_code('real', False)

    # Parser output
    real_sample_code_in_all_functions_expected_parser_output = default_get_sample_code('real', True)

    # ####### #
    #  TESTS  #
    # ####### #

    def test_fix_up_code_line(self):
        # Tests space removal, multiple space removal, tab & newline removal,
        # comment removal and quote conversion.
        expected_for_standard_skriv = 'skriv("text")'

        self.assertEqual(enkelt.fix_up_code_line("skriv ('text')"), expected_for_standard_skriv)
        self.assertEqual(enkelt.fix_up_code_line("skriv  ('text')"), expected_for_standard_skriv)
        self.assertEqual(enkelt.fix_up_code_line("skriv   ('text')"), expected_for_standard_skriv)
        self.assertEqual(enkelt.fix_up_code_line("skriv    ('text')\n"), expected_for_standard_skriv)
        self.assertEqual(enkelt.fix_up_code_line("skriv\t('text')"), expected_for_standard_skriv)
        self.assertEqual(enkelt.fix_up_code_line("skriv\t('text text2')"), 'skriv("text text2")')
        self.assertEqual(enkelt.fix_up_code_line('importera test'), 'importera test')
        self.assertEqual(enkelt.fix_up_code_line('\\"'), '|-ENKELT_ESCAPED_QUOTE-|')
        self.assertEqual(enkelt.fix_up_code_line('\\'), '|-ENKELT_ESCAPED_BACKSLASH-|')

    def test_has_numbers(self):
        self.assertEqual(enkelt.has_numbers('text'), False)
        self.assertEqual(enkelt.has_numbers('t1e2x3t4'), True)

    def test_translate_function(self):
        self.assertEqual(enkelt.translate_function('skriv'), 'print')
        self.assertEqual(enkelt.translate_function('definitely_not_a_function'), 'error')

    def test_translate_keyword(self):
        self.assertEqual(enkelt.translate_keyword('Sant'), 'True')
        self.assertEqual(enkelt.translate_keyword('definitely_not_a_keyword'), 'error')

    def test_translate_obj_notation(self):
        self.assertEqual(enkelt.translate_obj_notation('försök'), 'try')
        self.assertEqual(enkelt.translate_obj_notation('definitely_not_an_obj_notation'), 'error')

    def test_translate_output_to_swedish(self):
        to_be_translated = {
            'True': 'Sant',
            'False': 'Falskt',
        }

        data_types_to_be_translated = {
            'float': 'decimaltal',
            'str': 'sträng',
            'int': 'heltal',
            'list': 'lista',
            'dict': 'lexikon',
            'bool': 'boolesk',
            'NoneType': 'inget',
            'Exception': 'Feltyp'
        }

        for english in data_types_to_be_translated.keys():
            to_be_translated['<class \'' + english + '\'>'] = data_types_to_be_translated[english]

        for english in to_be_translated.keys():
            self.assertEqual(enkelt.translate_output_to_swedish(english), to_be_translated[english])

    def test_translate_clear(self):
        self.assertEqual(enkelt.translate_clear(), 'clear')

    def test_lex(self):
        # ###################### #
        #  NON REAL SAMPLE CODE  #
        # ###################### #
        loop_counter = 0

        for function in self.functions:
            if function != 'töm':
                for x, sample in enumerate(self.non_real_sample_code):
                    index = self.expected_output_index_calculator(loop_counter, x)

                    self.assertEqual(
                        get_enkelt_lex(function + '(' + sample + ')'),
                        self.non_real_sample_code_in_all_functions_expected_lexer_output[index]
                    )
                loop_counter += 1

        # ################## #
        #  REAL SAMPLE CODE  #
        # ################## #
        loop_counter = 0

        for x, sample in enumerate(self.real_sample_code):
            index = self.expected_output_index_calculator(loop_counter, x)

            self.assertEqual(
                get_enkelt_lex(sample),
                self.real_sample_code_in_all_functions_expected_lexer_output[index]
            )
        loop_counter += 1

    def test_parse(self):
        # ###################### #
        #  NON REAL SAMPLE CODE  #
        # ###################### #
        loop_counter = 0

        for function in self.functions:
            if function != 'töm':
                for x, sample in enumerate(self.non_real_sample_code):
                    index = self.expected_output_index_calculator(loop_counter, x)

                    enkelt.parse(get_enkelt_lex(function + '(' + sample + ')'), 0)

                    self.assertEqual(
                        ''.join(enkelt.source_code),
                        self.non_real_sample_code_in_all_functions_expected_parser_output[index]
                    )

                    enkelt.source_code = []

                loop_counter += 1

        # ################## #
        #  REAL SAMPLE CODE  #
        # ################## #
        loop_counter = 0

        for x, sample in enumerate(self.real_sample_code):
            index = self.expected_output_index_calculator(loop_counter, x)

            enkelt.parse(get_enkelt_lex(sample), 0)

            self.assertEqual(
                ''.join(enkelt.source_code).replace('\n', ''),
                self.real_sample_code_in_all_functions_expected_parser_output[index]
            )

            enkelt.source_code = []

        loop_counter += 1


if __name__ == '__main__':
    unittest.main()
    
