FROM justb4/jmeter

WORKDIR /tests

COPY test-plan.jmx /tests/test-plan.jmx

CMD ["jmeter", "-n", "-t", "/tests/test-plan.jmx"]
