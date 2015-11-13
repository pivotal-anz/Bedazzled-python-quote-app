cf push demo-b.py -n cf-demo-jack --no-route --no-manifest

cf map-route demo-b.py cfapps.io -n cf-demo-jack

cf unmap-route demo.py cfapps.io -n cf-demo-jack

cf d demo.py -f -r