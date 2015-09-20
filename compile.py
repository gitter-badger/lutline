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
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="./images/favicon.ico">
        <title>lutline - Python package</title>
        <link href="./css/bootstrap.min.css" rel="stylesheet">
        <link href="./css/jumbotron-narrow.css" rel="stylesheet">
        <script src="./js/ie-emulation-modes-warning.js"></script>
    </head>

    <body>
        <div class="container">
            <div class="header clearfix">
                <nav>
                    <a class="btn btn-lg btn-success" role="button" href="https://github.com/ffunenga/lutline"><span class="glyphicon glyphicon-console" aria-hidden="true"></span> View on GitHub</a>
                    <ul class="nav nav-pills pull-right">
                        <li role="presentation"><a href="https://github.com/ffunenga/lutline/zipball/master" class="btn"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> Download as .zip</a></li>
                        <li role="presentation"><a href="https://github.com/ffunenga/lutline/tarball/master" class="btn"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> Download as .tar.gz</a></li>
                    </ul>
                </nav>
            </div>

        <div class="jumbotron">
            <h1>lutline</h1>
            <p class="lead">Parse <code>argv</code> using a fast look-up table generated from your command-line interface specification.</p>
        </div>

        <div class="row">
            <div class="col-md-7">
              $body
              <a class="btn btn-default" href="get_started.html" style="margin-top:10px; margin-bottom:10px">Get Started <span class="glyphicon glyphicon-chevron-right"></span></a>
            </div>
            <div class="col-md-5">
                <div class="panel panel-default">
                    <div class="panel-body">
                    <p>Learn more:</p>
                        <ul>
                            $toc
                        </ul>
                    </div>
                </div>
           </div>
        </div>
        <footer class="footer">
            <div style="float:left;"><a href="https://github.com/ffunenga/lutline/blob/master/LICENSE">Check the MIT License</a></div>
            <div style="float:right;">$date</div>
        </footer>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
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
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="./images/favicon.ico">
        <title>lutline - Basics</title>
        <link href="./css/bootstrap.min.css" rel="stylesheet">
        <link href="./css/jumbotron-narrow.css" rel="stylesheet">
        <script src="./js/ie-emulation-modes-warning.js"></script>
    </head>

    <body>
        <div class="container">
            <div class="header fixed-top clearfix">
                <ul class="nav nav-pills">
                    <li role="presentation" style="margin-right:20px;"><a href="index.html"><span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span> Back</a></li>
                    <li role="presentation"><h3 class="pull-right" role="presentation">$title</h3></li>
                </ul>
            </div>
            <div style="float:right; margin-left:30px; width: 300px;">
                <div class="panel panel-default">
                    <div class="panel-body">
                        <p>Contents:</p>
                        <ul>
                            $toc
                        </ul>
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

with open("get_started.md") as f:
    basics = f.read()
with open("index.md") as f:
    index = f.read()
headings = [l[2:].strip() for l in basics.splitlines() if l.startswith("##")]
tags = [h.lower().replace(" ", "-") for h in headings]
__t = '<li><a href="get_started.html#{tag}">{heading}</a></li>'
toc = "\n".join(__t.format(tag=t, heading=h) for t, h in zip(tags, headings))
body = markdown2.markdown(index, extras=['fenced-code-blocks', 'toc'])
generated = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
generated = "This page was generated in " + generated
doc = string.Template(TEMPLATE_INDEX).safe_substitute(
        toc=toc, body=body, date=generated)
with open("index.html", "w") as f:
    f.write(doc)


title = "Tutorial - Getting started"
body = markdown2.markdown(basics, extras=['fenced-code-blocks', 'toc'])
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=toc, date=generated)
with open("get_started.html", "w") as f:
    f.write(doc)


with open("specfile.md") as f:
    specfile = f.read()
title = "The spec file"
body = markdown2.markdown(specfile, extras=['fenced-code-blocks', 'toc'])
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=toc, date=generated)
with open("specfile.html", "w") as f:
    f.write(doc)


with open("efficient.md") as f:
    efficient = f.read()
title = "Efficiency"
headings = [l[2:].strip() for l in efficient.splitlines() if l.startswith("##")]
tags = [h.lower().replace(" ", "-") for h in headings]
__t = '<li><a href="efficient.html#{tag}">{heading}</a></li>'
toc = "\n".join(__t.format(tag=t, heading=h) for t, h in zip(tags, headings))
body = markdown2.markdown(efficient, extras=['fenced-code-blocks', 'toc', 'tables'])
body = body.replace("<table>", '<table class="table table-striped">')
doc = string.Template(TEMPLATE_DOC).safe_substitute(
        title=title, body=body, toc=toc, date=generated)
with open("efficient.html", "w") as f:
    f.write(doc)
