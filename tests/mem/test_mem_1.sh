#!/bin/bash


echo "--- testing lutline ---"
echo "{
    'usage': ('Usage:\\n'
              '    ./kitchen burger [--raw | --medium | --overcooked]\\n'
              '    ./kitchen [-u <urgency>] <request>\\n'
              '    ./kitchen -h | --help | --version\\n'),
    'spec': [
        ['exc', [
            [
                ['c', 'burger'],
                ['opt', [
                    ['exc', [
                        [['f', '-raw']],
                        [['f', '-medium']],
                        [['f', '-overcooked']]
                    ]]
                ]]
            ],
            [
                ['opt', [
                    ['f', 'u'],
                    ['a', 'urgency']]
                ],
                ['a', 'request']
            ],
            [
                ['exc', [
                    [['f', 'h']],
                    [['f', '-help']],
                    [['f', '-version']]
                ]]
            ]
        ]]
    ]
}
" > spec.py
lutline -l python -o cli.py spec.py
echo "import resource
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()

import cli
args = cli.parse()

end = get_mem()
print 'delta:', '%.02f MB' % (end - ini)
" > main.py
python main.py burger --medium
rm spec.py cli.py cli.pyc main.py


echo "--- testing docopt ---"
echo "import resource
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()

import docopt
d = ('Usage:\n'
     '    ./kitchen burger [--raw | --medium | --overcooked]\n'
     '    ./kitchen [-u <urgency>] <request>\n'
     '    ./kitchen -h | --help | --version\n')
args = docopt.docopt(d)

end = get_mem()
print 'delta:', '%.02f MB' % (end - ini)
" > main.py
python main.py burger --medium
rm main.py
exit

echo "--- testing compago ---"
echo "import resource
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()

import compago
app = compago.Application()
@app.option('-f', dest='fout')
def main(fout, fin):
    'Basic memory test.'
    end = get_mem()
    print 'delta:', '%.02f MB' % (end - ini)
    return fout, fin
app.run()
" > main.py
python main.py main -f bye.txt hello.txt
rm main.py


echo "--- testing plac ---"
echo "import resource
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()

import plac
def main(fout, fin):
    'Basic memory test.'
    end = get_mem()
    print 'delta:', '%.02f MB' % (end - ini)
    return fout, fin
main.__annotations__ = dict(
    fout=('prints more info', 'option', 'f')
)
plac.call(main)
" > main.py
python main.py -f bye.txt hello.txt
rm main.py


echo "--- testing argparse ---"
echo "import resource
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()

import argparse
parser = argparse.ArgumentParser(description='Basic memory test.')
parser.add_argument('-f', default='')
parser.add_argument('fin')

args = parser.parse_args()

end = get_mem()
print 'delta:', '%.02f MB' % (end - ini)
" > main.py
python main.py -f bye.txt hello.txt
rm main.py


echo "--- testing click ---"
echo "import resource
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()

import click
@click.command()
@click.option('-f', required=False, is_flag=True)
@click.argument('fout', required=False)
@click.argument('fin', required=True)
def main(f, fout, fin):
    'Basic memory test.'
    end = get_mem()
    print 'delta:', '%.02f MB' % (end - ini)
    return f, fout, fin
main()
" > main.py
python main.py -f bye.txt hello.txt
rm main.py
