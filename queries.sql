
-- SQLite
DROP TABLE IF EXISTS LatinUpperAlphabet;
DROP TABLE IF EXISTS LatinLowerAlphabet;
DROP TABLE IF EXISTS ArabicNumerals;
DROP TABLE IF EXISTS PunctuationCharacters;

CREATE TABLE IF NOT EXISTS LatinUpperAlphabet (
    latin_upper_alphabet_index INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    uppercase_letter VARCHAR(1) NOT NULL
);                  

INSERT INTO LatinUpperAlphabet (uppercase_letter) VALUES
    ('A'),
    ('B'),
    ('C'),
    ('D'),
    ('E'),
    ('F'),
    ('G'),
    ('H'),
    ('I'),
    ('J'),
    ('K'),
    ('L'),
    ('M'),
    ('N'),
    ('O'),
    ('P'),
    ('Q'),
    ('R'),
    ('S'),
    ('T'),
    ('U'),
    ('V'),
    ('W'),
    ('X'),
    ('Y'),
    ('Z')
;

CREATE TABLE IF NOT EXISTS LatinLowerAlphabet (
    latin_lower_alphabet_index INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    lowercase_letter VARCHAR(1) NOT NULL
);

INSERT INTO LatinLowerAlphabet (lowercase_letter) VALUES
    ('a'),
    ('b'),
    ('c'),
    ('d'),
    ('e'),
    ('f'),
    ('g'),
    ('h'),
    ('i'),
    ('j'),
    ('k'),
    ('l'),
    ('m'),
    ('n'),
    ('o'),
    ('p'),
    ('q'),
    ('r'),
    ('s'),
    ('t'),
    ('u'),
    ('v'),
    ('w'),
    ('x'),
    ('y'),
    ('z')
;

CREATE TABLE IF NOT EXISTS ArabicNumerals(
    arabic_numerals_index INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    numeral VARCHAR(1) NOT NULL
);

INSERT INTO ArabicNumerals (numeral) VALUES
    ("0"),
    ("1"),
    ("2"),
    ("3"),
    ("4"),
    ("5"),
    ("6"),
    ("7"),
    ("8"),
    ("9")
;


CREATE TABLE IF NOT EXISTS PunctuationCharacters (
    punctuation_characters_index INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    punctuation_character VARCHAR(1) NOT NULL
);

INSERT INTO PunctuationCharacters (punctuation_character) VALUES
    ('!'),
    ('"'),
    ('#'),
    ('$'),
    ('%'),
    ('&'),
    (''''),
    ('('),
    (')'),
    ('*'),
    ('+'),
    (','),
    ('-'),
    ('.'),
    ('/'),
    (':'),
    (';'),
    ('<'),
    ('='),
    ('>'),
    ('?'),
    ('@'),
    ('['),
    ('\'),
    (']'),
    ('^'),
    ('_'),
    ('`'),
    ('{'),
    ('|'),
    ('}'),
    ('~')
;