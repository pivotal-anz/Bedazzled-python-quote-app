cf push bedazzled-python-quote-app-green -n bedazzled-python-quote-app-green --no-route --no-manifest

cf map-route bedazzled-python-quote-app-green cfapps.io -n bedazzled-python-quote-app

cf unmap-route bedazzled-python-quote-app cfapps.io -n bedazzled-python-quote-app

cf d bedazzled-python-quote-app -f
