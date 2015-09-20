#!/bin/bash


echo "--- testing lutline ---"
echo "{
    'usage': 'usage: ./cli [-f <fout>] <fin>',
    'spec': [
        ['opt', [['f', 'f'], ['a', 'fout']]],
        ['a', 'fin']
    ]
}
" > spec.py
echo "import resource
import time
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()
sta = time.time()

import cli
args = cli.parse()

fin = time.time()
end = get_mem()
print 'delta:', '%.02f MB' % (end - ini), 'in', '%.02f ms' % ((fin - sta) * 1000)
" > main.py
lutline -l python -o cli.py spec.py
python main.py hello.txt
rm spec.py cli.py cli.pyc main.py


echo "--- testing docopt ---"
echo "import resource
import time
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()
sta = time.time()

import docopt
d = 'usage: main.py [-f <fout>] <fin>'
args = docopt.docopt(d)

fin = time.time()
end = get_mem()
print 'delta:', '%.02f MB' % (end - ini), 'in', '%.02f ms' % ((fin - sta) * 1000)
" > main.py
python main.py -f bye.txt hello.txt
rm main.py


echo "--- testing compago ---"
echo "import resource
import time
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()
sta = time.time()

import compago
app = compago.Application()
@app.option('-f', dest='fout')
def main(fout, fin):
    'Basic memory test.'
    fin = time.time()
    end = get_mem()
    print 'delta:', '%.02f MB' % (end - ini), 'in', '%.02f ms' % ((fin - sta) * 1000)
    return fout, fin
app.run()
" > main.py
python main.py main -f bye.txt hello.txt
rm main.py


echo "--- testing plac ---"
echo "import resource
import time
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()
sta = time.time()

import plac
def main(fout, fin):
    'Basic memory test.'
    fin = time.time()
    end = get_mem()
    print 'delta:', '%.02f MB' % (end - ini), 'in', '%.02f ms' % ((fin - sta) * 1000)
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
import time
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()
sta = time.time()

import argparse
parser = argparse.ArgumentParser(description='Basic memory test.')
parser.add_argument('-f', default='')
parser.add_argument('fin')

args = parser.parse_args()

fin = time.time()
end = get_mem()
print 'delta:', '%.02f MB' % (end - ini), 'in', '%.02f ms' % ((fin - sta) * 1000)
" > main.py
python main.py -f bye.txt hello.txt
rm main.py


echo "--- testing click ---"
echo "import resource
import time
get_mem = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.
ini = get_mem()
sta = time.time()

import click
@click.command()
@click.option('-f', required=False, is_flag=True)
@click.argument('fout', required=False)
@click.argument('fin', required=True)
def main(f, fout, fin):
    'Basic memory test.'
    fin = time.time()
    end = get_mem()
    print 'delta:', '%.02f MB' % (end - ini), 'in', '%.02f ms' % ((fin - sta) * 1000)
    return f, fout, fin
main()
" > main.py
python main.py -f bye.txt hello.txt
rm main.py
