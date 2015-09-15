#!/usr/bin/env python
#-*- coding:utf-8 -*-


import datetime
import string
import markdown2


TEMPLATE = """\
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

    <div style="float:right; margin-left:30px; width: 300px;">
        <div class="panel panel-default">
          <div class="panel-body">
            <p>Learn more:</p>
            <ul>
               $toc
            </ul>
          </div>
        </div>
    </div>
    $body
    <br>
    <footer class="footer">
        <div style="float:left;"><a href="https://github.com/ffunenga/lutline/blob/master/LICENSE">Check the MIT License</a></div>
        <div style="float:right;">$date</div>
    </footer>
    </div>

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

with open("index.md") as f:
    index = f.read()
with open("basics.md") as f:
    basics = f.read()
headings = [l[2:].strip() for l in basics.splitlines() if l.startswith("##")]
tags = [h.lower().replace(" ", "-") for h in headings]
__t = '<li><a href="basics#{tag}">{heading}</a></li>'
toc = "\n".join(__t.format(tag=t, heading=h) for t, h in zip(tags, headings))
body = markdown2.markdown(index, extras=['fenced-code-blocks', 'toc'])
doc = string.Template(TEMPLATE).safe_substitute(toc=toc, body=body, date="This page was generated in " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
with open("index.html", "w") as f:
    f.write(doc)
