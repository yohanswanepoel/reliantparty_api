# reliantparty_api

http://127.0.0.1:8000/api/v1/reliantparties/

/api/v1/health/

# TODO
* Patch Build Config
* Needs test DB in Postgresql
strategy:
    sourceStrategy:
      env:
        - name: PIP_INDEX_URL
        - name: DATABASE_NAME
          value: sampledb
        - name: DATABASE_USER
          value: user
        - name: DATABASE_PASSWORD
          value: password
        - name: DATABASE_SERVICE_NAME
          value: testdb
      from:
        kind: ImageStreamTag
        name: 'python:3.6'
        namespace: openshift

--patch '{"spec":{"strategy": {"sourceStrategy":{env:}}}'