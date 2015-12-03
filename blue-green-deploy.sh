cf push bedazzled-python-quote-app-green.py -n bedazzled-python-quote-app-green --no-route --no-manifest

cf map-route bedazzled-python-quote-app-green.py pcfdemo.info -n bedazzled-python-quote-app-green

cf unmap-route bedazzled-python-quote-app.py pcfdemo.info -n bedazzled-python-quote-app

cf d bedazzled-python-quote-app.py -f -r