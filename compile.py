#!/usr/bin/env python
#-*- coding:utf-8 -*-


import datetime
import string
import markdown2


TEMPLATE_INDEX = """\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="With lutline you generate a look-up table based on a command-line interface specification, and the code needed to access it while looping through argv.">
        <meta name="author" content="Filipe Funenga">
        <link rel="icon shortcut" href="images/favicon.ico">
        <title>lutline - Efficient command-line interface</title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/jumbotron-narrow.css" rel="stylesheet">
    </head>

    <body>
        <div class="container">
            <div class="header clearfix">
                <nav>
                    <a class="btn btn-success" role="button" href="https://github.com/ffunenga/lutline"><span class="glyphicon glyphicon-console" aria-hidden="true"></span> View on GitHub</a>
                    <ul class="nav nav-pills pull-right">
                        <li role="presentation"><a href="https://github.com/ffunenga/lutline/zipball/master" class="btn"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> Download as .zip</a></li>
                        <li role="presentation"><a href="https://github.com/ffunenga/lutline/tarball/master" class="btn"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> Download as .tar.gz</a></li>
                    </ul>
                </nav>
            </div>

        <div class="jumbotron">
            <h1>lutline</h1>
            <p class="lead">Parse <code>argv</code> using a fast look-up table generated from your command-line interface specification.</p>
            <a class="btn btn-default" href="get_started.html" style="margin-top:10px; margin-bottom:10px">Get Started <span class="glyphicon glyphicon-chevron-right"></span></a>
        </div>

        <div class="row">
            <div class="col-md-2">
                <center>
                    <span class="glyphicon glyphicon-eye-open" style="font-size: 250%;"></span>
                </center>
            </div>
            <div class="col-md-10">
                $bullet0
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col-md-2">
                <center>
                    <span class="glyphicon glyphicon-tower" style="font-size: 250%;"></span>
                </center>
            </div>
            <div class="col-md-10">
                $bullet1
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col-md-2">
                <center>
                    <span class="glyphicon glyphicon-dashboard" style="font-size: 250%;"></span>
                </center>
            </div>
            <div class="col-md-10">
                $bullet2
            </div>
        </div>
        <br>
        $bullet3
        <br>
        <footer class="footer">
            <div style="float:left;"><a href="https://github.com/ffunenga/lutline/blob/master/LICENSE">Check the MIT License</a></div>
            <div style="float:right;">$date</div>
        </footer>

        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
            ga('create', 'UA-35879263-5', 'auto');
            ga('send', 'pageview');
        </script>
    </body>
</html>
"""


TEMPLATE_DOC = """\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="With lutline you generate a look-up table based on a command-line interface specification, and the code needed to access it while looping through argv.">
        <meta name="author" content="Filipe Funenga">
        <link rel="icon shortcut" href="images/favicon.ico">
        <title>lutline - $title</title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/jumbotron-narrow.css" rel="stylesheet">
        <style>
            .toc {
                margin-top: 30px;
            }
            @media (min-width: 768px) {
                .toc {
                    margin-top: 0px;
                    float:right;
                    margin-left:30px;
                    width: 300px;
                }
            }
        </style>
    </head>

    <body>
        <div class="container">
            <div class="header fixed-top clearfix">
                <ul class="nav nav-pills">
                    <li role="presentation" style="margin-right:20px;"><a href="index.html"><span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span> Home</a></li>
                    <li role="presentation"><h3 class="pull-right" role="presentation">$title</h3></li>
                </ul>
            </div>
            <div class="toc">
                <div class="panel panel-default">
                    <div class="panel-body">
                        <p>Contents:</p>
                        $toc
                    </div>
                </div>
            </div>
            $body
            <footer class="footer">
                <div style="float:left;"><a href="https://github.com/ffunenga/lutline/blob/master/LICENSE">Check the MIT License</a></div>
                <div style="float:right;">$date</div>
            </footer>
        </div>
        <script src="js/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
            ga('create', 'UA-35879263-5', 'auto');
            ga('send', 'pageview');
        </script>
    </body>
</html>
"""


generated = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
generated = "This page was generated in " + generated

extras = ['fenced-code-blocks', 'toc', 'cuddled-lists', 'tables']

with open("docs/index.md") as f:
    index = f.read()
index = index.split("\n\n")
bullet0 = markdown2.markdown(index[0], extras=extras)
bullet1 = markdown2.markdown(index[1], extras=extras)
bullet2 = markdown2.markdown(index[2], extras=extras)
bullet3 = markdown2.markdown("\n\n".join(index[3:]), extras=extras)
doc = string.Template(TEMPLATE_INDEX).safe_substitute(
    bullet0=bullet0, bullet1=bullet1, bullet2=bullet2, bullet3=bullet3, date=generated)
with open("index.html", "w") as f:
    f.write(doc)


with open("docs/get_started.md") as f:
    basics = f.read()
title = "Tutorial - Getting started"
body = markdown2.markdown(basics, extras=extras)
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=body.toc_html, date=generated)
with open("get_started.html", "w") as f:
    f.write(doc)


with open("docs/specfile.md") as f:
    specfile = f.read()
title = "Command-line interface specification"
body = markdown2.markdown(specfile, extras=extras)
toc = getattr(body, "toc_html", "")
body = body.replace("<table>", '<table class="table table-striped">')
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=toc, date=generated)
with open("specfile.html", "w") as f:
    f.write(doc)


with open("docs/problem.md") as f:
    data = f.read()
title = "The problem of parsing a command-line"
body = markdown2.markdown(data, extras=extras)
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=body.toc_html, date=generated)
with open("problem.html", "w") as f:
    f.write(doc)


with open("docs/solution.md") as f:
    data = f.read()
title = "The lutline approach"
body = markdown2.markdown(data, extras=extras)
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=body.toc_html, date=generated)
with open("solution.html", "w") as f:
    f.write(doc)


with open("docs/validation.md") as f:
    data = f.read()
title = "Validating the non-ambiguoty of a pattern"
body = markdown2.markdown(data, extras=extras)
toc = getattr(body, "toc_html", "")
body = body.replace("<table>", '<table class="table table-striped">')
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=toc, date=generated)
with open("validation.html", "w") as f:
    f.write(doc)


with open("docs/efficient.md") as f:
    efficient = f.read()
title = "Efficiency analysis"
body = markdown2.markdown(efficient, extras=extras)
toc = getattr(body, "toc_html", "")
body = body.replace("<table>", '<table class="table table-striped">')
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=toc, date=generated)
with open("efficient.html", "w") as f:
    f.write(doc)
