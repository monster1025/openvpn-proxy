#SHELL := /bin/bash

ARGS = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

update_secrets_sample:
	@echo "Masking env files..."
	@find . -name *.env | xargs -I{} cp {} {}.sample
	@find . -name *.env.sample | xargs -I{} sed -i "s/\=.*/\=xxxxxxxxx/g" {}

commit: update_secrets_sample
	git add .
	git diff-index --quiet HEAD || git commit -m "$(call ARGS,\"updating configuration\")"
	git push

%:
    @:
