#!/usr/bin/env python3


import unittest
import lutline


class TestCase(unittest.TestCase):

    def test_split_sections(self):
        spec_strs = [
            """\

                ...
            """,
            """\
                ...

            """,
            """\
                ...
            """,
            """\
                ...
                usage: app.py [-f] <in_filename>
            """,
            """\
                ...
                usage: app.py [-f] <in_filename>

            """,
            """\
                ...

                usage: app.py [-f] <in_filename>
            """,
            """\
                ...

                usage: app.py [-f] <in_filename>

            """,
            """\
                ...
                usage: app.py [-f] <in_filename>

                Create a new image from a container's changes
                    (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
                    (-c | --change) <changes>   Apply Dockerfile instruction to the created image
            """,
            """\
                ...
                usage:

                Create a new image from a container's changes
                    (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
                    (-c | --change) <changes>   Apply Dockerfile instruction to the created image
            """,
            """\
                ...
                usage:
                Create a new image from a container's changes
                    (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
                    (-c | --change) <changes>   Apply Dockerfile instruction to the created image
            """,
            """\
                ...
                usage:
            """,
            """\
                ...
                usage:

            """,
            """\
                ...

                usage:
            """,
            """\
                ...

                usage:

            """,
            """\
                ...
                app.py [-f] <in_filename>
                Create a new image from a container's changes
                    (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
                    (-c | --change) <changes>   Apply Dockerfile instruction to the created image
            """,
            """\
                ...
                Create a new image from a container's changes
                    (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
                    (-c | --change) <changes>   Apply Dockerfile instruction to the created image
            """,
            "",
            """\

            """,
        ]
        rsts = [(True, False, False),
                (True, False, False),
                (True, False, False),
                (True, True, False),
                (True, True, False),
                (True, True, False),
                (True, True, False),
                (True, True, True),
                (True, False, True),
                (True, False, True),
                (True, False, False),
                (True, False, False),
                (True, False, False),
                (True, False, False),
                (True, False, False),
                (True, False, False),
                (False, False, False),
                (False, False, False)]
        for idx, spec_str in enumerate(spec_strs):
            spec_str = "\n".join(l[16:] for l in spec_str.splitlines())
            r = lutline.speclang.split_sections(spec_str)
            flags = (not r[0] == None, not r[1] == None, not r[2] == None)
            self.assertEqual(flags, rsts[idx])

    def test_remove_comments(self):
        spec_str = """\
            exclusive:
                required:
                    explicit cook  # ola
                    optional:
                        exclusive:
                            explicit -u
                            explicit --urg#ent
                    #explicit t table
                    oneormore:
                        explicit i# #item
                        optional:
                            implicit style
                required:
                #   explicit checkout
                    explicit t #table
                    implicit payment_method#
                required: #
                    explicit menu
                    explicit set
                    atleastone:
                        explicit recepies"""
        spec_str = "\n".join(l[12:] for l in spec_str.splitlines())
        lines = lutline.speclang.remove_comments(spec_str)
        self.assertEqual(19, len(lines))

    def test_robust_args(self):
        self.assertRaises(AssertionError, lutline.speclang.parse, True, True)
        self.assertRaises(AssertionError, lutline.speclang.parse, None, None)
        self.assertRaises(AssertionError, lutline.speclang.parse)
        self.assertRaises(AssertionError, lutline.speclang.parse, spec_str=1)
        spec_str = """\
        """
        spec_str = "\n".join(l[12:] for l in spec_str.splitlines())
        self.assertRaises(AssertionError, lutline.speclang.parse, spec_str=spec_str)
        spec_str = """\

        """
        spec_str = "\n".join(l[12:] for l in spec_str.splitlines())
        self.assertRaises(AssertionError, lutline.speclang.parse, spec_str=spec_str)
        spec_str = """\
            usage:
            Create a new image from a container's changes
                (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
                (-c | --change) <changes>   Apply Dockerfile instruction to the created image
        """
        spec_str = "\n".join(l[12:] for l in spec_str.splitlines())
        self.assertRaises(AssertionError, lutline.speclang.parse, spec_str=spec_str)

    def test_parse(self):
        cases = [
            (
                """\
                    required:
                        optional:
                            explicit -f
                        implicit input_fn
                    usage: app.py [-f] <input_fn>
                """,
                ['required',
                    [
                        ['optional',
                            [
                                ['explicit', '-f']
                            ]
                        ],
                        ['implicit', 'input_fn']
                    ]
                ],
                'usage: app.py [-f] <input_fn>',
                None
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
                ['exclusive',
                    [
                        ['explicit', 'parse'],
                        ['required',
                            [
                                ['optional',
                                    [
                                        ['explicit', '--template']
                                    ]
                                ],
                                ['implicit', 'input_fn']
                            ]
                        ]
                    ]
                ],
                'usage: app.py (parse | [--template] <input_fn>)',
                None
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
                            atleastone:
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
                            atleastone:
                                explicit recepies
                """,
                ['exclusive',
                    [
                        ['required',
                            [
                                ['explicit', 'cook'],
                                ['optional',
                                    [
                                        ['exclusive',
                                            [
                                                ['explicit', '-u'],
                                                ['explicit', '--urgent']
                                            ]
                                        ]
                                    ]
                                ],
                                ['explicit', '--table'],
                                ['implicit', 'table'],
                                ['atleastone',
                                    [
                                        ['explicit', '--item'],
                                        ['implicit', 'item']
                                    ]
                                ]
                            ]
                        ],
                        ['required',
                            [
                                ['explicit', 'checkout'],
                                ['explicit', '--table'],
                                ['explicit', '--payment_method']
                            ]
                        ],
                        ['required',
                            [
                                ['explicit', 'menu'],
                                ['explicit', 'set'],
                                ['atleastone',
                                    [
                                        ['explicit', 'recepies']
                                    ]
                                ]
                            ]
                        ]
                    ]
                ],
                None,
                None
            ),
        ]
        for spec, p, u, d in cases:
            spec = "\n".join(l[20:] for l in spec.splitlines())
            pattern, usage, description = lutline.speclang.parse(spec_str=spec)
            if 0:
                print(pattern)
                continue
            self.assertEqual(pattern, p)
            self.assertEqual(usage, u)
            self.assertEqual(description, d)
