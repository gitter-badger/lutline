#!/usr/bin/env python3


import unittest
import lutline


class TestCase(unittest.TestCase):

    def test_generate(self):
        cases = [
            (
                """\
                    required:
                        optional:
                            explicit -f
                        implicit input_fn
                    usage: app.py [-f] <input_fn>
                """,
                "1,,,input_fn|2,0,-f,-f;input_fn"
            ),
            (
                """\
                    required:
                        optional:
                            explicit template
                        implicit template

                    usage: app.py [template] <template>
                """,
                "1,,,template|2,0,template,template_explicit;template"
            ),
            (
                """\
                    exclusive:
                        explicit parse
                        required:
                            optional:
                                explicit --template
                            implicit input_fn
                    usage: app.py (parse | [--template] <input_fn>)
                """,
                "1,,,input_fn|1,0,parse,parse|2,0,--template,--template;input_fn"
            ),
            (
                """\
                    exclusive:
                        required:
                            explicit cook  # ola
                            optional:
                                exclusive:
                                    explicit -u
                                    explicit --urgent
                            explicit --table
                            implicit table  # this is a comment
                            required:
                                explicit --item
                                implicit item
                                #optional:
                                #    explicit --style
                                #    explicit style
                        required:
                            explicit checkout
                            explicit --table
                            explicit --payment_method
                        required:
                            explicit menu
                            explicit set
                            required:
                                explicit recepies
                """,
                "3,0;1;2,menusetrecepies,menu;set;recepies|3,0;1;2,checkout--table--payment_method,checkout;--table;--payment_method|5,0;1;3,cook--table--item,cook;--table;table;--item;item|6,0;1;2;4,cook--urgent--table--item,cook;--urgent;--table;table;--item;item|6,0;1;2;4,cook-u--table--item,cook;-u;--table;table;--item;item"
            ),
            (
                """\
                    unordered:
                        explicit -a
                        explicit --author
                        implicit author
                        explicit -c
                        explicit --change
                """,
                "5,0;1;3;4,--change-c--author-a,--change;-c;author;--author;-a|5,0;1;3;4,--change-c-a--author,--change;-c;author;-a;--author|5,0;1;2;4,--change-c--author-a,--change;-c;--author;author;-a|5,0;1;2;3,--change-c--author-a,--change;-c;--author;-a;author|5,0;1;2;4,--change-c-a--author,--change;-c;-a;author;--author|5,0;1;2;3,--change-c-a--author,--change;-c;-a;--author;author|5,0;2;3;4,--change-c--author-a,--change;author;-c;--author;-a|5,0;2;3;4,--change-c-a--author,--change;author;-c;-a;--author|5,0;2;3;4,--change--author-c-a,--change;author;--author;-c;-a|5,0;2;3;4,--change--author-a-c,--change;author;--author;-a;-c|5,0;2;3;4,--change-a-c--author,--change;author;-a;-c;--author|5,0;2;3;4,--change-a--author-c,--change;author;-a;--author;-c|5,0;1;2;4,--change--author-c-a,--change;--author;-c;author;-a|5,0;1;2;3,--change--author-c-a,--change;--author;-c;-a;author|5,0;1;3;4,--change--author-c-a,--change;--author;author;-c;-a|5,0;1;3;4,--change--author-a-c,--change;--author;author;-a;-c|5,0;1;2;3,--change--author-a-c,--change;--author;-a;-c;author|5,0;1;2;4,--change--author-a-c,--change;--author;-a;author;-c|5,0;1;2;4,--change-a-c--author,--change;-a;-c;author;--author|5,0;1;2;3,--change-a-c--author,--change;-a;-c;--author;author|5,0;1;3;4,--change-a-c--author,--change;-a;author;-c;--author|5,0;1;3;4,--change-a--author-c,--change;-a;author;--author;-c|5,0;1;2;3,--change-a--author-c,--change;-a;--author;-c;author|5,0;1;2;4,--change-a--author-c,--change;-a;--author;author;-c|5,0;1;3;4,-c--change--author-a,-c;--change;author;--author;-a|5,0;1;3;4,-c--change-a--author,-c;--change;author;-a;--author|5,0;1;2;4,-c--change--author-a,-c;--change;--author;author;-a|5,0;1;2;3,-c--change--author-a,-c;--change;--author;-a;author|5,0;1;2;4,-c--change-a--author,-c;--change;-a;author;--author|5,0;1;2;3,-c--change-a--author,-c;--change;-a;--author;author|5,0;2;3;4,-c--change--author-a,-c;author;--change;--author;-a|5,0;2;3;4,-c--change-a--author,-c;author;--change;-a;--author|5,0;2;3;4,-c--author--change-a,-c;author;--author;--change;-a|5,0;2;3;4,-c--author-a--change,-c;author;--author;-a;--change|5,0;2;3;4,-c-a--change--author,-c;author;-a;--change;--author|5,0;2;3;4,-c-a--author--change,-c;author;-a;--author;--change|5,0;1;2;4,-c--author--change-a,-c;--author;--change;author;-a|5,0;1;2;3,-c--author--change-a,-c;--author;--change;-a;author|5,0;1;3;4,-c--author--change-a,-c;--author;author;--change;-a|5,0;1;3;4,-c--author-a--change,-c;--author;author;-a;--change|5,0;1;2;3,-c--author-a--change,-c;--author;-a;--change;author|5,0;1;2;4,-c--author-a--change,-c;--author;-a;author;--change|5,0;1;2;4,-c-a--change--author,-c;-a;--change;author;--author|5,0;1;2;3,-c-a--change--author,-c;-a;--change;--author;author|5,0;1;3;4,-c-a--change--author,-c;-a;author;--change;--author|5,0;1;3;4,-c-a--author--change,-c;-a;author;--author;--change|5,0;1;2;3,-c-a--author--change,-c;-a;--author;--change;author|5,0;1;2;4,-c-a--author--change,-c;-a;--author;author;--change|5,1;2;3;4,--change-c--author-a,author;--change;-c;--author;-a|5,1;2;3;4,--change-c-a--author,author;--change;-c;-a;--author|5,1;2;3;4,--change--author-c-a,author;--change;--author;-c;-a|5,1;2;3;4,--change--author-a-c,author;--change;--author;-a;-c|5,1;2;3;4,--change-a-c--author,author;--change;-a;-c;--author|5,1;2;3;4,--change-a--author-c,author;--change;-a;--author;-c|5,1;2;3;4,-c--change--author-a,author;-c;--change;--author;-a|5,1;2;3;4,-c--change-a--author,author;-c;--change;-a;--author|5,1;2;3;4,-c--author--change-a,author;-c;--author;--change;-a|5,1;2;3;4,-c--author-a--change,author;-c;--author;-a;--change|5,1;2;3;4,-c-a--change--author,author;-c;-a;--change;--author|5,1;2;3;4,-c-a--author--change,author;-c;-a;--author;--change|5,1;2;3;4,--author--change-c-a,author;--author;--change;-c;-a|5,1;2;3;4,--author--change-a-c,author;--author;--change;-a;-c|5,1;2;3;4,--author-c--change-a,author;--author;-c;--change;-a|5,1;2;3;4,--author-c-a--change,author;--author;-c;-a;--change|5,1;2;3;4,--author-a--change-c,author;--author;-a;--change;-c|5,1;2;3;4,--author-a-c--change,author;--author;-a;-c;--change|5,1;2;3;4,-a--change-c--author,author;-a;--change;-c;--author|5,1;2;3;4,-a--change--author-c,author;-a;--change;--author;-c|5,1;2;3;4,-a-c--change--author,author;-a;-c;--change;--author|5,1;2;3;4,-a-c--author--change,author;-a;-c;--author;--change|5,1;2;3;4,-a--author--change-c,author;-a;--author;--change;-c|5,1;2;3;4,-a--author-c--change,author;-a;--author;-c;--change|5,0;1;2;4,--author--change-c-a,--author;--change;-c;author;-a|5,0;1;2;3,--author--change-c-a,--author;--change;-c;-a;author|5,0;1;3;4,--author--change-c-a,--author;--change;author;-c;-a|5,0;1;3;4,--author--change-a-c,--author;--change;author;-a;-c|5,0;1;2;3,--author--change-a-c,--author;--change;-a;-c;author|5,0;1;2;4,--author--change-a-c,--author;--change;-a;author;-c|5,0;1;2;4,--author-c--change-a,--author;-c;--change;author;-a|5,0;1;2;3,--author-c--change-a,--author;-c;--change;-a;author|5,0;1;3;4,--author-c--change-a,--author;-c;author;--change;-a|5,0;1;3;4,--author-c-a--change,--author;-c;author;-a;--change|5,0;1;2;3,--author-c-a--change,--author;-c;-a;--change;author|5,0;1;2;4,--author-c-a--change,--author;-c;-a;author;--change|5,0;2;3;4,--author--change-c-a,--author;author;--change;-c;-a|5,0;2;3;4,--author--change-a-c,--author;author;--change;-a;-c|5,0;2;3;4,--author-c--change-a,--author;author;-c;--change;-a|5,0;2;3;4,--author-c-a--change,--author;author;-c;-a;--change|5,0;2;3;4,--author-a--change-c,--author;author;-a;--change;-c|5,0;2;3;4,--author-a-c--change,--author;author;-a;-c;--change|5,0;1;2;3,--author-a--change-c,--author;-a;--change;-c;author|5,0;1;2;4,--author-a--change-c,--author;-a;--change;author;-c|5,0;1;2;3,--author-a-c--change,--author;-a;-c;--change;author|5,0;1;2;4,--author-a-c--change,--author;-a;-c;author;--change|5,0;1;3;4,--author-a--change-c,--author;-a;author;--change;-c|5,0;1;3;4,--author-a-c--change,--author;-a;author;-c;--change|5,0;1;2;4,-a--change-c--author,-a;--change;-c;author;--author|5,0;1;2;3,-a--change-c--author,-a;--change;-c;--author;author|5,0;1;3;4,-a--change-c--author,-a;--change;author;-c;--author|5,0;1;3;4,-a--change--author-c,-a;--change;author;--author;-c|5,0;1;2;3,-a--change--author-c,-a;--change;--author;-c;author|5,0;1;2;4,-a--change--author-c,-a;--change;--author;author;-c|5,0;1;2;4,-a-c--change--author,-a;-c;--change;author;--author|5,0;1;2;3,-a-c--change--author,-a;-c;--change;--author;author|5,0;1;3;4,-a-c--change--author,-a;-c;author;--change;--author|5,0;1;3;4,-a-c--author--change,-a;-c;author;--author;--change|5,0;1;2;3,-a-c--author--change,-a;-c;--author;--change;author|5,0;1;2;4,-a-c--author--change,-a;-c;--author;author;--change|5,0;2;3;4,-a--change-c--author,-a;author;--change;-c;--author|5,0;2;3;4,-a--change--author-c,-a;author;--change;--author;-c|5,0;2;3;4,-a-c--change--author,-a;author;-c;--change;--author|5,0;2;3;4,-a-c--author--change,-a;author;-c;--author;--change|5,0;2;3;4,-a--author--change-c,-a;author;--author;--change;-c|5,0;2;3;4,-a--author-c--change,-a;author;--author;-c;--change|5,0;1;2;3,-a--author--change-c,-a;--author;--change;-c;author|5,0;1;2;4,-a--author--change-c,-a;--author;--change;author;-c|5,0;1;2;3,-a--author-c--change,-a;--author;-c;--change;author|5,0;1;2;4,-a--author-c--change,-a;--author;-c;author;--change|5,0;1;3;4,-a--author--change-c,-a;--author;author;--change;-c|5,0;1;3;4,-a--author-c--change,-a;--author;author;-c;--change"
            )
        ]
        for spec, r in cases:
            spec = "\n".join(l[20:] for l in spec.splitlines())
            p, u, d = lutline.speclang.parse(spec_str=spec)
            embodiments = lutline.embodiments.process(p)
            lut = lutline.lut.generate(embodiments)
            self.assertEqual(r, lutline.templates.serialize(lut))
